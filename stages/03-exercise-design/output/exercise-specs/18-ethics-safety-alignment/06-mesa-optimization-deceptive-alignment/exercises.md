# Exercises — Mesa-Optimization and Deceptive Alignment

## Exercises

1. Implement a function `classify_alignment(training_reward, deployment_reward, objective_match)` that takes three floats and returns one of `"aligned"`, `"corrigible"`, or `"deceptive"` based on the criteria from the lesson: objective match between mesa-objective and base objective, training performance, and deployment performance. Call it on six scenarios of your own design — two per category — and print a formatted table showing the inputs and predicted label for each. Verify that your classifier produces the expected label for all six.

2. Implement a generation-based population simulation of mesa-optimizer emergence. Initialize 200 agents, each with a randomly assigned internal objective vector (a 3-tuple of floats representing relative weights on three sub-goals). Apply selection pressure using a base-objective scoring function that differs from any agent's internal objective. Run 50 generations of selection plus mutation. At each generation, print the generation number, the mean base-objective score, the mean internal-objective divergence (cosine distance between each agent's internal objective and the base objective), and the number of surviving agents whose internal objective diverges from the base objective by more than 0.3. Report whether divergent mesa-optimizers survive and thrive.

3. Build
