# Troubleshooting — Lab 8 (Decision Trees)

## 1) Missing packages
**Symptom:** `ModuleNotFoundError: No module named 'sklearn'` (or numpy).  
**Fix (your preferred method):**
```bash
pip3 install --break-system-packages scikit-learn numpy matplotlib
```

---

## 2) Accuracy not exactly 100%
**Reason:** Different `random_state` or scikit-learn versions may produce a slightly different split/tree; 100% is common on Iris but not guaranteed.  
**Fix:** Keep `random_state=42` in both `train_test_split` and `DecisionTreeClassifier` for reproducibility.

---

## 3) Reproducibility check
Run twice and confirm the same accuracy is printed. If it changes, ensure both places use `random_state=42`.