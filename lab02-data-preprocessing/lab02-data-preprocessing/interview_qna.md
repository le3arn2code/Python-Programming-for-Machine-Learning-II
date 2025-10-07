# Interview Q&A — Lab 2: Data Preprocessing

1. **Q:** Why is handling missing values important before modeling?  
   **A:** Many algorithms cannot handle NaNs and will error or produce biased results. Imputation (mean/median/mode or model-based) preserves dataset size and improves model stability.

2. **Q:** When would you use mean vs. median imputation?  
   **A:** Use **mean** when the distribution is roughly symmetric and outliers are minimal; use **median** when the distribution is skewed or has outliers.

3. **Q:** What is Min–Max scaling and when is it appropriate?  
   **A:** It rescales features to a fixed range (typically 0..1). It’s useful for distance-based or gradient-based models (e.g., k-NN, neural nets) so features contribute comparably.

4. **Q:** Difference between normalization and standardization?  
   **A:** Normalization scales to a range (e.g., 0..1), while standardization centers to mean 0 with unit variance (z-score). Choice depends on algorithm and data distribution.

5. **Q:** Why set `random_state` in `train_test_split`?  
   **A:** Ensures reproducible splits across runs, enabling consistent comparisons.

6. **Q:** How do you prevent data leakage during scaling?  
   **A:** Fit the scaler **only on training data** and transform both train and test using that fitted scaler. (In this lab we scaled first for simplicity; in production, split → fit on train → transform train/test.)

7. **Q:** What’s the risk of imputing target (label) values?  
   **A:** It can corrupt labels and mislead the model. Prefer removing rows with missing labels or carefully modeling label imputation separately.

8. **Q:** How can outliers affect Min–Max scaling?  
   **A:** Extreme values stretch the range, compressing most data near 0, which can reduce discrimination. Consider robust scaling or clipping outliers first.

9. **Q:** How to detect columns with many missing values quickly?  
   **A:** `df.isna().mean().sort_values(ascending=False)` shows fraction of missing per column.

10. **Q:** Why did the Series `.fillna(..., inplace=True)` raise a warning? What’s the fix?  
    **A:** Pandas is moving away from Series-inplace operations which may not affect the parent DataFrame. Use DataFrame-level `df.fillna({...}, inplace=True)` or assignment to the column (`df['col'] = df['col'].fillna(val)`).