# Dispatcher System — Reference & How-To

The dispatcher system generates curriculum content at scale by routing lesson slots to GLM-5.1 via the Z.ai API. Three dispatchers cover three pipeline stages; `run.ps1` wraps all three with `.env` loading.

---

## Architecture

```
run.ps1
  └─ loads .env (ZHIPUAI_API_KEY)
  └─ routes to dispatcher

dispatch-stage02.py           dispatch-stage03.py           dispatch-stage04.py
  manifest.json (510 rows)      manifest.json (built from S2)  manifest.json (built from S2)
  ThreadPoolExecutor            ThreadPoolExecutor              ThreadPoolExecutor
  GLM-5.1 (max_tokens=8000)    GLM-5.1 (max_tokens=2000)      GLM-5.1 (max_tokens=2500)
  → hybrid-lessons/.../en.md   → exercise-specs/.../md         → quiz-bank/.../cards.json
```

**Governed maze pattern:** Each GLM-5.1 call receives only a ≤500-token extract of the author brief + the specific lesson's outline/content. The full repo is never passed. This keeps GLM focused and prevents context bleed.

---

## Stage 02 — Lesson Injection

**Input:** `stages/02-lesson-injection/output/manifest.json` (510 rows from Stage 01)  
**Output:** `stages/02-lesson-injection/output/hybrid-lessons/<phase>/<lesson>/docs/en.md`

Each lesson follows the six-beat structure: Learning Objectives / The Problem / The Concept / Build It / Use It / Ship It / Exercises / Key Terms / Sources.

### CLI flags

| Flag | Default | Effect |
|------|---------|--------|
| `--workers N` | 3 | Parallel threads. Safe range: 3–5. Never exceed 6 without monitoring 429 rate. |
| `--sample N` | 0 (all) | Run only the first N pending lessons. Use 5 for the human gate before a full run. |
| `--phase SLUG` | all | Filter to one phase slug, e.g. `01-math-foundations`. |
| `--retry-failed` | off | Include rows with `status: failed` in the run. |
| `--dry-run` | off | Print what would run without calling the API. Manifest is not mutated. |

### Output file

`stages/02-lesson-injection/output/hybrid-lessons/<phase>/<lesson>/docs/en.md`

Minimum valid output: 500 characters. Shorter output is rejected and the row is marked `failed`.

---

## Stage 03 — Exercise Design

**Input:** Stage 02 manifest (reads `done` rows) + the generated `docs/en.md` for each lesson  
**Output:** `stages/03-exercise-design/output/exercise-specs/<phase>/<lesson>/exercises.md`

Generates 4–6 exercises per lesson. Hard exercises (5–6) specify artifact paths:
- `signals/examples/<name>.py`
- `handlers/<name>.py`
- `outputs/skill-<name>.md`

### CLI flags

Same as Stage 02: `--workers`, `--sample`, `--phase`, `--retry-failed`, `--dry-run`.

**Important:** Stage 03 reads Stage 02 lesson content and strips any `## GTM Redirect Rules` bleed via regex before passing to GLM. If Stage 02 output contains bleed, Stage 03 handles it automatically.

---

## Stage 04 — Quiz Bank

**Input:** Stage 02 manifest (done rows) + Stage 03 exercise specs  
**Output:** `stages/04-quiz-recall/output/quiz-bank/<phase>/<lesson>/cards.json`

Generates exactly 6 questions per lesson in FSRS schema:

| ID | Type | When shown |
|----|------|-----------|
| `pre-q0` | pre | Before reading — tests baseline |
| `check-q0` | check | During lesson — section 1 |
| `check-q1` | check | During lesson — section 2 (must reference an exercise) |
| `check-q2` | check | During lesson — section 3 |
| `post-q0` | post | After lesson — requires applying the concept |
| `post-q1` | post | After lesson — applied to GTM context |

Output is validated: must be valid JSON and must contain exactly 6 questions. Markdown fences are stripped automatically if GLM wraps the output in ` ```json `.

### CLI flags

Same as Stage 02: `--workers`, `--sample`, `--phase`, `--retry-failed`, `--dry-run`.

---

## run.ps1 — Command Reference

Load `.env` and dispatch without manually exporting environment variables.

```powershell
.\run.ps1 <command> [flags]
```

| Command | Effect |
|---------|--------|
| `stage02` | Run Stage 02 dispatcher with any flags passed through |
| `stage03` | Run Stage 03 dispatcher |
| `stage04` | Run Stage 04 dispatcher |
| `status` | Print done/failed/pending counts for all three manifests |
| `check` | Print masked ZHIPUAI_API_KEY (confirms .env loaded) |

### Examples

```powershell
# Human gate: first 5 lessons only, review output before full run
.\run.ps1 stage02 --sample 5

# Full run at 5 workers
.\run.ps1 stage02 --workers 5

# Retry all failed rows from a previous run
.\run.ps1 stage02 --retry-failed --workers 5

# One phase at a time
.\run.ps1 stage02 --phase 01-math-foundations --workers 5

# Check pipeline health
.\run.ps1 status
```

---

## Self-Correction Mechanisms

All three dispatchers share the same reliability stack.

### Global rate pause

When any thread hits a 429 (rate limit), it sets a shared `threading.Event` that causes **all** threads to wait 30 seconds before their next API call. This prevents a rate-limit cascade from one thread triggering retries across all threads simultaneously.

### Circuit breaker

A rolling window tracks the last 10 completed jobs. If the failure rate exceeds 30%, all threads pause 60 seconds and the window resets. This catches sustained degradation (e.g. Z.ai outage) without terminating the run.

### API call timeout

Each GLM-5.1 call has `timeout=120`. If the API connection hangs, the thread raises a timeout error after 2 minutes, marks the row `failed`, and moves to the next job. Without this, a single hung connection would block a thread indefinitely.

### Pause sentinel

Create a file to freeze all threads without killing the process:

```powershell
# Pause (all threads will stop before their next API call)
New-Item stages/02-lesson-injection/output/.dispatcher-pause

# Resume
Remove-Item stages/02-lesson-injection/output/.dispatcher-pause
```

Use the same path pattern for Stage 03 (`stages/03-exercise-design/output/.dispatcher-pause`) and Stage 04 (`stages/04-quiz-recall/output/.dispatcher-pause`).

### Manifest writes

All manifest updates use atomic `tmp → rename` writes. If the process is killed mid-write, the manifest is never left in a corrupt state.

---

## Status Monitoring

### Quick status

```powershell
.\run.ps1 status
```

Output:
```
Stage 02: 57 done / 99 failed / 354 pending  (510 total)
Stage 03: no manifest yet
Stage 04: no manifest yet
```

### Live status (during a run)

The status file is updated every 10 completions:

```powershell
python3 -c "import json; print(json.dumps(json.load(open('stages/02-lesson-injection/output/status.json')), indent=2))"
```

Fields: `done`, `failed`, `pending`, `failure_rate`, `workers`, `elapsed_min`, `eta_min`, `updated_at`.

### Per-row status in the manifest

```powershell
python3 -c "
import json
from collections import Counter
rows = json.load(open('stages/02-lesson-injection/output/manifest.json'))
print(Counter(r['status'] for r in rows))
# List failed rows:
failed = [r['id'] for r in rows if r['status'] == 'failed']
print(f'Failed: {failed[:10]}')
"
```

---

## How to Run a Stage (Standard Procedure)

**Step 1: Verify prerequisites**

```powershell
# Check API key loaded
.\run.ps1 check

# Check Stage 02 has pending rows
.\run.ps1 status
```

**Step 2: Human gate — 5-lesson sample**

```powershell
.\run.ps1 stage02 --sample 5
```

Read 2–3 generated lessons in `stages/02-lesson-injection/output/hybrid-lessons/`. Verify:
- Six-beat structure present (Learning Objectives through Sources)
- No `## GTM Redirect Rules` bleed in output
- GTM application woven into AI concept beats
- Runnable code blocks present in Build It

**Step 3: Full run**

```powershell
.\run.ps1 stage02 --workers 5
```

Leave running. Terminal will show `[N/total] lesson-id -> done | rate | ETA`.

**Step 4: Retry failures**

```powershell
.\run.ps1 status   # check remaining failed count
.\run.ps1 stage02 --retry-failed --workers 3
```

**Step 5: Advance to next stage**

Stage 03 reads Stage 02 done rows automatically. No manifest prep needed.

```powershell
.\run.ps1 stage03 --sample 5   # human gate
.\run.ps1 stage03 --workers 5  # full run
```

---

## How to Recover from a Stalled Run

**Symptom:** Terminal shows no new output for 5+ minutes, blue blip in terminal tab, can't type.

**Cause:** The Python process is likely hung on a terminal lock or the ThreadPoolExecutor is waiting for a thread that timed out mid-KeyboardInterrupt. The `timeout=120` fix prevents new hangs, but old runs started without it may still be stuck.

**Recovery:**

1. Open Task Manager → find `python3.exe` → End Task
2. Open a new terminal tab
3. Check manifest state:
   ```powershell
   .\run.ps1 status
   ```
4. Resume with `--retry-failed`:
   ```powershell
   .\run.ps1 stage02 --retry-failed --workers 5
   ```

The manifest was written atomically at each completion, so no work is lost. Only the in-flight lessons at the moment of kill will be left as `failed` (not `done`), and `--retry-failed` picks them up.

---

## How to Pause Mid-Run Without Killing the Process

```powershell
# Create sentinel — all threads stop before their next API call (within ~30s)
New-Item stages/02-lesson-injection/output/.dispatcher-pause -ItemType File

# Inspect output, check status, etc.
.\run.ps1 status

# Resume — threads unblock immediately
Remove-Item stages/02-lesson-injection/output/.dispatcher-pause
```

---

## Failure Mode Reference

| Symptom | Cause | Fix |
|---------|-------|-----|
| `ZHIPUAI_API_KEY not set` | `.env` not loaded | Use `.\run.ps1` not `python3 ...` directly |
| Output too short (< 500 chars) | GLM returned thinking content only, no lesson | Automatic retry (up to 3x); if persistent, reduce `--workers` |
| `[429]` in output | Rate limit hit | Global backoff fires automatically; reduce workers if frequent |
| `[CIRCUIT BREAKER]` fires | >30% failure in 10 jobs | Z.ai degraded; wait 60s (auto), or pause with sentinel |
| Thread hangs (old run without timeout) | Missing `timeout=120` | Kill python3.exe, ensure dispatchers are updated, restart |
| `## GTM Redirect Rules` in Stage 02 output | GLM included input context in output | Strip manually or re-run that lesson; Stage 03 strips automatically |
| `manifest.json: FileNotFoundError` | Status file written on first 10 completions, not at start | Normal — wait for 10 completions or read manifest directly |

---

## Worker Count Guidelines

| Workers | Use case |
|---------|----------|
| 1 | Debugging a single lesson; tracing API calls |
| 3 | Conservative default; safe if quota is tight |
| 5 | Recommended with sufficient quota (95% remaining = safe) |
| 6 | Max tested without cascade failures; watch circuit breaker |
| 8+ | Confirmed cascade failures at this level — do not use |

The circuit breaker protects against cascade at higher worker counts, but recovery pauses (60s) reduce effective throughput. 5 workers with clean 429 rate outperforms 8 workers with frequent circuit trips.
