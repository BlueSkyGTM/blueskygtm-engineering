# Exercises — Tool Schema Design â€” Naming, Descriptions, Parameter Constraints

## Exercises

1. **Implement** five tool function definitions (as Python dicts) for a sales prospecting registry. Each must use a verb-noun name and include a description with three elements: (a) when the LLM should trigger this tool, (b) what inputs it expects, (c) the shape of its return value. Required tools: look up a company by domain, search contacts by job title, send a Slack notification, add a lead to a CRM, and check email verification status. Add a sixth tool with a deliberately ambiguous name such as `handle_data` — print it alongside the other five with a marker flag indicating it violates the verb-noun convention. Terminal output should show all six entries with a `VALID` or `INVALID NAME` tag on each.

2. **Define** a JSON Schema (as a Python dict) for two tool parameters: `email` (string, must match a basic email regex pattern) and `page` (integer, minimum 1, maximum 100). Validate three sample inputs against these constraints — use the `jsonschema` library (`pip install jsonschema`). Sample inputs: `{"email": "jane@acme.com", "page": 5}`, `{"email": "not-an-email", "page": 3}`, `{"email": "bob@x.io", "page": 0}`. Print `PASS` or `FAIL` with the specific constraint that was violated for each input.

3. **Apply** schema design principles to a different domain — a customer support ticketing system. Design three tool schemas (name + description + JSON Schema parameter constraints) for these actions: create a ticket, assign a ticket to an agent, and close a ticket. Use `enum` for priority levels
