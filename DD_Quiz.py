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
.stApp {
    background-color: #0E1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- QUESTIONS ----------------

QUESTIONS = [

{
    "question": "What is a Digital FTE?",
    "options": [
        "Digital Full-Time Employee",
        "Digital File Transfer Engine",
        "Data Function Tool Engine",
        "Distributed Task Executor"
    ],
    "answer": "Digital Full-Time Employee"
},

{
    "question": "What is the 10-80-10 model?",
    "options": [
        "Human executes all work",
        "Human directs, AI executes, Human verifies",
        "AI directs, Human executes",
        "AI performs everything"
    ],
    "answer": "Human directs, AI executes, Human verifies"
},

{
    "question": "In the 10-80-10 model, who performs the 80%?",
    "options": [
        "Customer",
        "Manager",
        "AI",
        "Developer"
    ],
    "answer": "AI"
},

{
    "question": "The final 10% represents:",
    "options": [
        "Deployment",
        "Coding",
        "Verification",
        "Marketing"
    ],
    "answer": "Verification"
},

{
    "question": "Agent Factory primarily promotes:",
    "options": [
        "Traditional programming",
        "AI-Native Development",
        "Hardware engineering",
        "Networking"
    ],
    "answer": "AI-Native Development"
},

{
    "question": "AI-Native means:",
    "options": [
        "AI integrated from the beginning",
        "AI added later",
        "No AI used",
        "Manual workflows"
    ],
    "answer": "AI integrated from the beginning"
},

{
    "question": "Human value in AI workflows mainly comes from:",
    "options": [
        "Typing speed",
        "Judgment and direction",
        "RAM size",
        "Internet speed"
    ],
    "answer": "Judgment and direction"
},

{
    "question": "Digital FTEs are used to:",
    "options": [
        "Scale knowledge work",
        "Increase storage",
        "Improve hardware",
        "Manage networks"
    ],
    "answer": "Scale knowledge work"
},

{
    "question": "What improves AI output quality most?",
    "options": [
        "Better monitor",
        "More RAM",
        "Better context",
        "Faster keyboard"
    ],
    "answer": "Better context"
},

{
    "question": "AI should be viewed as:",
    "options": [
        "Perfect intelligence",
        "A collaborator",
        "A replacement for thinking",
        "A database"
    ],
    "answer": "A collaborator"
},

{
    "question": "Why is verification necessary?",
    "options": [
        "AI can hallucinate",
        "AI is slow",
        "AI lacks storage",
        "AI lacks internet"
    ],
    "answer": "AI can hallucinate"
},

{
    "question": "Which is NOT part of 10-80-10?",
    "options": [
        "Direct",
        "Execute",
        "Verify",
        "Ignore"
    ],
    "answer": "Ignore"
},

{
    "question": "AI excels at:",
    "options": [
        "Scaling repetitive work",
        "Perfect truth",
        "Legal decisions",
        "Human emotions"
    ],
    "answer": "Scaling repetitive work"
},

{
    "question": "Context engineering refers to:",
    "options": [
        "Building CPUs",
        "Managing information given to AI",
        "Creating hardware",
        "Installing browsers"
    ],
    "answer": "Managing information given to AI"
},

{
    "question": "Human-AI collaboration combines:",
    "options": [
        "Human judgment + AI scale",
        "Human speed + AI emotions",
        "Human memory + AI hardware",
        "Human coding + AI networking"
    ],
    "answer": "Human judgment + AI scale"
},

{
    "question": "Agent Factory emphasizes:",
    "options": [
        "Outcome-focused work",
        "Syntax memorization",
        "Hardware design",
        "Networking"
    ],
    "answer": "Outcome-focused work"
},

{
    "question": "Digital FTEs help organizations:",
    "options": [
        "Scale operations",
        "Reduce storage",
        "Replace databases",
        "Increase electricity"
    ],
    "answer": "Scale operations"
},

{
    "question": "AI-generated work should always be:",
    "options": [
        "Verified",
        "Ignored",
        "Deleted",
        "Trusted blindly"
    ],
    "answer": "Verified"
},

{
    "question": "Which skill becomes more important in AI?",
    "options": [
        "Problem definition",
        "Typing speed",
        "Keyboard shortcuts",
        "Hardware assembly"
    ],
    "answer": "Problem definition"
},

{
    "question": "The most important takeaway from Orientation is:",
    "options": [
        "Humans direct AI",
        "AI replaces humans",
        "Coding disappears",
        "Browsers are obsolete"
    ],
    "answer": "Humans direct AI"
},
{
    "question": "What does the first 10% in the 10-80-10 model represent?",
    "options": [
        "Verification",
        "Direction",
        "Execution",
        "Deployment"
    ],
    "answer": "Direction"
},

{
    "question": "What does the 80% in the 10-80-10 model represent?",
    "options": [
        "Human review",
        "Planning",
        "AI execution",
        "Testing"
    ],
    "answer": "AI execution"
},

{
    "question": "What does the final 10% in the 10-80-10 model represent?",
    "options": [
        "Prompting",
        "Coding",
        "Verification",
        "Training"
    ],
    "answer": "Verification"
},

{
    "question": "Digital FTEs are designed to augment:",
    "options": [
        "Knowledge workers",
        "Networks",
        "Hardware",
        "Databases"
    ],
    "answer": "Knowledge workers"
},

{
    "question": "The main goal of AI-Native Development is:",
    "options": [
        "More hardware",
        "Better outcomes",
        "More coding",
        "Less automation"
    ],
    "answer": "Better outcomes"
},

{
    "question": "What should humans primarily provide to AI?",
    "options": [
        "Storage",
        "Bandwidth",
        "Direction",
        "Electricity"
    ],
    "answer": "Direction"
},

{
    "question": "Which capability makes AI valuable for organizations?",
    "options": [
        "Monitor size",
        "Scalability",
        "Mouse speed",
        "CPU color"
    ],
    "answer": "Scalability"
},

{
    "question": "AI can help increase:",
    "options": [
        "Productivity",
        "Screen brightness",
        "Electricity",
        "Hardware weight"
    ],
    "answer": "Productivity"
},

{
    "question": "What is the most important human responsibility when using AI?",
    "options": [
        "Networking",
        "Typing",
        "Verification",
        "Hardware setup"
    ],
    "answer": "Verification"
},

{
    "question": "AI systems should be treated as:",
    "options": [
        "Perfect experts",
        "Assistants",
        "Managers",
        "Databases"
    ],
    "answer": "Assistants"
},

{
    "question": "Human judgment is important because AI can:",
    "options": [
        "Make mistakes",
        "Use RAM",
        "Open browsers",
        "Connect networks"
    ],
    "answer": "Make mistakes"
},

{
    "question": "What helps AI produce better results?",
    "options": [
        "Quality context",
        "Expensive keyboard",
        "Large monitor",
        "Faster mouse"
    ],
    "answer": "Quality context"
},

{
    "question": "Which approach is encouraged by Agent Factory?",
    "options": [
        "Experimentation",
        "Avoiding AI",
        "Manual repetition",
        "Hardware repair"
    ],
    "answer": "Experimentation"
},

{
    "question": "AI-Native workflows focus on:",
    "options": [
        "Outcomes",
        "Syntax",
        "Hardware",
        "Networking"
    ],
    "answer": "Outcomes"
},

{
    "question": "Digital FTEs can help businesses:",
    "options": [
        "Scale work",
        "Reduce electricity",
        "Replace internet",
        "Increase heat"
    ],
    "answer": "Scale work"
},

{
    "question": "What is one risk of AI-generated content?",
    "options": [
        "Hallucinations",
        "Monitor damage",
        "Keyboard failure",
        "CPU melting"
    ],
    "answer": "Hallucinations"
},

{
    "question": "Humans should always review AI outputs before:",
    "options": [
        "Using them",
        "Typing",
        "Saving files",
        "Opening browsers"
    ],
    "answer": "Using them"
},

{
    "question": "What does AI-Native Development encourage?",
    "options": [
        "Working with AI from the start",
        "Ignoring AI",
        "Manual coding only",
        "Hardware assembly"
    ],
    "answer": "Working with AI from the start"
},

{
    "question": "Which quality is most valuable in AI collaboration?",
    "options": [
        "Clear thinking",
        "Fast typing",
        "Large monitor",
        "Gaming skills"
    ],
    "answer": "Clear thinking"
},

{
    "question": "The purpose of context engineering is to:",
    "options": [
        "Provide useful information",
        "Build hardware",
        "Install software",
        "Upgrade networks"
    ],
    "answer": "Provide useful information"
},

{
    "question": "AI works best when given:",
    "options": [
        "Clear objectives",
        "Random tasks",
        "No instructions",
        "Contradictions"
    ],
    "answer": "Clear objectives"
},

{
    "question": "The future workplace is expected to involve:",
    "options": [
        "Human-AI collaboration",
        "No technology",
        "Only humans",
        "Only robots"
    ],
    "answer": "Human-AI collaboration"
},

{
    "question": "AI can help automate:",
    "options": [
        "Repetitive tasks",
        "Human emotions",
        "Electricity generation",
        "Weather"
    ],
    "answer": "Repetitive tasks"
},

{
    "question": "What remains uniquely human in AI workflows?",
    "options": [
        "Judgment",
        "Token prediction",
        "Automation",
        "Scaling"
    ],
    "answer": "Judgment"
},

{
    "question": "Organizations use Digital FTEs to improve:",
    "options": [
        "Efficiency",
        "Screen size",
        "Power cables",
        "Keyboards"
    ],
    "answer": "Efficiency"
},

{
    "question": "AI output quality depends heavily on:",
    "options": [
        "Input quality",
        "Monitor size",
        "Mouse sensitivity",
        "Desk size"
    ],
    "answer": "Input quality"
},

{
    "question": "The orientation promotes a mindset of:",
    "options": [
        "Learning and experimentation",
        "Avoiding change",
        "Manual work only",
        "Hardware upgrades"
    ],
    "answer": "Learning and experimentation"
},

{
    "question": "AI should support humans rather than:",
    "options": [
        "Replace judgment",
        "Increase productivity",
        "Assist work",
        "Provide ideas"
    ],
    "answer": "Replace judgment"
},

{
    "question": "A successful AI workflow combines:",
    "options": [
        "Human oversight and AI execution",
        "AI only",
        "Humans only",
        "Hardware only"
    ],
    "answer": "Human oversight and AI execution"
},

{
    "question": "The key lesson of Orientation Presentation is:",
    "options": [
        "Humans lead, AI assists",
        "AI replaces everyone",
        "Hardware is everything",
        "Coding is obsolete"
    ],
    "answer": "Humans lead, AI assists"
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