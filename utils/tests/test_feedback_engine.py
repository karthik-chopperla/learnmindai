from feedback_engine import generate_feedback

def test_feedback_positive():
    evaluations = [("Q1", "2", "2", True)]
    feedback = generate_feedback(evaluations)
    assert len(feedback) == 1

def test_feedback_negative():
    evaluations = [("Q2", "3", "5", False)]
    feedback = generate_feedback(evaluations)
    assert "Correct" in feedback[0]
