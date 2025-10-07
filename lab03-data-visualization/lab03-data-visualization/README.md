# Lab 3: Data Visualization with Matplotlib

## Lab Objective
In this lab, you will use **Matplotlib** for basic data visualization. You will:
1) Plot histograms and scatter plots  
2) Create line charts and bar charts  
3) Customize plot aesthetics (titles, labels, legends)

---

## Prerequisites (fresh VM)
Install with your preferred method (**no apt upgrade**, pip with break-system packages):
```bash
pip3 install --break-system-packages matplotlib numpy
```
> Headless servers need a non-interactive backend. This lab sets `matplotlib.use('Agg')` to save plots as PNGs instead of showing windows.

---

## Step-by-Step (nano friendly)

### Step 1 — Create the script
```bash
cd ~
mkdir -p lab03 && cd lab03
nano data_visualization.py
```
Paste the script from this repo (below), then save (CTRL+O) and exit (CTRL+X).

### Step 2 — Run the script
```bash
python3 data_visualization.py
```

### Step 3 — Verify generated plots
```bash
ls -lh screenshots/
```
You should see:
- `histogram_random.png`
- `scatter_random.png`
- `line_sin.png`
- `bar_categories.png`

---

## Files
- `data_visualization.py` — main script (saves all plots into `./screenshots/`)
- `README.md` — this file
- `commands.sh` — nano-friendly commands to execute the lab
- `troubleshooting.md` — issues we hit and how we fixed them
- `interview_qna.md` — 10 interview Q&A (with answers)
- `layman_explanation.md` — plain-English explanation
- `screenshots/` — saved charts as PNG images

---

## Conclusion
You created histogram, scatter, line, and bar charts and customized them with titles, labels, legends, and grids. These foundations help you explore data shapes, relationships, and trends before deeper analysis.


Screenshots included: bar_categories.png, histogram_random.png, line_sin.png, scatter_random.png
