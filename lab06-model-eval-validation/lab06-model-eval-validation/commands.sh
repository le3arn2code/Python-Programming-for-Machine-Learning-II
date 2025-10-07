#!/usr/bin/env bash
set -euo pipefail

# Lab 6: Model Evaluation and Validation (nano-friendly)

# 0) Prereqs (your preferred method: pip with --break-system-packages)
pip3 install --break-system-packages numpy scikit-learn || true

# 1) Workdir
cd ~
mkdir -p lab06 && cd lab06

# 2) Create the script if missing
if [ ! -f model_evaluation.py ]; then
  nano model_evaluation.py
fi

# 3) Run
python3 model_evaluation.py