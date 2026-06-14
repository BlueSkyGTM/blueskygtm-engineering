# Exercises — Dimensionality Reduction

## Exercises

1. **Extend the curse of dimensionality demo from the lesson.** Add dimensions 5000 and 10000 to the existing loop, then compute the coefficient of variation (std / mean) of pairwise distances at each dimension. Print an updated table showing both the max/min ratio and the CV. Observe how both metrics confirm distance concentration — the CV should shrink toward zero as dimensions grow.

2. **Implement PCA from scratch on a synthetic 2D dataset.** Generate 200 points from a multivariate normal with a strong correlation between the two features (e.g., covariance `[[3, 2.5], [2.5, 3]]`). Center the data, compute the covariance matrix, eigendecompose it, sort eigenvalues in descending order, and project onto the first principal component. Verify your results match `sklearn.decomposition.PCA` by printing the first 5 projected values from both implementations side by side.

3. **Compute explained variance ratios from scratch and select components for 95% retention.** Load the sklearn digits dataset (64 features, 1797 samples). Compute the covariance matrix, eigendecompose it, and derive explained variance ratios without using sklearn's PCA. Determine the minimum number of components needed to retain 95% of total variance. Print a cumulative explained variance table for the first 20 components and state the selected k value.

4. **Compare PCA, t-SNE, and UMAP on GTM firmographic data.** Generate a synthetic dataset of
