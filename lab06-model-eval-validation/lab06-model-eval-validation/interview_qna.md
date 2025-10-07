# Interview Q&A — Lab 6: Model Evaluation & Validation

1. **Q:** Why split data into train and validation sets?  
   **A:** To estimate performance on unseen data and tune choices without contaminating the final test set.

2. **Q:** What is k-fold cross-validation and why use it?  
   **A:** It partitions data into k folds and rotates the validation fold, giving a more reliable performance estimate and reducing variance due to a single split.

3. **Q:** Why set a random seed?  
   **A:** For reproducibility of splits and generated data to ensure results are consistent.

4. **Q:** What does MSE measure?  
   **A:** The average squared difference between predictions and true values—lower is better and penalizes large errors.

5. **Q:** When might MSE be a poor choice?  
   **A:** When targets have heavy tails/outliers or you care more about absolute errors; use MAE or robust metrics instead.

6. **Q:** What does shuffling in KFold do?  
   **A:** Randomizes the order before splitting into folds to avoid biased partitions (especially when data is ordered).

7. **Q:** Can LinearRegression accept y as 2D?  
   **A:** Yes, scikit-learn allows y as shape (n_samples, 1) or (n_samples,). Both work for this lab.

8. **Q:** How would you add multiple features?  
   **A:** Create X as (n_samples, d) with d>1 and keep the same API; LinearRegression handles multivariate features.

9. **Q:** Difference between validation set and test set?  
   **A:** Validation is for model/parameter selection; test is a final untouched set for unbiased performance reporting.

10. **Q:** How to detect overfitting with cross-validation?  
    **A:** Large gaps between training error and cross-validation error or high variance across fold scores indicate overfitting.