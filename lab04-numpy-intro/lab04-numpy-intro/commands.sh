#!/usr/bin/env bash
set -euo pipefail

# Lab 4: Introduction to NumPy (nano-friendly)

# 0) Prereqs (your preferred method: pip with --break-system-packages)
pip3 install --break-system-packages numpy || true

# 1) Workdir
cd ~
mkdir -p lab04 && cd lab04

# 2) Create the script if missing
if [ ! -f numpy_intro.py ]; then
  nano numpy_intro.py
fi

# 3) Run
python3 numpy_intro.py