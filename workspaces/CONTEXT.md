# Handoff to Claude Code
## AI Engineering from Scratch — Migration + Build Brief

**Prepared:** 2026-05-31
**You are:** Claude Code — Dean · Horizon Coder

Read this once. Then open the repo and work.

---

## What you are inheriting

A curriculum with 473 lessons, 20 phases, ~320 hours. Partially finished.
Going in a new direction. Your job is to finish it, structure it for the
multi-agent system below, and set it up for portfolio integration.

**What was already fixed — do not redo:**
- Phase 04 schema repair: 28/28 committed
- Phase 05 lessons 01–12: schema repaired
- 7 anti-pattern quizzes: rebuilt from scratch
- Phase 19 (55 capstone lessons): gold standard quality

**What was left broken:**
- Phase 05 lessons 13–29: wrong quiz schema (8q)
- Phase 14 all 42 lessons: wrong quiz schema (7q)
- Phases 06–10, 12–13, 15–16: no quiz.json at all
- Phases 11, 17, 18: quizzes exist but empty explanations
- The entire repo still uses Cursor-native config — you are migrating it

---

## The agent system

| Agent | Role |
|-------|------|
| **You (Claude Code)** | Dean · Horizon Coder. Lesson planning, architecture, new content, batch briefs. |
| **Cline (GLM 5.1/4.7)** | Professor · Inline Coder. Teaches students, executes briefs, commits. |

---

## Migration: what you need to build

### 1. Project root structure

Create the parent directory above the curriculum repo:

```
[project-root]/
  CLAUDE.md                        ← Claude Code (Dean)
  work/
    batches/
      ACTIVE.md
      pending/
      done/
    run.log
  ai-engineering-from-scratch/     ← curriculum repo
    CLAUDE.md                      ← Cline (Professor · Inline Coder)
    .claude/                       ← NEW — replaces all Cursor config
      skills/
        lesson-planning/SKILL.md
        batch-orchestration/SKILL.md
        student-handbook/SKILL.md
        guidance-counselor/SKILL.md
        check-understanding/SKILL.md
        find-your-level/SKILL.md
        learning-style-setup/SKILL.md
      rules/
        curriculum-chat.md
        lesson-planning-gate.md
    phases/
    scripts/
    progress/
    site/
    graphify-out/
```

### 2. Migrate Cursor config to Claude native

Move `.cursor/skills/` → `.claude/skills/`
Move `.cursor/rules/` → `.claude/rules/`

Rename rule files from `.mdc` extension to `.md`.
Update any internal cross-references from `.cursor/` paths to `.claude/` paths.
Delete `.cursor/` directory after migration is verified.

Cline reads `.claude/` natively. No adapter needed.

### 3. Dissolve the quiz-factory boundary

The `quiz-factory/` directory was a makeshift workstation. Its scripts stay
in `quiz-factory/scripts/` because Cline needs them. But batch briefs move to
`cline-backlog/batches/` at the project root. The quiz-factory docs (`CLAUDE.md`,
`CONTEXT.md`, `REFERENCES.md`, `ARCHITECTURE.md`) can be archived or removed —
the batch brief format and skill files replace them.

---

## Graphify — install before exploring

```bash
pip install graphifyy
python3 scripts/refresh_graph.py
```

Read `graphify-out/GRAPH_REPORT.md` — Corpus, Freshness, God Nodes, Surprising
Links only. Skip Community Hubs. Never load `graph.json` into context.

Query first, grep second:
```bash
python3 scripts/query_graph.py query "<narrow question>"
python3 scripts/query_graph.py path "<symbol-A>" "<symbol-B>"
```

Skip refresh after quiz.json-only edits. Refresh after code/, docs/, or site/ edits.

---

## Skills to read before any lesson or quiz work

`.claude/skills/lesson-planning/SKILL.md` — seven insights, pedagogy gate,
quality bar. This governs every quiz design decision.

---

## Work queue — priority order

### P0 — Quiz schema repair (59 lessons, Cline executes)

| Phase | Pattern | Count |
|-------|---------|-------|
| Phase 05 lessons 13–29 | Trim 8q → 6q (drop 1 pre, drop 1 post) | 17 |
| Phase 14 lessons 01–42 | Trim 7q → 6q (drop 1 pre, add code ref) | 42 |

### P1 — Create quiz (154 lessons, Cline executes)

Phases 06, 07, 08, 09, 10, 12, 13, 15, 16 — no quiz.json exists.

### P2 — Fill explanations (62 lessons, Cline executes)

Phases 11, 17, 18 — quizzes exist but explanation fields are empty.

### P3 — Targeted fixes (4 lessons)

- `phases/19/22-jsonrpc-stdio-transport` — rewrite all explanations
- `phases/19/24-plan-execute-control-flow` — rewrite all explanations
- `phases/19/30-bpe-tokenizer-from-scratch` — add code symbol
- `phases/10/15-speculative-decoding-eagle3` — fix check Q2 math

### P4 — Write missing lessons (Claude Code writes)

Phases where content is thin or absent. This is your primary creative work.
Read the phase BATCH.md. Write all five lesson components. One commit per lesson.

### P5 — Infrastructure (parallel track)

Portfolio site integration. Backend replacement. Student progress API.

---

## How to brief Cline

1. Write `cline-backlog/batches/pending/batch-NNN-description.md`
2. Set `cline-backlog/batches/ACTIVE.md` → relative path to that file
3. Hand off to Cline: "read ACTIVE.md and execute"
4. Cline gates each lesson, commits, appends `cline-backlog/run.log`
5. Review `run.log` for blocked entries
6. Write next brief

**Every brief must include a locked skeleton.** Cline never invents structure:

```json
{
  "lesson": "<dir-slug>",
  "title": "<from docs/en.md H1>",
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

**Gold reference quizzes** — style anchors, never copy content:
- `phases/07-transformers-deep-dive/16-speculative-decoding/quiz.json`
- `phases/10-llms-from-scratch/34-gradient-checkpointing/quiz.json`
- `phases/19-capstone-projects/54-paper-writer/quiz.json`

---

## Two known gaps — never skip

**Stale manifest:** regenerate before any Cline quiz session:
```bash
python3 quiz-factory/scripts/generate_manifest.py --write
```

**Missing stage enforcement:** audit_lessons.py Tier A does not check stage
sequence yet. Manually verify `pre, check, check, check, post, post` before
every commit until L014 is implemented.

---

## First session checklist

- [ ] Read this document
- [ ] Create project root structure with `cline-backlog/batches/` directories
- [ ] Install graphify and build the graph
- [ ] Migrate `.cursor/` → `.claude/` (skills + rules)
- [ ] Regenerate manifest
- [ ] Read `.claude/skills/lesson-planning/SKILL.md`
- [ ] Write `cline-backlog/batches/pending/batch-001-phase05-13-17.md`
- [ ] Set `cline-backlog/batches/ACTIVE.md`
- [ ] Begin first lesson write OR hand batch-001 to Cline

---

## Current state
 
### First session checklist — run once on this machine
 
**Global installs (machine-level, do once):**
- [ ] Install gstack:
  ```bash
  git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup
  ```
- [ ] Install graphify:
  ```bash
  uv tool install graphifyy && graphify install
  ```
 
**Per-workspace installs (run inside each directory):**
- [ ] `cd ai-school-curriculum && graphify install --project`
- [ ] `cd ai-school-expansion && graphify install --project`
- [ ] `cd ai-school-anti-library && graphify install --project`
- [ ] `cd ai-school-website && graphify install --project`
**GBrain setup (via gstack, run once):**
- [ ] `/setup-gbrain` → pick PGLite local (zero accounts, ~30 seconds)
- [ ] `/sync-gbrain` inside each workspace to index it
**Project root:**
- [ ] `cline-backlog/batches/pending/`, `done/`, `run.log` created
- [ ] `CLAUDE.md` and `CONTEXT.md` at project root
- [ ] `ACTIVE.md` created (empty) in `cline-backlog/batches/`
**AI School migration:**
- [ ] `.cursor/` → `.claude/` migration complete
- [ ] Manifest regenerated: `python3 quiz-factory/scripts/generate_manifest.py --write`
- [ ] Run audit: `python3 scripts/audit_lessons.py > audit-output.txt`
- [ ] First batch brief written, `ACTIVE.md` set
---
 
### Migration status
- [ ] `.cursor/` → `.claude/` migration complete in `ai-school-curriculum/`
- [ ] `cline-backlog/batches/pending/`, `done/`, `run.log` created at project root
- [ ] `graphify-kit/` created at project root
- [ ] Manifest regenerated: `python3 quiz-factory/scripts/generate_manifest.py --write`
- [ ] First batch brief written and ACTIVE.md set
### What was already fixed — do not redo
- Phase 04 schema repair: 28/28 committed
- Phase 05 lessons 01–12: schema repaired
- 7 anti-pattern quizzes: rebuilt from scratch
- Phase 19 (55 capstone lessons): gold standard quality
### Known broken state — workspace 1
- Phase 05 lessons 13–29: wrong quiz schema (8q) — needs schema_repair
- Phase 14 all 42 lessons: wrong quiz schema (7q) — needs schema_repair
- Phases 06–10, 12–13, 15–16: no quiz.json — needs create_quiz
- Phases 11, 17, 18: empty explanations — needs fill_explanations
- 4 targeted fixes: 19/22, 19/24 (explanations), 19/30, 10/15 (code symbol / math)
---
 
## Work queue — priority order
 
| Priority | Job | Scope | Agent |
|----------|-----|-------|-------|
| P0 | schema_repair | Phase 05 lessons 13–29 (17) | Cline |
| P0 | schema_repair | Phase 14 all 42 lessons | Cline |
| P1 | create_quiz | Phases 06–10, 12–13, 15–16 (~154) | Cline |
| P2 | fill_explanations | Phases 11, 17, 18 (62) | Cline |
| P3 | targeted fixes | 19/22, 19/24, 19/30, 10/15 | Cline |
| P4 | create_lesson | Missing lessons — exact list pending audit | Claude Code |
| P5 | absorb | ai-school-expansion/ → AI School | Claude Code briefs |
| P6 | build | ai-school-website/ | Blocked until P0–P2 clear |
 
**Before starting P1 or P4:** run audit to confirm exact missing list:
```bash
python3 scripts/audit_lessons.py > audit-output.txt
```
 
---
 
## Known infra gaps — never skip
 
**Gap 1 — Stale manifest:**
```bash
python3 quiz-factory/scripts/generate_manifest.py --write
```
Run before any Cline quiz session. Manifest does not reflect disk state.
 
**Gap 2 — Missing stage enforcement (L014 pending):**
`audit_lessons.py` Tier A does NOT enforce stage sequence. Manually verify before every commit:
```
stages == ["pre", "check", "check", "check", "post", "post"]
```
 
---
 
## Batch brief contract
 
Every brief Cline executes must include:
 
```markdown
# Batch NNN — [phase] lessons [MM–MM]
 
job_type: schema_repair | create_quiz | fill_explanations | redo_quiz | absorb
phase: NN-phase-slug
[repair pattern if schema_repair]
 
Lessons (process in order, one commit each):
1. phases/NN-.../MM-lesson
 
Phase BATCH.md: phases/NN-.../BATCH.md
 
LOCKED SKELETON:
{ ... }
 
Gate before every commit:
  python3 scripts/audit_lessons.py --strict-quiz
  Manually verify: stages == pre, check, check, check, post, post
 
Commit format: fix(phase-NN/MM): repair quiz schema
```
 
**Gold reference quizzes** — style anchors, never copy content:
- `phases/07-transformers-deep-dive/16-speculative-decoding/quiz.json`
- `phases/10-llms-from-scratch/34-gradient-checkpointing/quiz.json`
- `phases/19-capstone-projects/54-paper-writer/quiz.json`
---
 
## Lesson loop spec (200 missing lessons)
 
Three-state recursion. Deterministic, headless, scriptable.
 
```
INSTRUCT → EXECUTE → VALIDATE
    ↑________________________↓ (fail, retry < 3)
              ↓ (pass)
           COMMIT + NEXT
              ↓ (retry = 3)
           BLOCKED → run.log → next lesson
```
 
**Four gates (all scriptable, all must exit 0):**
1. Structural: `test -f docs/en.md && test -f quiz.json && find code/ -name "main.*" | grep -q .`
2. Schema: `python3 scripts/audit_lessons.py --strict-quiz phases/.../`
3. Variance: `python3 quiz-factory/scripts/balance_answers.py phases/.../quiz.json`
4. Code: `cd phases/.../ && python3 code/main.*; echo "Exit: $?"`
Failure output feeds back into INSTRUCT on retry. Agent knows exactly what broke.
 
See `cline-backlog/lesson-loop/INSTRUCT-TEMPLATE.md` and `LOOP-SPEC.md` for full spec.
 
---
 
## run.log format
 
Append-only. One line per lesson. Cline writes, Claude Code reads.
 
```
2026-06-01T09:00:00Z | phases/07-.../17-lesson-slug | done    | abc1234
2026-06-01T09:15:00Z | phases/07-.../18-lesson-slug | blocked | gate 2: wrong stage order after 3 attempts
```
 
---
 
## Graphify quick reference
 
```bash
# Refresh (Cline only, after code/docs/site edits)
python3 graphify-kit/refresh_graph.py --workspace ai-school-curriculum/
 
# Query (Claude Code, before any broad exploration)
python3 graphify-kit/query_graph.py --workspace ai-school-curriculum/ query "<question>"
 
# Verify freshness
python3 graphify-kit/verify_graph.py --workspace ai-school-curriculum/ --strict
```
 
Read `ai-school-curriculum/graphify-out/GRAPH_REPORT.md` — Corpus, Freshness,
God Nodes, Surprising Links only. Never load `graph.json` into context.

---

## What you are not

- Not a chatbot — Cline handles students as Professor
- Not a line-by-line code reviewer — Cline handles iteration
- Not a firefighter — scoped, focused work only

*Prepared from full planning session. All source files read. All roles confirmed.*
