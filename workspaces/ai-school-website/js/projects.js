/* ============================================================
   AI SCHOOL · projects (trophy case of builds)
   A display-only view of derived stats — no new state.
   · Featured work: placeholder slots for YOUR own portfolio
     pieces (fill these in — see README slot table).
   · Capstone builds: generated from Phase 19 lessons. A build
     ships when you clear its lesson; unfinished builds stay
     shadowed/locked.
   · Achievements: the badge trophy case from game.js.
   ============================================================ */
(function () {
  'use strict';
  const { store, game, ui } = window.AIS;
  const { el } = ui;
  const $ = (s) => document.querySelector(s);

  store.seedIfEmpty(PHASES);
  const s = game.derive(PHASES, store.load());

  /* ---------- featured work (your portfolio — placeholders) ---------- */
  // Replace these with real projects: swap the .slot for an <img>/link and
  // edit name/desc/href. Kept deliberately empty so it reads as "to fill".
  const FEATURED = [
    { role: 'Shipped product', hint: 'A thing you built and put in front of users.' },
    { role: 'Open source',     hint: 'A repo, tool, or library you maintain.' },
    { role: 'Experiment',      hint: 'A demo, paper reimplementation, or weekend hack.' }
  ];
  $('#featured').replaceChildren(...FEATURED.map((f) => el('div', { class: 'proj is-locked' }, [
    el('div', { class: 'slot proj__art' }, 'cover 16×9'),
    el('div', { class: 'proj__body' }, [
      el('div', { class: 'proj__name' }, 'Add a project'),
      el('div', { class: 'proj__desc' }, f.hint),
      el('div', { class: 'proj__foot' }, [
        el('span', { class: 'proj__tag' }, f.role),
        el('span', { class: 'proj__st' }, 'empty')
      ])
    ])
  ])));

  /* ---------- capstone builds (from Phase 19) ----------
     Phase 19 carries 55 capstone lessons. Showing every one as a card
     is a monotonous wall, so we feature the first CAP and link the rest
     to the Roadmap manifest (filtered to world 19). */
  const CAP = 18;
  const cap = PHASES.find((p) => p.id === 19);
  const lessons = cap ? cap.lessons : [];
  const shipped = lessons.filter((_, i) => store.isDone(19, i)).length;
  $('#capcount').textContent = `${shipped} / ${lessons.length} shipped`;

  const tiles = lessons.slice(0, CAP).map((l, i) => {
    const done = store.isDone(19, i);
    const cls = 'proj ' + (done ? 'is-shipped' : 'is-locked');
    const foot = el('div', { class: 'proj__foot' }, [
      el('span', { class: 'proj__tag' }, l.lang && l.lang !== '—' ? l.lang : 'Capstone'),
      done && l.url
        ? el('a', { class: 'proj__link', href: l.url, target: '_blank', rel: 'noopener' }, 'View ↗')
        : el('span', { class: 'proj__st' }, done ? 'Shipped' : 'Locked')
    ]);
    return el('div', { class: cls }, [
      el('div', { class: 'slot proj__art' }, done ? 'build 16×9' : '🔒 locked'),
      el('div', { class: 'proj__body' }, [
        el('div', { class: 'proj__name' }, l.name),
        el('div', { class: 'proj__desc' }, l.summary || ''),
        foot
      ])
    ]);
  });

  // tail tile linking to the rest of the capstone catalogue
  if (lessons.length > CAP) {
    tiles.push(el('a', { class: 'proj is-locked proj--more', href: 'roadmap.html' }, [
      el('div', { class: 'slot proj__art' }, '+' + (lessons.length - CAP)),
      el('div', { class: 'proj__body' }, [
        el('div', { class: 'proj__name' }, '+' + (lessons.length - CAP) + ' more'),
        el('div', { class: 'proj__desc' }, 'See every capstone build in the Roadmap manifest.'),
        el('div', { class: 'proj__foot' }, [
          el('span', { class: 'proj__tag' }, 'World 19'),
          el('span', { class: 'proj__link' }, 'Open ↗')
        ])
      ])
    ]));
  }
  $('#builds').replaceChildren(...tiles);

  /* ---------- achievements (badge trophy case) ---------- */
  $('#trophies').replaceChildren(...s.badges.map((b) => el('div', { class: 'badge ' + (b.got ? 'is-got' : 'is-locked') }, [
    el('div', { class: 'slot badge__ic' }, b.got ? '★' : '?'),
    el('div', { class: 'badge__l' }, b.label)
  ])));
})();
