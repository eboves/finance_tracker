# TODO

Weekly goals for the Finance Tracker. Checked off as they're actually done and
verified working — not just attempted.

## This week (by Sun Aug 16, 2026) — finish V1

- [x] Working `get_connection()` in `database.py`
- [x] `accounts` table designed and created (`schema.sql`)
- [x] Working write path — `add_account.py` (parameterized INSERT)
- [x] Working read path — `get_accounts()` (`fetchall()`)
- [ ] Refactor `add_account.py`'s insert logic into a proper `add_account()`
      function in `database.py` (parameterized: name, account_type,
      institution, date_opened) — same extraction pattern as
      `get_connection()` / `get_accounts()`
- [ ] Design + create a `balances` table (`schema.sql`) — time-stamped
      snapshots, separate from `accounts` (see why in dev notes: static
      identity vs. value-over-time)
- [ ] Write `get_balances()` and `add_balance()` in `database.py`
- [ ] Add basic `try`/`except` error handling around the database functions

**Done with the list above = V1 complete.** Next up after that: V2, Flask.

## Later (not this week)

- More tables from original design: `dividends`, `contracts`, `concepts`
- README with real project description, ER diagram
- Flask app + routes (V2)
