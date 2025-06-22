# learnmindai/memory_decay_model.py

def predict_memory_decay(username, topic, score, total):
    if total == 0:
        return f"No questions attempted in {topic}. Unable to predict memory decay."

    retention = (score / total) * 100

    if retention == 100:
        return f"✅ Excellent memory on {topic}. Minimal risk of forgetting in the next 3–5 days."
    elif retention >= 70:
        return f"👍 Good retention. Revise {topic} in 2–3 days to keep it fresh."
    elif retention >= 40:
        return f"⚠️ You may forget 40–50% of {topic} within 2 days. Recommended to revise soon."
    else:
        return f"❗ Low memory on {topic}. Re-learn and revise within 24 hours."
