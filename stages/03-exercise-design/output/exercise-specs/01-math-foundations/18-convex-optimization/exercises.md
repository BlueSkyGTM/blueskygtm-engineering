# Exercises — Convex Optimization

## Exercises

1. **Implement** a convexity checker using SymPy. Given the single-variable functions f(x) = x⁴, f(x) = x³ − 2x, f(x) = −log(x), f(x) = e^(−x²), and f(x) = x·log(x), compute the second derivative symbolically and evaluate its sign at 50 evenly spaced points across each function's domain. Print a table showing each function, its f″(x) expression, the minimum value of f″ over the sampled points, and a verdict of "CONVEX" or "NOT CONVEX."

2. **Verify** convexity through Jensen's inequality without symbolic differentiation. For each of the following functions — (a) f(x) = exp(2x + 1), (b) f(x,y) = √(x² + y²), (c) f(x) = max(0, x)⁴, (d) f(x₁,x₂,x₃) = log(e^x₁ + e^x₂ + e^x₃) — sample 5000 random pairs of points, compute f(θx + (1−θ)y) and θf(x) + (1−θ)f(y) for a random θ ∈ [0,1], and report the maximum violation (f(θx + (1−θ)y) − θf(x) − (1−θ)f(y)). Print
