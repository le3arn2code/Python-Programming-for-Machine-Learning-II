# Lab 5: Implementing Linear Regression (NumPy)

## Lab Objective
You will:
1) Implement linear regression using NumPy (Normal Equation)  
2) Train on a simple synthetic dataset  
3) Evaluate with Mean Squared Error (MSE)

---

## Prerequisites (fresh VM)
Install with your preferred method (**no apt upgrade**, pip with break-system packages):
```bash
pip3 install --break-system-packages numpy
```

---

## Step-by-Step (nano friendly)

### Step 1 — Create the script
```bash
cd ~
mkdir -p lab05 && cd lab05
nano linear_regression.py
```
Paste the script from this repo (below), then save (CTRL+O) and exit (CTRL+X).

### Step 2 — Run training and print parameters
```bash
python3 linear_regression.py
```

### Step 3 — Verify output
You should see two numbers for **theta** (intercept, slope) and a **Mean Squared Error (MSE)**.

A console output capture is saved to `screenshots/run_output.txt` for reference.

---

## Files
- `linear_regression.py` — main script (implements normal equation + MSE)  
- `README.md` — this file  
- `commands.sh` — nano-friendly commands to execute the lab  
- `troubleshooting.md` — issues we hit and how we fixed them  
- `interview_qna.md` — 10 interview Q&A (with answers)  
- `layman_explanation.md` — plain-English explanation  
- `screenshots/run_output.txt` — captured terminal output from a successful run

---

## Conclusion
You computed linear regression parameters with the Normal Equation and measured fit quality via MSE—a foundation for supervised learning.