# AI Operations Lab

A portfolio-oriented learning track adapted from the concepts in Roberto Infante's *AI Agents and Applications* (Manning, 2026).

The goal is not to reproduce the book's examples. Each chapter is translated into a business-facing use case aligned with AI/data transformation, analytics, automation, operational systems, decision intelligence, and human-in-the-loop tooling.

## Learning roadmap

| Book chapter | Career-focused adaptation | Portfolio artifact |
|---|---|---|
| 1. Introduction to AI agents and applications | Map LLM apps, chatbots, agents, RAG, and tool use to operational transformation problems | Architecture notes + problem map |
| 2. Executing prompts programmatically | Convert messy operational requests into structured cases | Operational Intake Triage |
| 3. Summarizing text using LangChain | Turn long operational material into decision-ready briefs | Operations Brief Generator |
| 4. Building a research summarization engine | Synthesize evidence across market, process, and business sources | Transformation Evidence Synthesizer |
| 5. Agentic workflows with LangGraph | Model bounded multi-step transformation workflows with explicit state | Human-in-the-Loop Transformation Workflow |
| 6. RAG fundamentals with ChromaDB | Ground answers in SOPs, policies, process docs, and operating evidence | Operational Knowledge Base |
| 7. Q&A chatbots with LangChain and LangSmith | Build a traceable assistant for procedures and business context | SOP / Decision Support Assistant |
| 8. Advanced indexing | Improve retrieval across heterogeneous operational documents | Process Intelligence Index |
| 9. Question transformations | Rewrite vague business questions into answerable analytical queries | Analyst Query Clarifier |
| 10. Query generation, routing, and retrieval postprocessing | Route questions to the right data, evidence, or workflow | Decision Intelligence Router |
| 11. Building tool-based agents with LangGraph | Let an agent use bounded analytical and operational tools | Operations Analyst Agent |
| 12. Multi-agent systems | Coordinate specialist workflows under one accountable director | Career & Capital / Transformation Director prototype |
| 13. Building and consuming MCP servers | Expose reusable tools and data sources through MCP | Operations Toolkit MCP Server |
| 14. Productionizing AI agents | Add memory, guardrails, human approval, evaluation, and observability | Production Readiness Layer |

## Design principles

1. Business problem first, framework second.
2. Every project must produce structured, inspectable outputs.
3. Human approval is required before consequential external actions.
4. Developing skills are demonstrated through working proof rather than claimed as expertise.
5. Each project should be understandable by both a technical reviewer and an operations/business leader.
6. Evaluation, failure modes, and limitations are part of the artifact—not an afterthought.

## Current project

[Lesson 01 — Operational Intake Triage](./lesson-01-operational-intake-triage/)

This first project adapts the book's introductory and programmatic-prompting material into a small AI system that converts unstructured business problems into a structured operational case for analysis and action.
