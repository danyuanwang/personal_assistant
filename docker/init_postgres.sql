CREATE DATABASE event_broker_db;
CREATE DATABASE tracker_store_db;
CREATE DATABASE personal_assistant_db;
CREATE ROLE personal_assistant_db_admin WITH ENCRYPTED PASSWORD 'covidhub@io';
ALTER ROLE personal_assistant_db_admin WITH LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE REPLICATION;
GRANT ALL PRIVILEGES ON DATABASE event_broker_db TO personal_assistant_db_admin;
GRANT ALL PRIVILEGES ON DATABASE tracker_store_db TO personal_assistant_db_admin;
GRANT ALL PRIVILEGES ON DATABASE personal_assistant_db TO personal_assistant_db_admin;
ALTER ROLE personal_assistant_db_admin SET client_encoding TO 'utf8';
ALTER ROLE personal_assistant_db_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE personal_assistant_db_admin SET timezone TO 'UTC';

