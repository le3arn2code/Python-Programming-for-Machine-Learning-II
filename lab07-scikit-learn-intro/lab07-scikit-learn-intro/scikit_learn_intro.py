from sklearn.datasets import fetch_california_housing, make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

def load_dataset():
    # Primary: California housing (as_frame=True returns a DataFrame with MedHouseVal target)
    try:
        data = fetch_california_housing(as_frame=True)
        df = data.frame.copy()
        print("Loaded California housing dataset.")
        return df
    except Exception:
        print("Could not fetch California housing dataset (likely no internet). Using synthetic data instead.")
        X, y = make_regression(n_samples=20640, n_features=8, noise=15.0, random_state=42)
        cols = ["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude"]
        df = pd.DataFrame(X, columns=cols)
        df["target"] = (y - y.min()) / (y.max() - y.min()) * 5.0
        return df

def main():
    # 1) Load dataset
    df = load_dataset()

    # Display first few rows
    print("\n=== Head ===")
    print(df.head())

    # 2) Linear Regression with scikit-learn (NO LEAKAGE)
    if "MedHouseVal" in df.columns:
        y = df["MedHouseVal"]
        X = df.drop(columns=["MedHouseVal"])
    else:
        y = df["target"]
        X = df.drop(columns=["target"])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\nModel Coefficients:", model.coef_)
    print("Model Intercept:", model.intercept_)

    # 3) Evaluate: MSE and R^2
    mse = mean_squared_error(y_test, y_pred)
    r2 = model.score(X_test, y_test)
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"R-squared score: {r2}")

if __name__ == "__main__":
    main()
