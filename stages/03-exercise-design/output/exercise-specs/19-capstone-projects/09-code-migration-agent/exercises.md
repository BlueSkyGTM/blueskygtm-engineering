# Exercises — Capstone 09 â€” Code Migration Agent (Repo-Level Language / Runtime Upgrade)

## Exercises

1. **Implement a minimal four-phase migration loop on a single file.** Create a Python 3.8 source file containing `from collections import Mapping` and a trivial class that subclasses `Mapping`. Write a script that executes the four phases — parse the file with `libcst`, transform the import, verify the result compiles via `compile()`, and commit by writing the new file to disk. Print the phase name and a one-line status message as each phase completes.

2. **Implement the `collections.Mapping` → `collections.abc.Mapping` deterministic transformation rule.** Write a `libcst` `Transformer` subclass that matches `ImportFrom` nodes where `module` is `collections` and the imported name is `Mapping`, then rewrites it to import from `collections.abc`. Run your transformer against three sample files (each containing the deprecated import) and print the matched-node count per file.

3. **Compute leaf-first migration ordering from a dependency graph.** Given five Python files where `a.py` imports from `b.py`, `b.py` imports from `c.py` and `d.py`, and `e.py` imports from `a.py`, write a script that builds the import dependency graph and emits a topological ordering suitable for leaf-first migration. Print the resulting file order, one per line.

4. **Apply deterministic transformation to a CRM enrichment script.** A CRM sync script (used in an Apollo-driven outbound workflow) uses `datetime.utcnow()` to timestamp every contact-touch event. Implement the `datetime.utcnow()` → `datetime.now(timezone.utc)` rewrite as a `libcst` transformer. Run it against the script file and verify the transformed output imports cleanly by executing `python -c "import <module>"` from the terminal. Print the import check result.

5. **Build the complete deterministic migration agent.** Implement a four-phase agent (parse → transform → verify → commit) that runs all deterministic rules — `collections.Mapping`, `datetime.utcnow()`, and f-string conversion — across a five-file test repository. The agent must enforce strict rule precedence, print per-file transformation counts, and gate the commit phase on a test-suite run (`pytest`). Save the agent to `handlers/migration_agent_deterministic.py`. Terminal output must show the final pass/fail gate status for each file.

6. **Extend the agent with an LLM-assisted rule and compare pass rates.** Add a hybrid transformation rule for an ambiguous migration case (e.g., converting `imp` module usage to `importlib` where the source call doesn't map 1:1, or choosing between f-string formatting variants). Run both the deterministic-only agent and the hybrid agent against the same five-file repository. Capture per-file transformation counts, test-gate pass rates, and any LLM-rule activations. Write the comparison to `outputs/skill-migration-report.md` as a markdown table. Print the report path to the terminal.
