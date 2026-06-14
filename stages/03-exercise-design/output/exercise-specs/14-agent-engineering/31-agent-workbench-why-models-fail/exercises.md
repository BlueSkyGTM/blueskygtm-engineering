# Exercises — Agent Workbench Engineering: Why Capable Models Still Fail

## Exercises

1. **Trace** the four failure modes through a simulated agent run. Write a Python script that models a 10-step agent loop where each step logs its action, tool call, observation, and total token count. Inject one instance of each failure mode (context collapse, schema drift, plan abandonment, silent failure propagation) at specific steps. Run the script and print a structured log showing every step. Then, in the same script, print your diagnosis: for each failure mode, state which step it occurred on, what observable symptom gave it away, and the mechanism behind it.

2. **Implement** a schema validator that detects schema drift in real time. Write a function that takes a JSON object and a schema (field names, expected types, required flags) and returns a pass/fail verdict with a list of specific violations. Create five sample LLM tool-call outputs — two valid, three with drift (wrong type, missing required field, extra unexpected field). Run all five through your validator and print each result on its own line with the field-level error details.

3. **Compute** token-accumulation patterns across a multi-step agent run. Write a script that simulates a 15-step agent loop, assigning realistic token costs to each component (system prompt, tool definitions, tool calls, observations). At each step, print a row showing step number, tokens added this step, cumulative total, and a flag indicating whether the running total has crossed a 4,000-token compaction threshold. After the loop completes, print the step number where instruction fidelity is most at risk and explain in one printed sentence why that threshold is the danger zone.

4. **Apply** failure detection to a GTM enrichment workflow. Build a script that fetches prospect data from the Apollo person-search
