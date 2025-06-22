def summarize_text(text):
    return text if len(text) < 100 else text[:100] + "..."

def paraphrase_text(text):
    return text.replace("learn", "understand").replace("practice", "try")
