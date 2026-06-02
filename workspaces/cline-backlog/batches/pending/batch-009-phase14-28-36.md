# Batch 009 — Phase 14 Schema Repair (Lessons 28–36)

**Job type:** schema_repair
**Phase:** 14-agent-engineering
**Lessons:** 28–36 (9 lessons)
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
| 28 | 28-orchestration-patterns | `phases/14-agent-engineering/28-orchestration-patterns/quiz.json` |
| 29 | 29-production-runtimes | `phases/14-agent-engineering/29-production-runtimes/quiz.json` |
| 30 | 30-eval-driven-agent-development | `phases/14-agent-engineering/30-eval-driven-agent-development/quiz.json` |
| 31 | 31-agent-workbench-why-models-fail | `phases/14-agent-engineering/31-agent-workbench-why-models-fail/quiz.json` |
| 32 | 32-minimal-agent-workbench | `phases/14-agent-engineering/32-minimal-agent-workbench/quiz.json` |
| 33 | 33-instructions-as-executable-constraints | `phases/14-agent-engineering/33-instructions-as-executable-constraints/quiz.json` |
| 34 | 34-repo-memory-and-state | `phases/14-agent-engineering/34-repo-memory-and-state/quiz.json` |
| 35 | 35-initialization-scripts | `phases/14-agent-engineering/35-initialization-scripts/quiz.json` |
| 36 | 36-scope-contracts | `phases/14-agent-engineering/36-scope-contracts/quiz.json` |

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
for slug in 28-orchestration-patterns 29-production-runtimes 30-eval-driven-agent-development 31-agent-workbench-why-models-fail 32-minimal-agent-workbench 33-instructions-as-executable-constraints 34-repo-memory-and-state 35-initialization-scripts 36-scope-contracts; do
  python3 scripts/audit_lessons.py phases/14-agent-engineering/$slug
done
```
