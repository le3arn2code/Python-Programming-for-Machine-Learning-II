# Interview Q&A — Lab 8: Decision Trees

1. **Q:** What is a decision tree classifier?  
   **A:** A tree-structured model that splits feature space using decision rules to assign class labels.

2. **Q:** Why are trees easy to interpret?  
   **A:** Splits correspond to human-readable rules (e.g., "petal length <= 2.45").

3. **Q:** What does `max_depth` control?  
   **A:** The maximum number of levels in the tree; higher depth increases model capacity and overfitting risk.

4. **Q:** How do we prevent overfitting in trees?  
   **A:** Pruning/hyperparameters: `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_leaf_nodes`.

5. **Q:** Why set `random_state`?  
   **A:** For reproducible splits and tie-breaking in the tree algorithm.

6. **Q:** What metric does `DecisionTreeClassifier` use by default?  
   **A:** Gini impurity; you can switch to entropy with `criterion="entropy"`.

7. **Q:** Can trees handle non-linear decision boundaries?  
   **A:** Yes, by recursively partitioning the space they model complex, non-linear boundaries.

8. **Q:** Do trees require feature scaling?  
   **A:** No—trees are invariant to monotonic feature scaling.

9. **Q:** What is a typical downside of a single decision tree?  
   **A:** High variance; small changes in data can yield different trees. Ensembles (Random Forests, Gradient Boosting) mitigate this.

10. **Q:** How is accuracy computed?  
    **A:** `(number of correct predictions) / (total predictions)`; in scikit-learn via `accuracy_score(y_true, y_pred)`.