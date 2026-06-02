/* ============================================================
   AI SCHOOL · course (player card + curriculum accordion)
   Top of the page is your save file (level, rank, XP, career
   meters). Below it, every world as an accordion — tick a lesson
   to bank its XP. Hands-on builds happen in Claude Code; the
   "Read ↗" link opens each lesson's repo.
   ============================================================ */
(function () {
  'use strict';
  const { store, game, ui } = window.AIS;
  const { el } = ui;
  const $ = (s) => document.querySelector(s);

  store.seedIfEmpty(PHASES);

  /* ---------- player card (identity + career meters) ---------- */
  function renderCard() {
    const s = game.derive(PHASES, store.load());

    $('#id').replaceChildren(
      el('div', { class: 'slot card__ava' }, 'pixel avatar 32×32'),
      el('div', { class: 'card__lv pix' }, 'LV.' + String(s.level).padStart(2, '0')),
      el('div', { class: 'card__rank' }, s.rank),
      el('div', { class: 'card__name' }, 'building AI from scratch'),
      el('div', { class: 'xp', style: 'margin:16px 0 6px' }, el('i', { style: `--p:${s.pctIntoLevel}%` })),
      el('div', { class: 'xp__txt', style: 'text-align:center' }, `${s.intoLevel} / ${s.levelSpan} XP → LV.${String(s.level + 1).padStart(2, '0')}`),
      el('div', { class: 'card__actions' }, [
        el('span', { class: 'pill pill--flame' }, `🔥 ${s.streak}d`),
        el('button', { class: 'btn', onClick: exportJSON }, 'Export'),
        el('button', { class: 'btn', onClick: reset }, 'Reset')
      ])
    );

    const rows = [
      ['Lessons cleared', s.lessonsDone, s.lessonsDone / s.lessonsTotal],
      ['Worlds cleared', s.phasesCleared, s.phasesCleared / s.phasesTotal],
      ['Languages', `${s.languages}/${s.languagesTotal}`, s.languages / s.languagesTotal],
      ['Build artifacts', s.buildArtifacts, Math.min(1, s.buildArtifacts / 60)],
      ['Best streak', s.bestStreak + 'd', Math.min(1, s.bestStreak / 30)]
    ];
    $('#stats').replaceChildren(...rows.map(([l, v, p]) => el('div', { class: 'stat' }, [
      el('span', { class: 'stat__l' }, l),
      el('span', { class: 'bar' }, el('i', { style: `--p:${Math.round(p * 100)}%` })),
      el('span', { class: 'stat__v' }, String(v))
    ])));
  }

  function exportJSON() {
    const blob = new Blob([store.exportJSON()], { type: 'application/json' });
    const a = el('a', { href: URL.createObjectURL(blob), download: 'aischool-progress.json' });
    a.click();
  }
  function reset() {
    if (confirm('Reset all progress? (demo seed will reload on refresh)')) { store.reset(); location.reload(); }
  }

  /* ---------- curriculum accordion ---------- */
  const expanded = new Set();
  let filter = 'all';

  const phaseStat = (ph) => {
    let done = 0;
    ph.lessons.forEach((_, i) => { if (store.isDone(ph.id, i)) done++; });
    const total = ph.lessons.length;
    return { done, total, pct: total ? Math.round((done / total) * 100) : 0 };
  };

  const passes = (st) =>
    filter === 'all' ||
    (filter === 'cleared' && st.pct === 100) ||
    (filter === 'progress' && st.pct > 0 && st.pct < 100) ||
    (filter === 'untouched' && st.pct === 0);

  function lessonRow(ph, ls, i) {
    const done = store.isDone(ph.id, i);
    return el('div', { class: 'lesson' + (done ? ' is-done' : '') }, [
      el('button', { class: 'lesson__chk' + (done ? ' is-done' : ''), 'aria-label': 'toggle',
        onClick: () => { store.toggle(ph.id, i); renderCard(); render(); } }, done ? '✓' : ''),
      el('div', { class: 'lesson__main' }, [
        ls.url ? el('a', { class: 'lesson__nm', href: ls.url, target: '_blank', rel: 'noopener', style: 'border-bottom:1px solid transparent' }, ls.name)
               : el('div', { class: 'lesson__nm' }, ls.name),
        el('div', { class: 'lesson__meta' }, [
          el('span', { class: 'lesson__type', 'data-t': ls.type }, ls.type),
          el('span', null, ls.lang || '—'),
          el('span', null, '+' + game.xpFor(ls) + ' XP')
        ])
      ])
    ]);
  }

  function phaseBlock(ph) {
    const st = phaseStat(ph);
    const open = expanded.has(ph.id);
    const head = el('button', { class: 'toc__phase', 'aria-expanded': open ? 'true' : 'false',
      onClick: () => { open ? expanded.delete(ph.id) : expanded.add(ph.id); render(); } }, [
      el('span', { class: 'toc__num' }, String(ph.id).padStart(2, '0')),
      el('span', null, [
        el('span', { class: 'toc__nm' + (st.pct === 100 ? ' is-done' : '') }, ph.name),
        ph.id === 19 ? el('span', { class: 'toc__badge' }, '☠ boss') : null
      ].filter(Boolean)),
      el('span', { class: 'xp toc__count mini', style: 'height:8px' }, el('i', { style: `--p:${st.pct}%` })),
      el('span', { class: 'toc__count' }, `${st.done}/${st.total}`),
      el('span', { class: 'toc__chev' }, '▸')
    ]);
    const frag = [head];
    if (open) frag.push(el('div', { class: 'toc__lessons' }, ph.lessons.map((ls, i) => lessonRow(ph, ls, i))));
    return frag;
  }

  function render() {
    const list = PHASES.filter((ph) => passes(phaseStat(ph)));
    const host = $('#toc');
    host.replaceChildren();
    list.forEach((ph) => phaseBlock(ph).forEach((n) => host.append(n)));
    const s = game.derive(PHASES, store.load());
    $('#count').textContent = `${list.length} of ${PHASES.length} phases · ${s.lessonsDone}/${s.lessonsTotal} lessons cleared`;
  }

  $('#filter').addEventListener('change', (e) => { filter = e.target.value; render(); });
  renderCard();
  render();
})();
