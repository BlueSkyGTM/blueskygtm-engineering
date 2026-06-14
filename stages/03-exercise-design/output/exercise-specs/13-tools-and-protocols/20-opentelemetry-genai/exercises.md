# Exercises — OpenTelemetry GenAI â€” Tracing Tool Calls End-to-End

## Exercises

1. **Implement** a Python script that creates a single LLM span with all five required GenAI semantic convention attributes (`gen_ai.system`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.response.finish_reason`). Export it via `ConsoleSpanExporter` and run the script. Confirm all five attribute keys appear in the terminal output.

2. **Build** a tool-execution span as a child of an LLM span. Set `gen_ai.tool.name`, `gen_ai.tool.arguments` (as a JSON string), and `gen_ai.tool.result`. Export via `ConsoleSpanExporter`. Verify in the terminal that the tool span's `parent_span_id` matches the LLM span's `span_id`.

3. **Implement** a custom `SpanProcessor` that intercepts on-end and redacts email addresses and phone numbers from any span attribute named `gen_ai.tool.arguments` before the span reaches the exporter. Test it by creating a tool-execution span whose arguments JSON contains a personal email and phone number. Export via `ConsoleSpanExporter` and confirm the redacted output appears in the terminal.

4. **Build** a four-level nested trace representing a real GTM workflow: an agent span wrapping an LLM span wrapping a tool span (simulating an Apollo People Search API call) wrapping an inner MCP-call span. Each span must carry the correct GenAI semantic convention attributes for its type. Export via `ConsoleSpanExporter` and verify that all four spans share the same `trace_id` and form a connected parent-child chain.

5. **Implement** a simulated multi-tool agent that calls three tools in sequence — Apollo company lookup, Clay email enrichment, and CRM contact creation. Program the Clay enrichment step to fail (set its `gen_ai.tool.result` to an error string and mark span status `ERROR`). Export the full trace, then write a diagnostic report in `outputs/skill-agent-trace-diagnosis.md` that identifies which tool span errored, quotes the error message from the attribute, and reports total input and output tokens consumed across all LLM spans in the trace.

6. **Design and implement** a tail-based sampling configuration that retains 100% of traces containing at least one span with `status = ERROR` and 10% of fully-successful traces. Run 20 simulated agent traces (at least 4 with errors) through your sampler and print a summary table showing: traces sampled, traces dropped, error-trace retention rate, and success-trace retention rate. Save the sampler implementation to `handlers/tail_sampling_strategy.py`.
