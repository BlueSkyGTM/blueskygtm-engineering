# Exercises — Multi-Layer Networks and Forward Pass

## Exercises

1. Implement a forward pass through a 2-layer network (3 inputs → 4 hidden → 1 output) using NumPy. Initialize weight matrices and bias vectors with small random values (seed your RNG for reproducibility). Feed in the input vector `[0.5, -1.2, 0.8]`, apply ReLU after the hidden layer and sigmoid on the output, and print the final scalar prediction to the terminal.

2. Extend your network from Exercise 1 to three layers (3 → 4 → 2 → 1). Trace a single input vector through every layer and print the intermediate activation vector after each transformation. Label each printout clearly: `Layer 1 activations:`, `Layer 2 activations:`, `Output:`. Use tanh for both hidden layers and sigmoid for the output.

3. A colleague hands you four weight matrices with shapes `(2,3)`, `(3,5)`, `(4,2)`, and `(2,1)`, along with an input vector of dimension 3. Write a script that attempts a forward pass through every possible ordering of these matrices, catches shape errors, and prints a diagnostic message for each ordering indicating whether it succeeded or which matrix caused the dimension mismatch.

4. Load a CSV of 50 enriched Apollo company records with three numeric features (employee_count, annual_revenue, engagement_score). Implement a 2-layer network (3 → 5 → 1) and run the forward pass three times — once with ReLU, once with sigmoid, once with tanh as the hidden activation (keep weights fixed across all three). Print the min, max, and mean of the output lead-fit scores for each activation. State which activation produces the widest score range and which compresses scores most aggressively.

5. Generate a synthetic 2D dataset of 300 points where Class A points fall inside a circle of radius 1.0 centered at the origin and Class B points fall outside. Implement two classifiers using only forward passes (no training loop): a single-layer linear model and a 3-layer network (2 → 16 → 16 → 1) with tanh hidden activations. Initialize both with random weights. Compute classification accuracy for each over all 300 points. Write a summary to `outputs/skill-layer-capacity.md` containing both accuracy numbers and a 3–4 sentence explanation of why the multi-layer network separates the circular boundary while the single-layer model cannot.

6. Build a 3-layer lead
