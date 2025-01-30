#!/bin/bash

command -v screen >/dev/null 2>&1 || { echo >&2 "screen command not found. Please install screen first."; exit 1; }

# 啟動 Gunicorn
screen -S gunicorn_server -dm bash -c '
    source venv/bin/activate
    gunicorn --bind 0.0.0.0:443 --certfile cert.pem --keyfile key.pem server.wsgi
'

# 啟動 Celery Worker
screen -S celery_worker -dm bash -c '
    source venv/bin/activate
    celery -A server worker --loglevel=info
'

# 啟動 Celery Beat
screen -S celery_beat -dm bash -c '
    source venv/bin/activate
    celery -A server beat --loglevel=info
'