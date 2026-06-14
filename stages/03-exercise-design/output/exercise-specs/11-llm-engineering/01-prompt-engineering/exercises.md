# Exercises — Prompt Engineering: Techniques & Patterns

## Exercises

1. Implement three prompt variants — zero-shot, few-shot, and chain-of-thought — that each classify a sales lead's company description into one of three tiers: "Enterprise", "Mid-Market", or "SMB". Run all three variants against the same set of 5 company descriptions and print each variant's raw output side by side. Your terminal output should make visible differences in consistency and format across the three approaches.

2. Compute the token cost for each prompt variant from Exercise 1 across a hypothetical batch of 2,500 leads. Estimate input token counts by counting words in your prompt template plus an average lead description, and output token counts from the model's actual responses. Print a cost table showing: prompt variant, estimated input tokens per call, estimated output tokens per call, total batch cost at $0.005/1K input and $0.015/1K output
