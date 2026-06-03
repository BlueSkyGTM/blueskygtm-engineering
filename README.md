# Build modern AI, by hand.

Not tutorials. Not YouTube. Every algorithm written from scratch — tensors, backprop,
transformers, RAG, agents. Twenty chapters of AI engineering done the hard way,
inside Claude Code.

Built on top of [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch)
by Rohit Ghumare, with a full personal learning dashboard, gamification system,
and WordPress integration added on top.

---

## Twenty chapters. 470+ lessons. Everything you've done and everything left.

| Chapter | What you build |
|---------|---------------|
| 00 Setup & Tooling | Dev environment, GPU setup, APIs, Python toolchain |
| 01 Math Foundations | Linear algebra, calculus, probability, PCA + variance decomposition |
| 02 ML Fundamentals | Regression, classification, loss surfaces, gradient descent from scratch |
| 03 Deep Learning Core | Backprop by hand, activations, regularisation |
| 04 Computer Vision | CNNs, object detection, full vision pipeline capstone |
| 05 NLP: Foundations → Advanced | Tokenisation, embeddings, sequence models |
| 06 Speech & Audio | Spectrograms, ASR, audio feature extraction |
| 07 Transformers Deep Dive | Attention mechanism, multi-head, positional encoding — transformer from scratch |
| 08 Generative AI | GANs, diffusion, CLIP |
| 09 Reinforcement Learning | Policy gradients, Q-learning, environment loops |
| 10 LLMs from Scratch | Pre-training, tokenisation, scaling laws |
| 11 LLM Engineering | Fine-tuning, RLHF, evaluation, inference optimisation |
| 12 Multimodal AI | Vision-language models, multimodal agent capstone |
| 13 Tools & Protocols | MCP, tool use, function calling, tool ecosystem capstone |
| 14 Agent Engineering | ReAct, planning, memory, agent workbench capstone |
| 15 Autonomous Systems | Long-horizon agents, evaluation frameworks |
| 16 Multi-Agent & Swarms | Coordination, parallelism, swarm patterns |
| 17 Infrastructure & Production | Serving, monitoring, deployment pipelines |
| 18 Ethics, Safety & Alignment | Red-teaming, constitutional AI, safety evals |
| 19 Capstone Projects | 55 final builds — one per concept cluster |

**Languages:** Python · TypeScript · Rust · Julia

---

## What I added

The upstream repo is a curriculum. Everything below was built on top of it.

### Learning dashboard (`site-new/`)

Six pages. No framework. No build step. Every page derives its UI from one pure function
over the curriculum data.

| Page | What it does |
|------|-------------|
| **Course** | 20-chapter accordion, per-lesson ticks, live XP bar and rank |
| **Catalog** | 470+ lessons searchable by name, language, chapter, type |
| **Projects** | All 60 capstone builds — locked with descriptions, gold when shipped |
| **Library** | Curated free reading — math, ML, LLMs, Rust, production |
| **Glossary** | 83 flip cards. What people say vs what it actually means |
| **Home** | Navigation hub linking every section |

### Progress system

Every lesson tick earns XP. Level cost rises each level. Seven ranks unlock as you go:

```
LV.01–03  Initiate          LV.10–12  AI Engineer
LV.04–06  Practitioner      LV.13–15  Senior Engineer
LV.07–09  Apprentice Eng.   LV.16–18  Staff Engineer
                            LV.19+    AI Architect
```

`game.js` is a pure function — curriculum + progress in, all stats out.
No DOM, no side effects. Re-runs on every tick.

### WordPress integration

Progress persists to `/wp-json/aischool/v1/progress` when a nonce is present.
Falls back to localStorage silently. One-line backend swap — no screen code changes:

```js
Store.adapter = restAdapter;
```

### Toolchain

Built using [gstack](https://github.com/garrytan/gstack) — structured AI workflows
for `/design-review`, `/qa`, `/investigate`, and `/ship` directly from Claude Code.

---

## Engineering decisions

**No framework.** Personal tooling should outlive framework churn.
Files open directly in a browser. No node_modules, no build step, no config.

**Data-driven.** `PHASES` is the curriculum. Every page calls
`game.derive(PHASES, store.load())`. Adding a stat means editing data, not components.

**Pure game engine.** `game.js` works in a browser, a test runner, or Node —
same function, same output, no imports required.

**Adapter pattern.** localStorage and WordPress REST implement the same three-method
interface. Swapping backends touches zero screen code.

---

## What's coming

- **200+ quizzes** — per-lesson knowledge checks in the lesson reader
- **Graphify** — interactive prerequisite DAG: click any chapter, see what it needs and what it unlocks
- **Made With ML content** — practitioner exercises from [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML)
- **PCA + variance explorer** — interactive visualisations for the Math Foundations chapter
- **In-site lesson reader** — render lesson markdown without leaving the dashboard

---

## Run it

```bash
cd site-new
python3 -m http.server 8080
# http://localhost:8080
```

No install. No build. No config.

---

## Credits

| Repo | What it contributed |
|------|-------------------|
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Source curriculum — chapters, lessons, capstone structure |
| [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) | Practitioner-level content and references |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | Library curation |

All used with full permission. The dashboard, gamification, and WordPress integration
were built from scratch.
