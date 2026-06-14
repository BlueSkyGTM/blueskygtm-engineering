# Exercises — Speculative Decoding and EAGLE-3

## Exercises

1. **Trace the speculative decoding loop and verify distributional equivalence.** Implement a single round of speculative decoding where a draft model (a Python function returning a token-to-probability dict) proposes 4 tokens and a target verifier model (another such function) verifies them. Implement the modified rejection sampling criterion: for each draft token `x` with draft probability `q(x)`, draw `r ~ Uniform(0,1)`, accept if `r < min(1, p(x)/q(x))`; if rejected, resample from `norm(max(0, p(x) - q(x)))` and stop the round. If all 4 are accepted, emit a bonus token sampled from the verifier's distribution at position 5. Print the accepted sequence, per-token accept/reject decisions, and whether a bonus token fired. Then run 10,000 rounds and print a histogram of emitted tokens alongside the verifier's marginal distribution — they must match.

2. **Compute optimal draft length across operating regimes.** Implement the speedup formula `S = (1 + N·α) / (1 + N·c)` where `α` is acceptance rate, `c` is draft-to-verifier cost ratio, and `N` is draft length. For the
