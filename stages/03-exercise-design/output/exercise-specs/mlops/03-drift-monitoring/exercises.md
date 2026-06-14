# Exercises — MLOps 03 â€” Drift Monitoring

## Exercises

1. Implement the Kolmogorov-Smirnov two-sample test statistic from first principles using only NumPy. Compute the empirical CDFs of two arrays, find the maximum vertical distance between them, and compare your result against `scipy.stats.ks_2samp` on the same inputs. Use `np.random.normal` to generate a reference distribution and a shifted current distribution. Print both KS statistics side by side and confirm they match to at least 4 decimal places.

2. Implement Population Stability Index from scratch in NumPy. Bin a reference score distribution into 10 equal-frequency quantiles, compute the expected and actual proportions in each bin for a current distribution, and apply the PSI formula. Generate two log-normal distributions (one with a shifted mean) and report the PSI value along with a verdict: stable (<0.1), moderate (0.1–0.25), or significant (>0.25). Print the per-bin contributions so you can see which bins drive the drift.

3. Implement Jensen-Shannon divergence from first principles using `np.histogram` and the Shannon entropy formula (not `scipy.spatial.distance.jsc`). Then
