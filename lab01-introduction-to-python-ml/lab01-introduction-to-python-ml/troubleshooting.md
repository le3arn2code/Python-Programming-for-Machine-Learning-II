# Troubleshooting

## PEP 668 / Externally Managed Environment
Ubuntu may block system‑wide pip installs. Either:
- Use a **virtual environment** (recommended), or
- Use `python3 -m pip install --user ...`, or
- Use apt packages: `sudo apt install -y python3-numpy python3-pandas python3-matplotlib`

Avoid `--break-system-packages` unless you know the tradeoffs.

## `ModuleNotFoundError`
Install the missing package in your venv or with `--user` scope.

## Multiple Python Versions
Always run with `python3` and `python3 -m pip` to be explicit.

## Here‑doc syntax errors
Use this exact pattern to test imports:
```bash
python3 - <<'PY'
import numpy, pandas, matplotlib
print("OK: NumPy", numpy.__version__, "| Pandas", pandas.__version__, "| Matplotlib", matplotlib.__version__)
PY
```

## Permission problems
Keep installs in venv (`python3 -m venv .venv`) or user space (`--user`).