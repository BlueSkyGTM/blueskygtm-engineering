# Exercises — Transformer Block from Scratch

## Exercises

1. **Implement a single transformer encoder block** with post-norm ordering. Use the multi-head attention, feed-forward network, residual connection, and layer norm sublayers from the lesson. Instantiate your block with `d_model=64`, `n_heads=4`, `d_ff=256`, and `ffn_dropout=0.0`. Feed a random input tensor of shape `[2, 10, 64]` through the block and print the output shape. Verify it matches `[2, 10, 64]`.

2. **Trace the tensor through every sublayer** of your encoder block from Exercise 1. Before and after each component (attention projections, softmax, feed-forward expansion, residual add, layer norm), print the tensor name and its shape. Run with the same `[2, 10, 64]` input. Confirm every intermediate shape is what you expect and that no dimension changes except inside the feed-forward expansion/contraction.

3. **Implement both pre-norm and post-norm variants** of the transformer block. Run the same input tensor (`torch.randn(4, 16, 128)`, fixed seed) through each variant with identical hyperparameters. Compute and print the L2 norm of the difference between the two outputs, plus the mean activation magnitude of each. Report which variant produces larger activations and by how much.

4. **Diagnose a dimensional mismatch.** Construct a broken transformer block where the feed-forward network's hidden dimension does not project back to `d_model` (e.g., `d_ff=256` but the output linear layer maps to a wrong dimension). Feed a `[3, 8, 64]` tensor through the block and run your shape-tracing utility from Exercise 2. Print the full shape trace and the resulting error message. Then write a one-paragraph diagnosis identifying the exact sublayer and parameter that caused the failure.

5. **Configure and benchmark three transformer blocks** with different hyperparameter settings: (a) `d_model=128, n_heads=4, d_ff=512`, (b) `d_model=128, n_heads=8, d_ff=512`, (c) `d_model=256, n_heads=8, d_ff=1024`. For each, compute the total parameter count and the output shape on a `[4, 32, d_model]` input. Print a comparison table. Save the table and the three model definitions to `signals/examples/transformer_hyperparams.py`.

6. **Build a transformer-based intent scorer for GTM lead enrichment.** Load a CSV of company descriptions (use Apollo-style firmographic data or the sample at `data/companies_sample.csv` if available). Encode each description into a `[seq_len, d_model]` tensor using a simple bag-of-words or pretrained embedding. Run the tensor through a 2-layer transformer encoder you implement. Take the mean-pooled output and pass it through a linear classifier to produce an intent score (0–1). Print the top 10 highest-intent companies with their scores. Save the full scorer as `handlers/intent_scorer.py` and the ranked output table to `outputs/skill-intent-scores.md`.
