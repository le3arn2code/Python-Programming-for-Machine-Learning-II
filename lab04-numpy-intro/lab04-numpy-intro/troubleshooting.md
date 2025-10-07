# Troubleshooting — Lab 4 (NumPy)

## 1) Module import error
**Symptom:** `ModuleNotFoundError: No module named 'numpy'`  
**Fix (your preferred method):**
```bash
pip3 install --break-system-packages numpy
```

---

## 2) Python vs pip mismatch
**Symptom:** Installed numpy but `python3` can't import it.  
**Fix:** Ensure pip installs for Python 3:
```bash
python3 -m pip install --break-system-packages numpy
python3 -c "import sys, numpy; print(sys.version, numpy.__version__)"
```

---

## 3) Shape mismatch during arithmetic
**Symptom:** `ValueError: operands could not be broadcast together`  
**Cause:** Arrays must be the same shape (or broadcastable).  
**Fix:** Check shapes with `.shape` and align dimensions:
```python
# Example: ensure both arrays are length 3
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
```

---

## Final commands used successfully
```bash
python3 numpy_intro.py
```