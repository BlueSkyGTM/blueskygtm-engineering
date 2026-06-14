# Exercises — Watermarking â€” SynthID, Stable Signature, C2PA

## Exercises

1. Implement a function `detect_watermark(observed_values, expected_mean, expected_std)` that takes a list of token-level perturbation scores from a candidate text and computes the mean z-score against the expected unwatermarked baseline. Return the z-score and a confidence label: `"high"` if `|z| > 3`, `"medium"` if `2 < |z| ≤ 3`, `"low"` if `1 < |z| ≤ 2`, `"none"` if `|z| ≤ 1`. Write a test harness that runs three sample inputs — a clearly watermarked sequence, a
