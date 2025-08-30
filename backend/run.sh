#!/bin/bash
# 🚀 Run FastAPI backend in production with Gunicorn + Uvicorn workers

APP_MODULE=app.main:app
HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}
WORKERS=${WORKERS:-2}

echo "🔄 Starting backend: $APP_MODULE on $HOST:$PORT with $WORKERS workers"
exec gunicorn -k uvicorn.workers.UvicornWorker "$APP_MODULE" \
    --bind "$HOST:$PORT" \
    --workers "$WORKERS" \
    --timeout 120 \
    --log-level info
