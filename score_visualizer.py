import matplotlib.pyplot as plt
import streamlit as st
from user_tracker import user_scores

def plot_score_chart(username):
    data = user_scores.get(username, [])
    if not data:
        st.write("No progress yet.")
        return

    topics = [d["topic"] for d in data]
    scores = [d["score"] for d in data]

    fig, ax = plt.subplots()
    ax.bar(topics, scores, color="green")
    ax.set_ylabel("Score")
    ax.set_title(f"{username}'s Progress")
    st.pyplot(fig)
