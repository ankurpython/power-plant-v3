#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py add_data

gunicorn power_plants.wsgi:application --bind 0.0.0.0:8000

