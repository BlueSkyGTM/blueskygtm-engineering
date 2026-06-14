# Exercises — Embodied VLAs: RT-2, OpenVLA, Ï€0, GR00T

## Exercises

1. **Implement an action tokenizer for 7-DOF joint positions.** Write `encode(actions, n_bins)` and `decode(tokens, n_bins)` where each dimension is independently binned into `n_bins=256` uniform intervals over `[-1, 1]`. Generate 2 000 random action vectors, round-trip them through encode → decode, and print the mean and max absolute reconstruction error per dimension. Confirm that every dimension's max error is ≤ `2 / n_bins`. If any dimension exceeds the bound, diagnose whether your bin-edge logic is off-by-one.

2. **Sweep bin count and print a comparison table.** Re-run the tokenizer from Exercise 1 across `n_bins ∈ [8, 16, 32, 64, 128, 256, 512]`. For each value, print four columns: `n_bins`, `max_recon_error`, `mean_recon_error`, and `vocab_size` (computed as `n_bins ** 7` for 7 action dimensions). Identify and print the smallest `n_bins` whose vocabulary exceeds 32 000 — a typical subword-vocab ceiling. Comment in a one-line print statement on what this implies for RT-2's 256-bin choice.

3. **Build a multimodal action-distribution simulator.** Construct a 1-D bimodal action distribution (two Gaussian peaks at `−0.6` and `+0.6`, each `σ=0.08`). Implement two sampling strategies: (a) a **discrete-bin predictor** that returns the single argmax bin center, and (b) a **flow-matching sampler** that draws from the true mixture via velocity-field interpolation between a standard-normal source and the bimodal target. Run both 500
