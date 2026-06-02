# Batch 010 — Phase 14 Schema Repair (Lessons 37–42, Final)

**Job type:** schema_repair
**Phase:** 14-agent-engineering
**Lessons:** 37–42 (6 lessons — Phase 14 complete after this)
**Prepared:** 2026-06-02
**Status:** PENDING

---

## Task

Drop the **second** `pre` question (index 1) from each 7q quiz.
Result: `pre, check, check, check, post, post` (6q).

---

## Lessons

| # | Dir slug | Path |
|---|----------|------|
| 37 | 37-runtime-feedback-loops | `phases/14-agent-engineering/37-runtime-feedback-loops/quiz.json` |
| 38 | 38-verification-gates | `phases/14-agent-engineering/38-verification-gates/quiz.json` |
| 39 | 39-reviewer-agent | `phases/14-agent-engineering/39-reviewer-agent/quiz.json` |
| 40 | 40-multi-session-handoff | `phases/14-agent-engineering/40-multi-session-handoff/quiz.json` |
| 41 | 41-workbench-for-real-repos | `phases/14-agent-engineering/41-workbench-for-real-repos/quiz.json` |
| 42 | 42-agent-workbench-capstone | `phases/14-agent-engineering/42-agent-workbench-capstone/quiz.json` |

---

## Locked skeleton

```json
{
  "lesson": "<dir-slug>",
  "title": "<from existing quiz.json title field>",
  "questions": [
    {"stage": "pre",   "question": "", "options": ["","","",""], "correct": 0, "explanation": ""},
    {"stage": "check", "question": "", "options": ["","","",""], "correct": 0, "explanation": ""},
    {"stage": "check", "question": "", "options": ["","","",""], "correct": 0, "explanation": ""},
    {"stage": "check", "question": "", "options": ["","","",""], "correct": 0, "explanation": ""},
    {"stage": "post",  "question": "", "options": ["","","",""], "correct": 0, "explanation": ""},
    {"stage": "post",  "question": "", "options": ["","","",""], "correct": 0, "explanation": ""}
  ]
}
```

---

## Per-lesson procedure

1. Read `quiz.json` — confirm 7q with stages `pre, pre, check, check, check, post, post`
2. Remove question at index 1 (second `pre`)
3. Verify 6q: `pre, check, check, check, post, post`
4. Run `python3 scripts/audit_lessons.py phases/14-agent-engineering/<slug>` — must pass
5. Verify stage sequence manually
6. Commit: `fix(phase-14/<slug>): trim quiz schema 7q → 6q`

---

## Audit gate

```bash
for slug in 37-runtime-feedback-loops 38-verification-gates 39-reviewer-agent 40-multi-session-handoff 41-workbench-for-real-repos 42-agent-workbench-capstone; do
  python3 scripts/audit_lessons.py phases/14-agent-engineering/$slug
done
```

---

## Notes

- Phase 14 schema repair complete after this batch
- P0 schema repair fully done after this batch (Phase 05 + Phase 14)
- Next priority: P1 — create_quiz for Phases 06–10, 12–13, 15–16 (~154 lessons)
- Regenerate manifest before P1 begins: `python3 quiz-factory/scripts/generate_manifest.py --write`
