# Interview Q&A — Lab 3: Matplotlib

1. **Q:** When would you use a histogram?  
   **A:** To visualize the distribution (shape, spread, modality) of a single numeric variable.

2. **Q:** What’s the purpose of a scatter plot?  
   **A:** To show the relationship between two numeric variables (trend, clusters, outliers).

3. **Q:** When is a line chart more appropriate than a scatter plot?  
   **A:** For continuous series or ordered data (e.g., time on the x-axis) to convey trends over an ordered domain.

4. **Q:** When should you use a bar chart?  
   **A:** To compare values across categories (discrete groups, labels, or bins).

5. **Q:** Why add titles, axis labels, and legends?  
   **A:** To make charts self-explanatory: what the chart shows, what axes mean, and what each series represents.

6. **Q:** How do you avoid GUI errors on servers when using Matplotlib?  
   **A:** Use a non-interactive backend like Agg (`matplotlib.use('Agg')`) and save figures to files.

7. **Q:** What are typical steps to improve readability?  
   **A:** Add titles/labels, use legends where needed, add grids for quantitative reading, adjust figure size and tick rotation.

8. **Q:** Why avoid hard-coding colors/styles in a shared environment?  
   **A:** To keep scripts portable and compliant with style policies; defaults are often accessible and consistent. Customize only if needed.

9. **Q:** How do you ensure each chart doesn’t overwrite the previous one?  
   **A:** Create a new figure for each plot (`plt.figure()`), save it, then `plt.close()` to release memory.

10. **Q:** How to export multiple figures automatically?  
    **A:** Generate each figure programmatically and save with distinct filenames into a dedicated folder (e.g., `./screenshots/`).
