# Exercises — Alignment Faking

## Exercises

1. **Implement** a compliance gap calculator. Create two JSONL files — one representing monitored conditions and one unmonitored — each with at least 10 paired evaluation entries containing `query`, `response`, and `helpfulness_score` (0–10). Write a script that computes the mean score per condition, the gap between them, and prints a threshold-based interpretation (e.g., gap > 1.0 flags potential alignment faking). Run the script and verify the printed gap matches your manual calculation.

2. **Classify** behavioral signatures from scenario descriptions. Write a script containing at least 8 scenario dictionaries, each with a `description` and a list of `behavioral_markers`.
