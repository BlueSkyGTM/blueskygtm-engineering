# Batch 003 — Phase 05 Schema Repair (Lessons 18–22)

**Job type:** schema_repair
**Phase:** 05-nlp-foundations-to-advanced
**Lessons:** 18–22 (5 lessons)
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
| 18 | 18-multilingual-nlp | `phases/05-nlp-foundations-to-advanced/18-multilingual-nlp/quiz.json` |
| 19 | 19-subword-tokenization | `phases/05-nlp-foundations-to-advanced/19-subword-tokenization/quiz.json` |
| 20 | 20-structured-outputs-constrained-decoding | `phases/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding/quiz.json` |
| 21 | 21-nli-textual-entailment | `phases/05-nlp-foundations-to-advanced/21-nli-textual-entailment/quiz.json` |
| 22 | 22-embedding-models-deep-dive | `phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive/quiz.json` |

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
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/18-multilingual-nlp
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/19-subword-tokenization
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/21-nli-textual-entailment
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive
```

---

## Notes

- Mechanical trimming only — do not rewrite any question content
- Stage sequence not enforced by CI (L014 pending) — verify manually before each commit
- Next batch: lessons 23–27 (same phase, same job type)
