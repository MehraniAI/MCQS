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

# ---------------- QUESTIONS ----------------# ==========================
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
    "answer": "A lightweight markup language",
    "explanation": "Markdown is a simple markup language used to format text easily."
},

{
    "question": "HTML stands for:",
    "options": [
        "HyperText Markup Language",
        "High Transfer Machine Language",
        "Hyper Tool Management Logic",
        "Home Text Markup Layer"
    ],
    "answer": "HyperText Markup Language",
    "explanation": "HTML is the standard language used to create web pages."
},

{
    "question": "Markdown is mainly used for:",
    "options": [
        "Writing formatted content easily",
        "Building CPUs",
        "Networking",
        "Graphics cards"
    ],
    "answer": "Writing formatted content easily",
    "explanation": "Markdown is used to write formatted text quickly without complex code."
},

{
    "question": "Which creates a heading in Markdown?",
    "options": [
        "# Heading",
        "@ Heading",
        "$ Heading",
        "% Heading"
    ],
    "answer": "# Heading",
    "explanation": "The # symbol is used to create headings in Markdown."
},

{
    "question": "Which Markdown syntax creates bold text?",
    "options": [
        "**text**",
        "//text//",
        "%%text%%",
        "##text##"
    ],
    "answer": "**text**",
    "explanation": "Double asterisks are used to make text bold in Markdown."
},

{
    "question": "Which Markdown syntax creates italic text?",
    "options": [
        "*text*",
        "##text##",
        "@@text@@",
        "++text++"
    ],
    "answer": "*text*",
    "explanation": "Single asterisks are used to make text italic in Markdown."
},

{
    "question": "Which symbol creates a bullet list?",
    "options": [
        "-",
        "$",
        "@",
        "&"
    ],
    "answer": "-",
    "explanation": "The dash (-) symbol creates bullet lists in Markdown."
},

{
    "question": "HTML uses:",
    "options": [
        "Tags",
        "Tokens only",
        "Variables only",
        "APIs only"
    ],
    "answer": "Tags",
    "explanation": "HTML uses tags to structure web content."
},

{
    "question": "Which HTML tag creates a heading?",
    "options": [
        "<h1>",
        "<img>",
        "<div>",
        "<table>"
    ],
    "answer": "<h1>",
    "explanation": "The <h1> tag is used for main headings in HTML."
},

{
    "question": "Which HTML tag creates a paragraph?",
    "options": [
        "<p>",
        "<img>",
        "<a>",
        "<ul>"
    ],
    "answer": "<p>",
    "explanation": "The <p> tag defines a paragraph in HTML."
},

{
    "question": "Which Markdown creates a link?",
    "options": [
        "[Text](URL)",
        "{Text}",
        "<link>",
        "@url"
    ],
    "answer": "[Text](URL)",
    "explanation": "Markdown links use square brackets for text and parentheses for URLs."
},

{
    "question": "HTML is interpreted by:",
    "options": [
        "Web browsers",
        "CPUs only",
        "Routers",
        "Databases"
    ],
    "answer": "Web browsers",
    "explanation": "Web browsers read and render HTML pages."
},

{
    "question": "Markdown is easier than:",
    "options": [
        "Writing raw HTML",
        "Using browsers",
        "Reading text",
        "Opening websites"
    ],
    "answer": "Writing raw HTML",
    "explanation": "Markdown is simpler and faster than writing full HTML code."
},

{
    "question": "Which HTML tag displays images?",
    "options": [
        "<img>",
        "<p>",
        "<h1>",
        "<ul>"
    ],
    "answer": "<img>",
    "explanation": "The <img> tag is used to display images in HTML."
},

{
    "question": "Markdown can be converted into:",
    "options": [
        "HTML",
        "PDF",
        "Documentation",
        "All of the above"
    ],
    "answer": "All of the above",
    "explanation": "Markdown can be converted into multiple formats like HTML and PDF."
},

{
    "question": "Which HTML tag creates a hyperlink?",
    "options": [
        "<a>",
        "<img>",
        "<h1>",
        "<div>"
    ],
    "answer": "<a>",
    "explanation": "The <a> tag is used to create clickable links."
},

{
    "question": "What does <ul> represent?",
    "options": [
        "Unordered List",
        "Underline",
        "URL Link",
        "Upload List"
    ],
    "answer": "Unordered List",
    "explanation": "<ul> is used for bullet point lists."
},

{
    "question": "What does <ol> represent?",
    "options": [
        "Ordered List",
        "Object Link",
        "Online List",
        "Output Layout"
    ],
    "answer": "Ordered List",
    "explanation": "<ol> is used for numbered lists."
},

{
    "question": "What does <div> represent?",
    "options": [
        "Container Element",
        "Image Tag",
        "Heading Tag",
        "Link Tag"
    ],
    "answer": "Container Element",
    "explanation": "<div> is used as a container for grouping elements."
},

{
    "question": "Which tag is commonly used for page sections?",
    "options": [
        "<div>",
        "<img>",
        "<a>",
        "<br>"
    ],
    "answer": "<div>",
    "explanation": "<div> is commonly used to structure sections of a webpage."
},

# TRUE / FALSE
{"question":"Markdown improves readability.","options":["True","False"],"answer":"True","explanation":"Markdown makes text easier to read and write."},
{"question":"HTML structures web pages.","options":["True","False"],"answer":"True","explanation":"HTML defines the structure of web pages."},
{"question":"<a> creates hyperlinks.","options":["True","False"],"answer":"True","explanation":"The <a> tag creates clickable links."},
{"question":"<ul> means unordered list.","options":["True","False"],"answer":"True","explanation":"<ul> is used for bullet lists."},
{"question":"<ol> means ordered list.","options":["True","False"],"answer":"True","explanation":"<ol> is used for numbered lists."},
{"question":"Browsers render HTML.","options":["True","False"],"answer":"True","explanation":"Browsers display HTML content."},
{"question":"Markdown is human-friendly.","options":["True","False"],"answer":"True","explanation":"Markdown is easy for humans to read and write."},
{"question":"HTML uses opening and closing tags.","options":["True","False"],"answer":"True","explanation":"Most HTML elements have opening and closing tags."},
{"question":"Markdown is common in documentation.","options":["True","False"],"answer":"True","explanation":"Markdown is widely used in README files and docs."},
{"question":"Headings organize content.","options":["True","False"],"answer":"True","explanation":"Headings help structure content clearly."},
{"question":"HTML supports semantic structure.","options":["True","False"],"answer":"True","explanation":"HTML includes semantic tags for meaning."},
{"question":"Accessibility matters in HTML.","options":["True","False"],"answer":"True","explanation":"Accessible HTML helps all users use websites."},
{"question":"Markdown is plain text.","options":["True","False"],"answer":"True","explanation":"Markdown is written as plain text with symbols."},
{"question":"HTML can contain images.","options":["True","False"],"answer":"True","explanation":"HTML supports embedding images."},
{"question":"HTML can contain links.","options":["True","False"],"answer":"True","explanation":"HTML allows hyperlinks using <a> tags."},
{"question":"Markdown requires a compiler.","options":["True","False"],"answer":"False","explanation":"Markdown does not need compilation."},
{"question":"HTML is a programming language.","options":["True","False"],"answer":"False","explanation":"HTML is a markup language, not programming."},
{"question":"Markdown supports lists.","options":["True","False"],"answer":"True","explanation":"Markdown supports bullet and numbered lists."},
{"question":"Documentation often uses Markdown.","options":["True","False"],"answer":"True","explanation":"Markdown is popular in documentation systems."},
{"question":"AI can generate Markdown and HTML.","options":["True","False"],"answer":"True","explanation":"AI tools can generate structured formats."},
{"question":"# creates headings.","options":["True","False"],"answer":"True","explanation":"# is used for headings in Markdown."},
{"question":"**text** creates bold text.","options":["True","False"],"answer":"True","explanation":"Double asterisks make text bold."},
{"question":"*text* creates italic text.","options":["True","False"],"answer":"True","explanation":"Single asterisks create italics."},
{"question":"HTML uses tags.","options":["True","False"],"answer":"True","explanation":"HTML is based on tags."},
{"question":"<img> displays images.","options":["True","False"],"answer":"True","explanation":"<img> is used for images."},
{"question":"<p> defines a paragraph.","options":["True","False"],"answer":"True","explanation":"<p> defines text paragraphs."},
{"question":"<h1> defines a heading.","options":["True","False"],"answer":"True","explanation":"<h1> is the main heading tag."},
{"question":"Markdown is lightweight.","options":["True","False"],"answer":"True","explanation":"Markdown is simple and lightweight."},
{"question":"Links are supported in Markdown.","options":["True","False"],"answer":"True","explanation":"Markdown supports hyperlink formatting."},
{"question":"AI can convert Markdown to HTML.","options":["True","False"],"answer":"True","explanation":"AI and tools can convert Markdown into HTML."}
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
    - 30 Seconds Per Question
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