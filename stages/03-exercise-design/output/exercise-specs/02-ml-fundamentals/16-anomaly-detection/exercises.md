# Exercises — Anomaly Detection

## Exercises

1. **Implement Z-score anomaly detection on account data.** Write a Python script that loads `data/account_engagement.csv` (columns: `account_id`, `page_views`, `email_opens`, `meetings_booked`), computes the Z-score for the `page_views` column, and prints every account whose absolute Z-score exceeds 3.0. Format each line as `account_id | z_score | page_views`. Run the script and confirm terminal output shows the flagged accounts.

2. **Implement IQR anomaly detection on the same dataset.** Compute the 25th and 75th percentiles for `email_opens`, derive the IQR fence (1.5 × IQR above Q3 and below Q1), and print every account that falls outside the fence. Format each line as `account_id | email_opens | fence_lower | fence_upper`. Run the script and confirm terminal output. Compare which accounts differ from the Z-score flags in Exercise 1.

3. **Implement Isolation Forest detection and compare against statistical methods.** Using `sklearn.ensemble.IsolationForest`, fit a model on `page_views`, `email_opens`, and `meetings_booked` jointly with `contamination=0.05` and `n_estimators=200`. Print every flagged account with its anomaly score (`decision_function` output). Then print a summary count: how many accounts Isolation Forest flagged that Z-score or IQR did not, and vice versa.

4. **Tune contamination and tree count, then document the effect.** Write a script that runs Isolation Forest on the same dataset across contamination rates `[0.01, 0.05, 0.10, 0.20]` and tree counts `[50, 100, 200, 500]`. For each combination, print the number of flagged accounts and the mean anomaly score. Observe which parameter moves the flag count most and which has diminishing returns.

5. **Deploy an anomaly detector on GTM pipeline data and route flagged accounts to a webhook.** Pull account engagement data from your CRM or an enrichment API (HubSpot, Apollo, or a Clay export CSV), run Isolation Forest with tuned parameters from Exercise 4, and for each flagged account send a POST request to a local webhook server (`http://localhost:8080/anomaly`) with a JSON payload containing `account_id`, `anomaly_score`, and the top contributing features. Start the webhook receiver first (use Python's `http.server` or Flask) so it logs each incoming payload. Produce the detector script as a reusable module at `handlers/anomaly_router.py`.

6. **Design and justify a multi-method anomaly pipeline.** Build a script that runs Z-score, IQR, and Isolation Forest on a dataset of your choice (GTM account data, SaaS usage logs, or synthetic engagement data). For each method, compute the flagged account count, the overlap with the other two methods, and write a one-paragraph interpretation of which method is most appropriate for this dataset and why. Save the full analysis—flagged accounts, scores, overlap matrix, and written justification—to `outputs/skill-anomaly-comparison.md`.
