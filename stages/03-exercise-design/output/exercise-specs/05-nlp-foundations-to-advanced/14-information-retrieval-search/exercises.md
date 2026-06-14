# Exercises — Information Retrieval and Search

## Exercises

1. **Implement BM25 scoring from scratch** on a corpus of 10 short product descriptions (no `rank_bm25` or `scikit-learn` — write the formula yourself: IDF, term frequency saturation, and document length normalization). Accept a query string from a command-line argument, compute the BM25 score for every document, and print results sorted by score in descending order. Verify your output by confirming that a document containing all query terms outranks one containing a single query term. Use `k1=1.5` and `b=0.75`.

2. **Compute cosine similarity by hand** on a 3-document corpus with manually assigned 4-dimensional embedding vectors. Pick a query embedding, implement the dot-product and L2-norm calculations yourself (no library vector ops), and print each document's cosine similarity score alongside its BM25 score (reuse your Exercise 1 scorer). Identify and print which document(s) the two methods rank differently, and state in a printed summary line which method favors short keyword-heavy documents versus long semantically related ones.

3. **Implement reciprocal rank fusion from scratch.** Given two ranked lists — one from your BM25 scorer and one from a dense cosine-similarity scorer — fuse them using the RRF formula `score(d) = Σ 1/(k + rank_i(d))`. Build a 15-document corpus of B2B SaaS company descriptions (write them yourself). For the query `"customer data enrichment platform"`, print three fused rankings side by side: `k=1`, `k=10`, and `k=60`. In
