# Exercises — Multi-Head Attention

## Exercises

1. **Implement multi-head attention from scratch in NumPy.** Given a random input `X` of shape `(8, 64)` (8 tokens, `d_model=64`), write a function that performs all four stages — project to Q/K/V via learned weight matrices, split into 4 heads (`d_head=16`), run
