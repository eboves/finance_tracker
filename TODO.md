# TODO

Weekly goals for the Finance Tracker. Checked off as they're actually done and
verified working — not just attempted.

## This week (by Sun Aug 30, 2026) — V3, full REST semantics

V2 finished early (Aug 20, 3 days ahead of its own deadline) — new goal
starts now rather than waiting for the calendar week to reset.

- [ ] `update_account()` in `database.py` — real `UPDATE ... WHERE id = %s`
      SQL (first time using `UPDATE`; the `WHERE` clause is not optional —
      omit it and every row gets overwritten, not just one)
- [ ] `PUT /accounts/<int:account_id>` route — full replacement semantics,
      validated fields (same `400` pattern as POST), returns `200` (not
      `201` — nothing new was created)
- [ ] `PATCH /accounts/<int:account_id>` — partial update (only the fields
      actually sent get changed, everything else stays as-is); different
      semantics from PUT on purpose, not just a copy of it
- [ ] `DELETE /accounts/<int:account_id>` — `delete_account()` with the same
      `WHERE id = %s` safety rule, correct status code for a successful
      delete (`204 No Content` is conventional — no body needed)
- [ ] Apply the same PUT/PATCH/DELETE pattern to `/balances/<id>` — mostly
      independently this time, same shape already built once for accounts

**Done with the list above = V3 complete: full CRUD, all major HTTP
methods, on both existing resources.** After that: `dividends`,
`contracts`, `concepts` tables become a more independent "build it, I'll
review" exercise rather than a taught lesson (see reasoning below).

## Previous week (by Sun Aug 23, 2026) — V2, Flask

Already done today (Aug 16), carried here for the record:
- [x] Install Flask, minimal "Hello World" app (`app.py`)
- [x] `GET /accounts` route, wired to `get_accounts()`
- [x] `GET /balances` route, wired to `get_balances()`
- [x] Switched reader functions (`get_accounts`, `get_balance`, `get_balances`)
      to `RealDictCursor` — JSON now returns labeled objects, not bare
      positional arrays

Remaining this week:
- [x] Set up Thunder Client (VS Code extension) — needed because browsers can
      only easily test `GET` requests; testing `POST` requires a real API
      client
- [x] `POST /accounts` route — reads data from the incoming request body
      (`request.json`), calls `add_account()`, returns `201` + echoes
      submitted data (found/fixed real bugs along the way: `request.json` is
      a property not a method, a misplaced status-code tuple, a typo'd dict
      key, and Thunder Client's 415 error from not setting body type to JSON)
- [x] `POST /balances` route — same idea, wired to `add_balance()` (also
      fixed a REST consistency bug: route was `/balance` singular while GET
      was `/balances` plural — same resource must use the same URL path,
      method is what differs)
- [x] Use correct HTTP status codes — `201` for "successfully created" on
      both POST routes
- [x] Basic request validation — `400` + clear message on both POST routes
      when a required field is missing (found/fixed a real bug along the
      way: checks were testing extracted *values* against `data` instead of
      the literal string keys, and extraction was happening before
      validation instead of after)
- [x] `GET /accounts/<id>` — route parameter (`<int:account_id>`), new
      `get_account_by_id()` using `fetchone()` (not `fetchall()` — an `id`
      is unique, at most one row possible), `404` on a nonexistent id,
      `RealDictCursor` for consistent labeled JSON

**V2 COMPLETE as of Aug 19/20, 2026** — a Flask app with working GET/POST
routes on two resources, proper status codes (200/201/400/404), real
request validation, and a single-resource route. Next up: V3, full REST
semantics (PUT/PATCH, DELETE, deeper validation).

## Completed

### V1 — Python + PostgreSQL foundation (done Aug 8-15, 2026)
- Working `get_connection()`, `accounts` + `balances` tables (with a real
  foreign key), full read/write on both, `try`/`except`/`finally` error
  handling across every database function.

### V2 — Flask (done Aug 16-20, 2026)
- Flask app with GET/POST routes on two resources, `RealDictCursor` for
  labeled JSON, proper status codes (200/201/400/404), real request
  validation, single-resource route with a URL parameter.

## Later (not this week)

- More tables from original design: `dividends`, `contracts`, `concepts` —
  once V3 is done, this becomes a semi-independent "you build it, I review"
  exercise rather than a taught lesson (depth-before-breadth decision made
  Aug 20 2026 — full REST on 2 resources beats partial REST on 5)
- README with real project description, ER diagram
- Authentication (V4)
- pytest (V5)
- Deployment (V6, Railway/Render)
- **Frontend — AFTER backend (V1-V7) is done, not before.** Decided:
  Flask + Jinja2 server-rendered HTML, NOT React — no new language/build
  tooling, no CORS (same origin as the API), simpler deployment (one app,
  not two), and a stronger story for backend-focused interviews. Scope
  small on purpose: a simple read-only dashboard against the existing
  `GET /accounts` and `GET /balances` endpoints (totals, account list) —
  not a full CRUD UI with forms. Elvis writes the Python/Jinja2 logic
  himself; AI help is fair game specifically for HTML/CSS visual styling,
  which he can honestly frame in interviews as "I built the backend and
  the page logic; used AI for the parts outside my specialty (visual
  design)" — a legitimate, honest positioning, not something to hide.
  Timing risk to watch: backend is projected to finish ~early-to-mid Oct,
  job target is November — keep this to 1-3 focused sessions when the
  time comes, not an open-ended build that eats into interview prep.