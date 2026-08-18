# TODO

Weekly goals for the Finance Tracker. Checked off as they're actually done and
verified working — not just attempted.

## This week (by Sun Aug 23, 2026) — V2, Flask

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
- [ ] Basic request validation — check required fields actually exist in the
      request body before calling the database function, return `400` with
      a clear message if something's missing (not yet done on either POST
      route — currently a missing field would crash with a raw 500 error)
- [ ] `GET /accounts/<id>` — a route with a URL parameter, returning one
      specific account instead of all of them

**Done with the list above = V2 substantially complete.** Next up after
that: V3, full REST semantics (PUT/PATCH, DELETE, more validation).

## Completed

### V1 — Python + PostgreSQL foundation (done Aug 8-15, 2026)
- Working `get_connection()`, `accounts` + `balances` tables (with a real
  foreign key), full read/write on both, `try`/`except`/`finally` error
  handling across every database function.

## Later (not this week)

- More tables from original design: `dividends`, `contracts`, `concepts`
- `PUT`/`PATCH`, `DELETE` routes (V3)
- README with real project description, ER diagram
- Authentication (V4)
- pytest (V5)