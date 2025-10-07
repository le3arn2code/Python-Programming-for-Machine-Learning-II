# Troubleshooting — Lab 10 (TensorFlow/Keras)

## What we hit in a minimal environment
On some sandboxed/minimal machines, `tensorflow` may fail to import due to missing system libraries or lack of wheel availability.

**Symptom we captured:** ImportError when running `python3 neural_network.py` (see `screenshots/run_output.txt`).

### Fixes on a fresh Ubuntu VM
1) Prefer CPU build & ensure pip is recent:
```bash
python3 -m pip install --upgrade --break-system-packages pip setuptools wheel
pip3 install --break-system-packages tensorflow
```
2) If resources are tight, install CPU‑only variant (some distros):  
```bash
pip3 install --break-system-packages tensorflow-cpu
```
3) Make sure these system libs exist (common on server images):
```bash
sudo apt-get update && sudo apt-get install -y libstdc++6
```
4) Verify import:
```bash
python3 - << 'PY'
import tensorflow as tf
print("TF version:", tf.__version__)
PY
```

### Other common issues
- **AVX/CPU flags**: Very old CPUs may not support wheels; use a machine with a newer CPU or a prebuilt container.
- **OneHotEncoder warning**: On newer sklearn, use `OneHotEncoder(sparse_output=False)`; current code uses `sparse=False` for wide compatibility.