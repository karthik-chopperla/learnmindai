def adapt_difficulty(score, total):
    if score == total:
        return "Advanced"
    elif score >= total // 2:
        return "Intermediate"
    return "Beginner"
