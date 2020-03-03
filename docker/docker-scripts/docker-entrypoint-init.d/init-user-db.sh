#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER webworker;
    CREATE USER phpadmin;
    CREATE DATABASE vmctap;
    GRANT ALL PRIVILEGES ON DATABASE vmctap TO webworker;
EOSQL