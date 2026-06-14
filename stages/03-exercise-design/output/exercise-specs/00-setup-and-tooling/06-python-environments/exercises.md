# Exercises — Python Environments

## Exercises

1. Create a virtual environment named `gtm-env`, activate it, and print `sys.path` from both the global interpreter and the venv interpreter using `python -c "import sys; print('\n'.join(sys.path))"`. Identify which `sys.path` entry contains the venv-specific `site-packages` directory versus the global one. Record the two different `sys.prefix` values you observe — this confirms isolation.

2. Inside an active venv, run `pip install requests`. Confirm the install location with `pip show requests` and note the `Location:` field. Deactivate the venv and run `pip show requests` again from the global interpreter. Execute `python -c "import requests; print(requests.__file__)"` from both environments and observe which one raises `ModuleNotFoundError`. Add a comment to a file explaining which `sys.path` entry the successful import resolved from and why the other environment cannot find the package.

3. Build a script that loads Apollo API credentials from a `.env` file using `python-dotenv`, reads the value via `os.getenv("APOLLO_API_KEY")`, and prints a masked version showing only the first 4 characters followed by `****`. Create a `.env` file with a dummy key, add `.env` to `.gitignore`, and confirm that running the script outputs the masked key while the raw key never appears in stdout.

4. Install `requests==2.28.0` in a fresh venv and generate a `requirements.txt` via `pip freeze > requirements.txt`. Delete the venv, recreate it, and reconstruct the environment from the file using `pip install -r requirements.txt`. Verify the reconstruction by running `pip show requests` and confirming the version matches exactly. Then upgrade to `requests==2.31.0`, regenerate the file, and `diff` the two versions to confirm only the version line changed.

5. You have two GTM scripts: one depends on `apollo-sdk` (which pins `requests<2.29`) and another depends on a Clay enrichment client (which requires `requests>=2.31`). Attempt to install both in a single venv and capture the pip resolver error output. Then create two separate venvs and install each script's dependencies independently. Implement a reusable diagnostic script at `handlers/dependency_audit.py` that accepts a list of `requirements.txt` file paths, attempts a combined
