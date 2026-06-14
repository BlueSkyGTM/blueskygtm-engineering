# Exercises — Tokenized Dataset with Sliding Window

## Exercises

1. Load the file `data/corpus.txt` (a raw text corpus), encode it with your tokenizer's batch encode method, and produce a 1D tensor of token IDs. Print the total number of tokens and the first 20 token IDs in the tensor. Confirm the tensor is rank-1 before moving on.

2. Implement a `Dataset` class that accepts a 1D token-ID tensor, a `context_length`, and a `stride` equal to `context_length`. Print the first 3 `(input, target)` pairs as integer lists and verify that `target` equals `input[1:]` shifted by one position for each pair.

3. Write a function `count_windows(total_tokens, context_length, stride)` that returns the number of training examples produced by a given triple. Assert that the final target index `<= total_tokens - 1` for every configuration. Call the function with these five triples and print results side by side: `(1000, 32, 32)`, `(1000, 32, 16)`, `(1000, 32, 1)`, `(500, 64, 32)`, `(500, 64, 8)`. Raise a `ValueError` if any configuration is invalid.

4. Apply the sliding-window dataset to a real GTM dataset: load `data/apollo_company_descriptions.csv` (a column of company "short_description" strings from an Apollo export), concatenate all descriptions into a single text blob, tokenize it, and build two datasets — one with `stride == context_length` and one with `stride == 1`. Print the example count and estimated bytes-per-example for each. Report the overlap ratio (shared tokens between consecutive windows divided by `context_length`) for the first 5 window transitions in the `stride == 1` dataset.

5. Build a complete data pipeline in `handlers/transcript_dataset.py` that loads `data/crm_call_transcripts.json` (a JSON array of `{ transcript, deal_stage }` objects exported from a CRM), concatenates the `transcript` fields into one text corpus, tokenizes it, wraps it in your sliding-window `Dataset` with `context_length=128` and `stride=64`, and wraps that in a `DataLoader` with `batch_size=8`. Instantiate the DataLoader, fetch one batch, and print `inputs.shape` and `targets.shape`. Iterate the full DataLoader and print the total number of batches yielded. The artifact must be importable: `from handlers.transcript_dataset import build_dataloader`.

6. Design and run an experiment that answers the following question: *for a fixed corpus of 50 000 tokens, which `(stride, batch_size)` combination maximizes unique-token coverage per epoch while keeping wall-clock epoch time under 2 seconds?* Tokenize `data/corpus.txt`, sweep over `stride ∈ [8, 16, 32, 64, 128]` and `batch_size ∈ [4, 8, 16, 32]`, time a single epoch for each combination using `time.perf_counter`, and write the results table — sorted by coverage-per-second descending — to `outputs/skill-sliding-window-sweep.md`. Include a one-paragraph conclusion identifying the winning configuration and the trade-off it represents.
