# Exercises — Theory of Mind and Emergent Coordination

## Exercises

1. Implement a false-belief battery with three Sally-Anne variants: one first-order false-belief task, one second-order false-belief task ("John thinks that Mary thinks the marble is in the basket"), and one true-belief control (the observer witnessed the object being moved). Query an LLM on each variant across 5 trials per condition. Print a table showing per-condition accuracy (correct / total) and the raw model response for every incorrect trial.

2. Construct two decoy conditions designed to distinguish mechanistic ToM from pattern-matched narrative completion. Decoy A should closely mirror the Sally-Anne template but require a true-belief answer (the character saw the move). Decoy B should use an entirely different narrative structure (e.g., a workplace scenario) that tests the same first-order false-belief reasoning. Run both through your battery alongside the original conditions. Compute and print accuracy per decoy and identify which condition produces the highest error rate. State in a printed summary whether the model's failures are consistent with shallow template-matching or genuine belief-tracking.

3. Build a two-agent coordination system where two LLM instances must converge on a single integer between 1–100 by exchanging only a shared conversation transcript (no direct function calls between them; each agent reads the prior transcript and appends one message per round). Run 10 trials and print average rounds-to-convergence. Then repeat all 10 trials with a ToM-prompting intervention added to both agents ("Before responding, state what you believe the other agent is currently thinking"). Print the average rounds-to-convergence for both conditions and the delta.

4. Design a GTM outreach pipeline that models a buyer's belief state separately from the seller's. Load a prospect list (use the Apollo API or a CSV with columns:
