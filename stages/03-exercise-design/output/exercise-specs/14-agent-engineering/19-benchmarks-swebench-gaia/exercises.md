# Exercises — Benchmarks: SWE-bench, GAIA, AgentBench

## Exercises

1. **Compute pass@1 and pass@5 from raw patch results and observe rank instability.** Create a JSON file containing patch-trial results for three agents across 20 issues (5 attempts each, each marked pass or fail). Write a script that computes pass@1 (first attempt only) and pass@5 (best of five) per agent, prints a ranked leaderboard for each metric, and flags any agent whose rank changes between the two. Ensure
