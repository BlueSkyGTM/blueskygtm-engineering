# Exercises — GANs â€” Generator vs Discriminator

## Exercises

1. **Compute the GAN minimax losses from raw discriminator outputs.** Implement a function `compute_gan_losses(D_real, D_fake)` that takes arrays of discriminator probabilities on real and fake samples and returns both `D_loss = -(mean(log D_real) + mean(log(1 - D_fake)))` and `G_loss = -mean(log D_fake)`. Call it with `D_real=[0.95, 0.88, 0.92]` and `D_fake=[0.10, 0.25, 0.15]` and print both loss values. Then call it with `D_real=[0.5, 0.5]` and `D_fake=[0.5, 0.5]` and print again — confirm both losses equal `log(2) ≈ 0.693`, demonstrating equilibrium.

2. **Train a minimal generator–discriminator pair on a 2D Gaussian target.** Build a generator MLP (input: `z ∈ R⁸`, output: `x ∈ R²`) and a discriminator MLP (input: `x ∈ R²`, output: sigmoid scalar) in PyTorch. Train for 1000 alternating steps against samples drawn from `N([2, 2], 0.5·I)`. After training, generate 500 samples from `G`, compute their mean and standard deviation along each axis, and print them. Confirm the mean is close to `[2, 2]` and the std is close to `0.5`.

3. **Diagnose mode collapse on a two-mode target.** Create a target distribution that is a 50/50 mixture of `N([-3, -3], 0.3·I)` and `N([3, 3], 0.3·I)`. Train a small GAN for 2000 steps. After training, generate 1000 samples and compute the fraction that fall within radius `1.0` of each mode center. Print both fractions — in a healthy GAN both should be near `0.5`; in mode collapse one will be near `1.0` and the other near `0.0`. Also print the discriminator's average output on real vs. fake samples to check whether `D` has collapsed to a constant.

4. **Compare GAN sample sharpness to autoencoder reconstruction.** Train a simple MLP autoencoder (encoder: `R²→R⁸`, decoder: `R⁸→R²`) with MSE reconstruction loss on the same Gaussian target from Exercise 2. After training, generate 500 samples two ways: (a) decode random latent vectors `z ~ N(0, I)` through the autoencoder, and (b) run `G(z)` from your Exercise 2 generator.
