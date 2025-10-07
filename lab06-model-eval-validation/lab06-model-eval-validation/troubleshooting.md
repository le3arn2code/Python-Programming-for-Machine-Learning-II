# Troubleshooting — Lab 6 (Model Evaluation & Validation)

## 1) Module import errors
**Symptom:** `ModuleNotFoundError: No module named 'numpy'` or `'sklearn'`.  
**Fix (your preferred method):**
```bash
pip3 install --break-system-packages numpy scikit-learn
```

---

## 2) Shape mismatch issues
**Symptom:** `ValueError: Found input variables with inconsistent numbers of samples`.  
**Cause:** X and y must have the same first dimension.  
**Fix:** Ensure they are created together (as in the lab) or inspect `X.shape, y.shape`.

---

## 3) Reproducibility differences vs. instructions
**Symptom:** Your MSE values differ slightly.  
**Cause:** Randomness in data and cross-validation shuffling.  
**Fix:** We set `np.random.seed(42)` and `KFold(..., random_state=42)` to match results across runs.

---

## Final commands used successfully
```bash
python3 model_evaluation.py
```