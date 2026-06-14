# Exercises — The Agent Loop: Observe, Think, Act

## Exercises

1. **Implement** a minimal observe-think-act loop in under 60 lines of Python. Your loop must include a `tool_registry` dictionary with at least two callable tools (e.g., `search(query)` returning a fake string, `calculate(expression)` returning a numeric result), a `state` dict that accumulates observations, and a `max_iterations` termination guard set to 5. Use a simple rules-based "think" function (no LLM call required) that picks a tool based on keywords in the user query. Print the iteration number, phase name, tool invoked, and tool result to the terminal on each cycle. Run the loop against the query *"What is 23 times 47?"* and confirm it terminates and prints the correct product.

2. **Trace** state mutation across iterations by building a replay function. Hardcode a list of five `(phase, payload)` tuples representing a completed agent run (e.g., observe user message, think decide-search, act search-result, think decide-calc, act calc-result). Write a function that folds these events into a state dictionary and prints the state after each event. Manually predict the final state before running, then verify your prediction matches the program output.

3. **Compare** single-shot prompting against agent-loop execution for a task that requires two tool calls: *"Find the founding year of Acme Corp, then compute how many years ago that was."* Implement both approaches: (a) a single LLM call with all context stuffed into one prompt, and (b) an agent loop that calls a `search` tool then a `calculate` tool across two iterations. Log total input tokens, output tokens, and iteration count for each approach. Print a side-by-side comparison table to the terminal. Use any local or API LLM; if no API key is available, simulate token counts with a `len(prompt.split())` heuristic and document that substitution in a comment.

4. **Diagnose** an infinite-loop failure. Below is a trace from an agent that enriches leads from an Apollo-style contacts API:

   ```
   Iter 1 | think: call enrich_email(domain=acme.com)
   Iter 1 | act:  returned email=info@acme.com
   Iter 2 | think: call enrich_email(domain=acme.com)
   Iter 2 | act:  returned email=info@acme.com
   Iter 3 | think: call enrich_email(domain=acme.com)
   ...
   ```

   The agent never terminates. Identify which guard is missing — a deduplication check on prior tool results, a max-iterations cap, or a "done" signal in the think output. Write a corrected version of the loop dispatcher that includes the missing guard and demonstrate termination by replaying the trace through your fixed dispatcher. Print the iteration at which the loop now stops.

5. **Build** a GTM enrichment agent that discovers tools from a registry and dispatches them inside an observe-think-act loop. Your registry must include at least three tools: `lookup_company(domain)` returning a fake company record, `find_contacts(company_id)` returning a list of contact dicts, and `score_lead(contact)` returning a numeric score. Seed the agent with a list of three real company domains (e.g., `stripe.com`, `notion.so`, `linear.app`). The loop must iterate until all three companies are enriched and scored, then terminate. Write the result as a JSON array to `outputs/skill-gtm-enrichment-agent.json` and print a summary table (company, contact count, top score) to the terminal. Save your implementation to `handlers/gtm_enrichment_agent.py`.

6. **Design** a termination strategy specification for budget-aware agent loops. Write a Markdown document that defines three termination conditions beyond `max_iterations`: (1) a token-budget ceiling, (2) a cost ceiling in USD given per-model pricing, and (3) a semantic "task complete" signal parsed from model output. For each condition, specify the data the observe phase must collect, where the check lives in the loop, and one failure mode if the check is omitted. Include a pseudocode snippet for the combined termination function. Save the document to `outputs/skill-termination-strategy.md`.
