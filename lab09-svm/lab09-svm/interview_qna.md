# Interview Q&A — Lab 9: SVM

1. **Q:** What is the intuition behind SVM for classification?  
   **A:** It finds the hyperplane that maximizes the margin between classes; support vectors are the closest points to the boundary.

2. **Q:** What do `C` and `gamma` control?  
   **A:** `C` controls regularization (trade-off between margin size and misclassification). `gamma` (for RBF/poly/sigmoid) controls the influence radius of each training sample.

3. **Q:** When would you prefer a linear kernel?  
   **A:** When data is approximately linearly separable or the feature space is high-dimensional and linear works well.

4. **Q:** Why stratify the train/test split?  
   **A:** To keep class proportions similar in train and test sets, preventing biased evaluation.

5. **Q:** What is the effect of a very large `C`?  
   **A:** Tighter fit to training data (less regularization) — risk of overfitting.

6. **Q:** What does `gamma='scale'` do?  
   **A:** Sets gamma to `1 / (n_features * X.var())`, a sensible default that adapts to feature scale.

7. **Q:** How do you handle features with different scales for SVM?  
   **A:** Standardize features (e.g., `StandardScaler`) especially for RBF kernel; linear SVM is also helped by scaling.

8. **Q:** Difference between `SVC` and `LinearSVC`?  
   **A:** `SVC` supports kernels and uses libsvm; `LinearSVC` uses liblinear, is faster for large linear problems, and exposes different loss/penalty options.

9. **Q:** How do you evaluate SVMs beyond accuracy?  
   **A:** Use precision/recall/F1, ROC-AUC, confusion matrix, and cross-validation scores depending on the problem.

10. **Q:** What’s the role of support vectors?  
    **A:** They define the decision boundary; only these points directly influence the fitted hyperplane.