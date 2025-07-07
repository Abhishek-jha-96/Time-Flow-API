#!/bin/bash

set -e

export DJANGO_SETTINGS_MODULE=time_flow_api.settings

if [ "$ENVIRONMENT" = "local" ]; then
    echo "Running local development server."
    exec python manage.py runserver "$BASE_URL"
else
    echo "Running gunicorn server."
    exec gunicorn time_flow_api.wsgi:application \
        --name time_flow_api \
        --bind "$BASE_URL" \
        --reload \
        --workers 2 \
        --log-level=debug \
        "$@"
fi
