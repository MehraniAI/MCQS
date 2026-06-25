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
    -webkit-text-fill-color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- QUESTIONS ----------------
# ==========================
# SECTION 5: Markdown In, HTML Out
# 50 MCQs
# ==========================

QUESTIONS = [

{
    "question": "Markdown is:",
    "options": [
        "A lightweight markup language",
        "A database",
        "A browser",
        "An operating system"
    ],
    "answer": "A lightweight markup language"
},

{
    "question": "HTML stands for:",
    "options": [
        "HyperText Markup Language",
        "High Transfer Machine Language",
        "Hyper Tool Management Logic",
        "Home Text Markup Layer"
    ],
    "answer": "HyperText Markup Language"
},

{
    "question": "Markdown is mainly used for:",
    "options": [
        "Writing formatted content easily",
        "Building CPUs",
        "Networking",
        "Graphics cards"
    ],
    "answer": "Writing formatted content easily"
},

{
    "question": "Which creates a heading in Markdown?",
    "options": [
        "# Heading",
        "@ Heading",
        "$ Heading",
        "% Heading"
    ],
    "answer": "# Heading"
},

{
    "question": "Which Markdown syntax creates bold text?",
    "options": [
        "**text**",
        "//text//",
        "%%text%%",
        "##text##"
    ],
    "answer": "**text**"
},

{
    "question": "Which Markdown syntax creates italic text?",
    "options": [
        "*text*",
        "##text##",
        "@@text@@",
        "++text++"
    ],
    "answer": "*text*"
},

{
    "question": "Which symbol creates a bullet list?",
    "options": [
        "-",
        "$",
        "@",
        "&"
    ],
    "answer": "-"
},

{
    "question": "HTML uses:",
    "options": [
        "Tags",
        "Tokens only",
        "Variables only",
        "APIs only"
    ],
    "answer": "Tags"
},

{
    "question": "Which HTML tag creates a heading?",
    "options": [
        "<h1>",
        "<img>",
        "<div>",
        "<table>"
    ],
    "answer": "<h1>"
},

{
    "question": "Which HTML tag creates a paragraph?",
    "options": [
        "<p>",
        "<img>",
        "<a>",
        "<ul>"
    ],
    "answer": "<p>"
},

{
    "question": "Which Markdown creates a link?",
    "options": [
        "[Text](URL)",
        "{Text}",
        "<link>",
        "@url"
    ],
    "answer": "[Text](URL)"
},

{
    "question": "HTML is interpreted by:",
    "options": [
        "Web browsers",
        "CPUs only",
        "Routers",
        "Databases"
    ],
    "answer": "Web browsers"
},

{
    "question": "Markdown is easier than:",
    "options": [
        "Writing raw HTML",
        "Using browsers",
        "Reading text",
        "Opening websites"
    ],
    "answer": "Writing raw HTML"
},

{
    "question": "Which HTML tag displays images?",
    "options": [
        "<img>",
        "<p>",
        "<h1>",
        "<ul>"
    ],
    "answer": "<img>"
},

{
    "question": "Markdown can be converted into:",
    "options": [
        "HTML",
        "PDF",
        "Documentation",
        "All of the above"
    ],
    "answer": "All of the above"
},

{
    "question": "Which HTML tag creates a hyperlink?",
    "options": [
        "<a>",
        "<img>",
        "<h1>",
        "<div>"
    ],
    "answer": "<a>"
},

{
    "question": "What does <ul> represent?",
    "options": [
        "Unordered List",
        "Underline",
        "URL Link",
        "Upload List"
    ],
    "answer": "Unordered List"
},

{
    "question": "What does <ol> represent?",
    "options": [
        "Ordered List",
        "Object Link",
        "Online List",
        "Output Layout"
    ],
    "answer": "Ordered List"
},

{
    "question": "What does <div> represent?",
    "options": [
        "Container Element",
        "Image Tag",
        "Heading Tag",
        "Link Tag"
    ],
    "answer": "Container Element"
},

{
    "question": "Which tag is commonly used for page sections?",
    "options": [
        "<div>",
        "<img>",
        "<a>",
        "<br>"
    ],
    "answer": "<div>"
},

# 21–50 TRUE/FALSE

{"question":"Markdown improves readability.","options":["True","False"],"answer":"True"},
{"question":"HTML structures web pages.","options":["True","False"],"answer":"True"},
{"question":"<a> creates hyperlinks.","options":["True","False"],"answer":"True"},
{"question":"<ul> means unordered list.","options":["True","False"],"answer":"True"},
{"question":"<ol> means ordered list.","options":["True","False"],"answer":"True"},
{"question":"Browsers render HTML.","options":["True","False"],"answer":"True"},
{"question":"Markdown is human-friendly.","options":["True","False"],"answer":"True"},
{"question":"HTML uses opening and closing tags.","options":["True","False"],"answer":"True"},
{"question":"Markdown is common in documentation.","options":["True","False"],"answer":"True"},
{"question":"Headings organize content.","options":["True","False"],"answer":"True"},
{"question":"HTML supports semantic structure.","options":["True","False"],"answer":"True"},
{"question":"Accessibility matters in HTML.","options":["True","False"],"answer":"True"},
{"question":"Markdown is plain text.","options":["True","False"],"answer":"True"},
{"question":"HTML can contain images.","options":["True","False"],"answer":"True"},
{"question":"HTML can contain links.","options":["True","False"],"answer":"True"},
{"question":"Markdown requires a compiler.","options":["True","False"],"answer":"False"},
{"question":"HTML is a programming language.","options":["True","False"],"answer":"False"},
{"question":"Markdown supports lists.","options":["True","False"],"answer":"True"},
{"question":"Documentation often uses Markdown.","options":["True","False"],"answer":"True"},
{"question":"AI can generate Markdown and HTML.","options":["True","False"],"answer":"True"},
{"question":"# creates headings.","options":["True","False"],"answer":"True"},
{"question":"**text** creates bold text.","options":["True","False"],"answer":"True"},
{"question":"*text* creates italic text.","options":["True","False"],"answer":"True"},
{"question":"HTML uses tags.","options":["True","False"],"answer":"True"},
{"question":"<img> displays images.","options":["True","False"],"answer":"True"},
{"question":"<p> defines a paragraph.","options":["True","False"],"answer":"True"},
{"question":"<h1> defines a heading.","options":["True","False"],"answer":"True"},
{"question":"Markdown is lightweight.","options":["True","False"],"answer":"True"},
{"question":"Links are supported in Markdown.","options":["True","False"],"answer":"True"},
{"question":"AI can convert Markdown to HTML.","options":["True","False"],"answer":"True"}

]
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
