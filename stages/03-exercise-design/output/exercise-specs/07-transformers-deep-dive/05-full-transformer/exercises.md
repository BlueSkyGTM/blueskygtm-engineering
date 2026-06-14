# Exercises — The Full Transformer â€” Encoder + Decoder

## Exercises

1. **Trace the forward pass.** Run the lesson's encoder-decoder model on a `(src_len=8, tgt_len=6, d_model=64)` random tensor pair. Insert print statements at each sub-layer — encoder self-attention output, decoder masked self-attention output, cross-attention output, feed-forward output, and final logits. Label each printed tensor with its originating component (`ENC_SelfAttn`, `DEC_MaskedAttn`, `CrossAttn`, `FFN`). Confirm that `CrossAttn` output shape is `(6, 64)` — queries from decoder, not encoder.

2. **Compare cross-attention against decoder-only self-attention.** Build a minimal single-layer decoder-only block (masked causal self-attention + FFN, no cross-attention) with the same `d_model`, `n_heads`, and `d_ff` as the lesson's encoder-decoder model. Feed both architectures the same source and target tensors. Print the total parameter count, the attention weight matrix shapes, and the number of distinct sequences each block attends over. Confirm that the decoder-only block has zero attention matrices whose Q and K originate from different tensors.

3. **Implement a single-layer encoder-decoder Transformer from scratch.** Build the full stack in PyTorch without importing any existing module from the lesson: bidirectional self-attention encoder, causal-masked decoder self-attention, cross-attention (Q from decoder, K/V from encoder), feed-forward, layer norms, and residual connections. Instantiate with `d_model=128, n_heads=4, d_ff=512`. Run a forward pass on random
