"""
Watchdog — dispatcher stall monitor and auto-recovery.

Conductor runs this (not the Director). Polls stage status.json files, detects
stalls, gracefully stops via PAUSE_SENTINEL, then restarts with --retry-failed.

Usage:
  python3 skills/operator-kit/watchdog.py --stage 02
  python3 skills/operator-kit/watchdog.py --stage 02 --stage 03 --stage 04
  python3 skills/operator-kit/watchdog.py --all

Escalates to Conductor (writes to watchdog-recovery.log) after 3 failed recoveries.

Recovery is considered failed when:
  - Restarted dispatcher completes with 0 new done rows
  - Status file absent for >5 min after restart
"""

import os
import sys
import json
import time
import argparse
import subprocess
import threading
from pathlib import Path
from datetime import datetime

# ── Config ────────────────────────────────────────────────────────────────────

STAGE_CONFIG = {
    "02": {
        "status":   Path("stages/02-lesson-injection/output/status.json"),
        "sentinel": Path("stages/02-lesson-injection/output/.dispatcher-pause"),
        "cmd":      ["python3", "skills/operator-kit/dispatch-stage02.py", "--retry-failed", "--workers", "3"],
    },
    "03": {
        "status":   Path("stages/03-exercise-design/output/status.json"),
        "sentinel": Path("stages/03-exercise-design/output/.dispatcher-pause"),
        "cmd":      ["python3", "skills/operator-kit/dispatch-stage03.py", "--retry-failed", "--workers", "3"],
    },
    "04": {
        "status":   Path("stages/04-quiz-recall/output/status.json"),
        "sentinel": Path("stages/04-quiz-recall/output/.dispatcher-pause"),
        "cmd":      ["python3", "skills/operator-kit/dispatch-stage04.py", "--retry-failed", "--workers", "3"],
    },
}

POLL_INTERVAL      = 60    # seconds between status checks
STALL_THRESHOLD    = 300   # seconds with no progress = stall (5 minutes)
ABSENT_THRESHOLD   = 120   # seconds after launch with no status.json = stall (2 minutes)
SENTINEL_DRAIN     = 30    # seconds to wait for graceful drain after sentinel
MAX_RECOVERIES     = 3     # escalate to Conductor after this many failed recoveries

LOG_PATH = Path("skills/operator-kit/watchdog-recovery.log")


# ── Logging ───────────────────────────────────────────────────────────────────

def log(stage: str, msg: str) -> None:
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] stage={stage} {msg}"
    print(line)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def escalate_to_conductor(stage: str, recoveries: int) -> None:
    msg = (
        f"ESCALATE stage={stage} recoveries={recoveries} — "
        f"auto-recovery failed {recoveries}x. Manual intervention required. "
        f"Check status: run.ps1 status. Resume: run.ps1 stage{stage} --retry-failed"
    )
    log(stage, msg)
    print(f"\n{'='*60}")
    print(f"  WATCHDOG ESCALATION — STAGE {stage}")
    print(f"  Auto-recovery failed {recoveries} times.")
    print(f"  Conductor: check watchdog-recovery.log and intervene.")
    print(f"{'='*60}\n")


# ── Status reading ─────────────────────────────────────────────────────────────

def read_done_count(status_path: Path) -> int | None:
    """Return done count from status.json, or None if file absent/unreadable."""
    try:
        data = json.loads(status_path.read_text(encoding="utf-8"))
        return data.get("done", 0)
    except Exception:
        return None


def is_finished(status_path: Path) -> bool:
    """Return True if dispatcher completed cleanly."""
    try:
        data = json.loads(status_path.read_text(encoding="utf-8"))
        return bool(data.get("finished", False))
    except Exception:
        return False


# ── Recovery ──────────────────────────────────────────────────────────────────

def graceful_stop(stage: str, sentinel: Path) -> None:
    """Signal dispatcher to stop by creating PAUSE_SENTINEL; wait for drain."""
    log(stage, f"graceful stop — creating sentinel {sentinel}")
    sentinel.touch()
    log(stage, f"waiting {SENTINEL_DRAIN}s for in-flight calls to drain")
    time.sleep(SENTINEL_DRAIN)
    # Remove sentinel so the restarted dispatcher can run freely
    sentinel.unlink(missing_ok=True)


def kill_dispatcher(stage: str) -> None:
    """Hard kill any running dispatcher process for this stage."""
    script = f"dispatch-stage{stage}.py"
    killed = 0
    try:
        result = subprocess.run(
            ["python3", "-c",
             f"import psutil; [p.kill() for p in psutil.process_iter(['cmdline']) "
             f"if p.info['cmdline'] and any('{script}' in c for c in p.info['cmdline'])]"],
            capture_output=True, timeout=10,
        )
        killed = 1 if result.returncode == 0 else 0
    except Exception:
        # psutil not available — try taskkill on Windows
        try:
            subprocess.run(
                ["taskkill", "/F", "/FI", f"IMAGENAME eq python3.exe"],
                capture_output=True, timeout=10,
            )
        except Exception:
            pass
    log(stage, f"kill dispatcher (killed={killed})")


def restart_dispatcher(stage: str, cmd: list[str]) -> int:
    """Restart dispatcher subprocess and return its exit code."""
    log(stage, f"restarting: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, timeout=3600)
        return result.returncode
    except subprocess.TimeoutExpired:
        log(stage, "restart subprocess timed out after 60min")
        return 1
    except Exception as e:
        log(stage, f"restart failed: {e}")
        return 1


# ── Per-stage watch loop ───────────────────────────────────────────────────────

def watch_stage(stage: str, cfg: dict) -> None:
    """Monitor one stage. Runs in its own thread."""
    status_path: Path = cfg["status"]
    sentinel:    Path = cfg["sentinel"]
    cmd:         list = cfg["cmd"]

    last_done:    int | None = None
    last_progress_time: float = time.time()
    recovery_count: int = 0
    launch_time:    float = time.time()

    log(stage, "watchdog started")

    while True:
        time.sleep(POLL_INTERVAL)

        # Stop watching if dispatcher finished cleanly
        if is_finished(status_path):
            log(stage, "dispatcher finished cleanly — watchdog exiting")
            return

        done = read_done_count(status_path)
        now  = time.time()

        # Detect absent status.json after ABSENT_THRESHOLD seconds
        if done is None:
            if (now - launch_time) > ABSENT_THRESHOLD:
                log(stage, f"status.json absent >{ABSENT_THRESHOLD}s after launch — stall detected")
            else:
                log(stage, "status.json not yet created — normal startup, waiting")
                continue
        else:
            if done != last_done:
                last_done = done
                last_progress_time = now
                log(stage, f"progress: done={done}")
                continue

        # Check stall threshold
        stall_secs = now - last_progress_time
        if stall_secs < STALL_THRESHOLD:
            log(stage, f"no new progress for {stall_secs:.0f}s (threshold={STALL_THRESHOLD}s) — monitoring")
            continue

        # Stall confirmed — recover
        recovery_count += 1
        log(stage, f"STALL detected ({stall_secs:.0f}s no progress) — recovery #{recovery_count}")

        if recovery_count > MAX_RECOVERIES:
            escalate_to_conductor(stage, recovery_count)
            return

        done_before = done or 0
        graceful_stop(stage, sentinel)
        kill_dispatcher(stage)

        exit_code = restart_dispatcher(stage, cmd)
        time.sleep(10)  # let status.json initialize

        done_after = read_done_count(status_path) or 0
        if done_after <= done_before and exit_code != 0:
            log(stage, f"recovery #{recovery_count} produced no new done rows — counting as failed")
        else:
            log(stage, f"recovery #{recovery_count} succeeded: done {done_before} → {done_after}")
            recovery_count = 0  # reset on success

        last_done = done_after
        last_progress_time = time.time()
        launch_time = time.time()


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Watchdog — dispatcher stall monitor")
    parser.add_argument("--stage", action="append", choices=["02", "03", "04"],
                        help="Stage(s) to watch (repeat for multiple)")
    parser.add_argument("--all",   action="store_true", help="Watch all three stages")
    args = parser.parse_args()

    stages = []
    if args.all:
        stages = ["02", "03", "04"]
    elif args.stage:
        stages = args.stage
    else:
        parser.error("Specify --stage 02 (or --all)")

    log("*", f"Watchdog starting for stages: {stages}")
    log("*", f"Poll interval: {POLL_INTERVAL}s | Stall threshold: {STALL_THRESHOLD}s | Max recoveries: {MAX_RECOVERIES}")

    threads = []
    for stage in stages:
        cfg = STAGE_CONFIG[stage]
        t = threading.Thread(target=watch_stage, args=(stage, cfg), daemon=True, name=f"watchdog-{stage}")
        t.start()
        threads.append(t)

    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        log("*", "Watchdog stopped by user")


if __name__ == "__main__":
    main()
