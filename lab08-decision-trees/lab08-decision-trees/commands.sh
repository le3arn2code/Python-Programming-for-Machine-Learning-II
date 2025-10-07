#!/usr/bin/env bash
set -euo pipefail

# Lab 8: Implementing Decision Trees (nano-friendly)

# 0) Prereqs (your preferred method: pip with --break-system-packages)
pip3 install --break-system-packages scikit-learn numpy matplotlib || true

# 1) Workdir
cd ~
mkdir -p lab08 && cd lab08

# 2) Create the script if missing
if [ ! -f decision_tree_classifier.py ]; then
  nano decision_tree_classifier.py
fi

# 3) Run
python3 decision_tree_classifier.py