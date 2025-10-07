#!/usr/bin/env bash
set -euo pipefail

# Lab 5: Implementing Linear Regression (NumPy)

# 0) Prereqs (your preferred method: pip with --break-system-packages)
pip3 install --break-system-packages numpy || true

# 1) Workdir
cd ~
mkdir -p lab05 && cd lab05

# 2) Create the script if missing
if [ ! -f linear_regression.py ]; then
  nano linear_regression.py
fi

# 3) Run
python3 linear_regression.py