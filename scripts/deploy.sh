#!/bin/bash
set -e

APP_DIR="/opt/devops-app"

echo "===== DevOps Deployment ====="

# Step 1: Update source code
echo "[1] Updating source..."
cd "$APP_DIR"
git pull --ff-only origin main

# Step 2: Install dependencies
echo "[2] Installing dependencies..."
source "$APP_DIR/venv/bin/activate"
pip install -r "$APP_DIR/requirements.txt"

# Step 3: Restart application
echo "[3] Restarting application..."
sudo systemctl restart devops-app

# Step 4: Check service
echo "[4] Checking service..."
sudo systemctl is-active --quiet devops-app

# Step 5: Health check
echo "[5] Health check..."
if curl --fail http://localhost/health; then
    echo "Application is healthy."
    echo "Deployment successful."
else
    echo "Health check failed."
    exit 1
fi
