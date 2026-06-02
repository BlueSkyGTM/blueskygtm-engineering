# Batch 008 — Phase 14 Schema Repair (Lessons 19–27)

**Job type:** schema_repair
**Phase:** 14-agent-engineering
**Lessons:** 19–27 (9 lessons)
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
| 19 | 19-benchmarks-swebench-gaia | `phases/14-agent-engineering/19-benchmarks-swebench-gaia/quiz.json` |
| 20 | 20-benchmarks-webarena-osworld | `phases/14-agent-engineering/20-benchmarks-webarena-osworld/quiz.json` |
| 21 | 21-computer-use-agents | `phases/14-agent-engineering/21-computer-use-agents/quiz.json` |
| 22 | 22-voice-agents-pipecat-livekit | `phases/14-agent-engineering/22-voice-agents-pipecat-livekit/quiz.json` |
| 23 | 23-otel-genai-conventions | `phases/14-agent-engineering/23-otel-genai-conventions/quiz.json` |
| 24 | 24-agent-observability-platforms | `phases/14-agent-engineering/24-agent-observability-platforms/quiz.json` |
| 25 | 25-multi-agent-debate | `phases/14-agent-engineering/25-multi-agent-debate/quiz.json` |
| 26 | 26-failure-modes-agentic | `phases/14-agent-engineering/26-failure-modes-agentic/quiz.json` |
| 27 | 27-prompt-injection-defense | `phases/14-agent-engineering/27-prompt-injection-defense/quiz.json` |

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
for slug in 19-benchmarks-swebench-gaia 20-benchmarks-webarena-osworld 21-computer-use-agents 22-voice-agents-pipecat-livekit 23-otel-genai-conventions 24-agent-observability-platforms 25-multi-agent-debate 26-failure-modes-agentic 27-prompt-injection-defense; do
  python3 scripts/audit_lessons.py phases/14-agent-engineering/$slug
done
```
