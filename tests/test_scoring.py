from utils.scoring import calculate_uncertainty_score, calculate_task_completeness, calculate_handover_readiness, calculate_risk_score


def test_uncertainty_score():
    assert calculate_uncertainty_score(7, 6, 8, 7, 6) == 6.8


def test_risk_score():
    assert calculate_risk_score(4, 5) == 20


def test_handover_readiness():
    assert calculate_handover_readiness(8, 7, 8, 6, 7) == 72.0


def test_task_completeness():
    task = {'clear_objective': 'Yes', 'has_owner': 'Yes', 'has_output': 'No', 'acceptance_criteria': 'Yes', 'dependencies': 'T001', 'ai_metric': 'F1 score', 'risk_level': 'High', 'timeline': '2024-07-31', 'stakeholder_impact': 'High'}
    assert calculate_task_completeness(task) > 80
