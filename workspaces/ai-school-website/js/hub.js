/* ============================================================
   AI SCHOOL · hub (world map + phase drawer)
   Renders from PHASES (data.js) + derived stats. Mutations go
   through the store, then a single refresh() re-derives + repaints.
   ============================================================ */
(function () {
  'use strict';
  const { store, game, ui } = window.AIS;
  const { el, toast } = ui;
  const $ = (s) => document.querySelector(s);

  store.seedIfEmpty(PHASES);

  // Real prerequisite graph (from the curriculum's roadmap). Drawer shows
  // these as "recommended after" chips — the map already encodes the path
  // visually, so no separate roadmap page is needed.
  const PREREQS = {
    0: [], 1: [0], 2: [1], 3: [2], 4: [3], 5: [3], 6: [3], 7: [3], 8: [3, 7],
    9: [3], 10: [7], 11: [10], 12: [4, 6, 11], 13: [11], 14: [11, 13],
    15: [14], 16: [15], 17: [11], 18: [10], 19: [14, 15, 16, 17]
  };
  const phaseName = (id) => PHASES.find((p) => p.id === id)?.name || ('Phase ' + id);

  let stats;
  let openId = null;

  /* ---------- HUD ---------- */
  function renderHud() {
    const s = stats;
    $('#hud').replaceChildren(
      el('div', { class: 'slot hud__ava' }, 'avatar 16×16'),
      el('div', { class: 'hud__lvl' }, [String(s.level).padStart(2, '0'), el('small', null, 'level')]),
      el('div', { class: 'hud__mid' }, [
        el('div', { class: 'hud__rank', html: `Rank: <b>${s.rank}</b> &nbsp;·&nbsp; ${s.toNext} XP to LVL ${String(s.level + 1).padStart(2, '0')}` }),
        el('div', { class: 'xp', style: `margin-top:6px` }, el('i', { style: `--p:${s.pctIntoLevel}%` })),
        el('div', { class: 'xp__txt' }, `${s.intoLevel} / ${s.levelSpan} XP`)
      ]),
      el('div', { class: 'hud__stats' }, [
        el('span', { class: 'pill pill--flame' }, `🔥 ${s.streak}-day streak`),
        el('span', { class: 'pill' }, `${s.lessonsDone} / ${s.lessonsTotal} cleared`),
        el('span', { class: 'pill' }, `${s.badges.filter((b) => b.got).length} badges`)
      ])
    );
  }

  /* ---------- world map (archipelago trail) ----------
     The 20 phases are grouped into themed "lands" that stack down the page,
     each carrying its phase pins on a dotted road. This is the navigational
     overworld; the dependency/skill-tree view lives on the Roadmap page.
     To add a phase: drop its id into the right land (or add a new land). */
  const LANDS = [
    { name: 'Foundations',     phases: [0, 1, 2] },
    { name: 'Deep Learning',   phases: [3, 4, 5, 6] },
    { name: 'Generative Era',  phases: [7, 8, 9] },
    { name: 'Language Models', phases: [10, 11, 12] },
    { name: 'Agentic Systems', phases: [13, 14, 15, 16] },
    { name: 'Production',      phases: [17, 18, 19] }
  ];

  function pin(p, isYou) {
    const boss = p.id === 19;
    const cls = ['pin',
      p.status === 'done' ? 'is-done' : p.status === 'active' ? 'is-active' : 'is-locked',
      boss ? 'pin--boss' : ''].join(' ');
    return el('button', {
      class: cls, 'data-id': p.id,
      'aria-label': `${p.name} — ${p.pct}% complete`,
      onClick: () => openDrawer(p.id)
    }, [
      isYou ? el('span', { class: 'pin__you' }, 'you') : null,
      el('span', { class: 'pin__dot' }, String(p.id).padStart(2, '0')),
      el('span', { class: 'pin__nm' }, p.name)
    ].filter(Boolean));
  }

  function renderMap() {
    const ps = stats.phaseStats;
    const byId = (id) => ps.find((p) => p.id === id);
    const youId = ps.find((x) => x.pct < 100)?.id;

    const wrap = el('div', { class: 'worldmap' });
    LANDS.forEach((land, li) => {
      const cleared = land.phases.every((id) => byId(id)?.pct === 100);
      const range = String(land.phases[0]).padStart(2, '0') + '–' +
                    String(land.phases[land.phases.length - 1]).padStart(2, '0');
      const klass = 'land' +
        (land.phases.includes(19) ? ' land--boss' : '') +
        (cleared ? ' land--cleared' : '');
      wrap.append(el('div', { class: klass }, el('div', { class: 'land__plate' }, [
        el('div', { class: 'land__hd' }, [
          el('span', { class: 'land__name' }, land.name),
          el('span', { class: 'land__meta' }, `worlds ${range}${cleared ? ' · cleared' : ''}`)
        ]),
        el('div', { class: 'land__road' }, land.phases.map((id) => pin(byId(id), id === youId)))
      ])));
      if (li < LANDS.length - 1) wrap.append(el('div', { class: 'bridge' }, [el('span'), el('span'), el('span')]));
    });
    $('#map').replaceChildren(wrap);
  }

  /* ---------- phase drawer ---------- */
  function lessonRow(phase, ls, i) {
    const doneNow = store.isDone(phase.id, i);
    const links = [];
    if (ls.url) links.push(el('a', { href: ls.url, target: '_blank', rel: 'noopener' }, 'Read ↗'));
    links.push(el('a', { href: '#', title: 'Checkpoint quiz — wired from quiz-factory in production', onClick: (e) => e.preventDefault() }, 'Quiz'));

    return el('div', { class: 'lesson' + (doneNow ? ' is-done' : '') }, [
      el('button', { class: 'lesson__chk' + (doneNow ? ' is-done' : ''), 'aria-label': 'toggle complete',
        onClick: () => onToggle(phase.id, i) }, doneNow ? '✓' : ''),
      el('div', { class: 'lesson__main' }, [
        el('div', { class: 'lesson__nm' }, ls.name),
        el('div', { class: 'lesson__meta' }, [
          el('span', { class: 'lesson__type', 'data-t': ls.type }, ls.type),
          el('span', null, ls.lang || '—'),
          el('span', null, '+' + game.xpFor(ls) + ' XP')
        ]),
        el('div', { class: 'lesson__links' }, links)
      ])
    ]);
  }

  function recLine(id) {
    const reqs = PREREQS[id] || [];
    if (!reqs.length) {
      return el('div', { class: 'drawer__rec' }, [
        el('span', { class: 'drawer__rec-l' }, 'Path'),
        el('span', { class: 'drawer__rec-note' }, 'Starting point — jump in anytime.')
      ]);
    }
    return el('div', { class: 'drawer__rec' }, [
      el('span', { class: 'drawer__rec-l' }, 'Recommended after'),
      ...reqs.map((pid) => el('button', { class: 'rec-chip', onClick: () => openDrawer(pid) },
        String(pid).padStart(2, '0') + ' · ' + phaseName(pid)))
    ]);
  }

  function renderDrawer(id) {
    const phase = PHASES.find((p) => p.id === id);
    const ps = stats.phaseStats.find((p) => p.id === id);
    $('#drawer').replaceChildren(
      el('div', { class: 'drawer__head' }, [
        el('button', { class: 'drawer__close', 'aria-label': 'close', onClick: closeDrawer }, '×'),
        el('div', { class: 'drawer__num' }, `Phase ${String(id).padStart(2, '0')} · ${phase.lessons.length} lessons`),
        el('h2', { class: 'drawer__title' }, phase.name),
        el('p', { class: 'drawer__desc' }, phase.desc || ''),
        recLine(id),
        el('div', { class: 'drawer__bar' }, [
          el('div', { class: 'xp' }, el('i', { style: `--p:${ps.pct}%` })),
          el('span', { class: 'pill' }, `${ps.done}/${ps.total}`)
        ])
      ]),
      el('div', { class: 'drawer__list' }, phase.lessons.map((ls, i) => lessonRow(phase, ls, i)))
    );
  }

  function openDrawer(id) {
    openId = id;
    renderDrawer(id);
    $('#scrim').classList.add('is-open');
    $('#drawer').classList.add('is-open');
  }
  function closeDrawer() {
    openId = null;
    $('#scrim').classList.remove('is-open');
    $('#drawer').classList.remove('is-open');
  }

  /* ---------- mutation + level-up feedback ---------- */
  function onToggle(phaseId, i) {
    const before = { level: stats.level, badges: new Set(stats.badges.filter((b) => b.got).map((b) => b.id)) };
    store.toggle(phaseId, i);
    refresh();
    if (stats.level > before.level) toast('LEVEL UP!', `You reached LVL ${stats.level} · ${stats.rank}`);
    stats.badges.filter((b) => b.got && !before.badges.has(b.id))
      .forEach((b) => toast('★ BADGE', b.label));
  }

  function refresh() {
    stats = game.derive(PHASES, store.load());
    renderHud();
    renderMap();
    if (openId != null) renderDrawer(openId);
  }

  /* ---------- boot ---------- */
  $('#scrim').addEventListener('click', closeDrawer);
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeDrawer(); });
  refresh();
})();
