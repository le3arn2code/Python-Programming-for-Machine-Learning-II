import os
import numpy as np
import matplotlib
matplotlib.use('Agg')  # headless backend
import matplotlib.pyplot as plt

def ensure_outdir(path="screenshots"):
    os.makedirs(path, exist_ok=True)
    return path

def main():
    out = ensure_outdir()

    # 1) Histogram of random data
    data = np.random.randn(1000)
    plt.figure()
    plt.hist(data, bins=30)
    plt.title("Histogram of Random Data")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(out, "histogram_random.png"))
    plt.close()

    # 2) Scatter plot of random points
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.figure()
    plt.scatter(x, y)
    plt.title("Random Scatter Plot")
    plt.xlabel("X Value")
    plt.ylabel("Y Value")
    plt.tight_layout()
    plt.savefig(os.path.join(out, "scatter_random.png"))
    plt.close()

    # 3) Line chart: sin(x)
    x_line = np.linspace(0, 10, 100)
    y_line = np.sin(x_line)
    plt.figure()
    plt.plot(x_line, y_line, label="sin(x)")
    plt.title("Line Chart of sin(x)")
    plt.xlabel("X")
    plt.ylabel("sin(x)")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(out, "line_sin.png"))
    plt.close()

    # 4) Bar chart: categories
    categories = ["A", "B", "C", "D", "E"]
    values = [3, 7, 2, 5, 4]
    plt.figure()
    plt.bar(categories, values)
    plt.title("Bar Chart of Categories")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig(os.path.join(out, "bar_categories.png"))
    plt.close()

    print("Saved charts to:", out)

if __name__ == "__main__":
    main()
