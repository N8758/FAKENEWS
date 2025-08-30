#!/bin/bash
# 🔧 Development script to run backend (Uvicorn) + frontend (Vite) together

FRONTEND_DIR="../frontend"
BACKEND_DIR="../backend"

echo "🚀 Starting backend (FastAPI with Uvicorn)..."
(cd "$BACKEND_DIR" && . venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000) &

echo "🌐 Starting frontend (React with Vite)..."
(cd "$FRONTEND_DIR" && npm run dev)

# Kill background processes on exit
trap "kill 0" EXIT
