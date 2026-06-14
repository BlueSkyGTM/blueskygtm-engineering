# Exercises — Inference Metrics â€” TTFT, TPOT, ITL, Goodput, P99

## Exercises

1. **Compute** all five core metrics from a single request's raw timing data. Create a JSON file containing `request_arrival_ts`, `first_token_ts`, and an array of per-token emission timestamps for a simulated 50-token response. Write a script that loads this file and prints TTFT, TPOT, mean ITL, max ITL, and P99 ITL — each on its own line with units in milliseconds. Confirm that `TTFT + (TPOT × output_tokens)` approximates total elapsed time; print both values side by side.

2. **Instrument** a simulated streaming LLM endpoint — a Python generator that yields tokens with randomized inter-token delays (mix of fast ~10 ms and occasional stutter spikes ~80 ms). Capture wall-clock timestamps at request arrival, first token emission, and every subsequent token. Print a per-token ITL table showing token index, timestamp, and delta from previous token. Verify visually that TPOT smooths over the spike pattern that individual ITL values expose.

3. **Build** a goodput calculator over a batch of 50 requests. Generate a JSON dataset where each request has per-token timestamps, a total token count, and an `error` boolean (roughly 10% flagged as errors). Define a multi-constraint SLO: `TTFT < 500 ms AND TPOT < 15 ms AND E2E < 2000 ms AND error == False`. Compute goodput as the count of tokens from requests satisfying every constraint simultaneously divided by total tokens across all requests. Print the goodput percentage and a breakdown showing how many requests failed each individual constraint.

4. **Compare** percentile-based and mean-based latency reporting. Generate 1,000 simulated request latencies from a lognormal distribution (shape that produces a visible tail). Compute mean, P50, P90, P95, P99, and max latency. Print all six values and the P99-to-mean ratio. Then print a 2–3 sentence explanation of why a GTM operations
