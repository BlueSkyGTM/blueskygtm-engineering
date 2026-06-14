# Exercises — Plan-Execute Control Flow

## Exercises

1. Implement a planner function that accepts a goal string and returns a JSON array of step objects (each with `tool`, `args`, and `expected_outcome`). Implement an executor that iterates through the steps sequentially, dispatches each to a named tool in a mock tool registry (include at least three mock tools such as `search`, `fetch`, `format`), and prints each step's index, tool name, and result status to the terminal. Run it and confirm you see ordered execution output for every step.

2. Extend your executor so it detects when a tool returns a failure result (e.g., `{"status": "error", "message": "..."}`) and prints a structured failure line showing step index, tool name, expected outcome, and error message. Include at least one mock tool that always fails and one that fails conditionally. No re-planning yet — the executor should mark the step failed and continue to the next step. Verify the failure lines appear in terminal output alongside successful steps.

3. Implement the three failure dispatch paths — `abort`, `skip`, and `re-plan` — as a decision function that takes a failure result plus a failure-type label (e.g., `fatal`, `transient`, `missing_data`) and returns the chosen path. Wire it into your executor so that abort stops the entire run, skip continues to the next step, and re-plan calls the planner again with the accumulated error context appended to the goal. Test all three paths by injecting different failure types and print which dispatch path was selected at each failure point.

4. Add hard ceiling enforcement to your plan-execute agent: a maximum step count (e.g., 8) and a maximum re-plan count (e.g., 3). If either ceiling is exceeded, the executor must abort and print a budget-exceeded message identifying which ceiling was breached, how many steps or re-plans were consumed, and the last completed step. Design a scenario — for example, an Apollo company-search tool that returns partial results, triggering repeated re-plans — and verify the ceiling halts execution before costs spiral.

5. Build a complete plan-execute agent for a GTM enrichment workflow. The planner generates steps to enrich a list of target companies using mock Apollo person-search calls, mock Clay data enrichment, and a mock CRM-write step. The executor runs the plan with abort/skip/re-plan dispatch and step/re-plan budget enforcement. Write the full run report — original plan, step-by-step execution trace, every failure with its dispatch decision, and final enriched records — to `outputs/skill-plan-execute-gtm.md`.

6. Implement both a plan-execute agent and a simplified ReAct loop for the same goal (e.g., "find three companies matching an ICP and draft outreach"). Run both agents on at least two test goals, then produce a comparison document at `outputs/skill-plan-vs-react
