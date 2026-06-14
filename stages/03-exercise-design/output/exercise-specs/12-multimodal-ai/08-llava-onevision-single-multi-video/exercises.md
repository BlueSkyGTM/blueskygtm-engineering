# Exercises — LLaVA-OneVision: Single-Image, Multi-Image, Video in One Model

## Exercises

1. **Compute** the visual-token budget allocation for three input profiles: one high-resolution image, four multi-images, and sixteen video frames. Write a Python script that takes a target of 2880 tokens and prints a table with per-input token count and total for each modality. Verify all three modalities total to approximately 2880 (±50 tokens). Your script should exit with code 1 if any modality deviates beyond that threshold.

2. **Implement** a function `arrange_visual_tokens(assets: list[dict]) -> str` that takes a list of visual-asset descriptors (each containing a name, modality type, and token count) and returns a single string representing the language-model context window. Insert positional markers (e.g., `<image_1>…</image_1>`, `<frame_3>…</frame_3>`) around each asset's token block and prepend/append sample text tokens. Print the full arranged context for a mixed input of two images and four video frames. Assert that the marker count equals the asset count.

3. **Trace** the three-stage training curriculum by building a skill-transfer matrix. Define at least eight visual skills (e.g., OCR, object recognition, spatial layout reasoning, cross-image comparison, temporal action sequencing, cross-frame object tracking, UI-element detection, emotion recognition). For each skill, predict which training stage introduces it, whether it transfers forward to later stages, and the confidence level of that transfer. Output a formatted table and exit with a summary count of skills predicted to transfer from single-image to video.

4. **Build** a multimodal enrichment pipeline that ingests a CSV of prospect data exported from Apollo or a CRM (columns: `company_name`, `website`, `screenshot_url`, `landing_page_archive`, `demo_video_url`). Write a router function that normalizes each visual asset to the 2880-token budget — screenshots get full resolution, landing-page archives get multi-image allocation, demo videos get 16-frame allocation — and outputs a structured JSON enrichment record per prospect. Print the per-prospect token breakdown and a pipeline-level summary of total tokens consumed. Use `curl` against the Apollo People Search API or a local mock server to fetch at least five prospect records.

5. **Build** a token-budget drift monitor that wraps any visual-enrichment call
