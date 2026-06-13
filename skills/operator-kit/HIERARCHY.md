# ICM Hierarchy — Getting Started

This is the entry point for any agent or operator new to the BlueSkyGTM curriculum pipeline.

---

## The ICM Pattern

ICM = Independent Context Manifest. Every agent in this system gets a folder. The folder contains:
- **CONTEXT.md** — what this agent owns, what it reads, what it writes, how to escalate
- **status.json** — written by the running subprocess; polled by the monitoring agent
- **Tools** — scripts the agent can call (dispatch-peon.py, watchdog.py, etc.)

The upstream trigger IS the instruction. When the Conductor hands a Taskmaster a path to its CONTEXT.md, that's all it needs. No verbal briefing. No repo dump. Just the folder.

---

## Five Tiers, Staged Activation

```
Director (User)
  └─ Conductor (Claude Code)         ← you are here if you're reading this
       └─ Taskmasters (Claude sub-agents)    ← one active at a time per stage
            └─ Handlers (GLM-5.1)           ← 3-5 active, within worker budget
                 └─ Peons (GLM-Flash)       ← called synchronously by Handler, then exit
```

All five tiers are never active simultaneously. Peons are invoked inside Handler calls. Taskmasters run one stage at a time. The system is a pipeline, not a web.

---

## Quick Start for Conductor

### Run a single stage (Conductor does this directly):
```powershell
.\run.ps1 stage02 --sample 5      # human gate: review 5 lessons before full run
.\run.ps1 stage02 --workers 5     # full run
.\run.ps1 status                   # check all three stages
```

### Spawn a Taskmaster sub-agent (for autonomous runs):
See `TASKMASTER-PROTOCOL.md` for the Agent tool prompt template.
Point the sub-agent at `taskmasters/stage02-injector/CONTEXT.md`.

### Start the watchdog (run in background while dispatcher runs):
```powershell
python3 skills/operator-kit/watchdog.py --stage 02
```

### Validate the peon endpoint before first use:
```powershell
python3 skills/operator-kit/dispatch-peon.py --smoke-test
```

---

## Key Files

| File | Purpose |
|------|---------|
| `HANDLERS.md` | Full registry of every agent: what it does, failure modes, escalation |
| `DISPATCHERS.md` | CLI reference for run.ps1, stage flags, monitoring, recovery |
| `TASKMASTER-PROTOCOL.md` | How to spawn and brief Taskmaster sub-agents |
| `watchdog.py` | Stall monitor — Conductor runs this, not Director |
| `dispatch-peon.py` | Peon caller — used by GLM-5.1 Handlers for interrupt subtasks |
| `taskmasters/` | One folder per Taskmaster role, each with its own CONTEXT.md |

---

## Worker Budget (global)

**Max 5 concurrent GLM API calls across all active agents.**

| Active Taskmasters | Workers per Taskmaster |
|--------------------|----------------------|
| 1 | 5 |
| 2 | 2 |
| 3 | 1 |

Peon calls (GLM-Flash) are synchronous and nested inside Handler calls — they count against the budget.

---

## Escalation in One Line Per Tier

- **Peon fails** → raises PeonError → Handler uses fallback marker ([CITATION NEEDED])
- **Handler fails 3x** → row marked `failed` → Taskmaster sees it in status.json
- **Taskmaster subprocess fails** → retries once → reports BLOCKED to Conductor
- **Conductor stuck** → one message to Director with what's blocked and what was tried
- **Watchdog escalates** → writes to watchdog-recovery.log → Conductor reads it
