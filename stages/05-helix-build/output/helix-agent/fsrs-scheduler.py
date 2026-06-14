"""
Helix FSRS Scheduler
====================
Manages spaced repetition for quiz cards stored in progress/progress.json.

Usage (run from your mission-command root):
  python helix/fsrs-scheduler.py due              # list cards due today
  python helix/fsrs-scheduler.py due --json       # machine-readable (Helix reads this)
  python helix/fsrs-scheduler.py update           # interactive: enter ratings from your review session
  python helix/fsrs-scheduler.py update <card_id> <rating>  # single card (1=Again 2=Hard 3=Good 4=Easy)
  python helix/fsrs-scheduler.py stats            # summary: streak, total reviews, cards graduated
  python helix/fsrs-scheduler.py init <quiz_bank_dir>  # seed progress.json from quiz bank cards.json files

FSRS-5 parameters (locked — see stages/05-helix-build/output/helix-agent/fsrs-integration-spec.md):
  desired_retention = 0.90
  initial_stability = 1.0 day
  initial_difficulty = 5.0
  min_interval = 1 day
  max_interval = 365 days
  learning_steps = [1 min, 10 min]
  relearning_steps = [10 min]
  easy_bonus = 1.3
"""

import json
import math
import sys
import os
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── FSRS-5 Constants (LOCKED) ─────────────────────────────────────────────────

DESIRED_RETENTION  = 0.90
INITIAL_STABILITY  = 1.0
INITIAL_DIFFICULTY = 5.0
MIN_INTERVAL       = 1        # days
MAX_INTERVAL       = 365      # days
EASY_BONUS         = 1.3
FACTOR             = 19 / 81  # FSRS-5 retrieval formula constant
EXPONENT           = 0.5      # FSRS-5 retrieval formula constant

# Per-rating stability multipliers (FSRS-5 defaults)
STABILITY_MULTIPLIERS = {
    1: 0.5,   # Again — lapse, stability cut in half
    2: 0.85,  # Hard — small increase
    3: 1.2,   # Good — normal increase
    4: 1.6,   # Easy — large increase
}

# Difficulty adjustments per rating (FSRS-5: difficulty on 1-10 scale)
DIFFICULTY_DELTAS = {
    1:  0.8,   # Again — increases difficulty
    2:  0.3,   # Hard — slight increase
    3:  0.0,   # Good — no change
    4: -0.5,   # Easy — decreases difficulty
}

RATING_LABELS = {1: "Again", 2: "Hard", 3: "Good", 4: "Easy"}

PROGRESS_PATH = Path("progress/progress.json")


# ── FSRS-5 Core ───────────────────────────────────────────────────────────────

def retrieval_probability(t_days: float, stability: float) -> float:
    """R(t, S) = (1 + FACTOR * t / S) ^ (-EXPONENT)"""
    if stability <= 0:
        return 0.0
    return (1 + FACTOR * t_days / stability) ** (-EXPONENT)


def next_interval(stability: float) -> int:
    """Days until retrieval probability drops to desired_retention."""
    # Solve R(t, S) = desired_retention for t:
    # t = S / FACTOR * (R^(-1/EXPONENT) - 1)
    t = stability / FACTOR * (DESIRED_RETENTION ** (-1 / EXPONENT) - 1)
    interval = max(MIN_INTERVAL, min(MAX_INTERVAL, round(t)))
    return interval


def update_card_state(state: dict, rating: int) -> dict:
    """Apply an FSRS-5 review rating and return updated state."""
    now = datetime.now(timezone.utc)
    rating = max(1, min(4, rating))

    old_stability  = state.get("stability", INITIAL_STABILITY)
    old_difficulty = state.get("difficulty", INITIAL_DIFFICULTY)
    review_count   = state.get("review_count", 0)

    if rating == 1:
        # Lapse — re-enter relearning
        new_stability  = max(0.1, old_stability * STABILITY_MULTIPLIERS[1])
        new_difficulty = min(10.0, old_difficulty + DIFFICULTY_DELTAS[1])
        new_lapses     = state.get("lapses", 0) + 1
        # Relearning step: 10 minutes before next interval
        due = now + timedelta(minutes=10)
    else:
        # Normal review
        difficulty_penalty = (old_difficulty - 5.0) / 10.0  # normalized difficulty effect
        new_stability = old_stability * STABILITY_MULTIPLIERS[rating] * (1 - difficulty_penalty * 0.15)
        new_stability = max(0.1, new_stability)
        if rating == 4:
            new_stability *= EASY_BONUS
        new_difficulty = max(1.0, min(10.0, old_difficulty + DIFFICULTY_DELTAS[rating]))
        new_lapses = state.get("lapses", 0)
        interval   = next_interval(new_stability)
        due        = now + timedelta(days=interval)

    return {
        "stability":    round(new_stability, 3),
        "difficulty":   round(new_difficulty, 3),
        "due":          due.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "last_review":  now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "review_count": review_count + 1,
        "lapses":       new_lapses,
    }


# ── Progress file I/O ─────────────────────────────────────────────────────────

def load_progress() -> dict:
    if not PROGRESS_PATH.exists():
        return {"v": 1, "lessons": {}, "fsrs": {}, "updatedAt": 0}
    with open(PROGRESS_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_progress(data: dict) -> None:
    data["updatedAt"] = int(datetime.now(timezone.utc).timestamp() * 1000)
    PROGRESS_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = PROGRESS_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(PROGRESS_PATH)


def get_due_cards(fsrs_state: dict) -> list[dict]:
    """Return cards with due <= now, sorted by due date (most overdue first)."""
    now = datetime.now(timezone.utc)
    due = []
    for card_id, state in fsrs_state.items():
        due_str = state.get("due")
        if not due_str:
            continue
        try:
            due_dt = datetime.fromisoformat(due_str.replace("Z", "+00:00"))
        except ValueError:
            continue
        if due_dt <= now:
            days_overdue = (now - due_dt).days
            due.append({
                "card_id":     card_id,
                "due":         due_str,
                "days_overdue": days_overdue,
                "stability":   state.get("stability", INITIAL_STABILITY),
                "review_count": state.get("review_count", 0),
            })
    due.sort(key=lambda x: x["days_overdue"], reverse=True)
    return due


# ── CLI Commands ──────────────────────────────────────────────────────────────

def cmd_due(args) -> None:
    data = load_progress()
    fsrs = data.get("fsrs", {})
    due  = get_due_cards(fsrs)

    if args.json:
        # Machine-readable output for Helix to consume
        print(json.dumps({
            "cards_due_today": len(due),
            "due_cards": due[:10],  # first 10 for context
            "topics_overdue": list({c["card_id"].split(":")[0] for c in due}),
        }, indent=2))
        return

    if not due:
        print("No cards due. Check back later or start a lesson.")
        return

    print(f"\n{len(due)} card(s) due:\n")
    for card in due:
        overdue_str = f" ({card['days_overdue']}d overdue)" if card["days_overdue"] > 0 else " (due today)"
        print(f"  {card['card_id']}{overdue_str}")

    print(f"\nStart a review session with Helix, then run:")
    print(f"  python helix/fsrs-scheduler.py update")


def cmd_update(args) -> None:
    data = load_progress()
    fsrs = data.get("fsrs", {})

    if args.card_id and args.rating:
        # Single-card update from command line
        card_id = args.card_id
        rating  = int(args.rating)
        if card_id not in fsrs:
            print(f"ERROR: card '{card_id}' not found in progress.json")
            sys.exit(1)
        fsrs[card_id] = update_card_state(fsrs[card_id], rating)
        new_interval   = next_interval(fsrs[card_id]["stability"])
        print(f"Updated {card_id}: {RATING_LABELS[rating]} → next review in {new_interval} day(s)")
        data["fsrs"] = fsrs
        save_progress(data)
        print(f"Saved. Commit progress/progress.json to your fork.")
        return

    # Interactive mode — walk through due cards
    due = get_due_cards(fsrs)
    if not due:
        print("No cards due right now.")
        return

    print(f"\nEntering ratings for {len(due)} due card(s).")
    print("Ratings: 1=Again  2=Hard  3=Good  4=Easy  s=skip  q=quit\n")

    updated = 0
    for card in due:
        card_id = card["card_id"]
        state   = fsrs.get(card_id, {})
        print(f"Card: {card_id}")
        print(f"  Stability: {state.get('stability', INITIAL_STABILITY):.1f}d | "
              f"Reviews: {state.get('review_count', 0)} | "
              f"Lapses: {state.get('lapses', 0)}")

        while True:
            raw = input("  Rating [1-4 / s / q]: ").strip().lower()
            if raw == "q":
                print(f"\nQuitting. {updated} card(s) updated.")
                data["fsrs"] = fsrs
                save_progress(data)
                print("Saved. Commit progress/progress.json to your fork.")
                return
            if raw == "s":
                print("  Skipped.\n")
                break
            if raw in ("1", "2", "3", "4"):
                rating = int(raw)
                fsrs[card_id] = update_card_state(state, rating)
                new_interval = next_interval(fsrs[card_id]["stability"])
                print(f"  {RATING_LABELS[rating]} — next review in {new_interval} day(s)\n")
                updated += 1
                break
            print("  Enter 1, 2, 3, 4, s, or q.")

    data["fsrs"] = fsrs
    save_progress(data)
    print(f"{updated} card(s) updated. Commit progress/progress.json to your fork.")


def cmd_stats(args) -> None:
    data = load_progress()
    fsrs = data.get("fsrs", {})

    if not fsrs:
        print("No FSRS data yet. Complete some lessons and review sessions first.")
        return

    total   = len(fsrs)
    reviewed = sum(1 for s in fsrs.values() if s.get("review_count", 0) > 0)
    lapses  = sum(s.get("lapses", 0) for s in fsrs.values())
    due_now = len(get_due_cards(fsrs))

    # Graduated = stability > 21 days (out of learning phase)
    graduated = sum(1 for s in fsrs.values() if s.get("stability", 0) > 21)

    avg_stability = (
        sum(s.get("stability", 0) for s in fsrs.values()) / total if total > 0 else 0
    )

    print(f"\nFSRS Stats")
    print(f"  Total cards:     {total}")
    print(f"  Reviewed:        {reviewed}")
    print(f"  Due now:         {due_now}")
    print(f"  Graduated (>21d):{graduated}")
    print(f"  Total lapses:    {lapses}")
    print(f"  Avg stability:   {avg_stability:.1f} days")

    # Zone breakdown
    zones: dict[str, int] = {}
    for card_id in fsrs:
        zone = card_id.split("/")[0] if "/" in card_id else "unknown"
        zones[zone] = zones.get(zone, 0) + 1
    if zones:
        print(f"\n  Cards by zone:")
        for zone, count in sorted(zones.items()):
            print(f"    {zone}: {count}")


def cmd_init(args) -> None:
    """Seed progress.json with cards from a quiz bank directory."""
    bank_dir = Path(args.quiz_bank_dir)
    if not bank_dir.exists():
        print(f"ERROR: {bank_dir} not found")
        sys.exit(1)

    data   = load_progress()
    fsrs   = data.get("fsrs", {})
    added  = 0
    now    = datetime.now(timezone.utc)
    due_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    for cards_file in bank_dir.rglob("cards.json"):
        try:
            with open(cards_file, encoding="utf-8") as f:
                cards = json.load(f)
        except (json.JSONDecodeError, OSError):
            print(f"  WARN: skipping {cards_file} (parse error)")
            continue

        for card in cards if isinstance(cards, list) else cards.get("cards", []):
            card_id = card.get("card_id") or card.get("id")
            if not card_id:
                continue
            if card_id in fsrs:
                continue  # never overwrite existing FSRS state
            fsrs[card_id] = {
                "stability":    INITIAL_STABILITY,
                "difficulty":   INITIAL_DIFFICULTY,
                "due":          due_str,
                "last_review":  None,
                "review_count": 0,
                "lapses":       0,
            }
            added += 1

    data["fsrs"] = fsrs
    save_progress(data)
    print(f"Initialized {added} new card(s) in progress/progress.json")
    print(f"Commit your progress file: git add progress/progress.json && git commit -m 'init: seed FSRS cards'")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Helix FSRS Scheduler — manage spaced repetition for your mission command"
    )
    sub = parser.add_subparsers(dest="command")

    p_due = sub.add_parser("due", help="Show cards due for review")
    p_due.add_argument("--json", action="store_true", help="Output JSON (for Helix)")

    p_update = sub.add_parser("update", help="Record review ratings")
    p_update.add_argument("card_id", nargs="?", help="Card ID (optional — interactive if omitted)")
    p_update.add_argument("rating",  nargs="?", help="Rating: 1=Again 2=Hard 3=Good 4=Easy")

    sub.add_parser("stats", help="Show review statistics")

    p_init = sub.add_parser("init", help="Seed progress.json from quiz bank")
    p_init.add_argument("quiz_bank_dir", help="Path to quiz bank directory")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        "due":    cmd_due,
        "update": cmd_update,
        "stats":  cmd_stats,
        "init":   cmd_init,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
