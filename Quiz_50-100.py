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
QUESTIONS = [

{
    "question": "Why start in the browser?",
    "options": [
        "Easier access to AI tools",
        "Better gaming",
        "More RAM",
        "Better networking"
    ],
    "answer": "Easier access to AI tools"
},

{
    "question": "Browser-first learning reduces:",
    "options": [
        "Learning",
        "Setup friction",
        "Productivity",
        "Context"
    ],
    "answer": "Setup friction"
},

{
    "question": "What is the primary goal of browser-first learning?",
    "options": [
        "Build outcomes quickly",
        "Install Linux",
        "Learn hardware",
        "Configure servers"
    ],
    "answer": "Build outcomes quickly"
},

{
    "question": "Browser-based AI tools require:",
    "options": [
        "Internet access",
        "GPU cluster",
        "Data center",
        "Enterprise hardware"
    ],
    "answer": "Internet access"
},

{
    "question": "Which is a browser-based AI tool?",
    "options": [
        "ChatGPT",
        "BIOS",
        "Router",
        "CPU"
    ],
    "answer": "ChatGPT"
},

{
    "question": "Browser-first encourages:",
    "options": [
        "Rapid experimentation",
        "Slow learning",
        "Hardware assembly",
        "Network design"
    ],
    "answer": "Rapid experimentation"
},

{
    "question": "The main workspace becomes:",
    "options": [
        "Web applications",
        "Motherboard",
        "BIOS",
        "Operating system kernel"
    ],
    "answer": "Web applications"
},

{
    "question": "AI-native productivity focuses on:",
    "options": [
        "Outcomes",
        "Hardware",
        "Networking",
        "Assembly language"
    ],
    "answer": "Outcomes"
},

{
    "question": "Learning by doing is:",
    "options": [
        "Encouraged",
        "Discouraged",
        "Optional",
        "Obsolete"
    ],
    "answer": "Encouraged"
},

{
    "question": "Browser-first lowers:",
    "options": [
        "Entry barriers",
        "Internet access",
        "CPU performance",
        "RAM usage"
    ],
    "answer": "Entry barriers"
},

{
    "question": "Cloud AI tools typically require:",
    "options": [
        "Browser and internet",
        "Server rack",
        "GPU farm",
        "Custom hardware"
    ],
    "answer": "Browser and internet"
},

{
    "question": "What matters more than setup?",
    "options": [
        "Workflows",
        "Hardware",
        "Drivers",
        "BIOS"
    ],
    "answer": "Workflows"
},

{
    "question": "AI workflows are:",
    "options": [
        "Repeatable AI-assisted processes",
        "Hardware upgrades",
        "Network configurations",
        "Databases"
    ],
    "answer": "Repeatable AI-assisted processes"
},

{
    "question": "Fast feedback loops help:",
    "options": [
        "Learning",
        "Hardware",
        "Electricity",
        "Networking"
    ],
    "answer": "Learning"
},

{
    "question": "Browser-first aligns with:",
    "options": [
        "AI-Native development",
        "Hardware manufacturing",
        "Networking careers",
        "Electronics repair"
    ],
    "answer": "AI-Native development"
},

{
    "question": "Which mindset is promoted?",
    "options": [
        "Experimentation",
        "Fear of mistakes",
        "Manual repetition",
        "Avoiding AI"
    ],
    "answer": "Experimentation"
},

{
    "question": "AI tools help with:",
    "options": [
        "Research and content creation",
        "Replacing electricity",
        "Building CPUs",
        "Manufacturing chips"
    ],
    "answer": "Research and content creation"
},

{
    "question": "Browser-first learning emphasizes:",
    "options": [
        "Accessibility",
        "Hardware",
        "Servers",
        "Operating systems"
    ],
    "answer": "Accessibility"
},

{
    "question": "Clear objectives improve:",
    "options": [
        "AI outputs",
        "Hardware",
        "Storage",
        "Monitors"
    ],
    "answer": "AI outputs"
},

{
    "question": "The biggest advantage is:",
    "options": [
        "Starting immediately",
        "Bigger computers",
        "Better processors",
        "Faster networks"
    ],
    "answer": "Starting immediately"
},

# 21-50 True/False Style

{
    "question": "Browser-first learning reduces setup complexity.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "AI tools require custom hardware to begin.",
    "options": ["True", "False"],
    "answer": "False"
},

{
    "question": "Web applications are central to browser-first learning.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Experimentation is encouraged in AI-native learning.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Browser-first learning increases entry barriers.",
    "options": ["True", "False"],
    "answer": "False"
},

{
    "question": "Internet access is usually required for cloud AI tools.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Workflows are more important than setup details.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "AI workflows are repeatable processes.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Fast feedback loops improve learning.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Browser-first aligns with AI-native development.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "AI tools can help with research.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Accessibility is a major benefit of browser-first learning.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Clear objectives improve AI outputs.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "AI-native learning discourages experimentation.",
    "options": ["True", "False"],
    "answer": "False"
},

{
    "question": "Learning by doing is encouraged.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Cloud AI tools need enterprise hardware.",
    "options": ["True", "False"],
    "answer": "False"
},

{
    "question": "Browser-first learning allows immediate participation.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "AI workflows are only for developers.",
    "options": ["True", "False"],
    "answer": "False"
},

{
    "question": "Browser-based tools support rapid iteration.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Web applications can be used as AI workspaces.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "AI-native productivity focuses on outcomes.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Hardware knowledge is required before using AI tools.",
    "options": ["True", "False"],
    "answer": "False"
},

{
    "question": "Browser-first learning lowers setup friction.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Cloud AI services are accessible through browsers.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Fast feedback loops help users improve quickly.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Accessibility helps more people learn AI.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Starting immediately is a key browser-first advantage.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Experimentation supports better learning outcomes.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "AI tools are useful for content creation.",
    "options": ["True", "False"],
    "answer": "True"
},

{
    "question": "Browser-first learning supports AI-native workflows.",
    "options": ["True", "False"],
    "answer": "True"
}
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
