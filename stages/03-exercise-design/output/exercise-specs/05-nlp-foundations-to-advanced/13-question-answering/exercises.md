# Exercises — Question Answering Systems

## Exercises

1. **Trace a query failure through the four-stage QA pipeline.** You are given six pre-recorded pipeline traces in `data/qa_traces.jsonl`, each containing the input and output of every stage (chunk, embed, retrieve, generate) for a query that produced a wrong answer. Write a script that loads each trace, inspects the stage inputs and outputs, determines which stage introduced the failure, and prints the diagnosis as `[trace_id] STAGE: reason`. Run the script and confirm it outputs a verdict for all six traces.

2. **Build a minimal retrieval-augmented QA system.** Using the five short markdown files in `data/docs/` (each describes a product feature in 2–3 paragraphs), implement the full pipeline from scratch: chunk each file by paragraph, embed each chunk with a sentence-transformer model, store embeddings in a
