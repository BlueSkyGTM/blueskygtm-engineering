# Exercises — Autoencoders & Variational Autoencoders (VAE)

## Exercises

1. **Build a standard autoencoder on synthetic tabular data.** Generate a 32-dimensional dataset with `sklearn.datasets.make_classification` (1000 samples, 2 classes). Implement an encoder (32 → 16 → 8 → 3) and decoder (3 → 8 → 16 → 32) in PyTorch. Train for 50 epochs using MSE loss. After training, compute and print the mean reconstruction error on both the training set and a held-out test set. Confirm that test-set error is higher — this gap is the anomaly signal.

2. **Implement a VAE with the reparameterization trick on the same dataset.** Modify your encoder to output two heads: `μ(x)` and `log σ²(x)`, each of dimension 3. Implement the reparameterization as `z = μ + σ * ε` where `ε ~ N(0, I)`. Compute the KL divergence analytically as `−0.5 * Σ(1 + log σ² − μ² − σ²)`. Train for 50 epochs minimizing `reconstruction_loss + KL`. Print reconstruction loss and KL divergence separately at each epoch so you can watch the two terms settle.

3. **Compare latent geometry of the AE and VAE on held-out data.** For both models trained in Exercises 1 and 2, compute per-sample reconstruction error on the test set. Then compute the KL divergence between each model's encoded distribution and `N(0, I)` (for the AE, treat the latent code as a delta distribution so KL is effectively infinite or use a nearest-neighbor density estimate). Print a table with columns: model, mean reconstruction MSE, std reconstruction MSE, mean KL-to-prior. State which model reconstructs better and which has a latent space closer to the prior.

4. **Trace the effect of the KL weight on encoder regularization.** Train four VAE instances with β (the KL loss coefficient) set to 0.0, 0.25, 0.5
