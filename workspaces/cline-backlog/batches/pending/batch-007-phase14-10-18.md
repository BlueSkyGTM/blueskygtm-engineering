# Batch 007 — Phase 14 Schema Repair (Lessons 10–18)

**Job type:** schema_repair
**Phase:** 14-agent-engineering
**Lessons:** 10–18 (9 lessons)
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
| 10 | 10-skill-libraries-voyager | `phases/14-agent-engineering/10-skill-libraries-voyager/quiz.json` |
| 11 | 11-planning-htn-and-evolutionary | `phases/14-agent-engineering/11-planning-htn-and-evolutionary/quiz.json` |
| 12 | 12-anthropic-workflow-patterns | `phases/14-agent-engineering/12-anthropic-workflow-patterns/quiz.json` |
| 13 | 13-langgraph-stateful-graphs | `phases/14-agent-engineering/13-langgraph-stateful-graphs/quiz.json` |
| 14 | 14-autogen-actor-model | `phases/14-agent-engineering/14-autogen-actor-model/quiz.json` |
| 15 | 15-crewai-role-based-crews | `phases/14-agent-engineering/15-crewai-role-based-crews/quiz.json` |
| 16 | 16-openai-agents-sdk | `phases/14-agent-engineering/16-openai-agents-sdk/quiz.json` |
| 17 | 17-claude-agent-sdk | `phases/14-agent-engineering/17-claude-agent-sdk/quiz.json` |
| 18 | 18-agno-and-mastra-runtimes | `phases/14-agent-engineering/18-agno-and-mastra-runtimes/quiz.json` |

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
for slug in 10-skill-libraries-voyager 11-planning-htn-and-evolutionary 12-anthropic-workflow-patterns 13-langgraph-stateful-graphs 14-autogen-actor-model 15-crewai-role-based-crews 16-openai-agents-sdk 17-claude-agent-sdk 18-agno-and-mastra-runtimes; do
  python3 scripts/audit_lessons.py phases/14-agent-engineering/$slug
done
```
