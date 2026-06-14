# Exercises — Matrix Transformations

## Exercises

1. **Implement all four canonical 2D transforms.** Write a Python script that defines functions `scale_matrix(sx, sy)`, `rotate_matrix(theta)`, `shear_matrix(k)`, and `reflect_matrix(axis)` — each returning the appropriate 2×2 NumPy array. Apply each one to the vector `v = [3, 2]` and print all four results. Confirm that `rotate_matrix(np.pi / 2)` applied to `[1, 0]` produces `[0, 1]` (90° counterclockwise).

2. **Verify composition equivalence.** Choose a scale matrix `S = scale_matrix(2, 0.5)` and a rotation `R = rotate_matrix(np.pi / 4)`. Pick a vector `v` of your choice. Compute `result_composed = (S @ R) @ v` and `result_sequential = S @ (R @ v)`. Print both vectors and assert they are equal using `np.allclose`. Then reverse the order to `(R @ S) @ v` and print it — confirm it differs, demonstrating that matrix composition is order-dependent.

3. **Diagnose three mystery matrices.** You are given three 2×2 matrices (hardcode them in your script):
   ```
   A = [[2, 0], [0, 2]]
   B = [[0, 1], [1, 0]]
   C = [[1, 0.5], [0.3, 1]]
   ```
   For each matrix, print the column vectors, state what transformation it represents (scale, shear, reflect, rotate, or combination), and verify your diagnosis by applying it to the basis vectors `e1 = [1, 0]` and `e2 = [0, 1]`. Your script should print a one-line label for each matrix (e.g., `"A: uniform scale by 2"`).

4. **Build an account-scoring projection.** Create a 5×3 matrix `W` that projects 5-dimensional account feature vectors `[employee_count, revenue_millions, engagement_score, days_since_signup, page_views]` into a 3-dimensional scoring space `[buying_power, intent, fit]`. Generate 4 synthetic account vectors with realistic values, apply `W` to each via matrix multiplication, and print a ranked list of accounts by their `buying_power` score. Normalize the input features before projection so no single dimension dominates.

5. **Build an account-fit scoring artifact.** Write a standalone script at `handlers/account_transform.py` that accepts a JSON array of account records (each with keys `employees`, `revenue_millions`, `engagement_score`, `days_active`, `page_views`) via `sys.stdin`, applies a hand-tuned projection matrix to produce a composite `fit_score` for each account, and writes the ranked results to `outputs/skill-account-scoring.md` as a Markdown table. Design your projection matrix so that high-revenue, high-engagement, recently-active accounts score highest. Test with at least 5 accounts where you can predict the ranking by hand, and verify the output file matches your expectation.

6. **Prove column-diagnosis correctness and test on real CRM export.** Write a script at `signals/examples/transform_diagnostic.py` that loads a CSV of account features exported from your CRM or a sample dataset (use `pandas.read_csv` on any CSV with numeric columns), constructs a projection matrix whose column vectors you designed by hand to emphasize specific feature combinations, and applies it to produce a single `priority_score` per account. Print the projection matrix columns alongside a human-readable annotation of what each column amplifies (e.g., `"Col 1 weights revenue and headcount — captures enterprise readiness"`). Then export the top 10 prioritized accounts with scores to `outputs/skill-priority-accounts.md`. Verify that manually computing the same projection on the first row of the CSV by hand matches the script's output.
