# Exercises — Ensemble Methods

## Exercises

1. **Implement** a `BaggingClassifier` with 50 `DecisionTree` base estimators on the breast cancer dataset from `sklearn.datasets`. Print train accuracy, test accuracy, and the gap between them for `n_estimators` values of `[1, 5, 10, 25, 50, 100]`. Your terminal output should be a table showing how the train-test gap narrows as bagging adds estimators.

2. **Trace** the boosting aggregation path by fitting a `GradientBoostingClassifier` on the same dataset with `n_estimators=50`. Extract the staged prediction accuracy at each stage using `staged_score` and plot (or print) accuracy as a function of the number of estimators. Identify the iteration where test accuracy plateaus and report it as terminal output.

3. **Compute** the cross-validation accuracy mean and standard deviation across 10 folds for three configurations on the wine quality dataset (`sklearn.datasets.load_wine`): a single `DecisionTreeClassifier`, a `BaggingClassifier` wrapping that same tree with 100 estimators, and a `GradientBoostingClassifier` with 100 estimators. Print a comparison table. State which ensemble reduces variance most and which reduces bias most, supported by the numbers you printed.

4. **Diagnose** whether a model trained on the `digits` dataset from `sklearn.datasets` suffers from high bias or high variance. Train a `KNeighborsClassifier` with `n_neighbors=1` and another with `n_neighbors=50`. For each, print train accuracy, test accuracy, and the cross-validation variance. Based on the diagnostics you observe, select the appropriate ensemble family (bagging, boosting, or neither will help) and justify your choice in a printed one-line conclusion.

5. **Build** a stacking meta-learner over three heterogeneous base models (`RandomForestClassifier`, `GradientBoostingClassifier`, `SVC`) using `LogisticRegression` as the final estimator on the `covertype` sample dataset from `sklearn.datasets.fetch_covtype` (subsample to 5000 rows for speed). Print the stacked accuracy alongside each base model's standalone accuracy. Save the trained stacking pipeline as a serialized artifact at `handlers/stacked-classifier.pkl` and print the path on completion.

6. **Design** a boosting-to-enrichment-waterfall mapping that simulates sequential data enrichment stages where each stage corrects errors from the previous one. Implement this as a Python script that models a contact list of 1000 leads with missing email data, applies three enrichment passes (each modeled as a weak learner targeting previously-failed rows), and prints the cumulative coverage percentage after each stage. Persist the coverage curve and your written analysis of why the marginal gain shrinks at each stage to `outputs/skill-enrichment-boosting.md`.
