#!/bin/bash

while ! python manage.py migrate; do
    echo "Migration failed, retrying..."
    sleep 1
done

python manage.py createsuperuser --no-input
python manage.py collectstatic --no-input
gunicorn conf.wsgi:application --bind 0.0.0.0:8000 --workers 3