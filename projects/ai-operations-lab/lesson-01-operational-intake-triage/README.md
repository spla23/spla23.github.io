# Lesson 01 — Operational Intake Triage

## What this demonstrates

This project adapts the introductory and programmatic-prompting concepts from *AI Agents and Applications* into a business transformation use case.

Instead of asking an LLM to simply summarize or answer a question, the system converts a messy operational problem into a structured case that can be reviewed, prioritized, investigated, or routed into a downstream workflow.

### Input

A free-form business problem, for example:

> Store managers are manually reconciling loyalty redemptions against POS reports every Monday. It takes two people about three hours, numbers often disagree, and nobody is sure whether the source is the POS, loyalty platform, or export process.

### Output

A structured case containing:

- concise problem statement
- business domain
- issue type
- urgency
- likely impact
- evidence already present
- evidence gaps
- assumptions that require validation
- recommended next action
- whether human review is required

## Why this matters

Operational transformation starts before automation. The first problem is often turning an ambiguous complaint into a sufficiently structured representation that a person—or another system—can decide what to do next.

This is a small example of an AI transformation pattern:

**messy input → structured interpretation → evidence gaps → bounded next action → human review**

That pattern generalizes to support triage, process discovery, consulting intake, incident analysis, product operations, transformation portfolios, and decision-support systems.

## Concepts practiced

- programmatic LLM calls
- prompt structure and explicit instructions
- classification
- summarization
- structured output
- separating evidence from assumptions
- bounded recommendations
- human-in-the-loop design

## Setup

1. Create a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set `OPENAI_API_KEY` in your local environment. Do not commit credentials.
4. Optionally set `OPENAI_MODEL`; otherwise the example uses `gpt-5-mini`.
5. Run:

```bash
python app.py "Your messy operational problem here"
```

## Example

```bash
python app.py "Customer refund requests are copied from email into a spreadsheet, then manually checked against Stripe and our CRM. The queue is growing and managers cannot see which cases are high risk."
```

## Evaluation questions

A useful result should:

1. avoid inventing facts not contained in the request;
2. distinguish observed evidence from hypotheses;
3. choose an urgency level consistent with the stated impact;
4. identify information that would materially change the diagnosis;
5. recommend one bounded next action rather than a large transformation plan;
6. flag human review when the case could involve financial, legal, personnel, customer, or other consequential decisions.

## Next iteration

The next lesson will add reusable prompt templates, a small evaluation set, and comparison of prompt variants before moving into summarization and research synthesis.
