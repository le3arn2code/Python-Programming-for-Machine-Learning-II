#!/usr/bin/env bash
set -euo pipefail

# Lab 10: Simple Neural Network (nano-friendly)

# 0) Prereqs (TensorFlow CPU + libs)
pip3 install --break-system-packages tensorflow numpy matplotlib scikit-learn || true

# 1) Workdir
cd ~
mkdir -p lab10 && cd lab10

# 2) Create the script if missing
if [ ! -f neural_network.py ]; then
  nano neural_network.py
fi

# 3) Run
python3 neural_network.py