# Exercises — Vision Transformers (ViT)

## Exercises

1. **Compute** sequence lengths for a range of ViT configurations. Write a standalone script that takes image height, width, channels, patch size, and embedding dimension, then prints a formatted table showing: grid rows, grid columns, total patch tokens, flattened patch dimensionality, and sequence length after `[CLS]` prepending. Run it for at least four configurations: `(224, 224, 3, 16)`, `(384, 384, 3, 16)`, `(224, 224, 3, 32)`, and `(256, 512, 3, 16)`. Verify that the flattened patch dimension for `(224, 224, 3, 16)` equals `768` and that the final sequence length equals `197`. Terminal output should be the printed table.

2. **Implement** a `PatchEmbedding` module using `nn.Conv2d` with `kernel_size=patch_size`, `stride=patch_size`, and `out_channels=d_model`. Instantiate it for a `224×224×3` image with `P=16` and `d_model=768`. Run a forward pass on a random tensor of shape `(1, 3, 224, 224)`. Flatten the spatial dimensions of the conv output to produce `(1, num_patches, d_model)`. Print the conv output shape before and after flattening, and assert that the flattened shape matches `(1, 196, 7
