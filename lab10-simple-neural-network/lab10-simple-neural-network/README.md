# Lab 10: Building a Simple Neural Network (TensorFlow/Keras)

## Lab Objective
You will:
1) Install TensorFlow (includes Keras)  
2) Build & train a small neural network (Iris)  
3) Evaluate accuracy on a test set

---

## Prerequisites (fresh VM)
Verify Python/pip and install deps:
```bash
python3 --version
pip3 --version

# Install TensorFlow (CPU) and libs
pip3 install --break-system-packages tensorflow
pip3 install --break-system-packages numpy matplotlib scikit-learn
```
> If you hit install issues on minimal Ubuntu images, see `troubleshooting.md` for fixes.

---

## Step-by-Step (nano friendly)

### Step 1 — Create the script
```bash
cd ~
mkdir -p lab10 && cd lab10
nano neural_network.py
```
Paste the script from this repo (below), save (CTRL+O) and exit (CTRL+X).

### Step 2 — Run the script
```bash
python3 neural_network.py
```
You should see training logs for 50 epochs and final test accuracy.

A console output capture is saved to `screenshots/run_output.txt` for reference.

---

## Files
- `neural_network.py` — main script (build → train → evaluate)  
- `README.md` — this file  
- `commands.sh` — nano-friendly commands to execute the lab  
- `troubleshooting.md` — issues we hit and how we fixed them  
- `interview_qna.md` — 10 interview Q&A (with answers)  
- `layman_explanation.md` — plain-English explanation  
- `screenshots/run_output.txt` — captured program output (or install error details, if any)

---

## Conclusion
You trained a simple feed‑forward network with Keras for multi‑class classification and measured accuracy.