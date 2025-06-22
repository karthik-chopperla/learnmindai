import random

def get_revision_reminders(username):
    reminders = [
        "Review Math tomorrow morning.",
        "Take a short CS quiz on Thursday.",
        "Revise AI basics before the weekend.",
        "Practice communication by Friday."
    ]
    return random.sample(reminders, 2)
