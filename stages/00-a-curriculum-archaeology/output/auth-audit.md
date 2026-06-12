# Auth Audit
<!-- Derived from: site-new/js/auth.js, api/auth.js, api/_lib/auth.js -->
<!-- Capture date: 2026-06-12 | Git hash: 56e1283 -->

## Auth mechanism

GitHub OAuth, server-side. Flow:

```
User clicks "Sign in"
  → GET /api/auth
    → GitHub OAuth authorize (scope: read:user)
  → GitHub redirects to /api/auth/callback with code
    → Server exchanges code for token
    → Sets sa_user cookie: "login:avatar_url" (URL-encoded)
  → Client (site-new/js/auth.js) reads sa_user cookie on load
    → If cookie present: swaps AIS.store adapter to vercelAdapter
    → Renders avatar + username in header button
    → Progress reads/writes go to /api/progress (Vercel KV)
  → On logout: GET /api/logout → clears cookie → adapter reverts to localStorage
```

## Session model

Cookie name: `sa_user`  
Format: `{login}:{avatar_url}` (URL-encoded, colon-separated)  
Persistence: cookie-based (no JWT, no session store — cookie IS the session)  
Auth state: stateless on client — presence of valid `sa_user` cookie = authenticated

Progress adapter pattern (`site-new/js/store.js`):
```javascript
// Local (unauthenticated)
localAdapter: { read() → localStorage, write(p) → localStorage }

// Vercel (authenticated)
vercelAdapter: { read() → GET /api/progress, write(p) → POST /api/progress }
```

Swap is one line: `AIS.store.adapter = vercelAdapter`  
No page code changes needed — all screens call `store.read()` and `store.write()`.

## Known failure modes

| Mode | Symptom | What Stage 07 must handle |
|------|---------|--------------------------|
| Cookie parse failure | `getSaUser()` returns null, user treated as unauthenticated even if OAuth succeeded | Graceful fallback to localStorage — currently handled (silent) |
| Avatar URL missing | `colon === -1` in cookie value → returns null | Handled: `colon > 0` check, returns null instead of throwing |
| Store not loaded at cookie-check time | `window.AIS.store` undefined when auth.js runs | Handled: DOMContentLoaded listener swaps adapter if store loads late |
| `/api/progress` write fails | Progress write throws (network error, Vercel down) | Handled: silent catch — local copy already written, remote write fails silently |
| `/api/progress` read fails | Returns null → store falls back to empty state | Handled: null check → returns null, store treats as fresh state |
| **GitHub OAuth not configured** | `GITHUB_CLIENT_ID` env var missing → redirect to undefined | **UNHANDLED** — no guard in api/auth.js. Silent redirect to garbage URL. Stage 07 must add env validation. |
| **SITE_URL not set** | `redirect_uri` points to undefined → OAuth callback breaks | **UNHANDLED** — `api/auth.js` uses `process.env.SITE_URL` without fallback. Stage 07 must add fallback. |

## Stage 07 implications

**Architecture decision (resolved in 00-d):** The site auth backend is gutted. The site is read-only content delivery. Progress lives in `progress/progress.json` inside the student's mission command fork (the Albatross). Helix reads filesystem state, not a site API.

1. **DELETE the auth backend**: `api/auth.js`, `api/progress.js`, `api/_lib/auth.js` are removed. No GitHub OAuth. No Vercel KV. No sa_user cookie.

2. **Simplify store.js**: Remove `vercelAdapter` entirely. If `localAdapter` is kept at all, it is cosmetic only (lesson visit log) — not canonical state. The student's canonical state is in their repo.

3. **Gut auth.js**: `site-new/js/auth.js` is removed or replaced with a no-op stub. No cookie parsing, no header button rendering for OAuth, no adapter swapping.

4. **FSRS state location**: `progress/progress.json → fsrs: {}` in the mission command fork. Never on the site server. The schema from the current `/api/progress` endpoint is superseded — see `stages/00-d-helix-design/output/fsrs-integration-spec.md` for the new schema.

5. **The unhandled failure modes are moot**: `GITHUB_CLIENT_ID` missing and `SITE_URL` missing are no longer concerns — the OAuth flow does not exist after Stage 07.

## Auth files reference (post-Stage-07 state)

| File | Action | Reason |
|------|--------|--------|
| `api/auth.js` | DELETE | OAuth backend removed |
| `api/progress.js` | DELETE | Vercel KV progress removed |
| `api/_lib/auth.js` | DELETE | OAuth callback removed |
| `site-new/js/auth.js` | DELETE or stub | Cookie reader no longer needed |
| `site-new/js/store.js` | SIMPLIFY — remove vercelAdapter | localAdapter only (or remove if site tracks nothing) |
