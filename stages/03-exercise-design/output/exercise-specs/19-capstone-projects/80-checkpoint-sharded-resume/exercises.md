# Exercises — Sharded Checkpoint and Atomic Resume

## Exercises

1. **Implement a sharded checkpoint writer.** Simulate a 4-rank distributed job where each rank writes a file `rank_{r}_shard.pt` containing a random tensor sized `rank * 1000` elements. After all shards are written, rank 0 writes `manifest.json` recording each shard filename, its byte size on disk, the global step (passed as a CLI argument), and the world size. Run the script, then print the manifest JSON and a directory listing showing all files exist. Verify each shard's actual byte size matches what the manifest claims.

2. **Apply the atomic write pattern.** Write a function `atomic_checkpoint(ckpt_dir, world_size, step)` that writes all shards into a temp directory named `ckpt_dir.tmp`, then atomically renames it to `ckpt_dir` only after every shard and manifest are confirmed present. Simulate a mid-write crash by injecting an exception after the second shard. Run both the normal case and the crash case, printing the directory state after each. Confirm that a crash leaves no partial `ckpt_dir` on disk.

3. **Build a resume validator that detects three failure modes.** Implement `verify_checkpoint(ckpt_dir, expected_world_size)` that returns a list of human-readable error strings. Check for: (a) missing `manifest.json`, (b) any shard whose actual file size differs from the manifest's recorded byte size, (c) a world-size mismatch between the manifest and `expected_world_size`. Manually create three corrupted checkpoint directories — one per failure mode — and run the validator on each, printing the detected errors. An empty error list for a valid checkpoint must also be demonstrated.

4. **Compare gather-then-write against parallel sharded checkpointing.** Implement both strategies using `concurrent.futures.ThreadPoolExecutor`. In gather-then-write, a single writer collects all shard data via a shared queue, then writes sequentially. In parallel sharded, each "rank" writes its own 10 MB shard concurrently. Benchmark both at world sizes 1, 2, 4, 8, and 16. Print a table with columns: world size, gather wall-time, sharded wall-time, gather bandwidth (MB/s), sharded bandwidth (MB/s).
