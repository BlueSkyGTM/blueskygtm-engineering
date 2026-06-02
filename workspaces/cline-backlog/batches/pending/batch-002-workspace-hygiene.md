# Batch 002 — Workspace Hygiene

**Job type:** housekeeping  
**Scope:** `ai-engineering-from-scratch/` root and config directories  
**Prepared:** 2026-05-31  
**Status:** PENDING

This is not quiz work. Do not touch `phases/`, `quiz.json` files, `scripts/`, or `site/`.
Read this brief completely before making any changes.

---

## Agent roles (for reference)

| Agent | Role |
|-------|------|
| **Claude Code** | Dean · Horizon Coder — lesson planning, architecture, batch briefs |
| **Cline (you)** | Professor · Inline Coder — execution, commits, teaching |

---

## Problems to fix (7 tasks)

---

### Task 1 — Rename CONTEXT.md → AGENTS.md and update its content

**Problem:** `CONTEXT.md` at the curriculum root is actually the `AGENTS.md` operating manual. It was renamed by Cursor. Its content heading already says `# AGENTS.md`. It references `.cursor/rules/` as canonical and defines the old Otto/Navigator/Consultant roles.

**Steps:**
1. Rename `CONTEXT.md` → `AGENTS.md`
2. In `AGENTS.md`, find and replace all occurrences of `.cursor/rules/` → `.claude/rules/`
3. Find and replace `.cursor/skills/` → `.claude/skills/`
4. Find and replace `.mdc` extension → `.md`
5. Replace the Agent roles table:

**Old table:**
```
| Role | Who | Permissions |
|------|-----|-------------|
| **Consultant / Navigator / Otto** | Cursor chat (Auto) | Read-only. May read files... |
| **Implementer** | Cline | Same reasoning... |
```

**New table:**
```markdown
| Role | Who | Permissions |
|------|-----|-------------|
| **Dean · Horizon Coder** | Claude Code | Lesson planning, curriculum architecture, new content, batch briefs. Does not execute file edits directly. |
| **Professor · Inline Coder** | Cline | Student teaching and tutoring, all file edits, commits, quiz factory execution. |
```

6. Replace the line: `Both agents follow `.cursor/rules/consultant-charter.mdc` (Reasoning + Discipline on any topic — not engineering-only).`  
   With: `Both agents follow `.claude/rules/` (Reasoning + Discipline on any topic — not engineering-only).`

7. Replace: ``.cursor/rules/` is the canonical agent config directory for this repo.`  
   With: ``.claude/rules/` is the canonical agent config directory for this repo.`

8. Replace the Handoff line: `Handoff: Otto advises → user approves → Cline implements.`  
   With: `Handoff: Claude Code briefs → user approves → Cline implements.`

9. Check the Quiz quality policy section — update `.cursor/rules/lesson-planning-gate.mdc` → `.claude/rules/lesson-planning-gate.md` and `.cursor/skills/lesson-planning/SKILL.md` → `.claude/skills/lesson-planning/SKILL.md`

**Commit:** `fix(root): rename CONTEXT.md to AGENTS.md, update agent roles and config paths`

---

### Task 2 — Delete `.cursor/` directory

**Problem:** `.cursor/` was fully migrated to `.claude/` but the original was never removed. Two competing configs exist.

**Verify first:**
- `.claude/skills/` has the same skill directories as `.cursor/skills/`
- `.claude/rules/` has `.md` versions of all `.cursor/rules/*.mdc` files

**Steps:**
1. List `.cursor/skills/` and confirm each dir exists in `.claude/skills/`
2. List `.cursor/rules/*.mdc` and confirm each has a `.md` counterpart in `.claude/rules/`
3. If both checks pass: delete the entire `.cursor/` directory
4. If any file is missing from `.claude/`: copy it over first, then delete `.cursor/`

**Do not** archive `.cursor/` — it has already been migrated. Delete it.

**Commit:** `fix(config): remove .cursor/ — fully migrated to .claude/`

---

### Task 3 — Archive quiz-factory docs, keep scripts

**Problem:** `quiz-factory/` contains docs (CLAUDE.md, CONTEXT.md, ARCHITECTURE.md, DESIGN.md, QUALITY-RUBRIC.md, QUALITY-STANDARDS.md, README.md, templates/) that were the operating manual when quiz-factory was the batch workspace. Batch briefs have moved to `work/batches/`. The docs are now stale and reference `.cursor/`. The scripts and manifest must stay.

**Steps:**
1. Create `.claude/_archive/quiz-factory-docs/`
2. Move these files into it:
   - `quiz-factory/CLAUDE.md`
   - `quiz-factory/CONTEXT.md`
   - `quiz-factory/ARCHITECTURE.md`
   - `quiz-factory/DESIGN.md`
   - `quiz-factory/QUALITY-RUBRIC.md`
   - `quiz-factory/QUALITY-STANDARDS.md`
   - `quiz-factory/README.md`
   - `quiz-factory/REFERENCES.md`
3. Move `quiz-factory/templates/` into `.claude/_archive/quiz-factory-docs/templates/`
4. Move `quiz-factory/examples/` into `.claude/_archive/quiz-factory-docs/examples/`
5. **Leave in place:** `quiz-factory/scripts/`, `quiz-factory/manifest.json`, `quiz-factory/REFERENCES.md`, `quiz-factory/QUALITY-RUBRIC.md`, `quiz-factory/QUALITY-STANDARDS.md`

**Result:** `quiz-factory/` should contain only `scripts/`, `manifest.json`, `REFERENCES.md`, `QUALITY-RUBRIC.md`, and `QUALITY-STANDARDS.md` when done.

Also update `quiz-factory/REFERENCES.md` line: `../.cursor/skills/lesson-planning/SKILL.md` → `../.claude/skills/lesson-planning/SKILL.md`

**Commit:** `fix(quiz-factory): archive stale docs — batch briefs now live in work/batches/`

---

### Task 4 — Remove orphaned root files

**Note:** `quiz-factory.zip`, `skills-lock.json`, and `CURRICULUM_QA_FINDINGS_2026-05-30.md` are no longer at the repo root — already cleared or never present. No action needed here.

Skip this task.

---

### Task 5 — Remove empty directories

**Problem:** Several directories were scaffolded but are empty.

**Verify each is truly empty before deleting:**

All confirmed empty by audit:
- `projects/` — empty
- `web/` — empty
- `outputs/` — four subdirs with only `.gitkeep` files and an empty `index.json`. Nothing in scripts or site references this directory.

**Steps:**
1. Delete `projects/`
2. Delete `web/`
3. Delete `outputs/` (entire directory including index.json and subdirs)

**Commit:** `fix(root): remove empty scaffolding directories`

---

## Verification after all tasks

Run from `ai-engineering-from-scratch/`:

```bash
# No .cursor/ references should remain in .claude/ or AGENTS.md
grep -r "\.cursor/" .claude/ AGENTS.md --include="*.md"

# quiz-factory should only have scripts/ and manifest.json
ls quiz-factory/

# AGENTS.md should exist, CONTEXT.md should not
ls AGENTS.md
ls CONTEXT.md  # should fail

# Audit should still pass
python3 scripts/audit_lessons.py
```

All four checks must pass before you consider this batch done.

---

## What NOT to touch

- `phases/` — no lesson content changes
- `scripts/` — keep all scripts
- `quiz-factory/scripts/` — keep
- `quiz-factory/manifest.json` — keep
- `site/` — keep
- `progress/` — keep
- `glossary/` — keep
- `graphify-out/` — keep (gitignored anyway)
- `.claude/skills/` — keep (already correct)
- `.claude/rules/` — keep (already correct)
- `CLAUDE.md` — keep (already updated)

---

## Log entry format

Append to `../../work/run.log` after completion:

```
<ISO8601> | batch-002-workspace-hygiene | done | <commit hashes, one per task>
```
