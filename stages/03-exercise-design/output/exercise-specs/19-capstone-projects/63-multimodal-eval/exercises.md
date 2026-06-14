# Exercises — Multimodal Evaluation

## Exercises

1. **Compute CLIPScore for a set of image-caption pairs using a pretrained CLIP model.** Load the `openai/clip-vit-base-patch32` model and tokenizer. For each pair in a sample dataset (use any 5 local images with candidate captions you write), compute the cosine similarity between the image embedding and text embedding, then multiply by 2.5 (the standard CLIPScore scaling factor). Print each pair's score and rank them from highest to lowest alignment. Confirm that a deliberately mismatched caption scores lowest.

2. **Implement BLEU-4 from scratch — no NLTK, no sacrebleu.** Write a function that tokenizes candidate and reference captions, computes clipped 1-gram through 4-gram precision
