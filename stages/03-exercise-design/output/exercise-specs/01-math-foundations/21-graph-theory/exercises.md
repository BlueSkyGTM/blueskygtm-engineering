# Exercises — Graph Theory for Machine Learning

## Exercises

1. **Implement** an adjacency-list-to-adjacency-matrix converter. Start with a Python dict representing an undirected graph of 6 companies connected by shared technology vendors (e.g., `{"Acme": ["Beta", "Corp"], "Beta": ["Acme", "Delta"], ...}`). Build the adjacency matrix as a NumPy array, print it, then convert it back to an adjacency list and print that. Verify the round-trip produces an equivalent structure. Your terminal output should show both representations side by side.

2. **Implement** both BFS and DFS as functions that take an adjacency list and a start node, returning the visit order. Run both on the same graph from Exercise 1 starting from the same node. Print the two traversal orders and state in a comment which traversal you would use to answer "what is the shortest path (in hops) from Acme to Delta?" and why.

3. **Compute** degree centrality, betweenness centrality, and eigenvector centrality on a directed graph representing a sales org chart (build one with 8–10 employees and reporting edges). Use `networkx` or implement from scratch with NumPy. Print a ranked table of all three centrality measures sorted by eigenvector centrality descending. In a comment, write one sentence interpreting what the top-ranked node by betweenness represents in an org-chart context.

4. **Implement** one round of GNN-style message passing. Construct a weighted adjacency matrix for a 5-node account-similarity graph, add self-loops, compute the symmetric normalization `D^{-1/2} (A + I) D^{-1/2}`, multiply it by a random 5×4 node feature matrix, and print the result before and after message passing. Verify the output shape is unchanged and that updated features are weighted averages of neighbors.

5. **Build** an account-similarity graph from a small GTM dataset. Create `handlers/account_graph.py` that reads a CSV (you generate one with 10 companies and their tech stacks as comma-separated strings), constructs a weighted similarity graph where edge weight = Jaccard similarity of tech stacks, computes eigenvector centrality, and writes the top 5 most "central" accounts to `outputs/skill-account-similarity.md` as a ranked prospecting-priority list. The script should print the full adjacency matrix to the terminal when run and produce the markdown artifact on disk.
