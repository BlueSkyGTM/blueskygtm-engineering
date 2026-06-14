# Exercises — Capstone 82 â€” Jailbreak Taxonomy

## Exercises

1. Implement the rule-based classifier from the lesson. Define at least three sample prompts for each of the six attack families (18 total). Run the classifier and confirm every family label appears at least once in your terminal output. Add a counter that prints total prompts processed and per-family counts at the end.

2. Extend your classifier with a `--trace` flag. When enabled, for each prompt the script must print the family label **and** the specific trust boundary that was violated (e.g., `completion_continuation`, `authority_override`, `latent_retrieval`). Run it against your 18-prompt sample set and verify each of the three trust boundaries is triggered by at least two different families.

3. Build a defense-mechanism comparison matrix. For each of the six families, assign every defense layer a coverage score of `full`, `partial`, or `none`: input filter, output classifier, system-prompt hardening, context sanitization, rate limiting, and human review. Print the matrix as a formatted table to the terminal, then print three sentences explaining why no single defense layer achieves `full` across all six families.

4. You receive a Clay enrichment export at `inputs/clay_companies.csv` with a `company_description` column that will be fed into an LLM for personalized outbound. Scan every row with your classifier before the LLM call. Print any row index whose description matches a jailbreak family, the suspected family label, and a short excerpt of the triggering text. Confirm your script exits with a non-zero code if any injection is found.

5. Build a coverage-chart script that reads a JSONL file of labeled attacks (`inputs/attack_log.jsonl`, each line has `family`, `timestamp`, and `source`). Compute per-family volume, sort families by volume descending, and write a prioritized sprint backlog to `outputs/skill-coverage-backlog.md` listing the top three defense gaps as tickets with a title, rationale, and suggested defense layer. Run the script and verify the file is created with three tickets.

6. Implement a context-smuggling detector for RAG-retrieved documents. Your detector must scan a directory of retrieved documents for at least four smuggling signals: zero-width Unicode characters, base64-encoded instruction fragments, phrases like "ignore previous instructions" or "system:", and nested prompt-template patterns (e.g., text inside `{{ }}` or `<instructions>` tags). Write the detector to `handlers/rag_smuggling_detector.py` and run it against `inputs/rag_docs/`. Print each flagged file, the signal type, and the matched substring. Confirm at least two distinct signal types appear in your output.
