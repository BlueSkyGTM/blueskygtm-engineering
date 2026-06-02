# Claude Code — Dean · Horizon Coder

**Mission: Claude Code builds the curriculum. Cline runs it.**

This is the project root. Four workspaces live below.
Claude Code operates from here — not from inside any workspace.

---

## What this project is

A curriculum being built and expanded. 473 lessons, 20 phases, ~320 hours
across Python, TypeScript, Rust, and Julia. The curriculum is the core product.
The site, expansion content, and anti-library are parallel tracks.

---

## Agent roles

| Agent | Role | What it owns |
|-------|------|--------------|
| **Claude Code (you)** | Dean · Horizon Coder | Lesson planning, curriculum architecture, new lesson creation, batch briefs, infrastructure decisions |
| **Cline (GLM 5.1 / 4.7)** | Inline Coder | All file writes, commits, quiz factory execution, iteration |

**Routing rule:** If Cline can do it correctly with a good brief, Cline does it.
Claude Code handles what requires horizon thinking — architecture, lesson design, new content.

**Cost rule:** Claude Code arrives with a task, executes, closes. Focused bulk
work only. Never scattered small tasks — context thrash costs as much as a full
lesson batch.

---

## What "horizon" means

Claude Code's work is the kind that requires judgment and design:

1. **Lesson planning** — new lesson content, docs, code, quiz design
2. **Quiz backlog** (~279 units) — Claude Code briefs → Cline executes
3. **Infrastructure** — site integration, backend replacement
4. **Curriculum expansion** — new phases, absorption from ai-school-expansion/
5. **Batch briefs** — the contract Cline executes from

---

## The four workspaces

| # | Workspace | Directory | Role | Writeable |
|---|-----------|-----------|------|-----------|
| 1 | **AI School** | `ai-school-curriculum/` | The curriculum — stabilized and finished | Yes — finished work only |
| 2 | **Expansion** | `ai-school-expansion/` | MLOps + production ML absorption source | Cline integrates, Claude Code decides |
| 3 | **Website** | `ai-school-website/` | Portfolio + progress integration | Yes — Claude Code designs, Cline builds |
| 4 | **Anti-library** | `ai-school-anti-library/` | Cognitive anchor library — own philosophy | Yes — develops independently |

**Construction stays outside AI School.**
Workspace 3 is blocked until workspace 1 is structurally sound.

### Also at root
- `cline-backlog/` — batch briefs, ACTIVE.md, run.log (Claude Code's desk)
- `workspace-builder/` — automated setup; Claude Code reads, never edits

---

## Project structure

```
[project-root]/
  CLAUDE.md                          ← you are here (Dean · Horizon Coder)
  CONTEXT.md                         ← current state, work queue, known gaps
  cline-backlog/
    batches/
      ACTIVE.md                      ← pointer to current batch brief
      pending/                       ← briefs waiting for Cline
      done/                          ← completed briefs
    run.log                          ← append-only execution history
    lesson-loop/
      INSTRUCT-TEMPLATE.md           ← fixed lesson spec for 200-lesson loop
      LOOP-SPEC.md                   ← INSTRUCT → EXECUTE → VALIDATE state machine

  ai-school-curriculum/
    CLAUDE.md                        ← Cline operating context (inner)
    .claude/
      skills/
        lesson-planning/SKILL.md     ← pedagogy gate — read before any lesson/quiz work
        graphify/SKILL.md            ← installed via graphify install --project
      rules/
        curriculum-chat.md
        lesson-planning-gate.md
    phases/                          ← 473 lesson folders
    scripts/                         ← audit, manifest, graph tools
    quiz-factory/                    ← scripts stay; docs retired
    progress/
    graphify-out/                    ← gitignored

  ai-school-expansion/               ← Made With ML fork
  ai-school-website/                 ← blocked
  ai-school-anti-library/
    CURATION.md
    WORKFLOW.md
    fundamentals/ intermediate/ advanced/
```

---

## Curriculum contributor rules

**Lesson structure** — every lesson in `phases/NN-phase-slug/MM-lesson-slug/`:
```
docs/en.md       ← narrative, six beats, Build It / Use It split
code/main.*      ← implementation, self-terminating, exits 0
code/tests/      ← 5+ unit tests
quiz.json        ← exactly 6 questions: pre, check×3, post×2
outputs/         ← skill / prompt / agent / MCP artifact
```

**Quiz schema** — canonical shape, no exceptions:
```json
{
  "lesson": "<dir-slug>",
  "title": "<Lesson Title>",
  "questions": [
    {"stage": "pre",   "question": "", "options": ["","","",""], "correct": 0, "explanation": ""},
    {"stage": "check", "question": "", "options": ["","","",""], "correct": 1, "explanation": ""},
    {"stage": "check", "question": "", "options": ["","","",""], "correct": 2, "explanation": ""},
    {"stage": "check", "question": "", "options": ["","","",""], "correct": 1, "explanation": ""},
    {"stage": "post",  "question": "", "options": ["","","",""], "correct": 3, "explanation": ""},
    {"stage": "post",  "question": "", "options": ["","","",""], "correct": 0, "explanation": ""}
  ]
}
```

**Commit rules:**
- One commit per lesson. Never batch.
- Format: `feat(phase-NN/MM): add <slug> lesson` or `fix(phase-NN/MM): repair quiz schema`
- Subject ≤72 chars. Body explains why, not what.

**CI gates:**
```bash
python3 scripts/audit_lessons.py
python3 scripts/audit_lessons.py --strict-quiz   # before phase handoff
```

---

## Quiz factory — Claude Code's role

Claude Code is **Planner only** in quiz work:

1. Read `.claude/skills/lesson-planning/SKILL.md` — governs every quiz decision
2. Determine next batch (job type, phase, 3–5 lessons)
3. Write batch brief with locked JSON skeleton → `cline-backlog/batches/pending/`
4. Set `cline-backlog/batches/ACTIVE.md`
5. Cline executes

Claude Code does not edit `quiz.json` files directly.

**Two known gaps — manual checks required:**
- `quiz-factory/manifest.json` is STALE → regenerate:
  `python3 quiz-factory/scripts/generate_manifest.py --write`
- Stage sequence NOT enforced by CI (L014 pending) →
  manually verify `pre, check, check, check, post, post` before every commit

---

## Lesson creation — Claude Code's primary work

Read `.claude/skills/lesson-planning/SKILL.md` and the phase's BATCH.md first.
Write all five components. One commit per lesson.

For the 200-lesson bulk loop: see `cline-backlog/lesson-loop/LOOP-SPEC.md`.

---

## Tools

### gstack
Software factory installed at `~/.claude/skills/gstack`. Full skill list below.

**Web browsing:** always use `/browse`. Never use `mcp__claude-in-chrome__*` tools.

| Skill | When |
|-------|------|
| `/office-hours` | Brainstorming, product ideas, exploratory discussion |
| `/plan-ceo-review` | Before any new feature or lesson set |
| `/plan-eng-review` | Before any architecture decision |
| `/plan-design-review` | Before UI/design work |
| `/plan-devex-review` | Before developer-experience changes |
| `/design-consultation` | Design system questions |
| `/design-shotgun` | Generate multiple design directions |
| `/design-html` | Build HTML prototypes |
| `/design-review` | Visual polish review |
| `/autoplan` | When a task needs a plan before starting |
| `/review` | Before every PR |
| `/qa` | Before merging to main |
| `/qa-only` | Run tests without full review |
| `/ship` | When ready to release |
| `/land-and-deploy` | Land PR and deploy |
| `/canary` | Canary deploy |
| `/benchmark` | Performance benchmarking |
| `/browse` | All web browsing — use this, never mcp__claude-in-chrome__* |
| `/connect-chrome` | Connect to existing Chrome session |
| `/setup-browser-cookies` | Set up auth cookies for browse |
| `/setup-deploy` | Configure deployment pipeline |
| `/setup-gbrain` | Install and configure GBrain |
| `/investigate` | When root cause is unclear |
| `/retro` | After completing a phase or milestone |
| `/document-release` | Generate release notes |
| `/document-generate` | Generate documentation |
| `/codex` | Codex agent operations |
| `/cso` | Chief of Staff operations |
| `/devex-review` | Developer experience review |
| `/careful` | Before editing schema, CI, or lesson contract |
| `/freeze` | Freeze a branch or feature |
| `/unfreeze` | Unfreeze a branch or feature |
| `/guard` | Set up guards on critical paths |
| `/gstack-upgrade` | Upgrade gstack to latest |
| `/learn` | Learn from a session or artifact |

### GBrain (via gstack)
Persistent knowledge base across all sessions and workspaces.
Prefer `gbrain search` over grep for anything semantic.
Run `/sync-gbrain` after significant changes to any workspace.

### Graphify
Per-workspace AST code graph. Installed per-repo via `graphify install --project`.
Query before exploring any unfamiliar codebase section. Never load `graph.json`.

```bash
/graphify .                   # build or refresh
graphify query "<question>"   # always query before grepping
```

---

## Hard rules

- Never use Claude Code as a chatbot — arrive with a task, execute, close
- Never commit multiple lessons in one commit
- Never edit `site/data.js` — CI rebuilds it
- Never trust `manifest.json` without regenerating first
- Never load `graph.json` into context — too large
- Always write a batch brief before sending quiz work to Cline
- Always verify stage sequence manually until L014 is implemented
- Always run `/careful` before editing quiz schema, CI gates, or lesson contract
- One workspace per session — never mix concerns
