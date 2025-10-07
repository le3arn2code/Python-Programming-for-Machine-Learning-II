#!/usr/bin/env bash
set -euo pipefail

# Lab 9: SVM (nano-friendly)

# 0) Prereqs (your preferred method: pip with --break-system-packages)
pip3 install --break-system-packages scikit-learn numpy || true

# 1) Workdir
cd ~
mkdir -p lab09 && cd lab09

# 2) Create the script if missing
if [ ! -f svm_classifier.py ]; then
  nano svm_classifier.py
fi

# 3) Run
python3 svm_classifier.py