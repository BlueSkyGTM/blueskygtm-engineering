# Exercises — Capstone 01 â€” Terminal-Native Coding Agent

## Exercises

1. **Implement a minimal ReAct loop** with a single tool — `list_directory` — that takes a path argument and returns the entries. Give the model a task like "list the files in the current directory and summarize what you see." Run the loop, print each phase (reason, act, observe) to the terminal, and confirm the agent terminates after one tool call. Verify: terminal output shows one tool invocation followed by a final answer.

2. **Configure two tool schemas** — `read_file` and `count_lines` — each with a JSON Schema requiring a `path` string. Run the agent on the task "read `README.md` and tell me how many lines it has." Print the ordered list of tool calls the agent made. Verify: both tools are invoked and `count_lines` runs after `read_file`.

3. **Build error recovery into the loop.** Intentionally implement `read_file` so it raises a `FileNotFoundError` when given a relative path. Run the agent on "read the file `config.yaml`." The agent must receive the exception message as an observation, retry with an absolute path or a different filename, and produce a final answer. Verify: terminal output shows the failed call, the error string fed back as an observation, and a recovery step.

4. **Implement structured JSONL logging** in the loop. Each line must contain `step`, `thought`, `tool_call`, `tool_input`, and `observation`. Run the agent on a multi-step task (e.g., "list the directory, find the largest Python file, read it, count its functions"). Then write a separate script that reads the JSONL file and prints the step index and tool name for each call. Verify: the trace script outputs 3+ lines and the last step has no tool call (signaling termination).

5. **Build a GTM enrichment agent.** Define tools that call a real enrichment API — Apollo People Search or Companies API — and a `write_to_csv` tool. Give the agent the task: "Find 5 engineers at Series B SaaS companies in the data infrastructure space and export them to a CSV." The loop must call the enrichment API, parse the results, and write the file. Produce the agent module at `handlers/gtm_react_agent.py` and verify by running it and checking that `outputs/gtm_enrichment.csv` is created with 5 rows.

6. **Design a comparison artifact** that maps the ReAct loop to a Clay or Apollo enrichment workflow. Write a script that runs the agent from Exercise 5 on a 10-company list, then runs the same enrichment through a Clay-style column-based pipeline (plan → enrich → export as batch), and prints a side-by-side table of step count, total latency, error count, and recovered errors for each approach. Write the comparison module to `signals/examples/react_vs_enrichment.py` and verify the printed table shows both approaches completing the same task with measurable differences.
