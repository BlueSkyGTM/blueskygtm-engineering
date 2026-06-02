# AI School — project context

Gamified ("world map" RPG) front-end for the **AI Engineering From Scratch** curriculum.
Vanilla JS + CSS, **no build step for the app itself, no framework**. Designed to drop into
WordPress later (see the store adapter note below).

## Golden rules
1. **`js/data.js` is generated — never hand-edit it.** It is built from the curriculum repo
   (`ai-engineering-from-scratch/`, via its `build.js`). It defines two globals: `PHASES`
   (the 20 worlds + their lessons) and `GLOSSARY` (term cards). To change content, change the
   source repo and re-run its build, then replace `js/data.js`.
2. **All imagery is placeholder slots, not files.** There are *no* binary art assets wired in.
   Anywhere real pixel art goes, the code renders a `.slot` element with a text label of the
   intended size (e.g. `'avatar 16×16'`). See the slot table in `README.md`. Do not go looking
   for missing image files — none are referenced.
3. **Style only through tokens.** Every color/space/font is a CSS var in `css/tokens.css`.
   Components reference vars only — change a token, the whole app reskins. Don't hard-code
   colors downstream.
4. **One source of state.** `js/store.js` is the *only* thing that touches persistence
   (localStorage today). Screens never read storage directly — they read derived stats from
   `js/game.js` (a pure function). To move to a backend, swap `Store.adapter` (one line,
   documented in `store.js`); no screen code changes.

## Architecture (load order matters)
Everything namespaces onto `window.AIS`. Each HTML page loads scripts in this order:
`data.js` → `store.js` → `game.js` → `ui.js` → `<screen>.js`

| Layer | File | Role |
|---|---|---|
| Data | `js/data.js` | **generated.** `PHASES`, `GLOSSARY` globals |
| Persistence | `js/store.js` | `AIS.store` — read/write/toggle progress; adapter-swappable |
| Rules (pure) | `js/game.js` | `AIS.game.derive(PHASES, progress)` → stats; XP, levels, ranks, badges, streaks |
| DOM helper | `js/ui.js` | `AIS.ui.el(...)` builder + `toast()`. No framework |
| Screens | `js/hub.js` `course.js` `roadmap.js` `catalog.js` `glossary.js` `projects.js` | one file per page; render-only |

Nav order (all pages): **Home · Course · Roadmap · Catalog · Projects · Glossary**.

Pages:
- `index.html` — **Home**: orientation. A hero (what this is) + "Where to go" signpost cards
  + the world map. 20 phases grouped into 6 themed *lands* that stack down the page
  (archipelago trail); each phase is a pin on a dotted road. `hub.js` owns the `LANDS` array
  (which phase sits in which land) + the slide-in phase drawer.
- `course.html` — **Course**: the player card (level/rank/XP/career meters) pinned at the
  top, then the curriculum accordion. `course.js`.
- `roadmap.html` — **Roadmap**: the prerequisite dependency **graph only** (the DAG). Click a
  world to select it — lights its upstream prereqs + downstream unlocks, dims the rest;
  "Clear selection" resets. Hover previews. `roadmap.js`.
- `catalog.html` — **Catalog**: the searchable lesson index — big search box + type/status
  filter chips + a sortable manifest of all ~470 lessons. `catalog.js`.
- `projects.html` — **Projects**: trophy case. Featured-work placeholder slots, the Phase-19
  capstone builds (locked/greyed until cleared), and achievement badges. `projects.js`.
- `glossary.html` — **Glossary**: flip-to-reveal term cards. `glossary.js`.

## Ignore these (not app assets)
- `screenshots/`, `uploads/` — working captures/uploads, **not referenced by any code**.
- `AI School Wireframes.html` — a standalone design exploration doc, not part of the running app.

## Conventions
- IDs in markup are render targets (`#map`, `#drawer`, `#hud`, `#toc`, `#tree`, `#body`,
  `#builds`, `#featured`, `#trophies`, …); screen JS fills them via `replaceChildren`.
- `data-screen-label` marks high-level screens; keep them on the semantic equivalent if you restructure.
- Lesson identity is `phaseId + ':' + lessonIndex` — keep that key stable if you touch the store.
- **`PREREQS` (the dependency graph) is duplicated** in `hub.js` (drawer "recommended after"
  chips) and `roadmap.js` (the dependency graph). Edit both, or hoist it into `data.js` if you
  change it often.
- The world-map phase→land grouping lives in `LANDS` in `hub.js`. Add a new phase to a land
  (or add a land) there — see `ARCHITECTURE.md` §3.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
