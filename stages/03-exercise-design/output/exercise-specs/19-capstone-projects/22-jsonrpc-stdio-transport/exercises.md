# Exercises — JSON-RPC 2.0 Over Newline-Delimited Stdio

## Exercises

1. **Implement a minimal JSON-RPC 2.0 responder** that reads newline-delimited JSON objects from `stdin`, handles a single method `"ping"` (returns `{"jsonrpc": "2.0", "id": <echoed-id>, "result": "pong"}`), and writes each response followed
