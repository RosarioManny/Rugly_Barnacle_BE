CREATE DATABASE $DB_NAME;

CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';

GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;


-- RUN SCRIPT TO CREATEA DB ::
-- envsubst < create-database.sql | psql -U postgres
