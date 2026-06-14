# Exercises — GloVe, FastText, and Subword Embeddings

## Exercises

1. **Build a word-word co-occurrence matrix from a small corpus.** Implement a function that takes a list of tokenized sentences and a window size, then constructs the symmetric co-occurrence matrix `X` where `X[i][j]` counts how many times word `j` appears within `window` tokens of word `i`. Run it on this corpus:

   ```python
   corpus = [
       "the sales team uses crm software daily",
       "the crm software tracks customer interactions",
       "sales reps log customer interactions in crm",
       "customer interactions drive sales pipeline growth",
       "crm software integrates with marketing automation tools"
   ]
   ```

   Use a window size of 2. Print the full matrix as a labeled DataFrame (rows and columns indexed by vocabulary words). Verify that the entry for `("crm", "software")` is at least 3 and that `("sales", "customer")` is non-zero.

2. **Implement character n-gram extraction with boundary markers.** Write a function `get_ngrams(word, min_n=3, max_n=6)` that takes a word, wraps it in `<` and `>`, then extracts all character n-grams of lengths `min_n` through `max_n` (inclusive). Call it on the words `"datadog"`, `"saas"`, and `"b2b"`. Print each word alongside its full n-gram set. Confirm that `"saas"` produces at least 6 n-grams and that the boundary marker n-gram `"<sa"` appears for `"saas"`.

3. **Factorize a co-occurrence matrix via truncated SVD to produce GloVe-style embeddings.** Using the matrix you built in Exercise 1 (or a larger corpus of 15–20 GTM sentences you write yourself), apply `sklearn.decomposition.TruncatedSVD` with 5 components to extract a dense embedding matrix. Write a function `nearest_neighbors(word, embeddings, vocab, k=3)` that returns the `k` most cosine-similar words to the input. Print the 3 nearest neighbors for `"sales"`, `"crm"`, and `"customer"`. Confirm that related words cluster together (e.g., `"pipeline"` or `"reps"` should appear near `"sales"`).

4. **Compare pre-trained GloVe and FastText on OOV company names and product terms.** Load pre-trained GloVe vectors (e.g., `glove-wiki-gigaword-100` via `gensim.downloader`) and pre-trained FastText vectors (`fasttext-wiki-news-subwords-300`). For each of the following tokens, attempt to retrieve the vector from both models and report whether it exists: `"snowflake"`, `"datadog"`, `"okta"`, `"intent"` `"data"`, `"hubspot"`, `"gong"`, `" Outreach"` (capitalize the first letter), `"saas"`, `"b2b"`. Print a table showing `[token | GloVe? | FastText?]` with Yes/No for each. Then, for tokens that FastText can embed but GloVe cannot, print the top-5 nearest neighbors under FastText. Explain in a comment which model handles domain-specific vocabulary better and why.

5. **Build a FastText-style OOV vector composer for company names and write it as a reusable handler.** Download the pre-trained FastText model from Exercise 4. Implement a function `compose_oov_vector(token, ft_model, min_n=3, max_n=6)` that extracts character n-grams from the token (with `<`/`>` boundary markers), retrieves the vector for each n-gram from the FastText model's internal n-gram hash table (use the `_wv.vectors_ngrams` attribute or `ft_model.wv.word_vec` on subword tokens), and averages them to produce the OOV vector. Test it on 10 company names pulled from a live Apollo or Clay export (or from `signals/data/companies.csv` if you have one). For each company name, print the composed vector's top-5 nearest in-vocabulary neighbors from the FastText model. Save the function as a importable module at `handlers/oov_embedder.py`.

6. **Design and run a head-to-head evaluation of GloVe vs. FastText on a GTM similarity benchmark.** Build a benchmark file with 15 word-pair similarity judgments relevant to GTM (e.g., `("salesforce", "crm", 0.9)`, `("datadog", "monitoring", 0.8)`, `("clay", "enrichment", 0.7)`, `("gong", "call_recording", 0.85)` — include at least 5 pairs where one token is OOV for GloVe). Compute cosine similarity for each pair under both GloVe and FastText (using your OOV composer from Exercise 5 for FastText). Calculate Spearman rank correlation between predicted similarities and your human labels for each model. Print a summary table and write a 150-word analysis to `outputs/skill-embedding-eval.md` explaining which model wins, on which subset of pairs, and what the result implies for embedding choice in a GTM pipeline.
