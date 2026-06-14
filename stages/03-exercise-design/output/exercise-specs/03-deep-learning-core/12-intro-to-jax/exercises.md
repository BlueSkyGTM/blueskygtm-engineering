# Exercises — Introduction to JAX

## Exercises

1. Implement a cosine similarity function using `numpy`, then port it to `jax.numpy`. Compute the similarity between two 100-dimensional vectors (you may generate them with a fixed random seed) in both libraries and assert the outputs are numerically identical using `jnp.allclose` with a tolerance of `1e-6`. Print the similarity value and the assertion result.

2. Define a scalar-valued pure function `f(x) = 3x³ − 2x² + 5x − 7` using `jax.numpy` operations. Apply `jax.grad()` to obtain its derivative function, then evaluate both `f` and `f'` at `x = 2.0`. Verify the analytical derivative (`18x² − 4x + 5 → 81.0`) matches the JAX-computed value and print both.

3. Write a function that accepts an array and computes its mean, but includes a `print("computing mean of shape", x.shape)` statement inside the body. Call the raw function once, then call `jax.jit(function)` and invoke the jitted version twice. Observe and document (in a print statement at the end of your script) how many times the print fires and with what shape — explain whether the traced shape matches the runtime shape.

4. You are given a list of 500 lead feature vectors (each 8-dimensional: website visits, email opens, page depth, time on site, form submissions, demo requests, pricing page views, days since last visit). Generate this data synthetically with a fixed seed. Implement a per-lead score function `score(lead, weights)` that returns a scalar dot-product score. Use `jax.vmap()` to score all 500 leads in a single call with no explicit Python loop or batch dimension in the core function. Print the top-5 lead indices by score.

5. Compose `jax.jit(jax.vmap(jax.grad(loss_fn)))` to build a lead-scoring weight optimizer. Define a pure loss function that takes a single lead's features, a weight vector, and a binary conversion label, and returns logistic-regression-style negative log-likelihood. Generate 1000 synthetic leads with labels. Use the composed transform to compute per-example gradients across all leads, average them, and run 200 gradient-descent steps with a learning rate of `0.01`. Save the final weight vector and a short summary (final loss, iterations, learning rate) to `outputs/skill-jax-lead-optimizer.md`.

6. Implement the same mean-squared-error gradient computation three ways: (a) NumPy with manual chain-rule derivatives, (b) PyTorch with `loss.backward()` and `.backward()`-style autodiff, and (c) JAX with `jax.grad()`. Time each approach over 10,000 evaluations on a 50-dimensional input. Print a comparison table showing mean runtime, computed gradient norm, and lines-of-code for each implementation. Save the table to `outputs/skill-jax-execution-model-comparison.md`.
