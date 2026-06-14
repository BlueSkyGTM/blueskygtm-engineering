# Exercises — Capstone 83 â€” Prompt Injection Detector

## Exercises

1. Implement three regex-based `Rule` objects for known injection signatures: direct instruction overrides (`ignore previous instructions`, `disregard the above`), role-resetting phrases (`you are now a`, `act as an unrestricted`), and delimiter smuggling (fake `<system>` or `[/INST]` tags inside user input). Build a `Detector` with these rules and run it against five sample prompts — three malicious, two safe. Print each prompt's `Verdict` (category + confidence).

2. Build a classifier-based `Rule` that sends the input prompt to a secondary LLM acting as a guard model. The guard model should return a JSON verdict of `safe` or `injection` with a confidence score. Run this rule against six prompts — including two that paraphrase injection intent in ways your regex rules from Exercise 1 would miss — and print the score for each.

3. Build a labeled test suite of 20 prompts across at least four categories: `direct_override`, `role_reset`, `extraction_attempt`, and `safe`. Run your full detector (regex + classifier combined) against every prompt and compute per-category precision and recall. Print a summary table showing each category's counts.

4. Create five paraphrased injection prompts designed to bypass your regex rules — rewordings that preserve injection intent but avoid exact pattern matches. Add these to your test suite. Then implement a threshold sweep across confidence cutoffs 0.3, 0.5, 0.7, and 0.9 and print false-positive and false-negative counts at each threshold. Identify which threshold gives the best F1 score.

5. Build a production-ready pipeline that ingests a CSV export of lead messages from Clay (column: `message`), runs each row through your multi-signal detector, and writes results to `outputs/clay-injection-scan.csv` with columns `message`, `verdict`, `category`, `confidence`. Include at least 15 messages, four of which contain subtle injection attempts. Run the pipeline and print a summary of flagged vs. clean messages.

6. Design and implement a comprehensive evaluation harness that runs your full detector across a 40+ prompt test suite, produces a confusion matrix as a formatted text table, computes per-category precision/recall/F1, and sweeps thresholds from 0.2 to 0.9 in steps of 0.1. Write the full analysis — including a recommendation for the optimal operating threshold with justification — to `outputs/skill-detector-eval.md`.
