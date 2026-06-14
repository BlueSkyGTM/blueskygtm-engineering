# Exercises — Model Routing as a Cost-Reduction Primitive

## Exercises

1. **Compute blended cost for multiple routing splits and compare against a frontier-only baseline.** Given model pricing of $0.25/1M tokens (cheap), $3.00/1M tokens (mid-tier), and $15.00/1M tokens (frontier), write a script that accepts a routing distribution (e.g., `{"simple": 0.60, "medium": 0.30, "complex": 0.10}`) and prints the blended cost per 1M requests, the cost per 1M requests if every request hit the frontier model, and the percentage savings. Run the script for at least three different routing splits and print a comparison table to the terminal.

2. **Implement a rule-based classifier that routes prompts to tiers using keyword matching, regex patterns, and token-length thresholds.** Define rules such as: prompts under 50 tokens route to `simple`; prompts containing keywords like "translate," "rephrase," or "summarize" route to `simple`; prompts containing "analyze," "compare," or "evaluate" route to `medium`; everything else defaults to `complex`. Collect at least 10 sample prompts of genuinely varying difficulty, pass
