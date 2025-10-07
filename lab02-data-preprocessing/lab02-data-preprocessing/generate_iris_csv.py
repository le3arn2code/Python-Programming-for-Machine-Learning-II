# generate_iris_csv.py — creates iris.csv locally with no header (classic format)
from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
df = pd.DataFrame(iris.data, columns=["sepal_length","sepal_width","petal_length","petal_width"])
df["class"] = pd.Categorical.from_codes(iris.target, iris.target_names)
df.to_csv("iris.csv", index=False, header=False)
print("iris.csv written in current folder.")