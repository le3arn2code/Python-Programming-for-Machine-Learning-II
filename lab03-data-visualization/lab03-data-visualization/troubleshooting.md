# Troubleshooting — Lab 3 (Matplotlib)

## 1) No display / GUI errors (e.g., "cannot connect to X server")
**Cause:** Headless VM without a display server.  
**Fix (included in the script):** We force a non-interactive backend:
```python
import matplotlib
matplotlib.use('Agg')
```
This saves PNGs to `screenshots/` instead of opening windows.

---

## 2) Missing packages
**Symptom:** `ModuleNotFoundError: No module named 'matplotlib'` (or `numpy`).  
**Fix (your preferred method):**
```bash
pip3 install --break-system-packages matplotlib numpy
```

---

## 3) Permission errors writing screenshots
**Symptom:** `PermissionError: [Errno 13] Permission denied: 'screenshots/...'`  
**Fix:** Run from your home directory and ensure the folder exists:
```bash
mkdir -p screenshots
python3 data_visualization.py
```

---

## Final commands used successfully
```bash
python3 data_visualization.py
ls -lh screenshots/
```
