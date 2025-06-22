def check_answers(quiz, user_answers):
    score = 0
    evaluations = []
    for idx, user_ans in enumerate(user_answers):
        correct_ans = quiz[idx]["correct"]
        is_correct = user_ans == correct_ans
        if is_correct:
            score += 1
        evaluations.append((quiz[idx]["question"], user_ans, correct_ans, is_correct))
    return score, evaluations
