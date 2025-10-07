# Troubleshooting — Lab 5 (Linear Regression with NumPy)

## 1) Module import error
**Symptom:** `ModuleNotFoundError: No module named 'numpy'`  
**Fix (your preferred method):**
```bash
pip3 install --break-system-packages numpy
```

---

## 2) Shape mismatch errors
**Symptom:** `ValueError: shapes (N,2) and (M,1) not aligned`  
**Cause:** X and y must have the same number of rows; y should be 2D (N,1).  
**Fix:**
```python
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)
```

---

## 3) Singular matrix error on `np.linalg.inv`
**Symptom:** `LinAlgError: Singular matrix` when computing `(X^T X)^{-1}`.  
**Cause:** Perfect multicollinearity or duplicated rows can make `X^T X` non-invertible.  
**Resolution (if you hit this):** Use the pseudo-inverse for numerical stability:
```python
theta = np.linalg.pinv(X_b.T @ X_b) @ X_b.T @ y
```
For this lab's random data, the standard inverse works and no error occurred.

---

## Final commands used successfully
```bash
python3 linear_regression.py
```