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

# ---------------- DARK THEME ----------------+

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
        "question_no": 76,
        "question": "Browser-based platforms usually support:",
        "options": {
            "A": "Collaboration",
            "B": "Hardware repair",
            "C": "BIOS updates",
            "D": "Chip manufacturing"
        },
        "answer": "A"
    },
    {
        "question_no": 77,
        "question": "Most browser-based AI tools are updated by:",
        "options": {
            "A": "Service providers",
            "B": "End users",
            "C": "Internet cables",
            "D": "Printers"
        },
        "answer": "A"
    },
    {
        "question_no": 78,
        "question": "Which feature helps access the same work from multiple devices?",
        "options": {
            "A": "Cloud storage",
            "B": "USB cables",
            "C": "Local DVDs",
            "D": "CD-ROM"
        },
        "answer": "A"
    },
    {
        "question_no": 79,
        "question": "Browser-based development reduces dependency on:",
        "options": {
            "A": "High-end local hardware",
            "B": "Electricity",
            "C": "Internet",
            "D": "Accounts"
        },
        "answer": "A"
    },
    {
        "question_no": 80,
        "question": "AI tools in the browser generally provide:",
        "options": {
            "A": "Easy onboarding",
            "B": "Hardware assembly",
            "C": "Chip fabrication",
            "D": "Mechanical design"
        },
        "answer": "A"
    },
    {
        "question_no": 81,
        "question": "Modern AI education emphasizes:",
        "options": {
            "A": "Practical learning",
            "B": "Memorization only",
            "C": "No exercises",
            "D": "Offline-only learning"
        },
        "answer": "A"
    },
    {
        "question_no": 82,
        "question": "A browser-based editor is useful because it:",
        "options": {
            "A": "Requires little setup",
            "B": "Needs special hardware",
            "C": "Cannot save files",
            "D": "Only works offline"
        },
        "answer": "A"
    },
    {
        "question_no": 83,
        "question": "The cloud enables:",
        "options": {
            "A": "Remote computing",
            "B": "Local-only computing",
            "C": "Hardware replacement",
            "D": "BIOS programming"
        },
        "answer": "A"
    },
    {
        "question_no": 84,
        "question": "Which is an important digital skill?",
        "options": {
            "A": "Navigating browser-based tools",
            "B": "Repairing CPUs",
            "C": "Welding",
            "D": "Plumbing"
        },
        "answer": "A"
    },
    {
        "question_no": 85,
        "question": "Browser applications are generally accessed using:",
        "options": {
            "A": "URLs",
            "B": "HDMI cables",
            "C": "USB ports",
            "D": "Power adapters"
        },
        "answer": "A"
    },
    {
        "question_no": 86,
        "question": "AI platforms often include:",
        "options": {
            "A": "User dashboards",
            "B": "Engine oil",
            "C": "Car batteries",
            "D": "BIOS chips"
        },
        "answer": "A"
    },
    {
        "question_no": 87,
        "question": "Which statement is TRUE?",
        "options": {
            "A": "Browser-based tools make AI more accessible.",
            "B": "Browsers require programming chips.",
            "C": "Browsers cannot access AI.",
            "D": "Cloud computing is offline."
        },
        "answer": "A"
    },
    {
        "question_no": 88,
        "question": "Online AI services commonly use:",
        "options": {
            "A": "Secure login systems",
            "B": "Fax machines",
            "C": "CD players",
            "D": "Typewriters"
        },
        "answer": "A"
    },
    {
        "question_no": 89,
        "question": "Browser-based learning supports:",
        "options": {
            "A": "Flexibility",
            "B": "Less accessibility",
            "C": "Hardware dependence",
            "D": "Offline-only access"
        },
        "answer": "A"
    },
    {
        "question_no": 90,
        "question": "Cloud services help by:",
        "options": {
            "A": "Synchronizing data",
            "B": "Deleting browsers",
            "C": "Replacing monitors",
            "D": "Increasing keyboard size"
        },
        "answer": "A"
    },
    {
        "question_no": 91,
        "question": "Which is a common browser feature?",
        "options": {
            "A": "Tabs",
            "B": "CPU overclocking",
            "C": "RAM expansion",
            "D": "BIOS flashing"
        },
        "answer": "A"
    },
    {
        "question_no": 92,
        "question": "Students should keep browsers:",
        "options": {
            "A": "Updated",
            "B": "Uninstalled",
            "C": "Outdated forever",
            "D": "Disabled"
        },
        "answer": "A"
    },
    {
        "question_no": 93,
        "question": "Browser-based AI tools typically offer:",
        "options": {
            "A": "Cross-device access",
            "B": "Printer repair",
            "C": "Hard disk replacement",
            "D": "Network cables"
        },
        "answer": "A"
    },
    {
        "question_no": 94,
        "question": "The browser acts as the interface between:",
        "options": {
            "A": "Users and online services",
            "B": "CPU and RAM",
            "C": "Mouse and keyboard",
            "D": "Monitor and speakers"
        },
        "answer": "A"
    },
    {
        "question_no": 95,
        "question": "Cloud-hosted AI models execute primarily on:",
        "options": {
            "A": "Provider-managed servers",
            "B": "Your keyboard",
            "C": "USB drives",
            "D": "Local printers"
        },
        "answer": "A"
    },
    {
        "question_no": 96,
        "question": "Browser-first learning enables students to:",
        "options": {
            "A": "Focus on concepts before complex setup",
            "B": "Avoid learning AI",
            "C": "Replace programming languages",
            "D": "Build processors"
        },
        "answer": "A"
    },
    {
        "question_no": 97,
        "question": "Which practice improves security when using online tools?",
        "options": {
            "A": "Using strong passwords",
            "B": "Sharing passwords publicly",
            "C": "Ignoring updates",
            "D": "Using the same password everywhere"
        },
        "answer": "A"
    },
    {
        "question_no": 98,
        "question": "Browser-based AI platforms are popular because they are:",
        "options": {
            "A": "Convenient and accessible",
            "B": "Hardware-dependent",
            "C": "Offline-only",
            "D": "Difficult to use"
        },
        "answer": "A"
    },
    {
        "question_no": 99,
        "question": "The Foundations module emphasizes:",
        "options": {
            "A": "Building essential skills before advanced topics",
            "B": "Skipping the basics",
            "C": "Hardware repair",
            "D": "Database administration"
        },
        "answer": "A"
    },
    {
        "question_no": 100,
        "question": "The main outcome of Module 2 is that students can confidently:",
        "options": {
            "A": "Use browser-based tools as the foundation for learning AI",
            "B": "Build operating systems",
            "C": "Design CPUs",
            "D": "Assemble servers from scratch"
        },
        "answer": "A"
    }
]
{
        "question_no": 100,
        "question": "Prompt engineering is:",
        "options": {
            "A": "The process of designing effective prompts for AI",
            "B": "Repairing hardware",
            "C": "Installing Windows",
            "D": "Building CPUs"
        },
        "answer": "A"
},
{
        "question_no": 101,
        "question": "A good prompt should be:",
        "options": {
            "A": "Clear and specific",
            "B": "Confusing",
            "C": "Random",
            "D": "Very short only"
        },
        "answer": "A"
    },
{
        "question_no": 102,
        "question": "Which prompt provides the AI with a role?",
        "options": {
            "A": "Act as a teacher.",
            "B": "Hello",
            "C": "Computer",
            "D": "Random"
        },
        "answer": "A"
    },
{
        "question_no": 103,
        "question": "Why is context important in prompting?",
        "options": {
            "A": "It helps the AI understand the task",
            "B": "It increases RAM",
            "C": "It upgrades hardware",
            "D": "It changes the browser"
        },
        "answer": "A"
    },
{
        "question_no": 104,
        "question": "Which prompt is more effective?",
        "options": {
            "A": "Write a 100-word summary about AI for beginners.",
            "B": "AI",
            "C": "Write.",
            "D": "Help."
        },
        "answer": "A"
    },
{
        "question_no": 105,
        "question": "Few-shot prompting means:",
        "options": {
            "A": "Giving a few examples before asking the task",
            "B": "Asking one question",
            "C": "Using one computer",
            "D": "No examples"
        },
        "answer": "A"
    },
{
        "question_no": 106,
        "question": "Role prompting is:",
        "options": {
            "A": "Asking the AI to act in a specific role",
            "B": "Writing code",
            "C": "Opening a browser",
            "D": "Installing software"
        },
        "answer": "A"
    },
{
        "question_no": 107,
        "question": "Asking the AI to answer in a table is an example of specifying:",
        "options": {
            "A": "Output format",
            "B": "Hardware",
            "C": "Storage",
            "D": "Programming language"
        },
        "answer": "A"
    },
{
        "question_no": 108,
        "question": "Which prompt technique provides examples before asking the AI to perform a task?",
        "options": {
            "A": "Few-shot prompting",
            "B": "Zero-shot prompting",
            "C": "Random prompting",
            "D": "Browser prompting"
        },
        "answer": "A"
    },
{
        "question_no": 109,
        "question": "Zero-shot prompting means:",
        "options": {
            "A": "Asking the AI without giving examples",
            "B": "Giving ten examples",
            "C": "Writing code first",
            "D": "Training a new AI model"
        },
        "answer": "A"
    },
{
        "question_no": 110,
        "question": "One-shot prompting means:",
        "options": {
            "A": "Giving one example before the task",
            "B": "Asking one question only",
            "C": "Using one computer",
            "D": "Limiting the response to one sentence"
        },
        "answer": "A"
    },
{
        "question_no": 111,
        "question": "Which prompt is best for obtaining structured information?",
        "options": {
            "A": "Explain AI.",
            "B": "List five AI applications in a table with their benefits.",
            "C": "AI",
            "D": "Tell me everything."
        },
        "answer": "B"
    },
{
        "question_no": 112,
        "question": "Which of the following usually improves AI output?",
        "options": {
            "A": "Clear constraints",
            "B": "Ambiguous wording",
            "C": "Missing details",
            "D": "Contradictory instructions"
        },
        "answer": "A"
    },
{
        "question_no": 113,
        "question": "Asking the AI to summarize in 100 words specifies:",
        "options": {
            "A": "Length constraint",
            "B": "Hardware requirement",
            "C": "Programming language",
            "D": "Internet speed"
        },
        "answer": "A"
    },
{
        "question_no": 114,
        "question": "Which prompt is most effective?",
        "options": {
            "A": "Write.",
            "B": "Help.",
            "C": "Write a professional email requesting a meeting in under 150 words.",
            "D": "Email"
        },
        "answer": "C"
    },
{
        "question_no": 115,
        "question": "Iterative prompting means:",
        "options": {
            "A": "Improving prompts based on previous responses",
            "B": "Reinstalling the browser",
            "C": "Upgrading hardware",
            "D": "Restarting the computer"
        },
        "answer": "A"
    },
{
        "question_no": 116,
        "question": "Why is context important in prompting?",
        "options": {
            "A": "It helps the AI understand the task better.",
            "B": "It increases CPU speed.",
            "C": "It reduces internet usage.",
            "D": "It changes the programming language."
        },
        "answer": "A"
    },
{
        "question_no": 117,
        "question": "Which prompt asks for a specific audience?",
        "options": {
            "A": "Explain AI.",
            "B": "Explain AI to a 10-year-old student.",
            "C": "AI",
            "D": "Machine"
        },
        "answer": "B"
    },
{
        "question_no": 118,
        "question": "Which of the following is an example of a constraint?",
        "options": {
            "A": "Limit your answer to five bullet points.",
            "B": "Think about AI.",
            "C": "Write something.",
            "D": "Use any format."
        },
        "answer": "A"
    },
{
        "question_no": 119,
        "question": "What should you do if the AI response is incomplete?",
        "options": {
            "A": "Refine and clarify the prompt",
            "B": "Stop using AI",
            "C": "Restart the internet",
            "D": "Change the keyboard"
        },
        "answer": "A"
    },
{
        "question_no": 120,
        "question": "Prompt engineering is important because:",
        "options": {
            "A": "AI quality depends heavily on the instructions it receives",
            "B": "It increases RAM",
            "C": "It replaces programming languages",
            "D": "It repairs hardware"
        },
        "answer": "A"
    },
{
        "question_no": 121,
        "question": "Which prompt requests a comparison?",
        "options": {
            "A": "Define AI.",
            "B": "Compare Machine Learning and Deep Learning in a table.",
            "C": "Hello.",
            "D": "Computer"
        },
        "answer": "B"
    },
{
        "question_no": 122,
        "question": "Asking the AI to respond in JSON specifies the:",
        "options": {
            "A": "Output format",
            "B": "Programming language",
            "C": "Database",
            "D": "Browser"
        },
        "answer": "A"
    },
{
        "question_no": 123,
        "question": "Which is an example of role prompting?",
        "options": {
            "A": "Act as a cybersecurity expert.",
            "B": "Write code.",
            "C": "Open a browser.",
            "D": "Install Windows."
        },
        "answer": "A"
    },
{
        "question_no": 124,
        "question": "Which characteristic is NOT recommended for effective prompts?",
        "options": {
            "A": "Specificity",
            "B": "Clarity",
            "C": "Ambiguity",
            "D": "Relevant context"
        },
        "answer": "C"
    },
{
        "question_no": 125,
        "question": "The main goal of Module 4 is to:",
        "options": {
            "A": "Learn how to write effective prompts that produce accurate, useful AI responses",
            "B": "Learn hardware assembly",
            "C": "Study operating systems",
            "D": "Build databases"
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