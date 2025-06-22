import random
from config import POSITIVE_FEEDBACK, NEGATIVE_FEEDBACK

def generate_feedback(evaluations):
    feedback = []
    for question, user_ans, correct_ans, is_correct in evaluations:
        if is_correct:
            msg = random.choice(POSITIVE_FEEDBACK)
        else:
            msg = f"{random.choice(NEGATIVE_FEEDBACK)} Correct: {correct_ans}"
        feedback.append(f"{question} → {msg}")
    return feedback
