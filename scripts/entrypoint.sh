#!/bin/bash

touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &

exec pipenv run gunicorn \
    --bind :8000 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log \
    backend.wsgi:application --pythonpath backend &

exec service nginx start