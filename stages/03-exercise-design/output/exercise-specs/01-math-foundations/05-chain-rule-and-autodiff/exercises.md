# Exercises — Chain Rule & Automatic Differentiation

## Exercises

1. **Implement a scalar-valued autograd engine.** Build a `Scalar` class in pure Python that records every operation (add, mul, pow, relu) into a computation graph during the forward pass and computes gradients via topological-sort reverse-mode autodiff when `backward()` is called. Construct the function `f(x) = (x² + 3) · x`, run a forward pass at `x = 2.0`, call `backward()`, and print `x.grad`. Confirm the value equals the analytical derivative `3x² + 3 = 15.0`.

2. **Compare numerical, symbolic, and automatic differentiation on the same function.** For `f(x) = sin(x²) + exp(−x)` at `x = 1.5`, compute `df/dx` three ways: central-difference numerical approximation (h = 1e-7), symbolic derivative via `sympy.diff`, and your autograd engine from Exercise 1 (or PyT
