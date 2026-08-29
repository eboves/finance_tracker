CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    account_type TEXT NOT NULL CHECK(account_type IN ('checking','savings','roth_ira', 'credit_card', '401k', 'hsa', 'ira')),
    institution TEXT NOT NULL,
    date_opened DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );

CREATE TABLE IF NOT EXISTS balances (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    date DATE NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    account_id INTEGER NOT NULL REFERENCES accounts(id)
); 

CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    ticket TEXT NOT NULL,
    shares NUMERIC(12, 2) NOT NULL,
    pays_dividend BOOLEAN NOT NULL DEFAULT FALSE,
    account_id INTEGER NOT NULL REFERENCES accounts(id),
    how_often_pays TEXT NOT NULL CHECK (how_often_pays IN ('None', 'monthly', 'quaterly', 'semi_annual', 'annual'))
);