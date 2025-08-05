CREATE DATABASE $DB_NAME;

CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';

-- Connect to the database before granting schema privileges
\c $DB_NAME

-- Crucial grants:
GRANT CREATE ON SCHEMA public TO $DB_USER;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO $DB_USER;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO $DB_USER;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO $DB_USER;

-- For future objects:
ALTER DEFAULT PRIVILEGES IN SCHEMA public 
GRANT ALL PRIVILEGES ON TABLES TO $DB_USER;

ALTER DEFAULT PRIVILEGES IN SCHEMA public 
GRANT ALL PRIVILEGES ON SEQUENCES TO $DB_USER;

"""
RUN SCRIPT TO CREATEA DB ::
envsubst < create-database.sql | psql -U postgres

>> Why this script? << 

SQL, doesn't automatically detect variables.
So this uses envsubst to look at a file (.env) and replace the variables with their value.
"""