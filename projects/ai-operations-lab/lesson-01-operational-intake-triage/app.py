import json
import os
import sys
from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class OperationalCase(BaseModel):
    problem_statement: str = Field(description="Concise restatement of the observed business problem")
    domain: str = Field(description="Primary business or operational domain")
    issue_type: Literal[
        "process",
        "data",
        "integration",
        "customer",
        "financial",
        "risk",
        "capacity",
        "quality",
        "unknown",
    ]
    urgency: Literal["low", "medium", "high", "critical"]
    likely_impact: list[str] = Field(default_factory=list)
    evidence_present: list[str] = Field(default_factory=list)
    evidence_gaps: list[str] = Field(default_factory=list)
    assumptions_to_validate: list[str] = Field(default_factory=list)
    recommended_next_action: str = Field(
        description="One bounded next action that reduces uncertainty or advances resolution"
    )
    human_review_required: bool
    human_review_reason: str


PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an operational-intake analyst. Convert an unstructured business problem into a structured case for investigation.

Rules:
- Use only facts present in the user's description as evidence.
- Do not invent root causes, metrics, owners, deadlines, or system behavior.
- Put uncertain interpretations under assumptions_to_validate.
- Put missing information that could materially change the diagnosis under evidence_gaps.
- Recommend exactly one bounded next action.
- Prefer investigation before automation when the root cause is unclear.
- Set human_review_required to true when the case may involve consequential financial, legal, personnel, customer, safety, privacy, or external-communication decisions.
- Be concise and operationally specific.""",
        ),
        ("human", "Operational problem:\n{problem}"),
    ]
)


def build_model() -> ChatOpenAI:
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
        temperature=0,
        use_responses_api=True,
    )


def triage(problem: str) -> OperationalCase:
    model = build_model().with_structured_output(OperationalCase)
    chain = PROMPT | model
    return chain.invoke({"problem": problem})


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python app.py "Describe the operational problem"')

    problem = " ".join(sys.argv[1:]).strip()
    result = triage(problem)
    print(json.dumps(result.model_dump(), indent=2))


if __name__ == "__main__":
    main()
