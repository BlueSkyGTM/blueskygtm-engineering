# Batch 005 — Phase 05 Schema Repair (Lessons 28–29, Final)

**Job type:** schema_repair
**Phase:** 05-nlp-foundations-to-advanced
**Lessons:** 28–29 (2 lessons — Phase 05 complete after this)
**Prepared:** 2026-06-02
**Status:** PENDING

---

## Task

Each lesson has 8 questions with stages:
`pre, pre, check, check, check, post, post, post`

Trim to 6 questions: `pre, check, check, check, post, post`

**Drop rule:**
- Drop the **second** `pre` question (index 1)
- Drop the **third** `post` question (index 7, the last one)

**Do not touch:** question text, options, correct index, or explanations on the surviving 6 questions.

---

## Lessons

| # | Dir slug | Path |
|---|----------|------|
| 28 | 28-long-context-evaluation | `phases/05-nlp-foundations-to-advanced/28-long-context-evaluation/quiz.json` |
| 29 | 29-dialogue-state-tracking | `phases/05-nlp-foundations-to-advanced/29-dialogue-state-tracking/quiz.json` |

---

## Locked skeleton (output shape)

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

For each lesson:

1. Read `quiz.json` — confirm 8q with stages `pre, pre, check, check, check, post, post, post`
2. Remove question at index 1 (second `pre`)
3. Remove question at index 7 of the original (last `post`)
4. Verify resulting array is exactly 6 questions with stages `pre, check, check, check, post, post`
5. Run `python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/<slug>` — must pass
6. Verify stage sequence manually: `pre, check, check, check, post, post`
7. Commit: `fix(phase-05/<slug>): trim quiz schema 8q → 6q`

---

## Audit gate

```bash
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/28-long-context-evaluation
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/29-dialogue-state-tracking
```

---

## Notes

- Phase 05 schema repair complete after this batch
- Next: Phase 14 (batches 006–010) — same drop rule, 42 lessons, 7q → 6q
