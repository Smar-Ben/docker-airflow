CREATE SCHEMA IF NOT EXISTS benoit_test;
CREATE TABLE IF NOT EXISTS benoit_test.table_med(
    id_spe INTEGER PRIMARY KEY,
    name_spe VARCHAR NOT NULL,
    rem_mean FLOAT,
    rem_taux FLOAT
);  