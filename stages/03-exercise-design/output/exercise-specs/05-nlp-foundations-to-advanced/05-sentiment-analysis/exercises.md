# Exercises — Sentiment Analysis

## Exercises

1. Implement a lexicon-based sentiment scorer from scratch. Define a polarity dictionary with at least 20 entries spanning positive and negative words. Write a function that tokenizes an input string on whitespace, looks up each token, sums the scores, and normalizes by token count to produce a value in [-1.0, +1.0]. Run your scorer on five sentences you write yourself — two clearly positive, two clearly negative, one neutral — and print each sentence alongside its computed score. Verify that positive sentences produce positive scores and negative sentences produce negative scores.

2. Implement a Naive Bayes sentiment classifier from scratch with no ML libraries. Create a training set of at least 30 short labeled sentences (15 positive, 15 negative). Compute per-class log-probabilities for each token using Laplace smoothing. Write a `predict(text)` function that returns both the predicted label and the log-probability margin between classes. Train the model, then run it on five held-out test sentences and print predictions with margins. Confirm predicted labels match your manual labels for all five.

3. Build a diagnostic harness that feeds
