# Exercises — Collective Ops From Scratch

## Exercises

1. Implement `broadcast(root_data, n)` and `scatter(root_chunks, n)` as pure Python functions using only lists and loops. `broadcast` returns a list of `n` identical copies of `root_data`. `scatter` returns a list where worker `i` receives `root_chunks[i]`. Test with `root_data = {"campaign": "Q4_outbound"}` and `root_chunks = ["acme.com", "globex.com", "initech.com"]` across `n=4` workers (pad scatter output for the extra worker with `None`). Print the output list and verify every worker entry is visible in the terminal.

2. Implement `gather(worker_chunks)` and `reduce(worker_chunks, op)` where `op` is a callable like `sum` or `max`. `gather` concatenates all chunks into one ordered list. `reduce` applies `op` across all chunks and returns the single scalar. Test with `worker_chunks = [10, 25, 7, 42]` for both `sum` and `max`. Print both results — your terminal should show `84` and `42` respectively.

3. Implement all-reduce two ways and compare their message complexity. Write `all_reduce_naive(worker_values)` that gathers all values to a simulated root, computes the sum, then broadcasts it back to every worker. Then write `all_reduce_ring(worker_values)` that implements a ring-pattern reduce-scatter followed by a ring all-gather, where each worker sends exactly one element per step to its neighbor. Instrument both functions with a global transfer counter that increments every time an element moves between workers. Run both with `worker_values = list(range(1, 9))` and print the per-worker transfer count for each implementation. The ring version should show a lower count.

4. Below is a buggy `all_gather` implementation. It should produce every worker holding the full concatenated list `[10, 20, 30, 40]`, but worker 2 currently outputs `[10, 20, 0, 40]`:

   ```python
   def all_gather_buggy(worker_values):
       n = len(worker_values)
       result = [None] * n
       for i in range(n):
           result[i] = worker_values[i]
       return result  # every worker gets this same list
   ```

   Trace the intermediate partition state by adding print statements that show `result` after each loop iteration. Identify the bug (the function returns the accumulation buffer, not a copy per worker), fix it so that each worker receives `[10, 20, 30, 40]`, and print all four worker outputs to confirm.

5. A GTM team wants to enrich 500 companies pulled from Apollo across 4 parallel enrichment workers. Each worker runs a Clay enrichment webhook on its assigned slice, then results are merged. Build this as an explicit collective-op pipeline in `signals/examples/gtm_collective.py`: (a) `scatter` the 500-company list into 4 chunks, (b) simulate enrichment by calling a `mock_enrich(company)` function on each chunk that returns a dict with `company`, `employees`, `tech_stack`, (c) `gather` all enriched dicts into one ordered list, (d) `reduce` to compute total addressable market by summing `employees` across all results. Run the script and print the scattered chunk sizes, the gathered record count, and the final reduced TAM total. Artifacts land in `signals/examples/gtm_collective.py`.

6. Implement `reduce_scatter(worker_vectors, op)` and `all_gather(worker_values)` from scratch. `reduce_scatter` takes a list where each worker holds a vector of length `N` and produces a list where worker `i` holds the reduced result of the `i`-th element across all workers. `all_gather` takes one value per worker and produces the full list at every worker. Then compose these two to build `all_reduce_via_rs_ag(worker_vectors)` and verify it produces the same per-worker output as your naive all-reduce from Exercise 3. Finally, write a docstring that proves ring all-reduce sends `2(N−1)` messages per worker by arguing from the reduce-scatter phase (`N−1` sends) plus the all-gather phase (`N−1` sends). Print the proof as formatted output when the script runs with `--proof`. Artifacts land in `handlers/ring_allreduce.py`.
