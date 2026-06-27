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
# SECTION 4: AI Prompting in 2026
# 50 MCQs
# ==========================

QUESTIONS = [

{
    "question": "What is the primary goal of prompting in 2026?",
    "options": [
        "Writing longer prompts only",
        "Giving AI sufficient context to achieve a goal",
        "Using complex vocabulary",
        "Avoiding specifications"
    ],
    "answer": "Giving AI sufficient context to achieve a goal"
},

{
    "question": "What is Context Engineering?",
    "options": [
        "Building CPUs",
        "Designing and supplying the right information to AI",
        "Installing browsers",
        "Creating databases"
    ],
    "answer": "Designing and supplying the right information to AI"
},

{
    "question": "Which produces better results?",
    "options": [
        "Vague requests",
        "Clear specifications",
        "Random instructions",
        "Short commands only"
    ],
    "answer": "Clear specifications"
},

{
    "question": "A specification should include:",
    "options": [
        "Goals and requirements",
        "Keyboard settings",
        "Screen size",
        "Browser version"
    ],
    "answer": "Goals and requirements"
},

{
    "question": "What is role prompting?",
    "options": [
        "Giving AI a specific role or perspective",
        "Installing permissions",
        "Creating user accounts",
        "Database access"
    ],
    "answer": "Giving AI a specific role or perspective"
},

{
    "question": "Which is a good role prompt?",
    "options": [
        "Act as a senior software architect.",
        "Use electricity.",
        "Increase RAM.",
        "Open BIOS."
    ],
    "answer": "Act as a senior software architect."
},

{
    "question": "Why provide examples?",
    "options": [
        "To reduce clarity",
        "To demonstrate expected output format",
        "To slow AI down",
        "To increase token costs"
    ],
    "answer": "To demonstrate expected output format"
},

{
    "question": "Structured output means:",
    "options": [
        "Organized response format",
        "Random text generation",
        "Browser settings",
        "Hardware configuration"
    ],
    "answer": "Organized response format"
},

{
    "question": "Which output is more reliable?",
    "options": [
        "Defined JSON structure",
        "Unspecified format",
        "Random paragraphs",
        "Mixed formatting"
    ],
    "answer": "Defined JSON structure"
},

{
    "question": "What improves AI performance most?",
    "options": [
        "Better context",
        "Better monitor",
        "Faster mouse",
        "Larger keyboard"
    ],
    "answer": "Better context"
},

{
    "question": "AI should be given:",
    "options": [
        "Constraints",
        "Confusion",
        "Contradictions",
        "Random data"
    ],
    "answer": "Constraints"
},

{
    "question": "Constraints help AI:",
    "options": [
        "Produce targeted outputs",
        "Become slower",
        "Forget context",
        "Avoid reasoning"
    ],
    "answer": "Produce targeted outputs"
},

{
    "question": "A good prompt usually contains:",
    "options": [
        "Objective",
        "Context",
        "Constraints",
        "All of the above"
    ],
    "answer": "All of the above"
},

{
    "question": "Iteration means:",
    "options": [
        "Refining prompts and outputs",
        "Restarting computers",
        "Formatting disks",
        "Reinstalling browsers"
    ],
    "answer": "Refining prompts and outputs"
},

{
    "question": "Prompt evaluation helps:",
    "options": [
        "Measure quality",
        "Reduce quality",
        "Remove context",
        "Disable AI"
    ],
    "answer": "Measure quality"
},

{
    "question": "What is a system instruction?",
    "options": [
        "High-level guidance for AI behavior",
        "A motherboard component",
        "A browser extension",
        "A monitor setting"
    ],
    "answer": "High-level guidance for AI behavior"
},

{
    "question": "Modern prompting focuses more on:",
    "options": [
        "Collaboration",
        "Trick questions",
        "Hidden commands",
        "Keyword stuffing"
    ],
    "answer": "Collaboration"
},

{
    "question": "Why specify audience?",
    "options": [
        "To tailor communication",
        "To reduce accuracy",
        "To confuse AI",
        "To increase latency"
    ],
    "answer": "To tailor communication"
},

{
    "question": "Which prompt is better?",
    "options": [
        "Explain AI.",
        "Explain AI to a 12-year-old using simple examples.",
        "AI",
        "Tell me something."
    ],
    "answer": "Explain AI to a 12-year-old using simple examples."
},

{
    "question": "AI agents benefit from:",
    "options": [
        "Clear instructions",
        "Ambiguity",
        "Missing requirements",
        "No goals"
    ],
    "answer": "Clear instructions"
},

# 21–50 TRUE/FALSE

{"question":"Context is often more important than wording.","options":["True","False"],"answer":"True"},
{"question":"Examples improve output quality.","options":["True","False"],"answer":"True"},
{"question":"Specifications reduce ambiguity.","options":["True","False"],"answer":"True"},
{"question":"Constraints are useful.","options":["True","False"],"answer":"True"},
{"question":"Structured outputs improve reliability.","options":["True","False"],"answer":"True"},
{"question":"AI should be given goals.","options":["True","False"],"answer":"True"},
{"question":"Iteration improves results.","options":["True","False"],"answer":"True"},
{"question":"Prompt evaluation is valuable.","options":["True","False"],"answer":"True"},
{"question":"Role prompting can improve performance.","options":["True","False"],"answer":"True"},
{"question":"Audience matters.","options":["True","False"],"answer":"True"},
{"question":"Vague prompts usually perform better.","options":["True","False"],"answer":"False"},
{"question":"Context Engineering is important.","options":["True","False"],"answer":"True"},
{"question":"Specifications help AI understand tasks.","options":["True","False"],"answer":"True"},
{"question":"Examples clarify expectations.","options":["True","False"],"answer":"True"},
{"question":"AI works best without requirements.","options":["True","False"],"answer":"False"},
{"question":"Goal clarity improves outputs.","options":["True","False"],"answer":"True"},
{"question":"Constraints guide behavior.","options":["True","False"],"answer":"True"},
{"question":"JSON is an example of structured output.","options":["True","False"],"answer":"True"},
{"question":"AI can follow specifications.","options":["True","False"],"answer":"True"},
{"question":"Context quality matters.","options":["True","False"],"answer":"True"},
{"question":"Good prompts reduce ambiguity.","options":["True","False"],"answer":"True"},
{"question":"AI agents need instructions.","options":["True","False"],"answer":"True"},
{"question":"Prompt refinement is useful.","options":["True","False"],"answer":"True"},
{"question":"Examples are valuable.","options":["True","False"],"answer":"True"},
{"question":"Audience definition helps communication.","options":["True","False"],"answer":"True"},
{"question":"Specifications define requirements.","options":["True","False"],"answer":"True"},
{"question":"Iteration is part of prompting.","options":["True","False"],"answer":"True"},
{"question":"Role prompting can provide expertise framing.","options":["True","False"],"answer":"True"},
{"question":"Structured outputs are useful for automation.","options":["True","False"],"answer":"True"},
{"question":"Prompting is becoming more about Context Engineering.","options":["True","False"],"answer":"True"}

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

    This website is used for the MCQ Quiz 2026.

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
