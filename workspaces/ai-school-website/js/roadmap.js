/* ============================================================
   AI SCHOOL · roadmap (prerequisite dependency graph)
   True to the curriculum's original Roadmap: the DAG only.
   Click a world to SELECT it — lights everything it needs
   (upstream) + everything it unlocks (downstream), dims the
   rest. Click again or "Clear selection" to reset. Hover gives
   a quick preview without committing. The searchable lesson
   list lives on its own Catalog page.
   ============================================================ */
(function () {
  'use strict';
  const { store, game, ui } = window.AIS;
  const { el } = ui;
  const $ = (s) => document.querySelector(s);

  store.seedIfEmpty(PHASES);
  const stats = game.derive(PHASES, store.load());
  const byId = (id) => stats.phaseStats.find((p) => p.id === id);

  /* prerequisite graph (mirror of the curriculum roadmap).
     NOTE: also duplicated in hub.js — edit both. */
  const PREREQS = {
    0: [], 1: [0], 2: [1], 3: [2], 4: [3], 5: [3], 6: [3], 7: [3], 8: [3, 7],
    9: [3], 10: [7], 11: [10], 12: [4, 6, 11], 13: [11], 14: [11, 13],
    15: [14], 16: [15], 17: [11], 18: [10], 19: [14, 15, 16, 17]
  };
  const UNLOCKS = {};
  Object.entries(PREREQS).forEach(([id, reqs]) => reqs.forEach((r) => (UNLOCKS[r] = UNLOCKS[r] || []).push(+id)));

  /* ---------- DAG layout (column = longest path from a root) ---------- */
  const _depth = {};
  function depthOf(id) {
    if (id in _depth) return _depth[id];
    const reqs = PREREQS[id] || [];
    return (_depth[id] = reqs.length ? 1 + Math.max(...reqs.map(depthOf)) : 0);
  }
  function chain(id, graph) {
    const out = new Set();
    (function walk(x) { (graph[x] || []).forEach((n) => { if (!out.has(n)) { out.add(n); walk(n); } }); })(id);
    return out;
  }

  const TILE = 72, NW = 96, OFF = (NW - TILE) / 2, COL = 168, ROW = 128;

  function layout() {
    const ids = PHASES.map((p) => p.id);
    const maxD = Math.max(...ids.map(depthOf));
    const cols = Array.from({ length: maxD + 1 }, () => []);
    ids.forEach((id) => cols[depthOf(id)].push(id));
    const rowIndex = {};
    const bary = (id) => {
      const r = (PREREQS[id] || []).map((p) => rowIndex[p]).filter((v) => v != null);
      return r.length ? r.reduce((a, b) => a + b, 0) / r.length : 1e9;
    };
    cols.forEach((col, d) => {
      col.sort(d === 0 ? (a, b) => a - b : (a, b) => bary(a) - bary(b) || a - b);
      col.forEach((id, i) => (rowIndex[id] = i));
    });
    const colH = Math.max(...cols.map((c) => c.length)) * ROW;
    const pos = {};
    cols.forEach((col, d) => {
      const off = (colH - col.length * ROW) / 2;
      col.forEach((id, i) => (pos[id] = { x: d * COL, y: off + i * ROW }));
    });
    return { pos, width: maxD * COL + NW, height: colH + 24 };
  }

  /* ---------- selection / trace ---------- */
  let treeEl = null;
  let selected = null;

  function paint(id) {
    const lit = new Set([id, ...chain(id, PREREQS), ...chain(id, UNLOCKS)]);
    treeEl.classList.add('is-tracing');
    treeEl.querySelectorAll('.tnode').forEach((n) => n.classList.toggle('is-lit', lit.has(+n.dataset.id)));
    treeEl.querySelectorAll('.tree-edge').forEach((e) => e.classList.toggle('is-lit', lit.has(+e.dataset.f) && lit.has(+e.dataset.t)));
  }
  function unpaint() {
    treeEl.classList.remove('is-tracing');
    treeEl.querySelectorAll('.is-lit').forEach((n) => n.classList.remove('is-lit'));
  }

  function hoverIn(id) { paint(id); }                       // preview
  function hoverOut() { selected != null ? paint(selected) : unpaint(); }

  function select(id) {
    selected = (selected === id) ? null : id;
    treeEl.querySelectorAll('.tnode').forEach((n) => n.classList.toggle('tnode--sel', selected != null && +n.dataset.id === selected));
    $('#clear').hidden = selected == null;
    const p = byId(selected);
    $('#selinfo').textContent = selected == null ? '' :
      `World ${String(selected).padStart(2, '0')} · ${p.name} — needs ${chain(selected, PREREQS).size}, unlocks ${chain(selected, UNLOCKS).size}`;
    selected != null ? paint(selected) : unpaint();
  }
  function clearSel() { selected = null; $('#clear').hidden = true; $('#selinfo').textContent = ''; treeEl.querySelectorAll('.tnode--sel').forEach((n) => n.classList.remove('tnode--sel')); unpaint(); }

  function tnode(p) {
    const boss = p.id === 19;
    const cls = ['tnode',
      p.pct === 100 ? 'is-done' : p.pct > 0 ? 'is-active' : 'is-locked',
      boss ? 'tnode--boss' : ''].join(' ');
    return el('button', {
      class: cls, 'data-id': p.id,
      'aria-label': `${p.name} — ${p.pct === 100 ? 'complete' : p.pct > 0 ? 'in progress' : 'planned'}`,
      onClick: () => select(p.id),
      onMouseenter: () => hoverIn(p.id), onMouseleave: hoverOut,
      onFocus: () => hoverIn(p.id), onBlur: hoverOut
    }, [
      el('span', { class: 'tnode__tile' }, String(p.id).padStart(2, '0')),
      el('span', { class: 'tnode__nm' }, p.name)
    ]);
  }

  function renderTree() {
    const { pos, width, height } = layout();
    const edges = [];
    PHASES.forEach((p) => (PREREQS[p.id] || []).forEach((pr) => {
      const a = pos[pr], b = pos[p.id]; if (!a || !b) return;
      const x1 = a.x + OFF + TILE, y1 = a.y + TILE / 2, x2 = b.x + OFF, y2 = b.y + TILE / 2;
      const dx = Math.max(36, (x2 - x1) * 0.45);
      const trav = byId(pr)?.pct === 100 && byId(p.id)?.pct > 0 ? ' is-trav' : '';
      edges.push(`<path class="tree-edge${trav}" data-f="${pr}" data-t="${p.id}" d="M${x1},${y1} C${x1 + dx},${y1} ${x2 - dx},${y2} ${x2},${y2}"/>`);
    }));
    const tree = el('div', { class: 'tree', style: `width:${width}px;height:${height}px` });
    tree.innerHTML = `<svg class="tree-edges" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">${edges.join('')}</svg>`;
    stats.phaseStats.forEach((p) => {
      const n = tnode(p);
      n.style.cssText = `left:${pos[p.id].x}px;top:${pos[p.id].y}px`;
      tree.append(n);
    });
    $('#tree').replaceChildren(tree);
    treeEl = tree;
  }

  renderTree();
  $('#clear').addEventListener('click', clearSel);
})();
