# Exercises — MCP Gateways and Registries â€” Enterprise Control Planes

## Exercises

1. **Implement a registry lookup.** Build a registry that stores metadata for three MCP servers: a Salesforce CRM server, a Clay enrichment server, and an Apollo outreach server. Store the server ID, endpoint URL, tool schema name, auth requirements, and a health flag for each. Accept a tool name as a command-line argument and print the resolved server endpoint, auth requirement, and health status. If the tool is not registered, print a not-found error. Verify by running `python registry.py clay.enrich` (should resolve) and `python registry.py nonexistent.tool` (should error).

2. **Compare registry, gateway, and router responsibilities.** Write a script that defines a list of at least eight control plane operations (e.g., "resolve tool name to endpoint", "authenticate developer API key", "round-robin across two server instances", "check if server is healthy", "enforce per-minute rate limit", "cache tool schema for 5 minutes", "rotate expired OAuth token", "route request to least-loaded backend"). Classify each as handled by the registry, the gateway, or the
