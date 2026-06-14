# Exercises — Transfusion: Autoregressive Text + Diffusion Image in One Transformer

## Exercises

1. **Implement the heterogeneous attention mask.** Write a function that takes a sequence layout specification (a list labeling each position as `text`, `image`, `image_start`, or `image_end`) and constructs the Transfusion attention matrix: causal for text positions, fully bidirectional within each image block, and causal at every text→image boundary (image tokens attend to all preceding text, text tokens never attend to future image tokens). Run it on a 10-position layout `["text", "text", "image_start", "image", "image", "image", "image", "image_end", "text", "text"]` and print the resulting mask as a grid of 1s and 0s. Verify visually that the image block is a solid square of 1s while the text portions are lower-triangular.

2. **Implement the Transfusion dual-loss computation.** Given a mock batch containing (a) text logits shaped `[batch, seq_text, vocab_size]` with corresponding gold token
