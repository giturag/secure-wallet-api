#!/bin/bash
set -e

psql \
  --username "$POSTGRES_USER" \
  --dbname "$POSTGRES_DB" \
  --set=app_user="$APP_DB_USER" \
  --set=app_password="$APP_DB_PASSWORD" \
  --set=app_db="$APP_DB_NAME" <<'SQL'

CREATE ROLE :"app_user"
    LOGIN
    PASSWORD :'app_password'
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE;

CREATE DATABASE :"app_db"
    OWNER :"app_user";

SQL