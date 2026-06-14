# Exercises — AI Control â€” Safety Despite Subversion

## Exercises

1. **Implement a trusted monitor that scores untrusted outputs.** Write a Python script that takes a list of untrusted model outputs (as strings) and assigns each a suspicion score between 0 and 1. Use any method you like — keyword matching, output-length anomaly detection, or an LLM-as-judge call to a trusted model. Apply a threshold (default 0.5) and flag outputs at or above it for human review. Run the script on at least five sample outputs (include at least one that should be flagged) and print each output's score, flag status, and a summary count of flagged items.

2. **Compute the safety tax for a monitored protocol.** Write a script that takes three parameters — `catch_rate` (fraction of harmful outputs the monitor catches), `fp_rate` (fraction of safe outputs incorrectly flagged), and `trusted_usefulness` (the usefulness score of the trusted-only fallback, 0–1) — and computes: (a) the effective safety of the monitored protocol, (b) the effective usefulness assuming flagged outputs fall back to the trusted model, and (c) the safety tax (usefulness lost relative to untrusted-only at usefulness 1.0). Run your script with `catch_rate=0.9, fp_rate=0.15, trusted_usefulness=0.6` and print a formatted comparison table showing safety, usefulness, and safety tax for trusted-only, untrusted-only, and monitored protocols.

3. **Build a suspicion-based auditor.** Given a JSON file containing a list of suspicion scores from 200 runs of a single untrusted model session, implement an auditor that detects adversarial probing behavior. Compute the distribution of scores relative to the monitoring threshold and flag sessions where scores cluster within a narrow band just below the threshold (the "probing
