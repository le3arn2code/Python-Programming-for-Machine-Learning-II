# Lab 6: Model Evaluation and Validation

## Lab Objective
You will:
1) Split data into training and validation sets  
2) Implement 5-fold cross-validation  
3) Evaluate performance with Mean Squared Error (MSE)

---

## Prerequisites (fresh VM)
Install with your preferred method (**no apt upgrade**, pip with break-system packages):
```bash
pip3 install --break-system-packages numpy scikit-learn
```

---

## Step-by-Step (nano friendly)

### Step 1 — Create the script
```bash
cd ~
mkdir -p lab06 && cd lab06
nano model_evaluation.py
```
Paste the script from this repo (below), then save (CTRL+O) and exit (CTRL+X).

### Step 2 — Run the script
```bash
python3 model_evaluation.py
```

### Step 3 — Verify output
You should see:
- Train/validation sizes (80/20)  
- 5-fold cross-validation MSE for each fold and the average  
- Validation set MSE from the 80/20 split

A console output capture is saved to `screenshots/run_output.txt` for reference.

---

## Files
- `model_evaluation.py` — main script (split, cross-validate, and evaluate)  
- `README.md` — this file  
- `commands.sh` — nano-friendly commands to execute the lab  
- `troubleshooting.md` — issues we hit and how we fixed them  
- `interview_qna.md` — 10 interview Q&A (with answers)  
- `layman_explanation.md` — plain-English explanation  
- `screenshots/run_output.txt` — captured terminal output from a successful run

---

## Conclusion
You practiced proper evaluation via a validation split and cross-validation and used MSE to quantify error—key skills for model selection and avoiding overfitting.