# Batch 004 — Phase 05 Schema Repair (Lessons 23–27)

**Job type:** schema_repair
**Phase:** 05-nlp-foundations-to-advanced
**Lessons:** 23–27 (5 lessons)
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
| 23 | 23-chunking-strategies-rag | `phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag/quiz.json` |
| 24 | 24-coreference-resolution | `phases/05-nlp-foundations-to-advanced/24-coreference-resolution/quiz.json` |
| 25 | 25-entity-linking | `phases/05-nlp-foundations-to-advanced/25-entity-linking/quiz.json` |
| 26 | 26-relation-extraction-kg | `phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg/quiz.json` |
| 27 | 27-llm-evaluation-frameworks | `phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks/quiz.json` |

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
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/24-coreference-resolution
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/25-entity-linking
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks
```

---

## Notes

- Mechanical trimming only — do not rewrite any question content
- Stage sequence not enforced by CI (L014 pending) — verify manually before each commit
- Next batch: lessons 28–29 (phase 05 final), then Phase 14 schema repair begins
