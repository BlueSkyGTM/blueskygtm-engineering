# Exercises — GPU Setup & Cloud

## Exercises

1. **Compute minimum VRAM for Llama-2-7B at fp16.** Write a standalone Python script that takes a parameter count (7,000,000,000) and a precision identifier (`"fp16"`), applies the bytes-per-parameter multiplier (2), adds 20% overhead for KV cache and activation buffers, and prints the result in gigabytes rounded to two decimals. Run it and confirm the output is approximately 16.8 GB.

2. **Compare VRAM across four precision formats for the same model.** Extend your script from Exercise 1 to accept any model size and print a table showing minimum VRAM at fp32, fp16, int8, and int4. Run it against a 13-billion-parameter model and print the savings delta (in GB) between fp16 and int4. Verify the delta exceeds 10 GB.

3. **Compute cost-per-VRAM-GB across two providers.** Using the pricing data below, write a script that ranks all four instances by cost-per-VRAM-GB-hour and prints the ranked table with a recommendation for which instance to choose for a 7B fp16 inference workload (minimum 16.8 GB VRAM with headroom).

   | Provider | Instance | VRAM (GB) | $/hour |
   |---|---|---|---|
   | AWS | p3.2xlarge (V100) | 16 | 3.06 |
   | AWS | g5.2xlarge (A10G) | 24 | 1.01 |
   | GCP | a2-highgpu-1g (A100) | 40 | 2.93 |
   | GCP | t4-n1-standard-4 (T4) | 16 | 0.75 |

4. **Diagnose a simulated provisioning failure.** You are handed a VM where `nvidia-smi` reports driver version 525.85 but PyTorch was installed with CUDA 12.1 wheels. Write a diagnostic script that calls `nvidia-smi` via subprocess, parses the driver version, queries `torch.version.cuda`, and compares the driver's maximum supported CUDA version against the PyTorch-compiled CUDA version. Print `MATCH` or `MISMATCH` for each check. Also detect whether `torch.cuda.is_available()` returns `False` despite an `nvidia-smi` call succeeding, and flag that as a distinct failure mode. Run the script and confirm it prints at least one `MISMATCH` line.

5. **Build a reproducible GPU verification script for a GTM inference workload.** You are provisioning a GPU to run local inference on a CSV of 500 Apollo-enriched company profiles (assume a column `company_description` with ~200 tokens each). Your target model is Mistral-7B at int8 (minimum ~8.4 GB VRAM). Write `handlers/gpu_verify.py` that: loads the CSV with Python's `csv` module, counts rows and estimates token volume, checks `torch.cuda.is_available()` and queries total VRAM via `torch.cuda.get_device_properties`, compares available VRAM against the model requirement, emits a JSON diagnostic blob to stdout containing driver version, CUDA version, total VRAM, model VRAM requirement, row count, and pass/fail status, and exits with code `0` if all checks pass or `1` if any check fails. Run it against your local CSV and confirm the JSON output and exit code are correct.
