# Exercises — ZeRO Optimizer State Sharding

## Exercises

1. **Compute per-GPU optimizer memory for vanilla DDP and ZeRO Stages 1–3.** Write a Python script that accepts `--model-size` (in billions of parameters) and `--num-gpus` as CLI arguments. Assume FP16 parameters (2 bytes each) and Adam optimizer with FP32 master weights, first moment, and second moment (12 bytes per parameter of optimizer state). Print a table showing per-GPU optimizer-state memory for vanilla DDP and each ZeRO stage. Run it for a 7B model on 8 GPUs and confirm ZeRO Stage 1 divides the optimizer state by the GPU count while vanilla DDP replicates it fully.

2. **Derive and verify communication volume ratios for each ZeRO stage.** Write a Python script that takes a model size (in parameters) and prints the per-step communication volume in bytes for: vanilla DDP all-reduce, ZeRO Stage 1 (reduce-scatter + all-gather), ZeRO Stage 2, and ZeRO Stage 3. Compute and print the ratio of each stage's volume to vanilla DDP. Confirm Stages 1 and 2 come out to 1.0× and Stage 3
