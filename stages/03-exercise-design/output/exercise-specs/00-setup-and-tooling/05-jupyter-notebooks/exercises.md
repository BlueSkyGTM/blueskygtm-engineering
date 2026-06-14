# Exercises — Jupyter Notebooks

## Exercises

1. **Launch a Jupyter server** from the terminal and create a new notebook named `kernel_trace.ipynb`. Write four code cells that chain together: the first defines a list of company names, the second filters that list by string length, the third counts the filtered result, and the fourth prints the original list. Run all cells in document order and record the output. Then restart the kernel and run only cells 3 and 4 — observe what happens when the earlier cells never executed. Print the kernel's error or unexpected output to confirm the dependency chain.

2. **Create a second notebook** named `state_prediction.ipynb` with five code cells that progressively transform a small dataset (a CSV of accounts, a list of dicts, or a pandas DataFrame — your choice). Before executing any cell, add a markdown cell at the top where you predict which variables will exist in the kernel namespace after each cell runs in document order. Execute all cells top to bottom, then add a final code cell that prints every variable name currently in scope using `dir()` or `%who`. Compare the actual namespace against your predictions.

3. **Reproduce a hidden-state
