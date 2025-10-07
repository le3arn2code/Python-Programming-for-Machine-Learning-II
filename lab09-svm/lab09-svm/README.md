# Lab 9: Support Vector Machines (SVM)

## Lab Objective
You will:
1) Implement an SVM classifier using Scikit-Learn  
2) Train on a dataset (Iris)  
3) Tune hyperparameters with GridSearchCV

---

## Prerequisites (fresh VM)
Install with your preferred method (**no apt upgrade**, pip with break-system packages):
```bash
pip3 install --break-system-packages scikit-learn numpy
```

---

## Step-by-Step (nano friendly)

### Step 1 — Create the script
```bash
cd ~
mkdir -p lab09 && cd lab09
nano svm_classifier.py
```
Paste the script from this repo (below), then save (CTRL+O) and exit (CTRL+X).

### Step 2 — Run the script
```bash
python3 svm_classifier.py
```

### Step 3 — Verify output
You should see:
- Accuracy from a **linear kernel** SVM  
- Grid search progress (5-fold CV)  
- Best parameters and test accuracy after tuning

A console output capture is saved to `screenshots/run_output.txt` for reference.

---

## Files
- `svm_classifier.py` — main script (Iris → split → SVC → accuracy → GridSearchCV)  
- `README.md` — this file  
- `commands.sh` — nano-friendly commands to execute the lab  
- `troubleshooting.md` — issues we hit and how we fixed them  
- `interview_qna.md` — 10 interview Q&A (with answers)  
- `layman_explanation.md` — plain-English explanation  
- `screenshots/run_output.txt` — captured terminal output from a successful run

---

## Conclusion
You trained an SVM classifier and tuned hyperparameters with GridSearchCV—an essential workflow for strong baseline models.