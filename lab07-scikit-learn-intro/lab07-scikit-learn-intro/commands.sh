#!/usr/bin/env bash
set -euo pipefail

# Lab 7: Introduction to Scikit-Learn (nano-friendly)

# 0) Prereqs (your preferred method: pip with --break-system-packages)
pip3 install --break-system-packages scikit-learn numpy matplotlib pandas || true

# 1) Workdir
cd ~
mkdir -p lab07 && cd lab07

# 2) Create the script if missing
if [ ! -f scikit_learn_intro.py ]; then
  nano scikit_learn_intro.py
fi

# 3) Run
python3 scikit_learn_intro.py