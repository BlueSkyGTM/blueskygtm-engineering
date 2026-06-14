# Exercises — Dynamic Programming â€” Policy Iteration & Value Iteration

## Exercises

1. **Implement iterative policy evaluation** on a 4×4 gridworld MDP (terminal state in one corner, reward of −1 per step, uniform random policy). Run sweeps until the value function changes by less than 1e-6. Print the value function as a formatted grid after each sweep so you can watch it converge.

2. **Implement value iteration** on the same 4×4 gridworld. Use a single Bellman optimality backup loop until convergence (threshold 1e-6), then extract the greedy policy by computing argmax over actions in each state. Print the final optimal value grid and an arrow-grid showing the greedy policy.

3. **Compare convergence behavior** between policy iteration and value iteration on a larger MDP — use a 6×6 gridworld with two terminal states of opposite sign (+10 and −10). Implement both algorithms from scratch (no library DP solvers). For each algorithm, print: total outer iterations, total individual state-backups performed across all sweeps, and wall-clock time. Verify that both converge to the same optimal value function (print max absolute difference between the two final value vectors).

4. **Trace the Bellman optimality operator's contraction** on a small 3-state, 2-action MDP of your own construction (define explicit P and R arrays). Starting from V₀ = [0, 0, 0], apply T(V) = max_a Σ P(s'|s,a)[R + γV(s')] for 15 iterations. At each step, compute ‖V_{k+1} − V_k‖_∞ and the ratio ‖V_{k+1} − V_k‖_∞ / ‖V_k − V_{k−1}‖_∞. Print a table of iteration, infinity-norm change, and contraction ratio. Confirm every ratio is ≤ γ.

5. **Build a B2B customer-journey MDP solver.** Define states as pipeline stages (Cold → Engaged → MQL → SQL → Opportunity → Closed Won / Closed Lost, the last two terminal). Define actions per state (e.g., email, call, demo, wait). Populate transition probabilities and rewards from realistic assumptions or from aggregate CRM conversion data if available. Implement full policy iteration to find the optimal touchpoint strategy for each pipeline stage. Print the optimal policy per stage and the converged value of being in each stage. Persist your implementation as a reusable module at `handlers/customer_journey_dp.py` that can be imported and called with `python -m handlers.customer_journey_dp`.

6. **Write a diagnosis document** analyzing three real GTM decision problems — (a) optimizing an outbound email sequence, (b) dynamic ad bidding across channels, (c) churn-prevention intervention timing. For each, determine whether dynamic programming is applicable (i.e., the transition model is known or reliably estimable) or whether model-free RL is required, and justify the reasoning. Include pseudocode for the one problem where DP fits. Persist the artifact at `outputs/skill-dp-vs-model-free-gtm.md`.
