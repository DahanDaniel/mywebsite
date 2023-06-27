#!/bin/bash

# Backup the user model
python manage.py dumpdata auth.User --output=user_fixture.json

# Clear all data from your application
python manage.py flush --noinput

# Load the user data back into the database
python manage.py loaddata user_fixture.json
