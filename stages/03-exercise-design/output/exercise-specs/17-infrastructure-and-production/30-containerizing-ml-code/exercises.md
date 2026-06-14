# Exercises — Containerizing ML Code

## Exercises

1. **Build** a Docker image from `python:3.11-slim` that runs an inference script which loads a simple logistic-regression model trained on sample lead-score data and prints predictions for three hardcoded test inputs. Run the container twice and verify the printed predictions are byte-for-byte identical across both runs.

2. **Configure** a `.dockerignore` file in the same project directory that excludes `*.pkl`, `*.pt`, `data/`, `.venv/`, `__pycache__/`, and `.git/`. Rebuild the image with `docker build --progress=plain .` and compare the "transferred context" size that Docker reports before and after the `.dockerignore` was added. Print both numbers.

3. **Reorder** the Dockerfile from Exercise 1 so that `RUN pip install` executes before any `COPY` of application source. Modify the inference script (add a print statement), rebuild, and observe which layers Docker pulls from cache versus rebuilds. Run `time docker build` on both the old ordering and the new ordering and report the rebuild-time difference.

4. **Construct** a multi-stage Dockerfile for the same inference script. The first stage (`builder`) installs `gcc`, `build-essential`, and compiles all Python wheel dependencies. The second stage (`runtime`) uses `python:3.11-slim` and copies only the installed site-packages and application code. Compare the final image size against the single-stage image from Exercise 1 using `
