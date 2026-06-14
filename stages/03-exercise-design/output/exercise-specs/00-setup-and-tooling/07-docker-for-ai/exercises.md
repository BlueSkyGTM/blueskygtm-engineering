# Exercises — Docker for AI

## Exercises

1. **Build a GPU-enabled Docker image** from a CUDA 12.1 base image that installs PyTorch and runs a Python script printing `torch.cuda.is_available()`, the device count, and the device name. Build the image with `docker build` and run it. Confirm the terminal shows `True`, a nonzero device count, and the GPU model string.

2. **Verify NVIDIA Container Toolkit** by running `nvidia-smi` inside a container started with `--gpus all`. Compare the output to the same command on the host — the driver version and GPU name must match. Then run a short PyTorch snippet that allocates a tensor on `cuda:0` and prints its value to confirm end-to-end GPU passthrough.

3. **Mount a host directory as a volume** to persist a synthetic dataset across container rebuilds. Run a container that writes a CSV to `/data/enriched.csv` inside a mounted volume, remove the container, rebuild the image with a different tag, start a new container mounting the same volume, and read the file back. The file contents must survive both the container destruction and the image rebuild — print the row count to the terminal.

4. **Write a `docker-compose.yml`** with two services: a FastAPI app that exposes `/predict` and a Redis container for caching predictions. The FastAPI service must connect to Redis using the service hostname `redis` (not `localhost`). Bring the stack up with `docker compose up`, hit the endpoint with `curl`, and verify the response includes a cache hit on the second request. Terminal output: two curl responses showing a cache miss followed by a hit.

5. **Build both a single-stage and a multi-stage Dockerfile** for the same PyTorch serving app. Build each image, run `docker history <image>` on both, and record the size of every layer. Write a markdown report identifying which layers dominate (likely the CUDA base, pip install, or model-artifact copy), the total size delta between the two images, and which stages benefit from multi-stage builds vs. which are unavoidable. Save to `outputs/skill-docker-image-optimization.md`.

6. **Build a containerized GTM enrichment service** using Docker Compose with two services: one that queries the Apollo People Search API (or a Clay webhook endpoint) for contacts at a target company list, and a second FastAPI service that serves the enriched results over HTTP. Store the Apollo API key in a `.env` file loaded by Compose, mount a host volume at `/data` for the enriched contact cache, and verify the pipeline end-to-end by `curl`-ing the serving endpoint and confirming it returns enriched records with email and LinkedIn fields. Place the enrichment service code at `handlers/enrichment_service.py` and the compose file alongside it.
