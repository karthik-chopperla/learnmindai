user_profiles = {}

def get_or_create_user_profile(username):
    if username not in user_profiles:
        user_profiles[username] = {
            "strengths": [],
            "weaknesses": [],
            "preferences": []
        }
    return user_profiles[username]
