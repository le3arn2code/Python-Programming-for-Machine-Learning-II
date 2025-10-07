# Troubleshooting — Lab 7 (Intro to Scikit-Learn)

## 1) fetch_california_housing fails to download
**Symptom:** Network error or timeout when calling `fetch_california_housing`.  
**Cause:** First-time download requires internet. Some VMs block outbound traffic.  
**Fix used in our run:** The script automatically **falls back** to a synthetic regression dataset via `make_regression` to complete the lab steps (load → train → evaluate). On an internet-enabled VM, you'll get the real California dataset automatically.

---

## 2) Missing packages
**Symptom:** `ModuleNotFoundError: No module named 'sklearn'` (or `numpy`, `pandas`).  
**Fix (your preferred method):**
```bash
pip3 install --break-system-packages scikit-learn numpy matplotlib pandas
```

---

## 3) Memory constraints when printing the full frame
**Tip:** Only print `df.head()` as the lab specifies to avoid large console dumps.

---

## Final commands used successfully
```bash
python3 scikit_learn_intro.py
```