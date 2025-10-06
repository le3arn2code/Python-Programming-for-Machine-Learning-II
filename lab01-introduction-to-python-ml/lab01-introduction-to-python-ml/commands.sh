#!/usr/bin/env bash
set -euo pipefail

# (Optional) Create and use a virtual environment (recommended)
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python3 not found"; exit 1
fi

python3 -m venv .venv || true
source .venv/bin/activate || true

# Upgrade pip inside venv (safe)
python -m pip install --upgrade pip

# Install essentials
pip install numpy pandas matplotlib

# Run the script
python basic_script.py

# Stash a simple run artifact
mkdir -p screenshots
echo "Lab01 ran successfully on: $(date)" > screenshots/lab01_output.txt

# List artifacts
ls -lah screenshots/
