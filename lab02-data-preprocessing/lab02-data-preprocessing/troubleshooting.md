# Troubleshooting — Lab 2

## 1) FutureWarning when using Series.fillna(..., inplace=True)
**Observed (from our run):**
```
For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)'
or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
```
**Cause:** Using `inplace=True` on a **Series** (e.g., `df['petal_width'].fillna(..., inplace=True)`) is being phased out by pandas and may not modify the original frame in future versions.

**Fix we applied in final code:** Use **DataFrame-level** fill to avoid the warning:
```python
df.fillna({
    "sepal_length": df["sepal_length"].mean(),
    "petal_width": df["petal_width"].mean()
}, inplace=True)
```
This updates the original frame in-place without warnings.

---

## 2) Module import errors (pandas / scikit-learn)
**Symptom:** `ModuleNotFoundError: No module named 'pandas'` (or sklearn).  
**Fix (your preferred method):**
```bash
pip3 install --break-system-packages pandas scikit-learn
```

---

## 3) File not found: iris.csv
**Symptom:** `FileNotFoundError: 'iris.csv'`  
**Fix:** Generate it locally first:
```bash
python3 generate_iris_csv.py
```
Ensure `data_preprocessing.py` and `iris.csv` are in the same directory.

---

## Final commands we used successfully
```bash
cd ~
mkdir -p lab02 && cd lab02
python3 generate_iris_csv.py
python3 data_preprocessing.py
```