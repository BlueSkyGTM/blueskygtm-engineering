# Taskmaster Protocol — How the Conductor Spawns Sub-Agents

Taskmasters are Claude sub-agents spawned by the Conductor via the Agent tool. They are **thin launchers**, not heavy orchestrators. Their job is to read a CONTEXT.md, launch a Python subprocess, monitor it via status.json polling, and report back to the Conductor when done.

A Taskmaster should never accumulate lesson content or tool call history in its context. The moment it does, it risks context overflow and becomes unreliable. Keep Taskmasters stateless.

---

## The Pattern

```
Conductor reads: skills/operator-kit/taskmasters/<role>/CONTEXT.md
Conductor tells Agent tool: "You are a Taskmaster. Read CONTEXT.md at <path> and execute it."

Taskmaster (Claude sub-agent):
  1. Reads CONTEXT.md → knows exactly what to run and where outputs go
  2. Launches Python dispatcher as a subprocess (detached on Windows, background on Unix)
  3. Polls status.json every 60s (not accumulating output in context)
  4. When status.json shows "finished: true" OR all rows are done/failed:
     - Reports summary to Conductor (done count, failed count, any blocked rows)
     - Exits
```

---

## Conductor Prompt Template

When spawning a Taskmaster, the Conductor uses this Agent tool prompt:

```
You are a Taskmaster for the BlueSkyGTM curriculum pipeline.

Your CONTEXT.md is at: skills/operator-kit/taskmasters/<role>/CONTEXT.md

Read it now. It tells you exactly what to run, where outputs go, and how to monitor progress.

RULES:
- You are a thin launcher. Do NOT read lesson output files into your context.
- Do NOT accumulate GLM responses in your context.
- Poll status.json every 60 seconds. Read only the "done", "failed", "pending" fields.
- Report back when finished: total done, total failed, any rows with >3 failures.
- If subprocess exits with non-zero code: retry once, then report BLOCKED to Conductor.
```

---

## Worker Budget

The global Z.ai worker budget is **5 concurrent GLM calls across all Taskmasters**.

If the Conductor runs two Taskmasters in parallel, each must use `--workers 2` or `--workers 3` (not 5). The Conductor sets this based on how many Taskmasters are active:

| Active Taskmasters | Workers per Taskmaster |
|--------------------|----------------------|
| 1 | 5 |
| 2 | 2 |
| 3 | 1 |
| 4+ | 1 (serialize where possible) |

---

## Per-Taskmaster Manifests

Each Taskmaster writes to its own status.json. It does NOT write to the shared stage manifest during the run — only on completion merge.

On completion, the Taskmaster reports:
- How many rows it processed
- Which rows are `done`, which are `failed`
- The Conductor updates the main manifest by merging the Taskmaster's results

This prevents cross-process write contention.

---

## Folder Structure

```
skills/operator-kit/taskmasters/
  stage02-injector/
    CONTEXT.md        ← Taskmaster reads this on launch
    status.json       ← written by the subprocess; Taskmaster polls this
  stage03-exercises/
    CONTEXT.md
    status.json
  stage04-quizzes/
    CONTEXT.md
    status.json
```

---

## When to Use Multiple Taskmasters in Parallel

Taskmasters can run in parallel when their stages are independent. The current pipeline is sequential (Stage 03 requires Stage 02 done rows), so Taskmasters run one at a time. Future use cases for parallel Taskmasters:

- Running the same stage across different phase slices simultaneously (e.g., Taskmaster A handles phases 00-05, Taskmaster B handles phases 06-12)
- Running a quality check Taskmaster in parallel with a generation Taskmaster

---

## Escalation

| Event | Taskmaster does |
|-------|----------------|
| Subprocess exits non-zero | Retry once; if still fails, report BLOCKED |
| status.json absent >2 min | Report stall to Conductor; Conductor runs watchdog.py |
| >20% rows failed | Complete normally; flag high failure rate in report |
| Scope drift (unexpected output) | Stop; report SCOPE_DRIFT to Conductor with details |
