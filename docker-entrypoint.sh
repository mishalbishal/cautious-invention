#!/bin/bash

set -e

python manage.py makemigrations 2>&1
python manage.py migrate 2>&1
python manage.py loaddata fixtures/sites.json
python manage.py loaddata fixtures/auth.json

python manage.py runserver 0.0.0.0:8000
