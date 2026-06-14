# Exercises — Terminal & Shell

## Exercises

1. **Navigate and build a GTM project directory structure.** Using only shell commands, create the following tree inside your home directory: `gtm-project/`, with subdirectories `leads/`, `scripts/`, and `outputs/`. Then `cd` into `gtm-project`, run `pwd` to confirm your location, and run `ls -R` to display the full tree. Verify your terminal shows all three subdirectories.

2. **Create and append to a lead-tracking file.** Inside `gtm-project/leads/`, create a file named `accounts.txt` using `touch`. Append three company names (one per line) using `echo` and `>>`. Then use `cat` to print the full contents to your terminal. Confirm all three lines appear.

3. **Compute account counts from a CSV using pipes and redirection.** Create a file `gtm-project/leads/exports.csv` with at least 8 rows of mock data (columns: `company,domain,score`). Using pipes and redirection only — no Python, no opening an editor — produce a file `outputs/top_accounts.txt` containing only the rows where the score column is 60 or above, sorted by score descending. Verify by running `cat outputs/top_accounts.txt` and confirming only qualifying rows appear.

4. **Write a shell script that accepts arguments to filter lead data.** In `gtm-project/scripts/`, create `filter_leads.sh` that takes two arguments: a filename (the CSV to read) and a minimum score threshold. The script should print every row whose score meets or exceeds the threshold, or print `No matches` if none qualify. Make it executable with `chmod +x`. Run it against your `exports.csv` with a threshold of 50 and confirm the output matches expectation. Run it again with a threshold of 999 to confirm it prints `No matches`.

5. **Build a reusable enrichment-setup script.** Write a shell script at `scripts/setup_enrichment.sh` that creates a `config/` directory, writes an `.env` file containing two environment variables (`APOLLO_API_KEY` set to a placeholder string, `CLAY_WEBHOOK_URL` set to a placeholder string), then exports both variables into the current shell session and prints a confirmation line for each. Source the script (`source scripts/setup_enrichment.sh`) and then run `echo $APOLLO_API_KEY` to verify the value persists in your environment. The `.env` file at `config/.env` is the persistent artifact.

6. **Inspect and extend your `PATH` for a local tool.** Print your current `PATH` and identify each directory entry. Create a directory `~/.local-gtm-bin`, write a simple executable script inside it called `greet` that prints `GTM tools ready`, add that directory to your `PATH` for the current session using `export`, and confirm that typing `greet` from any directory now executes the script. Write the `export` line into your shell config file (`.bashrc` or `.zshrc`) so the change survives a new terminal session. Verify by opening a new terminal window and running `greet`.
