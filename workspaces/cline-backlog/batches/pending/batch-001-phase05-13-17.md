# Batch 001 — Phase 05 Schema Repair (Lessons 13–17)

**Job type:** schema_repair  
**Phase:** 05-nlp-foundations-to-advanced  
**Lessons:** 13–17 (5 of 17 total in this phase)  
**Prepared:** 2026-05-31  
**Status:** PENDING

---

## Task

Each lesson in this batch has 8 questions with stages:
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
| 13 | 13-question-answering | `phases/05-nlp-foundations-to-advanced/13-question-answering/quiz.json` |
| 14 | 14-information-retrieval-search | `phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/quiz.json` |
| 15 | 15-topic-modeling | `phases/05-nlp-foundations-to-advanced/15-topic-modeling/quiz.json` |
| 16 | 16-text-generation-pre-transformer | `phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/quiz.json` |
| 17 | 17-chatbots-rule-to-neural | `phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural/quiz.json` |

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

After all 5 lessons:

```bash
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/13-question-answering
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/14-information-retrieval-search
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/15-topic-modeling
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer
python3 scripts/audit_lessons.py phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural
```

---

## Notes

- Do not rewrite any question content — this is mechanical trimming only
- Stage sequence is not yet enforced by CI (L014 pending) — verify manually before each commit
- Next batch: lessons 18–22 (same phase, same job type)
