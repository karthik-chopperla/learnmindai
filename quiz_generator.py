# learnmindai/quiz_generator.py

import random
from config import DEFAULT_QUIZ_LENGTH

def generate_quiz(topic):
    easy_math = [
        ("What is {a} + {b}?", lambda a, b: str(a + b)),
        ("What is {a} * {b}?", lambda a, b: str(a * b)),
    ]
    hard_math = [
        ("What is {a}² + {b}²?", lambda a, b: str(a**2 + b**2)),
        ("Solve: ({a}+{b})²?", lambda a, b: str((a + b) ** 2)),
    ]

    easy_ai = [
        ("What is supervised learning?", "Learning with labeled data"),
        ("What is overfitting?", "Model fits too closely to training data"),
    ]
    hard_ai = [
        ("Define backpropagation.", "It updates weights using error gradients"),
        ("What does 'bias' mean in neural networks?", "A constant added to weighted sum before activation"),
    ]

    easy_cs = [
        ("What is a variable?", "A named storage for values"),
        ("What is a loop used for?", "Repeating a block of code"),
    ]
    hard_cs = [
        ("Explain time complexity of quicksort.", "O(n log n) on average"),
        ("What is dynamic programming?", "Breaking down problems into overlapping subproblems"),
    ]

    easy_soft = [
        ("What is active listening?", "Fully concentrating on what is being said"),
        ("What is communication?", "Exchange of information"),
    ]
    hard_soft = [
        ("How do you handle aggressive questions in interviews?", "Stay calm and answer confidently"),
        ("How do you show empathy in a conversation?", "By understanding others’ feelings"),
    ]

    topic_bank = {
        "Mathematics": easy_math + hard_math,
        "Artificial Intelligence": easy_ai + hard_ai,
        "Computer Science": easy_cs + hard_cs,
        "Soft Skills": easy_soft + hard_soft
    }

    templates = topic_bank.get(topic, [])
    selected = random.sample(templates, min(DEFAULT_QUIZ_LENGTH, len(templates)))

    quiz = []
    for t in selected:
        if callable(t[1]):
            a, b = random.randint(1, 10), random.randint(1, 10)
            q = t[0].format(a=a, b=b)
            correct = t[1](a, b)
            options = [correct, str(int(correct)+1), str(int(correct)+2), str(int(correct)-1)]
        else:
            q = t[0]
            correct = t[1]
            options = [correct, "Not sure", "Other", "None"]
        random.shuffle(options)
        quiz.append({ "question": q, "options": options, "correct": correct })
    return quiz
