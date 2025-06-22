import streamlit as st
from config import TOPICS
from quiz_generator import generate_quiz
from answer_checker import check_answers
from feedback_engine import generate_feedback
from study_plan_generator import generate_study_plan
from user_tracker import update_user_score, get_user_history
from memory_decay_model import predict_memory_decay
from score_visualizer import plot_score_chart
from reinforcement_reminder import get_revision_reminders
from topic_classifier import classify_user_profile
from user_profile import get_or_create_user_profile
from revision_quiz_generator import generate_revision_quiz

st.set_page_config(page_title="LearnMind.AI", layout="wide")

if "topic" not in st.session_state:
    st.session_state.topic = None
if "quiz" not in st.session_state:
    st.session_state.quiz = []
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "evaluations" not in st.session_state:
    st.session_state.evaluations = []

st.sidebar.title("📚 LearnMind.AI")
username = st.sidebar.text_input("Enter your name:", "")

if username:
    profile = get_or_create_user_profile(username)
    st.sidebar.success(f"Welcome, {username}!")
    selected_topic = st.sidebar.selectbox("Choose a topic to study:", TOPICS)

    if st.sidebar.button("Start Lesson"):
        st.session_state.topic = selected_topic
        st.session_state.quiz = generate_quiz(selected_topic)
        st.session_state.user_answers = []
        st.session_state.score = 0
        st.session_state.evaluations = []

st.title("LearnMind.AI – Self-Evolving Learning Companion")

if not username:
    st.info("👈 Enter your name to begin.")
elif st.session_state.topic:
    st.subheader(f"📘 Topic: {st.session_state.topic}")
    st.write("Answer the following questions:")

    user_responses = []
    for i, q in enumerate(st.session_state.quiz):
        st.markdown(f"**Q{i+1}: {q['question']}**")
        options = q['options']
        answer = st.radio(f"Choose one:", options, key=f"q{i}")
        user_responses.append(answer)

    if st.button("Submit Answers"):
        score, evaluations = check_answers(st.session_state.quiz, user_responses)
        feedback = generate_feedback(evaluations)
        st.session_state.score = score
        st.session_state.user_answers = user_responses
        st.session_state.evaluations = evaluations

        update_user_score(username, st.session_state.topic, score)

        st.success(f"✅ Score: {score} / {len(st.session_state.quiz)}")

        st.markdown("### 💬 Feedback")
        for fb in feedback:
            st.write("- " + fb)

        st.markdown("### 📊 Progress")
        plot_score_chart(username)

        st.markdown("### 🧠 Memory Prediction")
        st.write(predict_memory_decay(
            username,
            st.session_state.topic,
            st.session_state.score,
            len(st.session_state.quiz)
        ))

        st.markdown("### 📌 Study Plan")
        st.write(generate_study_plan(username))

        st.markdown("### 🔁 Revision Reminders")
        for r in get_revision_reminders(username):
            st.write("- " + r)

        st.markdown("### 🧪 Revision Quiz")
        revision_quiz = generate_revision_quiz(evaluations)
        if revision_quiz:
            for i, q in enumerate(revision_quiz):
                st.markdown(f"**{q['question']}**")
                st.radio("Choose one:", q["options"], key=f"rev_q{i}")
        else:
            st.success("🎉 No revision needed. You got everything right!")

        st.markdown("### 🧬 Learning Type")
        st.info(classify_user_profile(username))

        st.markdown("### 📈 Learning History")
        st.dataframe(get_user_history(username))
else:
    st.info("👈 Choose a topic to start.")
