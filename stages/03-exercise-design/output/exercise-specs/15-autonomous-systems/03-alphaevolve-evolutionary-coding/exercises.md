# Exercises — AlphaEvolve â€” Evolutionary Coding Agents

## Exercises

1. **Implement a fitness evaluation pipeline for candidate Python programs.** Write a function that accepts a list of candidate program source-code strings and a list of test-case tuples (input, expected_output). Each candidate is executed in a sandboxed `exec` call, tested against every case, and assigned a numeric fitness score equal to the fraction of tests passed. Print a table showing each candidate's index, fitness score, and any exceptions raised. Verify your output by confirming that a correct program scores 1.0 and a broken one scores 0.0.

2. **Implement tournament selection and fitness-proportionate selection, then compare their behavior.** Given a population of 20 programs with pre-assigned fitness scores (you may hardcode a spread from 0.1 to 0.95), implement both selection strategies. Run 50 parent selections with each method and print a histogram of how frequently each program was chosen. Vary tournament size (k=2, k=5, k=10) and observe how selection pressure shifts. Your terminal output should show the histograms for each configuration.

3. **Build a complete evolutionary loop on a numeric optimization problem without an LLM.** Evolve a population of candidate solutions (represented as lists of floating-point coefficients) to maximize an objective function such as the negative of the Rastrigin function or a custom polynomial. Use random Gaussian perturbation as your mutation operator and tournament selection for parent choice. Run the loop for at least 50 generations with a population of 30, printing the best and mean fitness at each generation. Then re-run with population sizes of 10 and 100 and mutation standard deviations of 0.01 and 1.0, printing a final comparison table of best fitness achieved in each configuration.

4. **Integrate an LLM as the mutation operator and compare evolutionary search
