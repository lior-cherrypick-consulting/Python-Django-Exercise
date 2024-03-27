#!/bin/bash

# This script is used as the entrypoint for Docker container. This will
# - Wait for the database to be ready
# - Create migrations for the Django app
# - Apply the migrations
# - Seed the database with data
# - Run the Django development server

# Note: Make this script executable by running: chmod +x entrypoint.sh

# Check if running tests
if [ "$RUN_TESTS" == "1" ]; then
  echo "Running tests, skipping database checks..."
  # Execute the passed command arguments (e.g., Django's test runner)
  exec "$@"
  exit 0
fi

# Wait for PostgreSQL to become available
if [ "$ENVIRONMENT" == "development" ]; then
    # Wait for PostgreSQL to become available
    until pg_isready -h db -p 5432 -U "${DB_USER}"; do
      echo "Waiting for PostgreSQL to start..."
      sleep 1
    done
fi

# Create migrations for the app
echo "Creating database migrations..."
python manage.py makemigrations

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Seed the database
echo "Seeding the database..."
python manage.py seed

# Start the main process: Django's runserver
echo "Starting Django development server..."
exec "$@"
