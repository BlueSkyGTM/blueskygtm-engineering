# Exercises — Swarm Optimization for LLMs (PSO, ACO)

## Exercises

1. **Implement a basic PSO loop.** Create a script that initializes 20 particles in a 2D continuous space representing `temperature` (0.0–2.0) and `top_p` (0.0–1.0). Use a mock fitness function such as the negative Euclidean distance from a hidden target point `(1.2, 0.8)`. Run 30 iterations, updating velocity with inertia weight 0.7, cognitive coefficient 1.5, social coefficient 1.5, and stochastic random coefficients. Print the iteration number, global best position, and global best fitness at each step. Confirm that the swarm converges within 30 ticks.

2. **Implement ACO over a 3-level prompt-component graph.** Define a graph with 3 greeting nodes, 3 value_prop nodes, and 2 CTA nodes. Assign each edge an initial pheromone of 0.1. Use a mock path-scoring function that returns a higher score for paths containing certain "winning" nodes (e.g., greetings[1], value_props[0], ctas[2]). Deploy 10 ants per iteration for 50 iterations with α = 1.0, β = 2.0, and an evaporation rate of 0.05. Print the best-scoring path discovered and the final pheromone matrix as a table.

3. **Compare PSO and ACO convergence on the same objective.** Implement both algorithms against a discretized Rastrigin function over the range [−5, 5] in two dimensions. For ACO, divide each dimension into 20 discrete bins. Track the best-so-far fitness at every iteration for both solvers. Run each for 100 iterations and print a side-by-side convergence table (iteration, PSO best, ACO best). State in a printed summary which algorithm converges faster and which reaches a higher final score.

4. **Configure a multi-objective fitness function for cold outreach.** Implement a fitness function that scores a generated outreach email on two objectives: a quality score (reward keyword presence like "discovered," "pipeline," "integration"; penalize subject-verb agreement issues or excessive length beyond 120 words) and a token-cost penalty scaled by `0.001 * estimated_token_count`. Combine them as `fitness = quality_score - cost_penalty`. Run your PSO loop from Exercise 1 using this fitness with a mock email generator that produces different text lengths based on `temperature` and `top_p`. Print the top 5 Pareto-optimal parameter sets and their scores.

5. **Build a full PSO-vs-grid-search comparison pipeline for LLM generation parameters.** Implement a PSO optimizer that searches `temperature`, `top_p`, and `frequency_penalty` to maximize a deterministic scoring metric on LLM
