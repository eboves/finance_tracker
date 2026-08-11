-- CREATE TABLE accounts (
--     id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     name TEXT NOT NULL,
--     account_type TEXT NOT NULL CHECK(account_type IN ('checking','savings','roth_ira', 'credit_card')),
--     institution TEXT NOT NULL,
--     date_opened DATE,
--     is_active BOOLEAN NOT NULL DEFAULT TRUE,
--     created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
--     );

-- DROP TABLE accounts;

SELECT * FROM accounts;