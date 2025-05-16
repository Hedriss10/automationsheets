CREATE SCHEMA IF NOT EXISTS spreed;

CREATE TABLE spreed.ro (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    cpf VARCHAR UNIQUE NOT NULL,
    age INTEGER,
    date_year TIMESTAMP,
    gender VARCHAR,
    uf VARCHAR(2),
    cep VARCHAR,
    phone_base VARCHAR,
    dd_one VARCHAR(3),
    phone_one VARCHAR,
    have_whatsapp_one VARCHAR,
    dd_two VARCHAR(3),
    phone_two VARCHAR,
    have_whatsapp_two VARCHAR,
    email VARCHAR,
    email_two VARCHAR,
    email_three VARCHAR,
    create_at TIMESTAMP DEFAULT now()
);