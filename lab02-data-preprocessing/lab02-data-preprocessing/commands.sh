#!/usr/bin/env bash
set -euo pipefail

# Lab 2: Data Preprocessing with Pandas (nano-friendly)

# 0) Prereqs (your preferred method: pip with --break-system-packages)
pip3 install --break-system-packages pandas scikit-learn || true

# 1) Workdir
cd ~
mkdir -p lab02 && cd lab02

# 2) (Optional) Generate iris.csv if missing
if [ ! -f iris.csv ]; then
  cat > generate_iris_csv.py <<'PY'
from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
df = pd.DataFrame(iris.data, columns=["sepal_length","sepal_width","petal_length","petal_width"])
df["class"] = pd.Categorical.from_codes(iris.target, iris.target_names)
df.to_csv("iris.csv", index=False, header=False)
print("iris.csv written.")
PY
  python3 generate_iris_csv.py
fi

# 3) Create the lab script if missing
if [ ! -f data_preprocessing.py ]; then
  nano data_preprocessing.py
fi

# 4) Run
python3 data_preprocessing.py