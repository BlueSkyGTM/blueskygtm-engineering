"""
Touch-up dispatcher — revise first 57 pre-GLM-5.1 lessons.

These lessons were generated before the GLM-5.1 model upgrade (2026-06-13).
Quality gaps: missing Mermaid diagram in The Concept, thin GTM weave,
no Sources block, weaker exercise depth.

This dispatcher reads each existing lesson, diagnoses its gaps, and sends
it back through GLM-5.1 with a targeted revision prompt. Output overwrites
the original file (atomic tmp→rename pattern).

Usage:
  python3 skills/operator-kit/dispatch-touchup.py --dry-run        # preview only
  python3 skills/operator-kit/dispatch-touchup.py --workers 3      # full run
  python3 skills/operator-kit/dispatch-touchup.py --lesson 00-setup-and-tooling/01-dev-environment
  python3 skills/operator-kit/dispatch-touchup.py --retry-failed   # retry only failed rows

Environment:
  export $(grep -v '^#' .env | xargs)

Governed maze: GLM-5.1 receives existing lesson text + gap diagnosis only.
"""

import os
import sys
import json
import time
import re
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    from openai import OpenAI, RateLimitError
except ImportError:
    print("ERROR: pip install openai")
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────

MANIFEST_PATH  = Path("stages/02-lesson-injection/output/manifest.json")
OUTPUT_ROOT    = Path("stages/02-lesson-injection/output/hybrid-lessons")
TOUCHUP_MANIFEST = Path("stages/02-lesson-injection/output/touchup-manifest.json")
PAUSE_SENTINEL = Path("stages/02-lesson-injection/output/.touchup-pause")

# First 57 lesson IDs (position 0-56 in the Stage 02 manifest — pre-GLM-5.1)
TOUCHUP_COUNT = 57

SYSTEM_PROMPT = """You are Lyra, a GTM engineering curriculum author. You are revising an existing lesson to fix specific quality gaps.

REQUIRED HEADING STRUCTURE (exact, in order — do not add or remove headings):
## Learning Objectives
## The Problem
## The Concept
## Build It
## Use It
## Ship It
## Exercises
## Key Terms

REVISION RULES:
- Keep all content that is already strong. Do not rewrite for the sake of it.
- Fix every gap listed in the GAPS section below.
- In ## The Concept: add exactly one Mermaid diagram if missing (sequence, flowchart, decision tree, or pipeline — use ```mermaid fenced block). Only skip if the concept is purely abstract/metaphor.
- In every GTM beat (Use It, Ship It): name the specific AI concept in the first sentence. GTM weave means the AI mechanism is explicit, not implied.
- End with a ## Sources block listing papers, docs, or tools cited. If no external sources, list the key papers for the core concept.
- All code must run unmodified and produce observable terminal output.
- No objectives starting with "Understand", "Learn", or "Know" — use action verbs.
- Peer-to-peer tone. No marketing claims.
- Output the complete revised lesson — not a diff, not a summary. The full lesson."""

# ── Global rate control ───────────────────────────────────────────────────────

_global_pause = threading.Event()
_global_pause.set()
_global_pause_lock = threading.Lock()


def global_rate_pause(duration: int = 30) -> None:
    with _global_pause_lock:
        if _global_pause.is_set():
            print(f"  [GLOBAL BACKOFF] Rate limit — pausing {duration}s")
            _global_pause.clear()
            threading.Timer(duration, _global_pause.set).start()


def wait_if_paused() -> None:
    _global_pause.wait()


def wait_if_sentinel() -> None:
    while PAUSE_SENTINEL.exists():
        print(f"  [SENTINEL] Paused — delete {PAUSE_SENTINEL} to resume")
        time.sleep(10)


# ── Gap diagnosis ─────────────────────────────────────────────────────────────

def diagnose_gaps(content: str) -> list[str]:
    """Identify quality gaps in a pre-GLM-5.1 lesson."""
    gaps = []
    if "```mermaid" not in content:
        gaps.append("Missing Mermaid diagram in ## The Concept")
    if "## Sources" not in content:
        gaps.append("Missing ## Sources block")
    # GTM weave check: Use It section should name the AI concept in first sentence
    use_it_match = re.search(r"## Use It\n+(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if use_it_match:
        first_sentence = use_it_match.group(1).strip().split(".")[0]
        # Weak weave if the AI concept word doesn't appear in first sentence
        gtm_words = {"gtm", "pipeline", "enrichment", "icp", "outreach", "crm", "sequence", "waterfall", "account"}
        ai_words  = {"model", "algorithm", "network", "embedding", "attention", "gradient", "loss", "training",
                     "inference", "vector", "transformer", "cluster", "layer", "weight", "token"}
        first_lower = first_sentence.lower()
        if not any(w in first_lower for w in ai_words):
            gaps.append("GTM weave in ## Use It does not name the AI mechanism in the first sentence")
    # Check for weak objectives
    obj_match = re.search(r"## Learning Objectives\n+(.*?)(?=\n## )", content, re.DOTALL)
    if obj_match:
        obj_text = obj_match.group(1)
        if re.search(r"\b(Understand|Learn|Know)\b", obj_text):
            gaps.append("Learning Objectives use passive verbs (Understand/Learn/Know) — replace with action verbs")
    if not gaps:
        gaps.append("General polish: strengthen GTM weave depth and exercise specificity")
    return gaps


# ── Touchup manifest ──────────────────────────────────────────────────────────

touchup_lock = threading.Lock()


def build_touchup_manifest(force: bool = False) -> list[dict]:
    """Build or load the touchup manifest from the first 57 Stage 02 slots."""
    if TOUCHUP_MANIFEST.exists() and not force:
        with open(TOUCHUP_MANIFEST, encoding="utf-8") as f:
            return json.load(f)

    with open(MANIFEST_PATH, encoding="utf-8") as f:
        stage02 = json.load(f)

    rows = []
    for slot in stage02[:TOUCHUP_COUNT]:
        output_file = slot.get("output_file", "")
        if not output_file:
            phase = slot.get("phase", "")
            lesson = slot.get("lesson", "")
            output_file = str(OUTPUT_ROOT / phase / lesson / "docs" / "en.md")

        rows.append({
            "id": slot["id"],
            "phase": slot.get("phase", ""),
            "lesson": slot.get("lesson", ""),
            "topic": slot.get("topic", ""),
            "output_file": output_file,
            "status": "pending",
        })

    TOUCHUP_MANIFEST.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Created touchup manifest: {len(rows)} lessons")
    return rows


def update_touchup_row(rows: list[dict], lesson_id: str, status: str) -> None:
    with touchup_lock:
        for row in rows:
            if row["id"] == lesson_id:
                row["status"] = status
                row["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                break
        tmp = TOUCHUP_MANIFEST.with_suffix(".tmp")
        tmp.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
        tmp.replace(TOUCHUP_MANIFEST)


# ── Single lesson touch-up ────────────────────────────────────────────────────

def touchup_lesson(row: dict, client: OpenAI, dry_run: bool = False) -> tuple[str, str]:
    """Revise one lesson. Returns (lesson_id, 'done'|'failed')."""
    lesson_id = row["id"]
    output_path = Path(row["output_file"])

    if not output_path.exists():
        print(f"  [SKIP] {lesson_id}: output file not found at {output_path}")
        return lesson_id, "failed"

    existing_content = output_path.read_text(encoding="utf-8")
    gaps = diagnose_gaps(existing_content)

    if dry_run:
        print(f"  [DRY] {lesson_id}: gaps={gaps}")
        return lesson_id, "pending"

    gap_text = "\n".join(f"- {g}" for g in gaps)
    user_prompt = f"""LESSON ID: {lesson_id}
TOPIC: {row.get('topic', lesson_id)}

GAPS TO FIX:
{gap_text}

EXISTING LESSON:
{existing_content}

Revise the lesson to fix all listed gaps. Output the complete revised lesson."""

    wait_if_paused()
    wait_if_sentinel()

    try:
        response = client.chat.completions.create(
            model="GLM-5.1",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": user_prompt},
            ],
            timeout=180,
        )
        revised = response.choices[0].message.content.strip()
    except RateLimitError:
        global_rate_pause(30)
        return lesson_id, "failed"
    except Exception as e:
        print(f"  [ERR] {lesson_id}: {e}")
        return lesson_id, "failed"

    if len(revised) < 500:
        print(f"  [FAIL] {lesson_id}: Output too short ({len(revised)} chars)")
        return lesson_id, "failed"

    # Atomic write
    tmp = output_path.with_suffix(".tmp")
    tmp.write_text(revised, encoding="utf-8")
    tmp.replace(output_path)

    return lesson_id, "done"


# ── Progress tracking ─────────────────────────────────────────────────────────

_progress_lock = threading.Lock()
_completed = 0
_start_time = 0.0


def report_progress(total: int, status: str, lesson_id: str) -> None:
    global _completed
    with _progress_lock:
        _completed += 1
        elapsed = time.time() - _start_time
        rate = _completed / elapsed if elapsed > 0 else 0
        remaining = total - _completed
        eta = remaining / rate / 60 if rate > 0 else 0
        print(f"  [{_completed}/{total}] {lesson_id} -> {status} | {rate:.1f} req/s | ETA {eta:.1f}min")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    global _start_time

    parser = argparse.ArgumentParser(description="Touch-up pre-GLM-5.1 lessons")
    parser.add_argument("--dry-run",      action="store_true", help="Preview gaps without writing")
    parser.add_argument("--workers",      type=int, default=3, help="Parallel workers (default 3)")
    parser.add_argument("--lesson",       type=str, help="Touch up a single lesson by ID")
    parser.add_argument("--retry-failed", action="store_true", help="Retry only failed rows")
    parser.add_argument("--rebuild",      action="store_true", help="Rebuild touchup manifest from scratch")
    args = parser.parse_args()

    api_key = os.environ.get("ZHIPUAI_API_KEY")
    if not api_key and not args.dry_run:
        print("ERROR: ZHIPUAI_API_KEY not set. Run: export $(grep -v '^#' .env | xargs)")
        sys.exit(1)

    client = OpenAI(
        api_key=api_key or "dry-run",
        base_url="https://open.bigmodel.cn/api/paas/v4/",
    )

    rows = build_touchup_manifest(force=args.rebuild)

    # Filter targets
    if args.lesson:
        targets = [r for r in rows if r["id"] == args.lesson]
        if not targets:
            print(f"ERROR: lesson '{args.lesson}' not in touchup manifest")
            sys.exit(1)
    elif args.retry_failed:
        targets = [r for r in rows if r["status"] == "failed"]
        if not targets:
            print("No failed lessons to retry.")
            return
    else:
        targets = [r for r in rows if r["status"] == "pending"]

    if not targets:
        done  = sum(1 for r in rows if r["status"] == "done")
        total = len(rows)
        print(f"All lessons already processed: {done}/{total} done")
        return

    if args.dry_run:
        print(f"\nDRY RUN — diagnosing {len(targets)} lessons:")
        for row in targets:
            touchup_lesson(row, client, dry_run=True)
        return

    print(f"\nTouching up {len(targets)} lessons | workers={args.workers} | dry_run=False\n")
    _start_time = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(touchup_lesson, row, client): row for row in targets}
        for future in as_completed(futures):
            lesson_id, status = future.result()
            update_touchup_row(rows, lesson_id, status)
            report_progress(len(targets), status, lesson_id)

    elapsed = (time.time() - _start_time) / 60
    done   = sum(1 for r in rows if r["status"] == "done")
    failed = sum(1 for r in rows if r["status"] == "failed")

    print(f"\n-- Summary ----------------------------------")
    print(f"  Done:   {done}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(targets)} in {elapsed:.1f}min")

    if failed:
        print(f"\n  Re-run failed: python3 skills/operator-kit/dispatch-touchup.py --retry-failed")


if __name__ == "__main__":
    main()
