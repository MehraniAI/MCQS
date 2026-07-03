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

QUESTIONS = [

{
    "question": "What is the primary goal of the Agent Factory AI Program?",
    "options": [
        "Learning graphic design",
        "Building AI agents and AI-powered applications",
        "Learning accounting",
        "Mobile phone repair"
    ],
    "answer": "Building AI agents and AI-powered applications"
},

{
    "question": "Agent Factory focuses primarily on:",
    "options": [
        "Traditional programming only",
        "AI agents, prompting, and automation",
        "Game development",
        "Networking"
    ],
    "answer": "AI agents, prompting, and automation"
},

{
    "question": "The first module of the course is mainly about:",
    "options": [
        "Python programming",
        "Orientation and introduction to the program",
        "Database management",
        "Robotics"
    ],
    "answer": "Orientation and introduction to the program"
},

{
    "question": "Students are expected to study the provided materials before:",
    "options": [
        "Graduation",
        "Final project",
        "Mid-Term Certification Exam",
        "Internship"
    ],
    "answer": "Mid-Term Certification Exam"
},

{
    "question": "The first certification mentioned is:",
    "options": [
        "AI Expert",
        "Agent Foundations and Prompting (L1: P1-AFAP)",
        "Python Professional",
        "Cloud Associate"
    ],
    "answer": "Agent Foundations and Prompting (L1: P1-AFAP)"
},

{
    "question": "The program mainly teaches students to build:",
    "options": [
        "Websites only",
        "AI Agents",
        "Android games",
        "Operating systems"
    ],
    "answer": "AI Agents"
},

{
    "question": "AI agents are designed to:",
    "options": [
        "Perform tasks intelligently",
        "Replace hardware",
        "Build computer chips",
        "Repair computers"
    ],
    "answer": "Perform tasks intelligently"
},

{
    "question": "Orientation helps students:",
    "options": [
        "Understand the course structure",
        "Learn advanced mathematics",
        "Assemble computers",
        "Study networking"
    ],
    "answer": "Understand the course structure"
},

{
    "question": "The curriculum emphasizes:",
    "options": [
        "Practical AI learning",
        "Mechanical engineering",
        "Civil engineering",
        "Chemistry"
    ],
    "answer": "Practical AI learning"
},

{
    "question": "Which skill is central to the Agent Factory program?",
    "options": [
        "Prompt Engineering",
        "AutoCAD",
        "Photoshop",
        "Excel VBA"
    ],
    "answer": "Prompt Engineering"
},

{
    "question": "AFAP stands for:",
    "options": [
        "Agent Foundations And Prompting",
        "Artificial Future AI Platform",
        "Advanced Functional AI Programming",
        "Agent Framework Application Program"
    ],
    "answer": "Agent Foundations And Prompting"
},

{
    "question": "AI agents commonly interact with:",
    "options": [
        "Tools and APIs",
        "Washing machines",
        "Television antennas",
        "Cameras only"
    ],
    "answer": "Tools and APIs"
},

{
    "question": "One benefit of AI agents is:",
    "options": [
        "Task automation",
        "Increased paperwork",
        "Manual calculations only",
        "Reduced internet access"
    ],
    "answer": "Task automation"
},

{
    "question": "Orientation explains:",
    "options": [
        "Course expectations",
        "Cricket rules",
        "Physics formulas",
        "Cooking recipes"
    ],
    "answer": "Course expectations"
},

{
    "question": "Students should follow:",
    "options": [
        "The official learning modules",
        "Random internet articles only",
        "Old textbooks only",
        "Unverified social media posts"
    ],
    "answer": "The official learning modules"
},

{
    "question": "The Agent Factory program encourages:",
    "options": [
        "Continuous learning",
        "Avoiding technology",
        "Memorization only",
        "Manual office work"
    ],
    "answer": "Continuous learning"
},

{
    "question": "AI agents can:",
    "options": [
        "Help automate workflows",
        "Cook food physically",
        "Repair roads",
        "Manufacture cars independently"
    ],
    "answer": "Help automate workflows"
},

{
    "question": "The certification exam mainly evaluates:",
    "options": [
        "Understanding of the course modules",
        "Football skills",
        "Driving ability",
        "Medical knowledge"
    ],
    "answer": "Understanding of the course modules"
},

{
    "question": "The program is designed for:",
    "options": [
        "Beginners and learners interested in AI",
        "Pilots only",
        "Doctors only",
        "Lawyers only"
    ],
    "answer": "Beginners and learners interested in AI"
},

{
    "question": "Orientation introduces students to:",
    "options": [
        "Learning resources",
        "Farming equipment",
        "Electrical wiring",
        "Biology experiments"
    ],
    "answer": "Learning resources"
},

{
    "question": "AI agents use prompts to:",
    "options": [
        "Receive instructions",
        "Charge batteries",
        "Install RAM",
        "Print documents"
    ],
    "answer": "Receive instructions"
},

{
    "question": "One important habit for success is:",
    "options": [
        "Practicing regularly",
        "Ignoring assignments",
        "Skipping modules",
        "Avoiding documentation"
    ],
    "answer": "Practicing regularly"
},

{
    "question": "The course emphasizes:",
    "options": [
        "Hands-on practice",
        "Theory only",
        "History only",
        "Memorizing definitions"
    ],
    "answer": "Hands-on practice"
},

{
    "question": "Students should use official documentation because it is:",
    "options": [
        "Reliable",
        "Outdated",
        "Unrelated",
        "Incomplete"
    ],
    "answer": "Reliable"
},

{
    "question": "AI agents often help users by:",
    "options": [
        "Solving problems",
        "Damaging computers",
        "Deleting hardware",
        "Formatting keyboards"
    ],
    "answer": "Solving problems"
},

{
    "question": "The orientation module is intended to:",
    "options": [
        "Build a strong foundation",
        "Teach advanced networking",
        "Replace later modules",
        "Skip AI basics"
    ],
    "answer": "Build a strong foundation"
},

{
    "question": "Certification Level L1 represents:",
    "options": [
        "Beginner/Foundation level",
        "Expert level",
        "Doctorate",
        "Internship"
    ],
    "answer": "Beginner/Foundation level"
},

{
    "question": "Students are encouraged to:",
    "options": [
        "Ask questions and practice",
        "Ignore exercises",
        "Memorize without understanding",
        "Skip documentation"
    ],
    "answer": "Ask questions and practice"
},

{
    "question": "AI agents primarily assist by:",
    "options": [
        "Performing intelligent tasks",
        "Replacing electricity",
        "Manufacturing CPUs",
        "Building houses"
    ],
    "answer": "Performing intelligent tasks"
},

{
    "question": "Prompting is the process of:",
    "options": [
        "Giving instructions to AI",
        "Repairing computers",
        "Installing Windows",
        "Creating hardware"
    ],
    "answer": "Giving instructions to AI"
},

{
    "question": "Agent Factory prepares students for:",
    "options": [
        "AI development",
        "Plumbing",
        "Civil construction",
        "Mechanical repairs"
    ],
    "answer": "AI development"
},

{
    "question": "Students should complete modules:",
    "options": [
        "In sequence",
        "Randomly",
        "Backwards only",
        "None of the above"
    ],
    "answer": "In sequence"
},

{
    "question": "Learning AI requires:",
    "options": [
        "Curiosity and practice",
        "Expensive hardware only",
        "No internet",
        "No study"
    ],
    "answer": "Curiosity and practice"
},

{
    "question": "Orientation explains course:",
    "options": [
        "Objectives",
        "Cricket scores",
        "Banking rules",
        "Tax laws"
    ],
    "answer": "Objectives"
},

{
    "question": "AI agents can improve:",
    "options": [
        "Productivity",
        "Pollution",
        "Traffic jams",
        "Weather"
    ],
    "answer": "Productivity"
},

{
    "question": "Students should rely on:",
    "options": [
        "Official course materials",
        "Rumors",
        "Random guesses",
        "Fake notes"
    ],
    "answer": "Official course materials"
},

{
    "question": "AI agents are built to:",
    "options": [
        "Assist users",
        "Damage systems",
        "Replace humans entirely",
        "Disable software"
    ],
    "answer": "Assist users"
},

{
    "question": "The orientation module is important because it:",
    "options": [
        "Sets expectations",
        "Teaches chemistry",
        "Covers accounting",
        "Focuses on networking"
    ],
    "answer": "Sets expectations"
},

{
    "question": "One goal of Agent Factory is to:",
    "options": [
        "Enable AI-powered solutions",
        "Teach plumbing",
        "Repair vehicles",
        "Manufacture electronics"
    ],
    "answer": "Enable AI-powered solutions"
},

{
    "question": "Students should review documentation:",
    "options": [
        "Regularly",
        "Never",
        "Once a year",
        "After graduation only"
    ],
    "answer": "Regularly"
},

{
    "question": "AI agents can work with:",
    "options": [
        "External tools and services",
        "Only calculators",
        "Only printers",
        "Only browsers"
    ],
    "answer": "External tools and services"
},

{
    "question": "Successful students usually:",
    "options": [
        "Practice consistently",
        "Skip exercises",
        "Avoid projects",
        "Ignore updates"
    ],
    "answer": "Practice consistently"
},

{
    "question": "The first module mainly introduces:",
    "options": [
        "The Agent Factory ecosystem",
        "Physics",
        "Mathematics",
        "Networking"
    ],
    "answer": "The Agent Factory ecosystem"
},

{
    "question": "Prompt engineering is important because it:",
    "options": [
        "Improves AI responses",
        "Repairs computers",
        "Builds hardware",
        "Creates internet connections"
    ],
    "answer": "Improves AI responses"
},

{
    "question": "Students preparing for certification should:",
    "options": [
        "Study all listed modules",
        "Study only one module",
        "Skip documentation",
        "Ignore practice"
    ],
    "answer": "Study all listed modules"
},

{
    "question": "AI learning becomes more effective through:",
    "options": [
        "Practice",
        "Guessing",
        "Memorization only",
        "Avoiding projects"
    ],
    "answer": "Practice"
},

{
    "question": "The course is designed to be:",
    "options": [
        "Practical and hands-on",
        "Entirely theoretical",
        "Offline only",
        "Hardware-focused only"
    ],
    "answer": "Practical and hands-on"
},

{
    "question": "AI agents help users by:",
    "options": [
        "Automating tasks",
        "Reducing storage space",
        "Damaging software",
        "Replacing electricity"
    ],
    "answer": "Automating tasks"
},

{
    "question": "The orientation module should be completed:",
    "options": [
        "Before advanced modules",
        "After graduation",
        "At the end of the course",
        "Only after the exam"
    ],
    "answer": "Before advanced modules"
},

{
    "question": "The overall purpose of Module 1 is to:",
    "options": [
        "Introduce the program, expectations, and AI agent learning journey",
        "Teach advanced Python",
        "Build mobile games",
        "Learn database optimization"
    ],
    "answer": "Introduce the program, expectations, and AI agent learning journey"
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