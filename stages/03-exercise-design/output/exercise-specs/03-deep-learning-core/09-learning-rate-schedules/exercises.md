# Exercises — Learning Rate Schedules and Warmup

## Exercises

1. **Implement all five schedule functions as plain Python.** Each function takes `step` (int) plus any needed hyperparameters and returns a single float. Write `constant`, `step_decay`, `cosine_annealing`, `warmup_cosine`, and `onecycle`. Then print a formatted table showing the learning rate each schedule produces at steps `[0, 50, 100, 500, 1000, 5000]` with `total_steps=10000`, `peak_lr=1e-3`, `warmup_steps=100`, `min_lr=1e-5`. The table should be human-readable in the terminal.

2. **Diagnose failure modes from loss curves.** Three Python lists of loss values (each 200 elements long) are stored in a file you create: one shows divergence (loss explodes after step ~30), one shows stalling (loss plateaus at a high value and never descends), one shows oscillation (loss bounces up and down without converging). Write a function that takes a list of losses and returns a string classification — `"divergence"`, `"stalling"`, `"oscillation"`, or `"healthy"`. Use heuristics such as: monotonic increase, variance of the last N values below a threshold, or sign-change frequency. Print the classification for all three arrays.

3. **Compare all five schedules on the same synthetic optimization task.** Define `f(x) = (x - 3.5)² + 0.5` and minimize it via vanilla gradient descent starting from `x = -5.0`. Run 2000 steps with each of the five schedules (use `peak_lr = 0.1`, `warmup_steps = 50`, `min_lr = 1e-4`). Print a ranked table showing final loss and `x` value for each schedule, best to worst.

4. **Wire a schedule config dict into a live PyTorch training loop.** Train a small MLP (2 hidden layers, 64 units each) on `sklearn.datasets.make_classification` (1000 samples, 20 features, 2 classes). Accept a config dict like `{"schedule": "warmup_cosine", "peak_lr": 1e-3, "warmup_steps": 50, "total_steps": 1000, "min_lr": 1e-5}`. Your loop must look up the schedule function by name from a registry, call it each step to get the LR, set `optimizer.param_groups[0]['lr']`, and print `step | lr | loss` every 100 steps. Run the loop twice — once with `"constant"` and once with `"warmup_cosine"` — and compare
