# TODO

Weekly goals for the Finance Tracker. Checked off as they're actually done and
verified working — not just attempted.

## Previous week (by Sun Aug 30, 2026) — V3, full REST semantics — DONE Aug 25

V2 finished early (Aug 20, 3 days ahead of its own deadline) — new goal
starts now rather than waiting for the calendar week to reset.

- [x] `update_account_by_id()` in `database.py` — real `UPDATE ... WHERE
      id = %s` SQL (first time using `UPDATE`), verified via `psql` that
      the row was overwritten in place (same `id`, unchanged `created_at`,
      new values) — not a new row created
- [x] `PUT /accounts/<int:account_id>` route — full replacement semantics,
      validated fields (same `400` pattern as POST), returns `200` (found
      and fixed a real bug: initially returned `201`, which is wrong —
      `201` means "created," this is an update to an existing resource)
- [x] `PATCH /accounts/<int:account_id>` — partial update, verified via
      `psql`: only the one field sent actually changed, everything else
      stayed exactly as it was (fixed a route-syntax bug along the way —
      `int:` converter must go *inside* the `<>` brackets, not before them
      — plus the same status-code and fallback-value bugs as before,
      applied consistently to all 4 fields this time)
- [x] `DELETE /accounts/<int:account_id>` — `delete_account_by_id()` using
      `cur.rowcount` to detect whether anything was actually deleted, `204`
      on success / `404` on a nonexistent id — all three verified via real
      server logs (found/fixed a real bug: the DB function was returning a
      tuple `(count, 204)` instead of a plain count, which silently broke
      the 404 check — `deleted == 0` can never be True when `deleted` is
      actually a tuple; status codes belong in the Flask layer, not the
      database layer)
- [x] Applied the same PUT/PATCH/DELETE pattern to `/balances/<id>` —
      built almost entirely independently, including `get_balance_by_id()`
      (needed for PATCH's fetch-then-merge, self-identified without being
      told), and correctly avoided repeating the earlier `DELETE` tuple bug
      on `delete_balance_by_id()` without prompting. Recovered from a real
      incident along the way: `update_balance_by_id()` initially filtered
      `WHERE account_id = %s` instead of `WHERE id = %s` — since
      `account_id` isn't unique (many balances can share one account), this
      overwrote multiple rows with the same values before being caught and
      fixed. All three methods verified via real `psql` snapshots showing
      selective, correct single-row targeting.

**V3 COMPLETE as of Aug 25, 2026** — full CRUD (all 4 HTTP methods),
correct status codes throughout, real validation, on BOTH `accounts` and
`balances`. Next: `dividends`/`contracts`/`concepts` tables become a
semi-independent "build it, I'll review" exercise rather than a taught
lesson (depth-before-breadth decision, see Later section).

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

### V3 — Full REST semantics (done Aug 20-25, 2026)
- Full CRUD (`GET`/`POST`/`PUT`/`PATCH`/`DELETE`) on both `accounts` and
  `balances`, correct status codes throughout, real validation. Recovered
  from a real data-corruption incident (wrong `WHERE` column) — genuine
  debugging experience, good interview material.

## Now up — semi-independent build (not this-week-scoped, ongoing)

- `dividends`, `contracts`, `concepts` tables — full CRUD each, same
  pattern as `accounts`/`balances`, built mostly independently with review
  rather than taught step by step (depth-before-breadth decision made
  Aug 20 2026 — full REST on 2 resources beats partial REST on 5)
- Two more tables identified from the dashboard mockup (Aug 2026): a
  `holdings` table (stock positions — ticker, company name, quantity, cost
  basis; NOT the same thing as `dividends`) and a `goals` table (target
  amount, current progress, optional target date — e.g. "AMEX payoff:
  $880/$4,000, target March 2027"). `concepts` may already be intended for
  the "this week's investing concept" educational card — confirm with
  Elvis when that table gets designed.
- README with real project description, ER diagram
- Authentication (V4)
- pytest (V5)
- Deployment (V6, Railway/Render)
- **Frontend — AFTER backend (V1-V7) is done, not before.** Decided:
  Flask + Jinja2 server-rendered HTML, NOT React — no new language/build
  tooling, no CORS (same origin as the API), simpler deployment (one app,
  not two), and a stronger story for backend-focused interviews. Elvis
  writes the Python/Jinja2 logic himself; AI help is fair game
  specifically for HTML/CSS visual styling — honest interview framing:
  "I built the backend and the page logic; used AI for the parts outside
  my specialty (visual design)."
  **Concrete target mockup provided Aug 2026** (dark dashboard, "Finance
  tracker — Money Sunday"): Net Worth / Total Assets / Total Liabilities /
  Monthly Dividends summary cards; Assets and Liabilities breakdown by
  account with progress bars; AMEX payoff progress with a target date;
  Stock portfolio section (ticker, price, % change, covered-calls badges);
  Dividends-this-month by ticker; Goals tracker (dividends/emergency
  fund/AMEX payoff, current vs target); "This week's investing concept"
  educational card. This is the destination, not something to build in one
  pass — needs the `holdings`/`goals` tables above plus aggregation logic
  (net worth = assets − liabilities, % of goal, etc.) before the page
  itself is worth building.
  **Live stock prices/% change via an external API — confirmed IN scope**
  (decided Aug 2026, not just a maybe): genuinely valuable backend skill
  (third-party API calls, handling their responses/errors, managing
  another secret safely). Sequenced with the `holdings` table build,
  since price data belongs to holdings, not accounts/balances — not
  something to start before then.
  Timing risk to watch: backend is projected to finish ~early-to-mid Oct,
  job target is November — keep the frontend phase to a handful of
  focused sessions when the time comes, not an open-ended build that eats
  into interview prep.