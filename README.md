# Python Programming for Machine Learning — II

A hands‑on, lab‑driven series that takes you from **data to models** with a clean, repeatable workflow. Each lab is production‑style: clear objectives, step‑by‑step tasks, nano‑friendly commands, troubleshooting notes, interview Q&A, and real screenshots. All plotting is headless‑safe and every script uses `python3` to match server/CI environments.

---

## 🚀 What you’ll get
- **10 polished labs (so far)** covering the essential ML pipeline — from NumPy and Pandas to Scikit‑Learn, SVMs, trees, and a first Keras neural net.
- **GitHub‑ready structure** in every lab: `README.md`, `commands.sh`, `troubleshooting.md`, `interview_qna.md`, code file(s), and `screenshots/`.
- **Reproducible runs**: deterministic seeds where relevant, `plt.close()` after plots, and terminal‑verified outputs.
- **Learning that transfers**: consistent patterns that scale to larger projects and real interviews.

---

## 📁 Repository structure
```
.
├── lab01-introduction-to-python-ml/
├── lab02-data-preprocessing/
├── lab03-data-visualization/
├── lab04-numpy-intro/
├── lab05-linear-regression/
├── lab06-model-eval-validation/
├── lab07-scikit-learn-intro/
├── lab08-decision-trees/
├── lab09-svm/
└── lab10-simple-neural-network/
```
Each lab folder contains:
```
README.md
commands.sh
troubleshooting.md
interview_qna.md
<one-or-more>.py
screenshots/
```

> **Note:** All labs prefer `python3` and headless plotting (`matplotlib` with `plt.close()` after saving).

---

## 🧭 Lab index (1–10)
| # | Lab | Folder | Key skills & outcomes |
|---:|-----|--------|-----------------------|
| 01 | Introduction to Python for ML | [`lab01-introduction-to-python-ml/`](lab01-introduction-to-python-ml/) | Python basics for ML, environment sanity checks, running scripts reliably with `python3`. |
| 02 | Data Preprocessing with Pandas | [`lab02-data-preprocessing/`](lab02-data-preprocessing/) | Import/clean data, handle nulls/outliers, encode/scale features, tidy DataFrame workflows. |
| 03 | Data Visualization with Matplotlib | [`lab03-data-visualization/`](lab03-data-visualization/) | Static plots (line, bar, hist, scatter), saving figures headlessly, labeling for insight. |
| 04 | Introduction to NumPy for ML | [`lab04-numpy-intro/`](lab04-numpy-intro/) | Arrays, broadcasting, vectorization, random seeds; performance‑aware numerical ops. |
| 05 | Linear Regression (NumPy) | [`lab05-linear-regression/`](lab05-linear-regression/) | From‑scratch linear regression with gradient intuition and evaluation basics. |
| 06 | Model Evaluation & Validation | [`lab06-model-eval-validation/`](lab06-model-eval-validation/) | Train/test split, K‑Fold, metrics (accuracy/precision/recall/F1), leakage avoidance. |
| 07 | Scikit‑Learn Introduction | [`lab07-scikit-learn-intro/`](lab07-scikit-learn-intro/) | Pipelines, estimators, transformers, consistent fit/transform/predict patterns. |
| 08 | Decision Trees (Iris) | [`lab08-decision-trees/`](lab08-decision-trees/) | Train/visualize trees, interpret splits, control depth/overfit, export figures. |
| 09 | SVM + GridSearchCV | [`lab09-svm/`](lab09-svm/) | Linear/RBF kernels, hyper‑parameters, grid search, cross‑validated model selection. |
| 10 | Simple Neural Network (Keras, Iris) | [`lab10-simple-neural-network/`](lab10-simple-neural-network/) | Dense network in TF/Keras, train/val curves, early stopping, saved metrics & plots. |

---

## 🔧 Quick start
1. **Clone** the repo
   ```bash
   git clone https://github.com/le3arn2code/Python-Programming-for-Machine-Learning-II.git
   cd Python-Programming-for-Machine-Learning-II
   ```
2. **(Optional) Create a venv**
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   ```
3. **Install common dependencies**
   ```bash
   python3 -m pip install --upgrade pip
   python3 -m pip install numpy pandas matplotlib scikit-learn tensorflow
   ```
4. **Run any lab script**
   ```bash
   cd lab03-data-visualization
   python3 lab03_data_visualization.py
   ls -l screenshots/
   ```

> If a lab needs extras (e.g., `graphviz`), see that lab’s `README.md` and `troubleshooting.md` for exact install notes and fixes.

---

## 🧪 Reproducibility & conventions
- Use `python3` everywhere (works on Ubuntu, macOS, WSL).
- Save plots to `screenshots/*.png` and call `plt.close()` after each figure.
- Use fixed seeds when relevant for repeatable results.
- Keep terminal outputs clean; verify key steps with `ls`, `head`, `python3 --version`, etc.

---

## 🤝 Contributing
Pull requests welcome! Match the existing lab format:
- Clear **Objectives → Tasks → What you learned** in `README.md`
- `commands.sh` with nano‑friendly steps
- `troubleshooting.md` with real errors and fixes
- `interview_qna.md` with 10 concise, practical Q&A
- Screenshots saved under `screenshots/`

---

## 🗺️ Roadmap
- 📚 Labs 11–20: Feature engineering, regularization, logistic regression, k‑NN, ensembles
- 🧠 Labs 21–30: Deeper Keras, callbacks, model saving/serving, simple CNNs/RNNs
- 📈 Labs 31–40: Model monitoring, drift checks, explainability (SHAP), data versioning
- 🚀 Labs 41–50: Mini end‑to‑end projects with packaging and CI hooks

---

## 📫 Contact
Questions or suggestions? Open an issue or start a discussion in this repo. Happy learning and shipping!


