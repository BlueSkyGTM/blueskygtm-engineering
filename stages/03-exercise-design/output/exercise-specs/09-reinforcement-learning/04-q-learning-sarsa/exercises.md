# Exercises — Temporal Difference â€” Q-Learning & SARSA

## Exercises

1. Implement the TD(0) state-value update on a 4-state linear chain. Each episode starts at state 0, transitions right with reward 0 at every step, and reaching state 3 yields reward +1 and terminates. Run 200 episodes with α=0.1, γ=0.9. Print V(s) for all four states every 50 episodes, and print the TD error δ for every step within episode 1. Verify that V(0) converges toward γ³ ≈ 0.729 and that δ shrinks over successive visits to the same state.

2. Implement the one-step Q-learning update and the one-step SARSA update as two pure functions that each accept (Q,
