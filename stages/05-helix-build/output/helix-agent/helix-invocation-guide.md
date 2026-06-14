# Helix — How to Use Your Tutor

*This guide ships with Zone 04 Lesson 01. It is not referenced in Zones 01–03.*

---

## What Just Happened

You opened Claude Code Desktop in your mission command folder. The response you got wasn't generic — it named your business, your zone, your due cards. That's Helix. It's been reading your repo.

Helix is not a chatbot. It is a governed tutor: it assesses your state, selects a response mode, executes, and checks. Every response is the result of that loop.

---

## How to Open Helix

```
cd your-mission-command-folder
claude
```

That's it. Claude Code Desktop reads `CLAUDE.md` in your working directory. When that file is Helix's operating layer, you're talking to Helix. No flags, no invocation command, no special syntax.

---

## What Helix Does at Session Start

Every time you open Claude Code in your mission command, Helix:

1. Reads `progress/progress.json` — your current zone, lesson, and FSRS card states
2. Scans your filesystem — which artifacts exist, which are missing
3. Opens with a grounded greeting — current position + what needs attention

You don't trigger this. It happens automatically before your first message.

---

## Working Through a Lesson

**Asking a concept question:**
> "What is cross-entropy loss?"

Helix explains the mechanism first, then shows where it applies in your context. It ends with a check question — not "does that make sense?" but something specific you can answer.

**After reading a lesson:**
> "I read the attention mechanism lesson"

Helix will quiz you before explaining further. This is intentional — recall before re-explanation is how FSRS works. You'll see: "I'm going to quiz you on this before explaining — you said you've read the lesson, so let's check recall first."

**When you're stuck:**
> "I don't understand why we need positional encoding"

Helix gives you the next useful piece — not a re-explanation of the whole concept. If you're still stuck after a hint, it will offer to switch to explanation mode.

---

## Review Sessions

Check what's due:
```bash
python helix/fsrs-scheduler.py due
```

Start your session by telling Helix:
> "I have 4 cards due, let's review"

Helix enters quiz mode. It presents one card at a time. After each card:
- You answer
- Helix scores it: "Correct." or "Incorrect."
- You rate your recall: **1=Again  2=Hard  3=Good  4=Easy**

At the end of the session, record your ratings:
```bash
python helix/fsrs-scheduler.py update
```

Then commit:
```bash
git add progress/progress.json
git commit -m "review: Zone 04 session"
```

Your fork is the cartridge. Ratings that aren't committed don't persist.

---

## Running Exercises

Exercises in this course run in the terminal. Copy the command from the lesson, run it, observe the output, paste it into the chat.

```bash
# Example: running a lesson exercise
python exercises/attention-mechanism.py
```

Paste the output to Helix. It reads what happened and responds based on what it sees.

There is no IDE. This is not a temporary constraint — it's the environment. Claude Code Desktop and the terminal are how practitioners build at scale.

---

## Stats

```bash
python helix/fsrs-scheduler.py stats
```

Shows: total cards, cards reviewed, cards graduated (stability > 21 days), total lapses, average stability, breakdown by zone.

---

## Seeding Cards from the Quiz Bank

If your FSRS deck isn't initialized yet:

```bash
python helix/fsrs-scheduler.py init stages/04-quiz-recall/output/quiz-bank/
```

This reads every `cards.json` in the quiz bank and seeds `progress/progress.json` with initial FSRS states. It never overwrites existing states.

---

## When Helix Doesn't Know Something

If you ask about a topic not in `phases/`:
> "That's outside the current curriculum. The closest thing we cover is [X] in Zone [N]."

One sentence. No apology. Redirect only.

If you think Helix is wrong about something, ask: "How do you know that?" It will cite the specific lesson file, handbook cluster, or paper. It will not say "I know this from my training."

---

## Operator Mode (Zone 20 Only)

When you complete Stage 10 validation, your progress file shows all gates cleared. At that point:

```
/rename <your-command-center-name>
/rename-helix <name>
```

The course was itself a loop. You were inside it the whole time.

Until then: this is Mission Command and your tutor is Helix.
