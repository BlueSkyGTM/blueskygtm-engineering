# Exercises — T5, BART â€” Encoder-Decoder Models

## Exercises

1. **[Easy]** Compare encoder-decoder, encoder-only, and decoder-only architectures. Load the configs for `t5-small`, `bert-base-uncased`, and `gpt2` via HuggingFace `AutoConfig`. Write a function that inspects each config's attributes and prints a formatted table to the terminal indicating which components each model possesses: encoder stack, decoder stack, bidirectional self-attention, causal self-attention, and cross
