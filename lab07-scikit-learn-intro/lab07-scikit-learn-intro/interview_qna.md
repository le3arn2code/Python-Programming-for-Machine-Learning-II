# Interview Q&A — Lab 7: Intro to Scikit-Learn

1. **Q:** What is Scikit-Learn primarily used for?  
   **A:** Classical machine learning tasks: preprocessing, model selection, training, evaluation, pipelines, and utilities (cross-validation, metrics).

2. **Q:** Why use built-in datasets like California housing?  
   **A:** They provide standardized, well-known datasets for quick experimentation and benchmarking.

3. **Q:** What is the difference between `train_test_split` and cross-validation?  
   **A:** `train_test_split` provides a single holdout set; cross-validation averages performance across multiple splits for more robust estimates.

4. **Q:** What are the outputs of a linear regression model in scikit-learn?  
   **A:** `coef_` for weights per feature and `intercept_` for the bias term.

5. **Q:** What does `model.score(X, y)` return for `LinearRegression`?  
   **A:** The coefficient of determination R² on the given data.

6. **Q:** When should you standardize features before linear regression?  
   **A:** When features have very different scales or when using regularized variants (e.g., Lasso/Ridge) where scale impacts penalty.

7. **Q:** How do you avoid data leakage during scaling?  
   **A:** Fit scalers on the training set only; transform both train and test with the fitted scaler.

8. **Q:** Why set `random_state=42` in the split?  
   **A:** Reproducibility—same split across runs.

9. **Q:** What’s the typical effect of multicollinearity in linear regression?  
   **A:** Inflated variance of coefficient estimates; consider regularization (Ridge/Lasso) or feature selection.

10. **Q:** How can you quickly compare multiple regressors in scikit-learn?  
    **A:** Use a loop over estimators, `cross_val_score`, or build a `Pipeline` and evaluate with cross-validation.