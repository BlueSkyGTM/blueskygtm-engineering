# Exercises — Checkpoint Save and Resume

## Exercises

1. **Implement an atomic checkpoint save.** Write a function `save_checkpoint_atomic(path, state_dict)` that serializes a PyTorch checkpoint dict to a temporary file (e.g., `path + ".tmp"`), then uses `
