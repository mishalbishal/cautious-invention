#!/bin/bash

set -e

python manage.py makemigrations 2>&1
python manage.py migrate 2>&1

exec "$@"
