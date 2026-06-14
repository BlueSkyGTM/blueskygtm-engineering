# Exercises — End-to-End Research Demo

## Exercises

1. Run the lesson's research pipeline end-to-end on a company of your choice. Pipe the final synthesized brief to `stdout` and verify it contains all required schema fields (`company_name`, `description`, `industry`, `founding_year`, `headquarters`, `key_products`, `recent_news`). Print any fields that are missing or null.

2. Add timing instrumentation around the fetch stage. Run the pipeline twice — once with sequential fetch and once with parallel fetch — on the same 3-source list. Print a comparison table showing wall-clock time per source and total elapsed time for each strategy. Note which strategy completed faster and by what margin.

3. Implement a new extraction function for a source type not covered in the lesson: a company's careers/jobs page. Design a prompt that extracts `open_role_count`, `top_departments_hiring`, `office_locations`, and `tech_stack_signals` into a JSON object. Run it against a real careers page URL and print the extracted JSON. Verify the output parses with `json.loads()` and contains every required key.

4. Modify the pipeline to simulate a source failure: inject a function that raises a `ConnectionError` for one of the three sources. Implement error handling that catches the exception, logs which source failed, and proceeds with the remaining two. Run the pipeline and confirm the synthesized brief still produces output with the two successful extractions merged. Print a summary line listing which sources succeeded and which failed.

5. Build a GTM prospect-research pipeline that combines data from Apollo's company enrichment API with web-sourced research (Wikipedia + company homepage). Fetch Apollo data for a target company, fetch the two web sources in parallel, extract structured fields from each, and synthesize a unified prospect brief that includes `icp_fit_score` (0–100) computed from the combined fields. Run it for 3 real companies and save the results to `outputs/skill-prospect-briefs.md` as a formatted markdown table.

6. Design and implement a brief validator that takes any synthesized research output and scores it on three dimensions: **completeness** (fraction of schema fields populated), **internal consistency** (e.g., founding year is plausible, employee count aligns with company stage, headquarters city is a real city), and **actionability** (presence of at least one concrete outreach hook — a recent funding event, product launch, or executive change). Run the validator on 5 briefs produced by your pipeline and save the scored report to `handlers/brief_validator.py` as a reusable tool, with the evaluation results printed to `stdout`.
