#!/usr/bin/env bash
set -euo pipefail

# Lab 3: Data Visualization with Matplotlib (nano-friendly)

# 0) Prereqs (your preferred method: pip with --break-system-packages)
pip3 install --break-system-packages matplotlib numpy || true

# 1) Workdir
cd ~
mkdir -p lab03 && cd lab03

# 2) Create the script if missing
if [ ! -f data_visualization.py ]; then
  nano data_visualization.py
fi

# 3) Run
python3 data_visualization.py

# 4) List outputs
ls -lh screenshots/
