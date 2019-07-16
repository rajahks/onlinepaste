#!/bin/bash

# Collect static files
echo "Collect static files"
python Clipstore/manage.py collectstatic --noinput

# Make database migrations
echo "Making database migrations"
python Clipstore/manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python Clipstore/manage.py migrate

# Start server
echo "Starting server"
python Clipstore/manage.py runserver 0.0.0.0:8000
