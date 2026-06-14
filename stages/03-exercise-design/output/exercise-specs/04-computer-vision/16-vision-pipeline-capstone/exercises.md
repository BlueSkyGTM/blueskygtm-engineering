# Exercises — Build a Complete Vision Pipeline â€” Capstone

## Exercises

1. **Run the full four-stage pipeline end-to-end** on the test image provided in the lesson. Execute the pipeline script and confirm terminal output shows each stage firing in sequence — ingest filename, preprocess shape, raw inference tensor summary, and postprocessed JSON. Then modify the data contract passed between preprocess and infer to include the original image dimensions alongside the tensor, and verify the pipeline still executes without errors.

2. **Compare filtered detection counts across three confidence thresholds.** Configure the postprocess stage to accept a `threshold` parameter, then run the pipeline at `0.25`, `0.50`, and `0.75`. Print a summary table to the terminal showing each threshold alongside how many detections survived filtering. State in a comment which threshold gives the best precision-recall tradeoff for this dataset and why.

3. **Build a complete vision pipeline from scratch for logo detection** instead of general object detection. Define typed data contracts for all four stages (ingest → preprocess → infer → postprocess), process three test images of your choice, and print the final structured JSON for each image. No lesson code — write every stage yourself.

4. **Extend your pipeline to batch-process a directory of images.** Each image should flow through all four stages independently, and the pipeline should emit a single JSON array containing every result. Print per-image detection counts and total wall-clock processing time. Verify the output is valid JSON by piping it through `python -m json.tool`.

5. **Build a production enrichment handler that processes website screenshots and emits Clay-ready JSON.** Each detection should map to Clay-compatible field names (`company_logo_detected`, `confidence_score`, `bbox_x`, `bbox_y`, `bbox_width`, `bbox_height`). Run the handler on five screenshot images and write the results to `handlers/screenshot_enrichment.py`. The script must print the final JSON array to the terminal and confirm it validates against the schema you define in a dataclass.

6. **Design and document a GTM enrichment waterfall that mirrors the four-stage vision pipeline.** Implement the waterfall in code — Find (Apollo prospecting query) → Enrich (confidence-scored enrichment lookup) → Transform (map enriched records to a CRM-ready schema) → Export (write structured JSON to disk). Save the implementation to `handlers/enrichment_waterfall.py` and write a markdown architecture document to `outputs/skill-pipeline-mapping.md` that maps each vision stage to its GTM counterpart, identifying the shared data contract pattern between them. Run the waterfall on a sample prospect list and print the enriched output.
