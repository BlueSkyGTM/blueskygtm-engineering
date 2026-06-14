# Exercises — Tokenizers: BPE, WordPiece, SentencePiece

## Exercises

1. **Implement** BPE merge training from scratch on a small corpus of GTM company descriptions (5–10 short strings). Initialize the vocabulary at the character level, then run 10 merge iterations, selecting the most frequent adjacent symbol pair at each step. Print the merge chosen and the total vocabulary size at the end of every iteration so you can trace growth from the terminal.

2. **Configure** `tiktoken` (encoding `cl100k_base`) and `sentencepiece` (load any pretrained `.model` such as `T5` or `XLNet`) to tokenize a production cold-outreach prompt string of your choosing. Print the token IDs, the decoded token strings, and the total token count from each library side by side. Confirm both libraries round-trip correctly by decoding the IDs back to the original text.

3. **Compare** BPE (via `tiktoken`), WordPiece (via `transformers.BertTokenizer`), and SentencePiece (via `sentencepiece`) on an identical set of at least eight GTM-related input strings: three company names (e.g., "Zuora", "Clari", "Gong"), two product URLs, two multi-word product descriptions, and one multilingual string. Print each tokenizer's token split and token count for every input so you can eyeball fragmentation differences directly.

4. **Compute** token-level cost differences across the three tokenizer implementations for a batch of at least 50 lead-enrichment records loaded from a CSV exported by Apollo (or a comparable CRM lead export). For each tokenizer, sum total tokens across all records, then multiply by a hypothetical cost-per-1K-tokens rate (e.g., $0.01 for GPT-4-class input). Print a summary table showing total tokens, total estimated cost, and the per-record average for each tokenizer. Identify which tokenizer is cheapest and by what percentage.

5. **Build** a tokenization failure diagnostic tool that accepts a list of company names, URLs, and multilingual phrases, runs each through `tiktoken` and `sentencepiece`, and flags any input that fragments into more than double its whitespace-word count (a proxy for poor vocabulary coverage). Print a per-input report showing the input text, token count, whitespace-word count, fragmentation ratio, and a PASS/FAIL flag. Persist the tool as `handlers/tokenizer_diagnostics.py` and run it on a curated list of at least 15 inputs, capturing the terminal output as proof of execution.
