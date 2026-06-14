# Exercises — Capstone 12 â€” Video Understanding Pipeline (Scene, QA, Search)

## Exercises

1. **Implement** a scene boundary detector that reads a video file frame-by-frame, computes normalized RGB histograms for consecutive frames, calculates the mean absolute difference between them, and prints every timestamp where the difference exceeds a configurable threshold. Run it on a sample video and verify the terminal prints detected cut timestamps in `HH:MM:ss.mmm` format.

2. **Compare** your histogram-based cut list from Exercise 1 against PySceneDetect's `detect_scenes` output on the same video file. Print both lists side-by-side along with a count of matching cuts (within ±1 second), false positives, and missed boundaries. Vary your threshold by ±20% and report how the agreement changes.

3. **Implement** visual question answering over detected scenes: for each scene, extract the middle frame as a keyframe, send it to a vision-language model API (Gemini 2.5, Qwen3-VL, or Molmo 2) with the prompt *"Describe the visual content, any text on screen, and the product or action shown,"* and print each scene's timestamp alongside its generated caption.

4. **Build** a searchable text index over the scene captions produced in Exercise 3. Use either TF-IDF cosine similarity or embedding-based nearest neighbor search. Accept a natural language query string from the command line and return the top-N matching scenes ranked by relevance score, each with its timestamp range and caption. Test with at least three queries (e.g., *"dashboard view,"* *"person speaking,"* *"logo on screen"*) and print the ranked results.

5. **Deploy** a CLI tool that accepts a video file path and a query string, runs the full pipeline — scene detection, keyframe VQA captioning, and text retrieval — and outputs timestamped scene matches with relevance scores. Support a `--threshold` flag for the histogram detector and a `--top-k` flag for result count. Persist the tool as a runnable module with a `__main__` entry point. **Artifact:** `handlers/video_search.py`

6. **Evaluate** the pipeline end-to-end against a labeled video with known scene cuts and ground-truth scene descriptions. Compute detection precision, recall, and F1 at the cut level. Then measure QA caption hallucination rate by comparing model-generated descriptions against ground-truth labels (flag captions containing claims unsupported by the keyframe). Finally, apply the pipeline to a directory of recorded sales demo videos, and export the top scene match per query into Clay as an enriched note on the corresponding prospect account via the Clay API. **Artifact:** `outputs/skill-video-gtm-eval.md`
