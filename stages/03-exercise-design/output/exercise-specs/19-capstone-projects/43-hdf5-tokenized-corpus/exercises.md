# Exercises — HDF5 Tokenized Corpus

## Exercises

1. **Build** an HDF5 file at `outputs/corpus.h5` containing two datasets: a flat `uint32` array of concatenated token IDs and a `uint64` array of document boundary offsets (one entry per document, storing the starting token position). Tokenize the 20 text files in `data/raw_docs/` using the GPT-2 tokenizer. Print the total token count, document count, and file size on disk.

2. **Configure** chunk sizes of `[1024, 4096, 16384, 65536]` and compression filters `[None, "gzip", "lzf"]` on the same token array. For each combination, write a separate HDF5 file and measure (a) file size in bytes and (b) median latency of 100 random 512-token reads. Print a table of results to the terminal.

3. **Implement** a function `get_span(h5_path, start, length)` that reads `length` tokens beginning at position `start` from the flat token array, then uses the boundary index to return both the token IDs and the list of source document indices those tokens span. Verify your function by printing the decoded text and document IDs for the span `[50000:50050]`.

4. **Compare** training-loop throughput between two storage layouts for the same corpus: (a) a single flat concatenated dataset and (b) a per-document group structure where each document gets its own dataset under `/docs/`. Write a benchmark that simulates 1000 random batch fetches of 8 × 512-token sequences from each layout. Print samples/sec for both and the ratio between them.

5. **Build** a reusable HDF5 corpus builder at `handlers/hdf5_corpus_builder.py` that accepts a directory of Apollo-exported prospect CSV files, concatenates the `person_bio` and `company_description` columns into per-row text, tokenizes them, and writes an HDF5 file with flat token storage, a document boundary index, and an auxiliary `source_row` dataset mapping each document to its original CSV row. Include chunk size and compression as CLI flags. Run it on `data/apollo_export/` and print a summary of total tokens, documents, file size, and config used.

6. **Design** a validation routine that loads any HDF5 corpus following your builder's schema and verifies three invariants: (a) every document boundary offset is within the token array bounds, (b) no two documents share overlapping token ranges, and (c) the `source_row` dataset length matches the boundary index length. Run it against the file produced in Exercise 5 and print `PASS` or the first violating invariant with details.
