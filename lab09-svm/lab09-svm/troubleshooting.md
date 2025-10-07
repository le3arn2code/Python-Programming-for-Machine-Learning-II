# Troubleshooting — Lab 9 (SVM)

## 1) Missing packages
**Symptom:** `ModuleNotFoundError: No module named 'sklearn'` (or numpy).  
**Fix (your preferred method):**
```bash
pip3 install --break-system-packages scikit-learn numpy
```

---

## 2) Class imbalance warnings or inconsistent splits
**Fix:** Use `stratify=y` in `train_test_split` to preserve class distribution (included in the script).

---

## 3) Grid search takes too long
**Tip:** Reduce the parameter grid (e.g., fewer `C` values) or set `cv=3` during testing.

---

## Final commands used successfully
```bash
python3 svm_classifier.py
```