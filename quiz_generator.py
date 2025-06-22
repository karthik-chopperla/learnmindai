import random
from config import DEFAULT_QUIZ_LENGTH

def generate_quiz(topic):
    base_questions = {
        "Mathematics": [
            ("What is {a} + {b}?", lambda a, b: str(a + b)),
            ("What is {a} * {b}?", lambda a, b: str(a * b)),
        ],
        "Artificial Intelligence": [
            ("What is the purpose of a learning rate?", "To control the update step size."),
            ("What is overfitting?", "Fitting training data too closely and failing to generalize."),
        ],
        "Computer Science": [
            ("What is a stack used for?", "LIFO operations."),
            ("Time complexity of binary search?", "O(log n)"),
        ],
        "Soft Skills": [
            ("What makes communication effective?", "Clarity and empathy."),
            ("How to handle conflict?", "Stay calm and listen."),
        ]
    }

    questions = []
    templates = base_questions.get(topic, [])[:DEFAULT_QUIZ_LENGTH]
    for t in templates:
        if callable(t[1]):
            a, b = random.randint(1, 10), random.randint(1, 10)
            q = t[0].format(a=a, b=b)
            correct = t[1](a, b)
            options = [correct] + [str(int(correct) + i) for i in range(1, 4)]
        else:
            q = t[0]
            correct = t[1]
            options = [correct, "Not sure", "None", "Other"]
        random.shuffle(options)
        questions.append({ "question": q, "options": options, "correct": correct })
    return questions
