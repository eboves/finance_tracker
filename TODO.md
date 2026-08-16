# TODO

Weekly goals for the Finance Tracker. Checked off as they're actually done and
verified working — not just attempted.

## This week (by Sun Aug 16, 2026) — finish V1

- [x] Working `get_connection()` in `database.py`
- [x] `accounts` table designed and created (`schema.sql`)
- [x] Working write path — `add_account.py` (parameterized INSERT)
- [x] Working read path — `get_accounts()` (`fetchall()`)
- [x] Refactor `add_account.py`'s insert logic into a proper `add_account()`
      function in `database.py` (parameterized: name, account_type,
      institution, date_opened) — same extraction pattern as
      `get_connection()` / `get_accounts()`
- [x] Design + create a `balances` table (`schema.sql`) — time-stamped
      snapshots, separate from `accounts`, with a real foreign key to
      `accounts(id)`
- [x] Write `add_balance()` in `database.py` (found and fixed two real bugs:
      unquoted `%s` placeholders, and passing a bare string instead of a
      one-item tuple as the params argument)
- [x] Write `get_balances()` — a real reader for the `balances` table
- [x] Add basic `try`/`except`/`finally` error handling around all database
      functions (`get_accounts`, `add_account`, `get_balance`, `add_balance`)
      — found and fixed several real bugs along the way: unsafe cleanup when
      `conn`/`cur` never got created, a copy-paste bug closing `conn` twice
      instead of `cur`, and `UnboundLocalError` risk on returning a variable
      that was never assigned when the query failed

**Done with the list above = V1 complete.** Next up after that: V2, Flask.

## Later (not this week)

- More tables from original design: `dividends`, `contracts`, `concepts`
- README with real project description, ER diagram
- Flask app + routes (V2)
