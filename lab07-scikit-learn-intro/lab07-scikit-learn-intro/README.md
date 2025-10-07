# Lab 7: Introduction to Scikit-Learn

## Lab Objective
You will:
1) Load a dataset using Scikit-Learn  
2) Implement Linear Regression using Scikit-Learn  
3) Evaluate with MSE and R²

---

## Prerequisites (fresh VM)
Install with your preferred method (**no apt upgrade**, pip with break-system packages):
```bash
pip3 install --break-system-packages scikit-learn numpy matplotlib pandas
```

---

## Step-by-Step (nano friendly)

### Step 1 — Create the script
```bash
cd ~
mkdir -p lab07 && cd lab07
nano scikit_learn_intro.py
```
Paste the script from this repo (below), then save (CTRL+O) and exit (CTRL+X).

### Step 2 — Run the script
```bash
python3 scikit_learn_intro.py
```

### Step 3 — Verify output
You should see:
- First few rows of the dataset (California housing)  
- Model coefficients and intercept  
- Mean Squared Error (MSE) and R-squared (R²)

A console output capture is saved to `screenshots/run_output.txt` for reference.

---

## Files
- `scikit_learn_intro.py` — main script (load data → split → train LinearRegression → evaluate)  
- `README.md` — this file  
- `commands.sh` — nano-friendly commands to execute the lab  
- `troubleshooting.md` — issues we hit and how we fixed them  
- `interview_qna.md` — 10 interview Q&A (with answers)  
- `layman_explanation.md` — plain-English explanation  
- `screenshots/run_output.txt` — captured terminal output from a successful run

---

## Conclusion
You loaded a dataset with Scikit-Learn, trained a Linear Regression model, and evaluated it using MSE and R²—core workflow for classical ML.