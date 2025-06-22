# learnmindai/revision_quiz_generator.py

def generate_revision_quiz(evaluations):
    revision_questions = []
    for question, user_ans, correct_ans, is_correct in evaluations:
        if not is_correct:
            options = [correct_ans, user_ans, "None of the above", "Not sure"]
            revision_questions.append({
                "question": question + " (REVIEW)",
                "options": options,
                "correct": correct_ans
            })
    return revision_questions
