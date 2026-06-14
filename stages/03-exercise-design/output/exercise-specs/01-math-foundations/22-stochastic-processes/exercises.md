# Exercises — Stochastic Processes

## Exercises

1. Implement a discrete-time Markov chain simulator. Write a function that accepts a transition matrix (as a NumPy array), a starting state index, and a number of steps. At each step, sample the next state from the row corresponding to the current state using `np.random.choice`. Run the chain for 1000 steps starting from state 0 using this 3-state matrix:

   ```
   P = [[0.7, 0.2, 0.1],
        [0.3, 0.5, 0.2],
        [0.1, 0.3, 0.6]]
   ```

   Print the full sequence of the first 50 states, then print the empirical frequency of each state across all 1000 steps. Confirm the frequencies are roughly stable when you re-run with a different random seed.

2. Simulate a Poisson process with rate λ = 5 events per unit time over a horizon of 200 time units. Generate inter-arrival times by drawing from an exponential distribution with scale `1/λ`, then compute arrival times as the cumulative sum. Bin arrivals into integer-length intervals and print a histogram of event counts per bin. Compare your empirical bin proportions against the theoretical Poisson(λ=5) PMF evaluated at k = 0, 1, 2, …, 15 — print both side by side.

3. You are given two event streams, each claimed to follow a Poisson process with λ = 3. Generate Stream A by simulating a true Poisson(3) process over 500 intervals. Construct Stream B by manually injecting periodicity: alternate between low-activity intervals (Poisson with λ=1) and high-activity intervals (Poisson with λ=5). Compute the mean and variance of event counts for each stream, then run a chi-square goodness-of-fit test comparing each stream's count distribution to the theoretical Poisson(3) PMF. Print the test statistic, p-value, and your verdict (consistent / anomalous) for each stream.

4. Export 500 leads from your CRM (or use a sample CSV with columns `lead_id` and `stage` recorded at weekly snapshots). Treat the sequence of stage transitions as a Markov chain with states `new`, `contacted`, `qualified`, `opportunity`, `won`, `lost`. Estimate the transition matrix by counting observed transitions between consecutive snapshots and normalizing each row. Print the matrix. Then compute the steady-state distribution by finding the left eigenvector associated with eigenvalue 1 (use `np.linalg.eig` on the transposed matrix). Report what fraction of leads end up in `won` versus `lost` at steady state.

5. Compute π using Monte Carlo integration: generate N random points in the unit square and count how many fall inside the quarter circle of radius 1. Run the estimation for N = 100, 1000, 10000, 100000, and 1000000. For each N, run 50 independent trials and record the mean absolute error between the estimated π and the true value. Print a table showing N, mean error, and error standard deviation across trials. Save the script and its tabular output to `signals/examples/monte_carlo_convergence.py`.

6. Design a monitoring handler that combines Markov steady-state analysis with anomaly detection for a GTM pipeline. The handler should read weekly stage-transition data from a CSV, estimate the transition matrix, compute the steady-state `won` rate, and then run a chi-square test comparing the most recent week's transition counts against the historical matrix. If the p-value drops below 0.01, emit a signal indicating pipeline behavior has shifted. Save the handler to `handlers/pipeline_stochastic_monitor.py`. Run it against a CSV you construct where the first 20 weeks follow one transition matrix and week 21 silently switches to a different matrix — confirm the handler flags week 21 and not the earlier weeks.
