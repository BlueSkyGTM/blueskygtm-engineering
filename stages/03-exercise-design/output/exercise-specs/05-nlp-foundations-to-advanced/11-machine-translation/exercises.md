# Exercises — Machine Translation

## Exercises

1. **Implement** a basic translator using the `Helsinki-NLP/opus-mt-fr-en` model. Load the model with `transformers.pipeline("translation_fr_to_en")`, translate five French sentences of your choice, and print both the source and the translation for each. Run it as `python translate.py` and confirm you see readable English output in the terminal.

2. **Compare** greedy decoding against beam search on the same five sentences. Run the translator once with `num_beams=1` (greedy) and once with `num_beams=5`, then print the outputs side by side. Identify at least one sentence where beam search produces a visibly better translation and note which decoding strategy you would ship.

3. **Compute** BLEU score for a batch of ten translated sentences against reference translations you write yourself. Use `sacrebleu` or `nltk.translate.bleu_score`, feed it your model's outputs and your references, and print the corpus-level BLEU score. Report whether the score clears 0.5 and what that tells you about output quality.

4. **Configure** a translation pipeline that accepts a list of prospect messages in mixed languages, detects each language using `langdetect`, routes each message to the correct `Helsinki-NLP/opus-mt-*-en` model, and prints the detected language alongside the English translation. Include at least French, German, and Spanish inputs.

5. **Build** a lead-enrichment translation handler that reads a JSON file of international prospects (each with a `bio` field in a non-English language), translates each bio into English, attaches a confidence score derived from the mean token probability, and flags any prospect whose confidence falls below 0.6 for human review. Write the results to `outputs/translated_leads.json` and print a summary count of auto-shipped vs flagged leads. Save the handler to `handlers/translate_leads.py`.

6. **Design** a quality-gate system that takes a validation set of source sentences with known-good English references, runs your translation pipeline, computes per-sentence BLEU using `sacrebleu.sentence_bleu`, and establishes a threshold below which translations are routed to human review. Run it on twenty sentence pairs, print the threshold value and the percentage of sentences that passed, and write your threshold rationale and results summary to `outputs/skill-translation-quality-gate.md`.
