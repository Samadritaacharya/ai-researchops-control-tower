"""Scoring functions for the AI ResearchOps Control Tower."""


def calculate_uncertainty_score(goal_volatility, data_uncertainty, model_uncertainty, stakeholder_dependency, legal_complexity):
    """Return the average uncertainty score on a 1-10 scale."""
    values = [goal_volatility, data_uncertainty, model_uncertainty, stakeholder_dependency, legal_complexity]
    return sum(float(v) for v in values) / len(values)


def calculate_task_completeness(task_dict):
    """Return task completeness as a percentage across nine readiness fields."""
    required_fields = [
        "clear_objective", "has_owner", "has_output", "acceptance_criteria",
        "dependencies", "ai_metric", "risk_level", "timeline", "stakeholder_impact",
    ]
    completed = 0
    for field in required_fields:
        value = str(task_dict.get(field, "")).strip().lower()
        if value and value not in {"no", "none", "nan", "not set", ""}:
            completed += 1
    return round((completed / len(required_fields)) * 100, 2)


def calculate_handover_readiness(evaluation_quality, reproducibility, stakeholder_alignment, risk_closure, documentation_maturity):
    """Return handover readiness as a 0-100 score."""
    values = [evaluation_quality, reproducibility, stakeholder_alignment, risk_closure, documentation_maturity]
    return round((sum(float(v) for v in values) / len(values)) * 10, 2)


def calculate_risk_score(impact, likelihood):
    """Return risk score from impact and likelihood."""
    return int(impact) * int(likelihood)


def is_high_risk(score):
    """Return True when the risk score is high severity."""
    return int(score) > 15


def classify_risk(score):
    """Classify risk as Low, Medium, or High."""
    score = int(score)
    if score > 15:
        return "High"
    if score >= 8:
        return "Medium"
    return "Low"
