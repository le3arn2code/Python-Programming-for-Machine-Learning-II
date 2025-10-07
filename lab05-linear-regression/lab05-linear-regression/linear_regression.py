import numpy as np

# 1. Implement linear regression using NumPy
def linear_regression(X, y):
    # Add a column of ones to X for the bias term (intercept)
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    # Calculate parameters using the Normal Equation: theta = (X'X)^(-1) X'y
    theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    return theta

# 4. Evaluate model performance using Mean Squared Error (MSE)
def mean_squared_error(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

def main():
    # 2. Create a simple dataset
    np.random.seed(42)  # For reproducibility
    X = 2 * np.random.rand(100, 1)  # 100 random data points
    y = 4 + 3 * X + np.random.randn(100, 1)  # Linear relation with noise

    # 3. Train the model
    theta = linear_regression(X, y)
    print(f"Calculated model parameters (theta):\n{theta}")

    # Predict using the model
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    y_pred = X_b.dot(theta)

    # Compute MSE
    mse = mean_squared_error(y, y_pred)
    print(f"\nMean Squared Error (MSE): {mse}")

if __name__ == "__main__":
    main()