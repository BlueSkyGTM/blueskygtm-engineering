# Exercises — RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance

## Exercises

1. Implement precision@k and recall@k in a Python script. Create a dictionary `qrels` mapping each query ID to a set of relevant document IDs, and a dictionary `retrieved` mapping each query ID to an ordered list of retrieved document IDs. For k=3 and k=5, compute precision@k and recall@k for every query and print a table showing query ID, metric name, and value. Confirm that a query where two of five retrieved docs are relevant yields precision@5 = 0.40.

2. Implement MRR@10 using the same `qrels` and `retrieved` fixtures from Exercise 1. For each query, find the rank position of the first relevant document (1-indexed) and compute the reciprocal (1/rank). If no relevant document appears in the top 10, score 0 for that query. Print MRR per query and the mean across all queries. Add one query where no relevant document appears in the results and confirm the mean drops accordingly.

3. Build a qrels fixture file named `signals/examples/gtm_qrels.json` containing five GTM-related queries (e.g., "What does Acme Corp sell?", "Who is the decision-maker at Globex?"), gold document IDs for each query, and a gold answer string per query. The file must be valid JSON loadable by `json.load` with no external dependencies. Then write a separate script that loads the fixture and computes nDCG@5 for each query using graded relevance (gold doc = relevance 3, partially relevant doc = 1, irrelevant = 0). Print per-query nDCG and the mean.

4. Implement a faithfulness checker that takes a generated answer and a retrieved context string, decomposes the answer into atomic claims by splitting on sentence boundaries and stripping conjunctions,
