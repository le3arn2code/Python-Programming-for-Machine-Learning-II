# Interview Q&A — Lab 10: Simple Neural Network

1. **Q:** Why use one-hot encoding for Iris labels?  
   **A:** Softmax output with `categorical_crossentropy` expects class probabilities; one‑hot encodes labels to match the 3 output neurons.

2. **Q:** What does `softmax` do in the final layer?  
   **A:** Converts logits to a probability distribution across classes that sums to 1.

3. **Q:** Why choose `Adam` optimizer here?  
   **A:** It adapts learning rates per parameter and works well out‑of‑the‑box for many problems.

4. **Q:** What’s the difference between `sparse_categorical_crossentropy` and `categorical_crossentropy`?  
   **A:** `sparse_…` takes integer class labels; `categorical_…` expects one‑hot vectors.

5. **Q:** Why split 80/20 train/test with a fixed random seed?  
   **A:** To evaluate generalization and ensure reproducible results.

6. **Q:** What role does `batch_size` play?  
   **A:** Number of samples per gradient update; smaller batches add noise (can help generalization), larger batches are more stable.

7. **Q:** How many parameters does the model have?  
   **A:** For Iris (4 features): (4×32+32) + (32×32+32) + (32×3+3) = 803 params.

8. **Q:** When should you add dropout or regularization?  
   **A:** When overfitting is observed (training acc >> validation/test acc).

9. **Q:** How to monitor validation accuracy each epoch?  
   **A:** Pass `validation_split=0.2` to `model.fit()` or provide `(X_val, y_val)` to `validation_data=`.

10. **Q:** How to save and load the trained model?  
    **A:** `model.save('model.keras')`; later `tf.keras.models.load_model('model.keras')`.