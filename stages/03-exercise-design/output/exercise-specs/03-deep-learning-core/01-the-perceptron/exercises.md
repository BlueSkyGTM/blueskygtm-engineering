# Exercises — The Perceptron

## Exercises

1. **Implement a `Perceptron` class from scratch.** Build a class with `__init__(self, n_features, lr=0.1)`, `fit(self, X, y, epochs=100)`, and `predict(self, X)` methods. Use the step activation `ŷ = 1 if z ≥ 0 else 0`. Train it on the AND gate truth table (`X = [[0,0],[0,1],[1,0],[1,1]], y = [0,0,0,1]`) for 50 epochs. Print the learned weights, bias, and predictions for all four inputs.

2. **Trace and verify a single weight update by hand.** Given initial weights `w = [0.5, -0.3]`, bias `b = 0.1`, learning rate `η = 0.1`, and training example `x = [1, 0], y_true = 1`, compute the perceptron's output and the updated weights and bias using pencil and paper. Then write a standalone script that performs the same update programmatically and prints both the hand-computed values (as hardcoded literals) and the computed values side by side so you can confirm they match.

3. **Demonstrate the XOR failure case.** Construct the XOR dataset (`X = [[0,0],[0,1],[1,0],[1,1]], y = [0,1,1,0]`) and train your perceptron for 1000 epochs. Print the total number of misclassifications per 100-epoch window (e.g., epochs 0–99, 100–199, etc.). You should observe that the misclassification count never reaches zero. At the end, print each input with its predicted vs. true label and a one-line statement to `stdout` explaining why convergence is impossible (cite the geometric argument about linear separability).

4. **Compare convergence across learning rates.** Generate a linearly separable dataset of 200 2D points using `numpy.random` (two Gaussian clusters centered at `(2, 2)` and `(-2, -2)`). Train your perceptron three times with `lr = 0.001`, `lr = 0.1`, and `lr = 1.0`, setting a max of 500 epochs and early-stopping when training accuracy hits 100%. Print a formatted table showing each learning rate, the epoch count at convergence (or "did not converge" if it hits the cap), and the final misclassification count.

5. **Serialize trained weights and build an inference-only classifier.** Train your perceptron on a dataset of your choice (e.g., the linearly separable points from Exercise 4 or a new one). Write
