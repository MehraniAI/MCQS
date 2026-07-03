import streamlit as st
import time
import random
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="MCQs Quiz 2026",
    page_icon="📚",
    layout="wide"
)

# ---------------- DARK THEME ----------------

st.markdown("""
<style>
input {
    color: white !important;
    -webkit-text-fill-color: white !important;
}

input::placeholder {
    color: white !important;
    -webkit-text-fill-color: white !important;
}

textarea {
    color: white !important;
    -webkit-text-fill-color:black!important;
}
</style>
""", unsafe_allow_html=True)

QUESTIONS= [
    
    {

        "question_no": 126,
        "question": "What is Markdown?",
        "options": {
            "A": "A lightweight markup language",
            "B": "A programming language",
            "C": "A database",
            "D": "An operating system"
        },
        "answer": "A"
    },
    {
        "question_no": 127,
        "question": "Markdown is mainly used to:",
        "options": {
            "A": "Format text",
            "B": "Create CPUs",
            "C": "Repair hardware",
            "D": "Install software"
        },
        "answer": "A"
    },
    {
        "question_no": 128,
        "question": "Which symbol creates a level-1 heading in Markdown?",
        "options": {
            "A": "#",
            "B": "*",
            "C": ">",
            "D": "-"
        },
        "answer": "A"
    },
    {
        "question_no": 129,
        "question": "Which Markdown syntax creates bold text?",
        "options": {
            "A": "**Bold**",
            "B": "*Bold*",
            "C": "__Bold__",
            "D": "#Bold"
        },
        "answer": "A"
    },
    {
        "question_no": 130,
        "question": "Which Markdown syntax creates italic text?",
        "options": {
            "A": "*Italic*",
            "B": "_Italic_",
            "C": "#Italic",
            "D": ">Italic"
        },
        "answer": "A"
    },
    {
        "question_no": 131,
        "question": "Which symbol creates a bullet list?",
        "options": {
            "A": "-",
            "B": "#",
            "C": "$",
            "D": "@"
        },
        "answer": "A"
    },
    {
        "question_no": 132,
        "question": "Which Markdown syntax creates a hyperlink?",
        "options": {
            "A": "[Google](https://google.com)",
            "B": "<Google>",
            "C": "Google{}",
            "D": "(Google)"
        },
        "answer": "A"
    },
    {
        "question_no": 133,
        "question": "Which syntax inserts an image?",
        "options": {
            "A": "![Alt](image.png)",
            "B": "Image",
            "C": "#Image",
            "D": "<img>"
        },
        "answer": "A"
    },
    {
        "question_no": 134,
        "question": "Markdown is popular because it is:",
        "options": {
            "A": "Easy to read and write",
            "B": "Complex",
            "C": "Hardware dependent",
            "D": "Slow"
        },
        "answer": "A"
    },
    {
        "question_no": 135,
        "question": "Which tag represents a paragraph in HTML?",
        "options": {
            "A": "<p>",
            "B": "<h1>",
            "C": "<img>",
            "D": "<ul>"
        },
        "answer": "A"
    },
    {
        "question_no": 136,
        "question": "HTML stands for:",
        "options": {
            "A": "HyperText Markup Language",
            "B": "Hyper Transfer Machine Language",
            "C": "High Text Machine Language",
            "D": "Hyper Technical Markup Language"
        },
        "answer": "A"
    },
    {
        "question_no": 137,
        "question": "HTML is used to:",
        "options": {
            "A": "Structure web pages",
            "B": "Train AI models",
            "C": "Manage databases",
            "D": "Create operating systems"
        },
        "answer": "A"
    },
    {
        "question_no": 138,
        "question": "Which HTML tag creates the largest heading?",
        "options": {
            "A": "<h1>",
            "B": "<h6>",
            "C": "<head>",
            "D": "<title>"
        },
        "answer": "A"
    },
    {
        "question_no": 139,
        "question": "Which HTML tag creates a hyperlink?",
        "options": {
            "A": "<a>",
            "B": "<p>",
            "C": "<img>",
            "D": "<div>"
        },
        "answer": "A"
    },
    {
        "question_no": 140,
        "question": "Which attribute specifies the destination of a hyperlink?",
        "options": {
            "A": "href",
            "B": "src",
            "C": "alt",
            "D": "class"
        },
        "answer": "A"
    },
    {
        "question_no": 141,
        "question": "Which HTML tag inserts an image?",
        "options": {
            "A": "<img>",
            "B": "<picture>",
            "C": "<photo>",
            "D": "<image>"
        },
        "answer": "A"
    },
{
        "question_no": 142,
        "question": "The src attribute specifies:",
        "options": {
            "A": "Image location",
            "B": "Font size",
            "C": "Page title",
            "D": "Link color"
        },
        "answer": "A"
    },
{
        "question_no": 143,
        "question": "The alt attribute provides:",
        "options": {
            "A": "Alternative text for an image",
            "B": "Font style",
            "C": "Image size",
            "D": "Hyperlink"
        },
        "answer": "A"
    },
{
        "question_no": 144,
        "question": "Which HTML tag creates an unordered list?",
        "options": {
            "A": "<ul>",
            "B": "<ol>",
            "C": "<li>",
            "D": "<list>"
        },
        "answer": "A"
    },
{
        "question_no": 145,
        "question": "Which HTML tag creates an ordered list?",
        "options": {
            "A": "<ol>",
            "B": "<ul>",
            "C": "<li>",
            "D": "<order>"
        },
        "answer": "A"
    },
{
        "question_no": 146,
        "question": "Which HTML tag represents a list item?",
        "options": {
            "A": "<li>",
            "B": "<list>",
            "C": "<item>",
            "D": "<ul>"
        },
        "answer": "A"
    },
{
        "question_no": 147,
        "question": "Markdown heading ## converts to:",
        "options": {
            "A": "<h2>",
            "B": "<h1>",
            "C": "<p>",
            "D": "<h3>"
        },
        "answer": "A"
    },
{
        "question_no": 148,
        "question": "Markdown is often converted into:",
        "options": {
            "A": "HTML",
            "B": "Java",
            "C": "Python",
            "D": "SQL"
        },
        "answer": "A"
    },
{
        "question_no": 149,
        "question": "Which HTML tag emphasizes text?",
        "options": {
            "A": "<strong>",
            "B": "<head>",
            "C": "<html>",
            "D": "<body>"
        },
        "answer": "A"
    },
{
        "question_no": 150,
        "question": "Which Markdown syntax creates inline code?",
        "options": {
            "A": "`code`",
            "B": "code",
            "C": "#code",
            "D": ">code"
        },
        "answer": "A"
    }
]

{
        "question_no": 175,
        "question": "The main objective of Module 5 is to:",
        "options": {
            "A": "Learn Markdown formatting and understand how it converts to HTML",
            "B": "Build operating systems",
            "C": "Learn database administration",
            "D": "Configure computer networks"
        },
        "answer": "A"
    }



# ---------------- SESSION ----------------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "questions" not in st.session_state:
    st.session_state.questions = random.sample(
        QUESTIONS,
        len(QUESTIONS)
    )

# ---------------- HOME PAGE ----------------

if st.session_state.page == "home":

    st.title("📚 MCQs Quiz 2026")

    st.markdown("""
    ## Welcome

    This website is temporarily used for MCQ Quiz 2026.

    ### Features
    - 60 Seconds Per Question
    - Progress Bar
    - Pass / Fail
    - Leaderboard
    - Certificate
    - Review Answers
    """)

    name = st.text_input("Enter Your Name")

    if st.button("🚀 Start Quiz"):

        if not name:
            st.warning("Please enter your name.")
            st.stop()

        st.session_state.name = name
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.start_time = time.time()
        st.session_state.page = "quiz"

        st.rerun()

# ---------------- QUIZ PAGE ----------------

elif st.session_state.page == "quiz":

    total = len(st.session_state.questions)

    if st.session_state.current_question >= total:
        st.session_state.page = "result"
        st.rerun()

    q = st.session_state.questions[
        st.session_state.current_question
    ]

    st.title("📚 Section A")

    progress = (
        st.session_state.current_question + 1
    ) / total

    st.progress(progress)

    elapsed = int(
        time.time() - st.session_state.start_time
    )

    remaining = max(0, 60 - elapsed)

    st.warning(
        f"⏱ Time Left: {remaining} seconds"
    )

    if remaining == 0:

        st.error("Time Up!")

        st.session_state.current_question += 1
        st.session_state.start_time = time.time()

        st.rerun()

    st.subheader(
        f"Question {st.session_state.current_question + 1}"
    )

    st.write(q["question"])

    selected = st.radio(
        "Choose Answer",
        q["options"]
    )

    if st.button("Next"):

        st.session_state.answers[
            st.session_state.current_question
        ] = selected

        if selected == q["answer"]:
            st.session_state.score += 1

        st.session_state.current_question += 1
        st.session_state.start_time = time.time()

        st.rerun()

# ---------------- RESULT PAGE ----------------

elif st.session_state.page == "result":

    total = len(st.session_state.questions)

    score = st.session_state.score

    percent = (score / total) * 100

    st.title("🎉 Quiz Finished")

    st.metric("Score", f"{score}/{total}")
    st.metric("Percentage", f"{percent:.2f}%")

    if percent >= 50:
        st.success("✅ PASS")
    else:
        st.error("❌ FAIL")

    # Leaderboard CSV

    leaderboard_file = "leaderboard.csv"

    row = pd.DataFrame([
        {
            "Name": st.session_state.name,
            "Score": score,
            "Percentage": percent,
            "Date": datetime.now()
        }
    ])

    try:
        old = pd.read_csv(leaderboard_file)
        row = pd.concat(
            [old, row],
            ignore_index=True
        )
    except:
        pass

    row.to_csv(
        leaderboard_file,
        index=False
    )

    st.subheader("🏆 Leaderboard")

    st.dataframe(
        row.sort_values(
            "Score",
            ascending=False
        )
    )

    if st.button("🎓 View Certificate"):
        st.session_state.page = "certificate"
        st.rerun()

    st.subheader("Review Answers")

    for i, q in enumerate(
        st.session_state.questions
    ):

        st.write(f"### Q{i+1}")

        user_answer = st.session_state.answers.get(
            i,
            "No Answer"
        )

        for option in q["options"]:

            if option == q["answer"]:
                st.success(f"✅ {option}")

            elif option == user_answer:
                st.error(f"❌ {option}")

            else:
                st.write(option)

        st.info(q["explanation"])

# ---------------- CERTIFICATE ----------------

elif st.session_state.page == "certificate":

    st.title("🎓 Certificate")

    st.markdown(f"""
    # Certificate of Participation

    Presented To

    ## {st.session_state.name}

    Successfully completed

    **MCQs Quiz 2026**

    Score: {st.session_state.score}

    Date: {datetime.now().strftime('%d-%m-%Y')}
    """)

    st.download_button(
        "📄 Download Certificate",
        data=f"""
Certificate of Participation

Name: {st.session_state.name}

Score: {st.session_state.score}
""",
        file_name="certificate.txt"
    )
    # ---------------- RESTART QUIZ ----------------

if st.button("🔄 Take Test Again"):

    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answers = {}

    st.session_state.questions = random.sample(
        QUESTIONS,
        len(QUESTIONS)
    )

    st.session_state.start_time = time.time()

    st.session_state.page = "quiz"

    st.rerun()