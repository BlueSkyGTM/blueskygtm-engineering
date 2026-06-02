# Batch 006 — Phase 14 Schema Repair (Lessons 01–09)

**Job type:** schema_repair
**Phase:** 14-agent-engineering
**Lessons:** 01–09 (9 lessons)
**Prepared:** 2026-06-02
**Status:** PENDING

---

## Task

Each lesson has 7 questions with stages:
`pre, pre, check, check, check, post, post`

Trim to 6 questions: `pre, check, check, check, post, post`

**Drop rule:**
- Drop the **second** `pre` question (index 1)

**Do not touch:** question text, options, correct index, or explanations on the surviving 6 questions.

---

## Lessons

| # | Dir slug | Path |
|---|----------|------|
| 01 | 01-the-agent-loop | `phases/14-agent-engineering/01-the-agent-loop/quiz.json` |
| 02 | 02-rewoo-plan-and-execute | `phases/14-agent-engineering/02-rewoo-plan-and-execute/quiz.json` |
| 03 | 03-reflexion-verbal-rl | `phases/14-agent-engineering/03-reflexion-verbal-rl/quiz.json` |
| 04 | 04-tree-of-thoughts-lats | `phases/14-agent-engineering/04-tree-of-thoughts-lats/quiz.json` |
| 05 | 05-self-refine-and-critic | `phases/14-agent-engineering/05-self-refine-and-critic/quiz.json` |
| 06 | 06-tool-use-and-function-calling | `phases/14-agent-engineering/06-tool-use-and-function-calling/quiz.json` |
| 07 | 07-memory-virtual-context-memgpt | `phases/14-agent-engineering/07-memory-virtual-context-memgpt/quiz.json` |
| 08 | 08-memory-blocks-sleep-time-compute | `phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/quiz.json` |
| 09 | 09-hybrid-memory-mem0 | `phases/14-agent-engineering/09-hybrid-memory-mem0/quiz.json` |

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

1. Read `quiz.json` — confirm 7q with stages `pre, pre, check, check, check, post, post`
2. Remove question at index 1 (second `pre`)
3. Verify resulting array is exactly 6 questions with stages `pre, check, check, check, post, post`
4. Run `python3 scripts/audit_lessons.py phases/14-agent-engineering/<slug>` — must pass
5. Verify stage sequence manually: `pre, check, check, check, post, post`
6. Commit: `fix(phase-14/<slug>): trim quiz schema 7q → 6q`

---

## Audit gate

```bash
python3 scripts/audit_lessons.py phases/14-agent-engineering/01-the-agent-loop
python3 scripts/audit_lessons.py phases/14-agent-engineering/02-rewoo-plan-and-execute
python3 scripts/audit_lessons.py phases/14-agent-engineering/03-reflexion-verbal-rl
python3 scripts/audit_lessons.py phases/14-agent-engineering/04-tree-of-thoughts-lats
python3 scripts/audit_lessons.py phases/14-agent-engineering/05-self-refine-and-critic
python3 scripts/audit_lessons.py phases/14-agent-engineering/06-tool-use-and-function-calling
python3 scripts/audit_lessons.py phases/14-agent-engineering/07-memory-virtual-context-memgpt
python3 scripts/audit_lessons.py phases/14-agent-engineering/08-memory-blocks-sleep-time-compute
python3 scripts/audit_lessons.py phases/14-agent-engineering/09-hybrid-memory-mem0
```

---

## Notes

- Drop only index 1 (one fewer drop than Phase 05 — Phase 14 has 7q not 8q)
- Stage sequence not enforced by CI (L014 pending) — verify manually before each commit
- Next batch: Phase 14 lessons 10–18
