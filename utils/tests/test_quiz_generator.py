from quiz_generator import generate_quiz

def test_quiz_length():
    quiz = generate_quiz("Mathematics")
    assert len(quiz) == 5

def test_quiz_structure():
    quiz = generate_quiz("Artificial Intelligence")
    for q in quiz:
        assert "question" in q and "options" in q and "correct" in q
