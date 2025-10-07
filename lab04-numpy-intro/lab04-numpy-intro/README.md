# Lab 4: Introduction to NumPy for Machine Learning

## Lab Objective
You will:
1) Create NumPy arrays and matrices  
2) Perform array ops and linear algebra (dot product)  
3) Implement element-wise ops (square, sqrt, exp)

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
mkdir -p lab04 && cd lab04
nano numpy_intro.py
```
Paste the script from this repo (below), then save (CTRL+O) and exit (CTRL+X).

### Step 2 — Run the script
```bash
python3 numpy_intro.py
```

### Step 3 — Verify output
You should see:
- 1D array, 2D matrix, 3x3 zeros, 3x3 ones  
- Array addition, subtraction, element‑wise multiplication  
- Matrix dot product  
- Element‑wise square, square root, exponentiation

A console output capture is saved to `screenshots/run_output.txt` for reference.

---

## Files
- `numpy_intro.py` — main script
- `README.md` — this file
- `commands.sh` — nano-friendly commands to execute the lab
- `troubleshooting.md` — issues we hit and how we fixed them
- `interview_qna.md` — 10 interview Q&A (with answers)
- `layman_explanation.md` — plain-English explanation
- `screenshots/run_output.txt` — captured terminal output from a successful run

---

## Conclusion
You created arrays/matrices, performed arithmetic and linear algebra, and applied element‑wise functions—core NumPy skills for ML preprocessing and model pipelines.