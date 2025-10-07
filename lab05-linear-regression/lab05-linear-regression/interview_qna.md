# Interview Q&A — Lab 5: Linear Regression

1. **Q:** What is the Normal Equation in linear regression?  
   **A:** It directly computes parameters without iterative optimization: \(\theta = (X^T X)^{-1} X^T y\) when \(X^T X\) is invertible.

2. **Q:** Why add a bias (intercept) column to X?  
   **A:** It allows the model to learn a non-zero intercept (baseline) instead of forcing the line through the origin.

3. **Q:** When can `(X^T X)` be singular?  
   **A:** With redundant/collinear features, insufficient samples, or duplicate columns/rows, making the matrix non-invertible.

4. **Q:** How does the pseudo-inverse help?  
   **A:** `pinv` provides a stable solution when `(X^T X)` is singular or ill-conditioned, effectively regularizing tiny singular values.

5. **Q:** What does MSE measure?  
   **A:** The average squared difference between predictions and true values; lower is better and penalizes large errors more strongly.

6. **Q:** Difference between closed-form (Normal Equation) and gradient descent?  
   **A:** Normal Equation is exact but scales poorly with many features; gradient descent iteratively improves parameters and scales to large datasets.

7. **Q:** How do you make predictions for new inputs?  
   **A:** Add a bias term and compute \(\hat{y} = X_b \theta\), where `X_b = [1, x]` for each sample when using a single feature.

8. **Q:** What assumptions underlie ordinary least squares?  
   **A:** Linear relationship, independent errors, homoscedasticity, and errors ~ N(0, \(\sigma^2\)) for inference.

9. **Q:** How would you extend to multiple features?  
   **A:** Let `X` be shape (N, d), add a ones column to form `X_b` (N, d+1), then apply the same Normal Equation or use `pinv`/`lstsq`.

10. **Q:** Why set `np.random.seed(42)`?  
    **A:** For reproducibility so that the generated data and resulting parameters are consistent across runs.