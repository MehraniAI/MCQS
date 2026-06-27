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

# ---------------- QUESTIONS ----------------

QUESTIONS = [
    
# ---------------- QUESTIONS ----------------
# Question 51
{
    "question": "Why start in the browser?",
    "options": [
        "Easier access to AI tools",
        "Better gaming",
        "More RAM",
        "Better networking"
    ],
    "answer": "Easier access to AI tools",
    "explanation": "Starting in the browser lets users access AI tools immediately without installing software or configuring hardware."
},

# Question 52
{
    "question": "Browser-first learning reduces:",
    "options": [
        "Learning",
        "Setup friction",
        "Productivity",
        "Context"
    ],
    "answer": "Setup friction",
    "explanation": "Browser-first learning removes installation and setup difficulties, allowing users to begin learning quickly."
},

# Question 53
{
    "question": "What is the primary goal of browser-first learning?",
    "options": [
        "Build outcomes quickly",
        "Install Linux",
        "Learn hardware",
        "Configure servers"
    ],
    "answer": "Build outcomes quickly",
    "explanation": "The focus is on creating useful results instead of spending time configuring computers."
},

# Question 54
{
    "question": "Browser-based AI tools require:",
    "options": [
        "Internet access",
        "GPU cluster",
        "Data center",
        "Enterprise hardware"
    ],
    "answer": "Internet access",
    "explanation": "Most browser-based AI services only need a web browser and an internet connection."
},

# Question 55
{
    "question": "Which is a browser-based AI tool?",
    "options": [
        "ChatGPT",
        "BIOS",
        "Router",
        "CPU"
    ],
    "answer": "ChatGPT",
    "explanation": "ChatGPT works directly inside a web browser without requiring software installation."
},

# Question 56
{
    "question": "Browser-first encourages:",
    "options": [
        "Rapid experimentation",
        "Slow learning",
        "Hardware assembly",
        "Network design"
    ],
    "answer": "Rapid experimentation",
    "explanation": "Users can test ideas quickly and improve through continuous experimentation."
},

# Question 57
{
    "question": "The main workspace becomes:",
    "options": [
        "Web applications",
        "Motherboard",
        "BIOS",
        "Operating system kernel"
    ],
    "answer": "Web applications",
    "explanation": "Most AI work is performed through online web applications."
},

# Question 58
{
    "question": "AI-native productivity focuses on:",
    "options": [
        "Outcomes",
        "Hardware",
        "Networking",
        "Assembly language"
    ],
    "answer": "Outcomes",
    "explanation": "AI-native productivity emphasizes achieving results rather than worrying about technical setup."
},

# Question 59
{
    "question": "Learning by doing is:",
    "options": [
        "Encouraged",
        "Discouraged",
        "Optional",
        "Obsolete"
    ],
    "answer": "Encouraged",
    "explanation": "Hands-on practice helps learners understand AI tools more effectively."
},

# Question 60
{
    "question": "Browser-first lowers:",
    "options": [
        "Entry barriers",
        "Internet access",
        "CPU performance",
        "RAM usage"
    ],
    "answer": "Entry barriers",
    "explanation": "Anyone with internet access can begin using AI tools without expensive hardware."
},

# Question 61
{
    "question": "Cloud AI tools typically require:",
    "options": [
        "Browser and internet",
        "Server rack",
        "GPU farm",
        "Custom hardware"
    ],
    "answer": "Browser and internet",
    "explanation": "Cloud services perform processing online, requiring only a browser and internet connection."
},

# Question 62
{
    "question": "What matters more than setup?",
    "options": [
        "Workflows",
        "Hardware",
        "Drivers",
        "BIOS"
    ],
    "answer": "Workflows",
    "explanation": "Well-designed workflows improve efficiency more than spending time configuring systems."
},

# Question 63
{
    "question": "AI workflows are:",
    "options": [
        "Repeatable AI-assisted processes",
        "Hardware upgrades",
        "Network configurations",
        "Databases"
    ],
    "answer": "Repeatable AI-assisted processes",
    "explanation": "AI workflows are repeatable steps that consistently help complete tasks."
},

# Question 64
{
    "question": "Fast feedback loops help:",
    "options": [
        "Learning",
        "Hardware",
        "Electricity",
        "Networking"
    ],
    "answer": "Learning",
    "explanation": "Immediate feedback allows users to improve quickly by correcting mistakes."
},

# Question 65
{
    "question": "Browser-first aligns with:",
    "options": [
        "AI-Native development",
        "Hardware manufacturing",
        "Networking careers",
        "Electronics repair"
    ],
    "answer": "AI-Native development",
    "explanation": "Browser-first learning supports AI-native development by making AI tools instantly available."
},

# Question 66
{
    "question": "Which mindset is promoted?",
    "options": [
        "Experimentation",
        "Fear of mistakes",
        "Manual repetition",
        "Avoiding AI"
    ],
    "answer": "Experimentation",
    "explanation": "Trying different prompts and approaches leads to better AI skills."
},

# Question 67
{
    "question": "AI tools help with:",
    "options": [
        "Research and content creation",
        "Replacing electricity",
        "Building CPUs",
        "Manufacturing chips"
    ],
    "answer": "Research and content creation",
    "explanation": "AI assists with writing, research, coding, brainstorming, and creating digital content."
},

# Question 68
{
    "question": "Browser-first learning emphasizes:",
    "options": [
        "Accessibility",
        "Hardware",
        "Servers",
        "Operating systems"
    ],
    "answer": "Accessibility",
    "explanation": "AI becomes available to more people regardless of technical background."
},

# Question 69
{
    "question": "Clear objectives improve:",
    "options": [
        "AI outputs",
        "Hardware",
        "Storage",
        "Monitors"
    ],
    "answer": "AI outputs",
    "explanation": "Clear instructions help AI produce more accurate and relevant responses."
},

# Question 70
{
    "question": "The biggest advantage is:",
    "options": [
        "Starting immediately",
        "Bigger computers",
        "Better processors",
        "Faster networks"
    ],
    "answer": "Starting immediately",
    "explanation": "Users can begin learning instantly without complicated installation."
},

# Question 71
{
    "question": "Browser-first learning reduces setup complexity.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Most browser-based AI tools require little or no installation."
},

# Question 72
{
    "question": "AI tools require custom hardware to begin.",
    "options": ["True", "False"],
    "answer": "False",
    "explanation": "Modern AI tools are designed to run in browsers on ordinary computers."
},

# Question 73
{
    "question": "Web applications are central to browser-first learning.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Browser-first learning depends mainly on online web applications."
},

# Question 74
{
    "question": "Experimentation is encouraged in AI-native learning.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Testing different prompts helps users understand AI more effectively."
},

# Question 75
{
    "question": "Browser-first learning increases entry barriers.",
    "options": ["True", "False"],
    "answer": "False",
    "explanation": "Browser-first learning lowers barriers by making AI easy to access."
},

# Question 76
{
    "question": "Internet access is usually required for cloud AI tools.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Cloud AI services operate online, so internet access is generally required."
},

# Question 77
{
    "question": "Workflows are more important than setup details.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Efficient workflows improve productivity more than spending time on configuration."
},

# Question 78
{
    "question": "AI workflows are repeatable processes.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Workflows consist of repeatable steps that can be reused for similar tasks."
},

# Question 79
{
    "question": "Fast feedback loops improve learning.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Immediate feedback helps learners identify and fix mistakes quickly."
},

# Question 80
{
    "question": "Browser-first aligns with AI-native development.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Browser-first supports AI-native development by providing quick access to AI tools."
},

# Question 81
{
    "question": "AI tools can help with research.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "AI can summarize information, organize ideas, and assist with research."
},

# Question 82
{
    "question": "Accessibility is a major benefit of browser-first learning.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Anyone with a browser and internet connection can start using AI."
},

# Question 83
{
    "question": "Clear objectives improve AI outputs.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Specific goals produce more accurate and useful AI responses."
},

# Question 84
{
    "question": "AI-native learning discourages experimentation.",
    "options": ["True", "False"],
    "answer": "False",
    "explanation": "Experimentation is encouraged because it helps users learn better."
},

# Question 85
{
    "question": "Learning by doing is encouraged.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Practical experience is one of the best ways to master AI tools."
},

# Question 86
{
    "question": "Cloud AI tools need enterprise hardware.",
    "options": ["True", "False"],
    "answer": "False",
    "explanation": "Heavy processing happens in the cloud, not on the user's computer."
},

# Question 87
{
    "question": "Browser-first learning allows immediate participation.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Users can begin learning instantly without complicated setup."
},

# Question 88
{
    "question": "AI workflows are only for developers.",
    "options": ["True", "False"],
    "answer": "False",
    "explanation": "AI workflows are useful for students, teachers, writers, designers, and many other users."
},

# Question 89
{
    "question": "Browser-based tools support rapid iteration.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Users can quickly revise prompts and improve results."
},

# Question 90
{
    "question": "Web applications can be used as AI workspaces.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Many AI platforms operate completely through web applications."
},

# Question 91
{
    "question": "AI-native productivity focuses on outcomes.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "The emphasis is on solving problems and achieving valuable results."
},

# Question 92
{
    "question": "Hardware knowledge is required before using AI tools.",
    "options": ["True", "False"],
    "answer": "False",
    "explanation": "Most AI tools are beginner-friendly and require little technical knowledge."
},

# Question 93
{
    "question": "Browser-first learning lowers setup friction.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Using a browser eliminates most installation and configuration steps."
},

# Question 94
{
    "question": "Cloud AI services are accessible through browsers.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Most cloud AI platforms can be accessed directly through a web browser."
},

# Question 95
{
    "question": "Fast feedback loops help users improve quickly.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Quick feedback allows users to refine prompts and develop better skills."
},

# Question 96
{
    "question": "Accessibility helps more people learn AI.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Easy access allows beginners and professionals alike to use AI."
},

# Question 97
{
    "question": "Starting immediately is a key browser-first advantage.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Browser-first learning removes delays caused by installation and setup."
},

# Question 98
{
    "question": "Experimentation supports better learning outcomes.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Testing different ideas helps users discover the best AI techniques."
},

# Question 99
{
    "question": "AI tools are useful for content creation.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "AI can generate text, presentations, code, images, summaries, and many other forms of content."
},

# Question 100
{
    "question": "Browser-first learning supports AI-native workflows.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Browser-first learning makes AI tools easy to access and integrate into everyday workflows."
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