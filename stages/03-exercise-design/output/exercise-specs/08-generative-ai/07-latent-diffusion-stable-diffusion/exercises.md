# Exercises — Latent Diffusion & Stable Diffusion

## Exercises

1. **Trace the latent diffusion pipeline end to end.** Load `runwayml/stable-diffusion-v1-5` via the `diffusers` library, then write a script that (a) tokenizes a text prompt and passes it through the CLIP text encoder, printing the embedding shape; (b) creates a random `512×512×3` image tensor, encodes it through the VAE encoder, and prints the resulting latent shape; (c) passes that latent through one U-Net denoising step with the text embedding as conditioning, printing the output latent shape; and (d) decodes the output latent back through the VAE decoder, printing the final pixel shape. Your terminal output should confirm each shape and show that the latent is `64×64×4` for a `512×512` input.

2. **Compute pixel-space vs. latent-space savings across resolutions.** Write a pure-Python function (no model loading needed) that accepts
