# Exercises — Group Chat and Speaker Selection

## Exercises

1. **Implement a round-robin group chat.** Create three agents — a summarizer, a critic, and a fact-checker — and wire them into a `GroupChat` with `selection_method="round_robin"` and `max_round=6`. Have a user proxy agent send a topic prompt (e.g., "Discuss whether cold outbound is dead"). Run the chat and print the full message history with each speaker's name. Verify that the three agents rotated in strict order and each spoke exactly twice.

2. **Configure termination by keyword and max rounds.** Set up a four-agent group chat using `selection_method="auto"`. Register a termination function that stops the chat when any message contains the token `"DONE"` and also set `max_round=10`. Run two conversations: one where an agent naturally says `"DONE"` around round 4, and one where no agent says it. Print the final round count for each run and confirm the keyword condition fired in the first case while the max-round condition fired in the second.

3. **Implement a custom speaker selection function.** Write a `speaker_selection_func(last_speaker, messages)` that inspects the most recent message text and routes to the next agent by keyword: `"enrich"` → DataAgent, `"draft"` → WriterAgent, `"review"` → EditorAgent, default → round-robin fallback. Register it on a `GroupChat` with those three agents plus a user proxy. Seed the conversation with a message containing `"enrich"`, then have the DataAgent's reply contain `"draft"`, and so on. Print which agent was selected at every turn alongside the keyword that triggered the routing decision.

4. **Compare routing accuracy, latency, and token cost across all three selection methods.** Build a script that runs the same three-agent task (e.g., research an ICP and produce a one-paragraph positioning statement) three times: once with `round_robin`, once with `auto`, and once with your custom function from Exercise 3. For each run, capture wall-clock time (use `time.perf_counter
