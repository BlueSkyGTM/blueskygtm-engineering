# Exercises — Alignment Research Ecosystem â€” MATS, Redwood, Apollo, METR

## Exercises

1. Implement a Python script that stores structured records for MATS, Redwood, Apollo Research, and METR using a dictionary or dataclass with fields `mandate`, `methodology`, and `output_format`. Print a formatted comparison table to stdout showing all four organizations side by side. Add a fifth column `is_independent` and mark whether each organization operates outside of any frontier lab.

2. Build a script that represents the alignment research dependency chain as an ordered list of tuples: `(stage_name, organization, produces, consumed_by)`. Traverse the chain from talent training through pre-deployment gating and print each stage with arrows showing what it feeds into the next. Verify your chain includes all four organizations and terminates at METR's pre-deployment gating evaluation.

3. Download the public Claude 3.5 Sonnet or GPT-4 system card (available as HTML or PDF from Anthropic's or OpenAI's website). Write a script that extracts every named third-party evaluation mentioned in the card and prints two lists: evaluations that include reported results, and evaluations that are referenced but contain no findings. Report counts for each list.

4. A GTM team plans to deploy an LLM-powered agent inside Clay that autonomously enriches CRM contact records, drafts personalized outreach, and sends emails without human review. Write a script that takes a model system card JSON as input and checks whether the card includes evaluations across these risk categories: `persuasion_and_deception`, `autonomous_agency`, `tool_use_and_safety`, and `data_exfiltration`. Print a deployment-readiness verdict for each category and an overall recommendation (`deploy`, `deploy_with_controls`, or `do_not_deploy`) based on coverage gaps.

5. Build a handler module at `handlers/deployment_risk_assessor.py` that accepts a model system card JSON file and a GTM use-case profile JSON file (containing fields like `autonomy_level`, `data_sensitivity`, `user_facing`, `tool_access`). The handler cross-references evaluation coverage against the use-case profile, classifies each gap as `high`, `medium`, or `low` deployment risk, and writes a formatted risk assessment report to `outputs/skill-deployment-risk.md`. Include specific mitigations for each high-risk gap.

6. Design and implement a comparison tool that ingests two model system card JSON files (for example, Claude 3.5 Sonnet vs GPT-4o) and produces a differential evaluation-coverage analysis. The tool must identify evaluations present in one card but absent in the other, flag asymmetric coverage in categories relevant to GTM deployment (persuasion, agency, cyber, tool use), and write the comparison to `outputs/skill-eval-coverage-comparison.md` as a decision aid for teams choosing between models.
