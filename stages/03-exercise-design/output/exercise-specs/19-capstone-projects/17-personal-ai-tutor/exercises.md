# Exercises — Capstone 17 â€” Personal AI Tutor (Adaptive, Multimodal, with Memory)

## Exercises

1. Implement an episodic memory store that persists tutor-learner exchanges to a JSON file. Write a function that accepts `(question, answer, correctness)` tuples, appends each entry to `outputs/session_log.json` with an ISO timestamp and session ID, and prints the full session history after each append. Run three simulated exchanges (two correct, one incorrect) and confirm the printed log shows all three in chronological order.

2. Build a multimodal file parser that reads both `.txt` and `.py` files and normalizes each into a common dictionary schema: `{"source_type", "content", "line_count", "detected_topics"}`. Create one sample `.txt` file (a paragraph about recursion) and one sample `.py` file (a recursive function). Run your parser on both and print the resulting dictionaries side by side to confirm they share the same structure despite different input formats.

3. Implement a Bayesian-style proficiency update loop with no starter code. Start with a proficiency prior of 0.5 for a topic called `python_basics`. Simulate 10 attempts with this correctness sequence: `[1, 0, 1, 1, 0, 1,
