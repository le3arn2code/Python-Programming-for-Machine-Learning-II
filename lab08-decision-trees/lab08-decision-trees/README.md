# Lab 8: Implementing Decision Trees

## Lab Objective
You will:
1) Implement a Decision Tree Classifier with Scikit-Learn  
2) Train on a classification dataset (Iris)  
3) Evaluate with **accuracy**

---

## Prerequisites (fresh VM)
Install with your preferred method (**no apt upgrade**, pip with break-system packages):
```bash
pip3 install --break-system-packages scikit-learn numpy matplotlib
```

---

## Step-by-Step (nano friendly)

### Step 1 — Create the script
```bash
cd ~
mkdir -p lab08 && cd lab08
nano decision_tree_classifier.py
```
Paste the script from this repo (below), then save (CTRL+O) and exit (CTRL+X).

### Step 2 — Run the script
```bash
python3 decision_tree_classifier.py
```

### Step 3 — Verify output
You should see the model’s accuracy printed, typically close to **100%** on the Iris test set.

A console output capture is saved to `screenshots/run_output.txt` for reference.

---

## Files
- `decision_tree_classifier.py` — main script (Iris → split → DecisionTree → accuracy)  
- `README.md` — this file  
- `commands.sh` — nano-friendly commands to execute the lab  
- `troubleshooting.md` — issues we hit and how we fixed them  
- `interview_qna.md` — 10 interview Q&A (with answers)  
- `layman_explanation.md` — plain-English explanation  
- `screenshots/run_output.txt` — captured terminal output from a successful run

---

## Conclusion
You trained and evaluated a Decision Tree Classifier using the Iris dataset and measured accuracy—foundation for classification workflows.