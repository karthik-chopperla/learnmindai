import pandas as pd

user_scores = {}

def update_user_score(username, topic, score):
    if username not in user_scores:
        user_scores[username] = []
    user_scores[username].append({ "topic": topic, "score": score })

def get_user_history(username):
    return pd.DataFrame(user_scores.get(username, []))
