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

# ---------------- QUESTIONS ----------------# 
# ==========================
# SECTION 7: Skills and Connectors
# 50 MCQs
# ==========================

QUESTIONS = [

{
    "question": "A Skill is:",
    "options": [
        "Reusable capability",
        "Hardware component",
        "Browser tab",
        "Database"
    ],
    "answer": "Reusable capability"
},

{
    "question": "A Connector is:",
    "options": [
        "Integration with external systems",
        "CPU component",
        "RAM module",
        "Monitor"
    ],
    "answer": "Integration with external systems"
},

{
    "question": "API stands for:",
    "options": [
        "Application Programming Interface",
        "Artificial Programming Intelligence",
        "Application Process Installer",
        "Advanced Program Integration"
    ],
    "answer": "Application Programming Interface"
},

{
    "question": "Connectors are primarily used to:",
    "options": [
        "Access external services",
        "Upgrade hardware",
        "Increase RAM",
        "Replace browsers"
    ],
    "answer": "Access external services"
},

{
    "question": "Skills should be:",
    "options": [
        "Reusable",
        "Disposable",
        "Hidden",
        "Random"
    ],
    "answer": "Reusable"
},

{
    "question": "Tool calling allows AI to:",
    "options": [
        "Use external capabilities",
        "Upgrade CPUs",
        "Change monitors",
        "Increase internet speed"
    ],
    "answer": "Use external capabilities"
},

{
    "question": "Connectors often interact with:",
    "options": [
        "APIs",
        "CPUs",
        "Monitors",
        "Routers"
    ],
    "answer": "APIs"
},

{
    "question": "Workflows can combine:",
    "options": [
        "Skills and Connectors",
        "CPU and RAM",
        "Monitor and Keyboard",
        "Router and Modem"
    ],
    "answer": "Skills and Connectors"
},

{
    "question": "Modular design improves:",
    "options": [
        "Maintainability",
        "Confusion",
        "Complexity only",
        "Cost only"
    ],
    "answer": "Maintainability"
},

{
    "question": "Skills can encapsulate:",
    "options": [
        "Business Logic",
        "Workflows",
        "Processes",
        "All of the above"
    ],
    "answer": "All of the above"
},

{
    "question": "Which technology enables systems to communicate?",
    "options": [
        "API",
        "Monitor",
        "Keyboard",
        "CPU"
    ],
    "answer": "API"
},

{
    "question": "A connector helps AI:",
    "options": [
        "Interact with external tools",
        "Build processors",
        "Increase storage",
        "Install Windows"
    ],
    "answer": "Interact with external tools"
},

{
    "question": "Skills help improve:",
    "options": [
        "Reusability",
        "Confusion",
        "Hardware",
        "Networking"
    ],
    "answer": "Reusability"
},

{
    "question": "An example of a connector is:",
    "options": [
        "Email API",
        "Keyboard",
        "CPU",
        "Monitor"
    ],
    "answer": "Email API"
},

{
    "question": "Which is an external service?",
    "options": [
        "Email provider",
        "Motherboard",
        "CPU",
        "RAM"
    ],
    "answer": "Email provider"
},

{
    "question": "AI agents often use:",
    "options": [
        "Tools",
        "Monitors",
        "Hard drives",
        "Printers"
    ],
    "answer": "Tools"
},

{
    "question": "What is a workflow?",
    "options": [
        "Series of steps to complete a task",
        "Hardware upgrade",
        "Network cable",
        "CPU instruction"
    ],
    "answer": "Series of steps to complete a task"
},

{
    "question": "Skills are building blocks for:",
    "options": [
        "AI systems",
        "Monitors",
        "Processors",
        "Graphics cards"
    ],
    "answer": "AI systems"
},

{
    "question": "Connectors expand:",
    "options": [
        "Capabilities",
        "RAM",
        "Monitor size",
        "CPU speed"
    ],
    "answer": "Capabilities"
},

{
    "question": "Automation often relies on:",
    "options": [
        "Skills and Connectors",
        "Hardware upgrades",
        "New monitors",
        "Bigger keyboards"
    ],
    "answer": "Skills and Connectors"
},

# 21–50 True / False

{"question":"APIs enable communication between systems.","options":["True","False"],"answer":"True"},
{"question":"Skills improve reusability.","options":["True","False"],"answer":"True"},
{"question":"Connectors support automation.","options":["True","False"],"answer":"True"},
{"question":"Agents can use tools.","options":["True","False"],"answer":"True"},
{"question":"External integrations expand capabilities.","options":["True","False"],"answer":"True"},
{"question":"Modular systems scale better.","options":["True","False"],"answer":"True"},
{"question":"Email services can be connected through connectors.","options":["True","False"],"answer":"True"},
{"question":"Databases can be connected using connectors.","options":["True","False"],"answer":"True"},
{"question":"Tool usage is important in modern AI agents.","options":["True","False"],"answer":"True"},
{"question":"Skills and connectors are foundational AI-agent concepts.","options":["True","False"],"answer":"True"},
{"question":"A connector is a hardware device.","options":["True","False"],"answer":"False"},
{"question":"Skills should be reusable.","options":["True","False"],"answer":"True"},
{"question":"Connectors often use APIs.","options":["True","False"],"answer":"True"},
{"question":"Workflows can combine multiple skills.","options":["True","False"],"answer":"True"},
{"question":"AI agents can interact with external services.","options":["True","False"],"answer":"True"},
{"question":"Business logic can be encapsulated in skills.","options":["True","False"],"answer":"True"},
{"question":"Automation reduces manual work.","options":["True","False"],"answer":"True"},
{"question":"Modularity improves maintainability.","options":["True","False"],"answer":"True"},
{"question":"Tool calling expands AI functionality.","options":["True","False"],"answer":"True"},
{"question":"Connectors help integrate systems.","options":["True","False"],"answer":"True"},
{"question":"APIs are used for communication.","options":["True","False"],"answer":"True"},
{"question":"Skills are reusable building blocks.","options":["True","False"],"answer":"True"},
{"question":"Agents cannot use external tools.","options":["True","False"],"answer":"False"},
{"question":"Connectors can access cloud services.","options":["True","False"],"answer":"True"},
{"question":"Workflows help organize processes.","options":["True","False"],"answer":"True"},
{"question":"External systems increase AI capabilities.","options":["True","False"],"answer":"True"},
{"question":"Tool calling is unnecessary in AI systems.","options":["True","False"],"answer":"False"},
{"question":"Skills make systems easier to maintain.","options":["True","False"],"answer":"True"},
{"question":"Connectors enable integration with other platforms.","options":["True","False"],"answer":"True"},
{"question":"Skills and connectors are important for automation.","options":["True","False"],"answer":"True"}

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

    remaining = max(0, 30 - elapsed)

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
