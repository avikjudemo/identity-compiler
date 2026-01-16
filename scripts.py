import json
from typing import Any, Dict, List

from pydantic import BaseModel, Field


# ---------- Data Models ----------

class IdentityDelta(BaseModel):
    market_expectations: List[str]
    current_signals: List[str]
    delta: List[str]
    top_3_non_obvious_gaps: List[str] = Field(min_length=3, max_length=3)


class QuestWeek(BaseModel):
    week: int
    mission: str
    deliverable: str
    evidence: str
    timebox_hours: float


class PortfolioArtifact(BaseModel):
    name: str
    why_it_counts: str
    acceptance_criteria: List[str]
    link_placeholder: str


class SignalPortfolio(BaseModel):
    high_signal_artifacts: List[PortfolioArtifact]
    medium_signal_artifacts: List[str]
    templates: Dict[str, str]


class ReadinessGate(BaseModel):
    signal_credibility_score: int = Field(ge=0, le=100)
    verdict: str
    reasons: List[str]
    minimum_to_reach_70: List[str]


class CompilerOutputs(BaseModel):
    identity_delta: IdentityDelta
    questline_24w: List[QuestWeek] = Field(min_length=24, max_length=24)
    signal_portfolio: SignalPortfolio
    readiness_gate: ReadinessGate


class CompilerResponse(BaseModel):
    mode: str
    profile: Dict[str, Any]
    outputs: CompilerOutputs


# ---------- Utility Functions ----------

def safe_load_json(text: str) -> Dict[str, Any]:
    """
    Load JSON safely. If markdown fences exist, strip them.
    """
    t = text.strip()
    if t.startswith("```"):
        t = t.strip("`")
        lines = t.splitlines()
        if lines and lines[0].lower().startswith("json"):
            t = "\n".join(lines[1:])
    return json.loads(t)


def validate_compiler_response(raw: Dict[str, Any]) -> CompilerResponse:
    return CompilerResponse.model_validate(raw)


def normalize_verdict(verdict: str) -> str:
    v = (verdict or "").strip().lower()
    if v in ("apply now", "apply_now"):
        return "apply_now"
    if v in ("do not apply yet", "do_not_apply_yet", "do-not-apply-yet"):
        return "do_not_apply_yet"
    return v