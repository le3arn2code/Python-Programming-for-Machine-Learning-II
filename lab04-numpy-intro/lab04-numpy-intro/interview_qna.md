# Interview Q&A — Lab 4: NumPy

1. **Q:** What advantages does NumPy have over Python lists for numerical work?  
   **A:** NumPy arrays are contiguous, typed memory blocks enabling vectorized operations in C, which makes them faster and more memory-efficient than Python lists for numerical computing.

2. **Q:** What is broadcasting in NumPy?  
   **A:** A set of rules to apply operations to arrays of different shapes by virtually expanding singleton dimensions (no real data copy), allowing concise vectorized code.

3. **Q:** Difference between element-wise `*` and matrix multiplication?  
   **A:** `*` is element-wise for arrays of the same shape; matrix multiplication uses `np.dot(A,B)` or `A @ B` following linear algebra rules.

4. **Q:** How do you create special matrices like zeros/ones/identity?  
   **A:** `np.zeros((m,n))`, `np.ones((m,n))`, `np.eye(n)`.

5. **Q:** How to check array shape, dims, dtype?  
   **A:** `.shape`, `.ndim`, `.dtype` respectively.

6. **Q:** Why prefer vectorization over Python loops?  
   **A:** Vectorized operations leverage optimized C/BLAS routines, yielding cleaner code and significant speedups.

7. **Q:** When will broadcasting fail?  
   **A:** When non-equal dimensions are not 1 or identical, making shapes incompatible (e.g., (3,) and (2,) cannot broadcast).

8. **Q:** How to compute row-wise or column-wise sums?  
   **A:** Use axis argument: `A.sum(axis=0)` (columns) or `A.sum(axis=1)` (rows).

9. **Q:** How do you get reproducible random numbers?  
   **A:** Set a seed with `np.random.seed(42)` (or use the Generator API `np.random.default_rng(42)`).

10. **Q:** When to use `@` vs `np.dot` vs `np.matmul`?  
    **A:** `@` and `np.matmul` are infix matrix multiplication (preferred for readability). `np.dot` works for 2D like matmul but has different behavior for 1D vectors; stick to `@`/`matmul` for linear algebra clarity.