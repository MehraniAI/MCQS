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
    "question": "The primary objective of the Foundations module is to:",
    "options": [
        "Learn advanced Python first",
        "Build a strong AI foundation using browser-based tools",
        "Learn networking",
        "Study operating systems"
    ],
    "answer": "Build a strong AI foundation using browser-based tools"
},

{
    "question": "Why does the course begin in the browser?",
    "options": [
        "It removes the need for complex software installation.",
        "Browsers are faster than all desktop apps.",
        "Browsers replace programming languages.",
        "Browsers work only with AI."
    ],
    "answer": "It removes the need for complex software installation."
},

{
    "question": "Which of the following is a benefit of browser-based learning?",
    "options": [
        "Easy access from almost any device",
        "Requires expensive hardware",
        "Cannot save work",
        "Works only offline"
    ],
    "answer": "Easy access from almost any device"
},

{
    "question": "Most modern AI applications are accessed through:",
    "options": [
        "Web browsers",
        "DVD drives",
        "Fax machines",
        "USB drives"
    ],
    "answer": "Web browsers"
},

{
    "question": "Cloud-based AI tools primarily run on:",
    "options": [
        "Remote servers",
        "Your keyboard",
        "Your monitor",
        "Your mouse"
    ],
    "answer": "Remote servers"
},

{
    "question": "One advantage of cloud computing is:",
    "options": [
        "Automatic updates",
        "Manual installation every day",
        "No internet required",
        "No storage available"
    ],
    "answer": "Automatic updates"
},

{
    "question": "Which device is commonly used to access browser-based AI tools?",
    "options": [
        "Laptop",
        "Smartphone",
        "Tablet",
        "All of the above"
    ],
    "answer": "All of the above"
},

{
    "question": "Browser-based AI development allows learners to:",
    "options": [
        "Start quickly",
        "Avoid learning completely",
        "Eliminate internet usage",
        "Replace programming forever"
    ],
    "answer": "Start quickly"
},

{
    "question": "A browser is primarily used to:",
    "options": [
        "Access websites and web applications",
        "Edit videos",
        "Build CPUs",
        "Repair hardware"
    ],
    "answer": "Access websites and web applications"
},

{
    "question": "Which is an example of a web browser?",
    "options": [
        "Chrome",
        "Excel",
        "Photoshop",
        "VLC"
    ],
    "answer": "Chrome"
},

{
    "question": "Browser-based tools are useful because they are:",
    "options": [
        "Platform-independent",
        "Windows-only",
        "Linux-only",
        "Mac-only"
    ],
    "answer": "Platform-independent"
},

{
    "question": "Most AI learning platforms require:",
    "options": [
        "Internet connectivity",
        "A gaming console",
        "A printer",
        "A scanner"
    ],
    "answer": "Internet connectivity"
},

{
    "question": "Browser-based environments reduce the need for:",
    "options": [
        "Local software installation",
        "Internet",
        "Accounts",
        "Learning"
    ],
    "answer": "Local software installation"
},

{
    "question": "Cloud services store data on:",
    "options": [
        "Remote servers",
        "Keyboards",
        "Speakers",
        "Monitors"
    ],
    "answer": "Remote servers"
},

{
    "question": "Browser-based development is especially helpful for:",
    "options": [
        "Beginners",
        "Mechanics",
        "Electricians",
        "Pilots only"
    ],
    "answer": "Beginners"
},

{
    "question": "A stable internet connection helps because:",
    "options": [
        "AI services run online",
        "It improves keyboard speed",
        "It changes RAM size",
        "It upgrades the CPU"
    ],
    "answer": "AI services run online"
},

{
    "question": "Which is NOT a browser?",
    "options": [
        "Chrome",
        "Firefox",
        "Edge",
        "Microsoft Word"
    ],
    "answer": "Microsoft Word"
},

{
    "question": "Cloud computing allows users to:",
    "options": [
        "Access applications from anywhere",
        "Work only on one computer",
        "Avoid accounts",
        "Remove security"
    ],
    "answer": "Access applications from anywhere"
},

{
    "question": "Browser-based AI tools usually require:",
    "options": [
        "User authentication",
        "A DVD",
        "A graphics card upgrade",
        "A printer cable"
    ],
    "answer": "User authentication"
},

{
    "question": "The browser acts as:",
    "options": [
        "A gateway to online AI tools",
        "A CPU replacement",
        "RAM",
        "A database"
    ],
    "answer": "A gateway to online AI tools"
},

{
    "question": "One advantage of cloud platforms is:",
    "options": [
        "Automatic feature updates",
        "Manual updates only",
        "No maintenance",
        "No security"
    ],
    "answer": "Automatic feature updates"
},

{
    "question": "AI learning platforms often provide:",
    "options": [
        "Interactive interfaces",
        "Mechanical tools",
        "Car engines",
        "Television channels"
    ],
    "answer": "Interactive interfaces"
},

{
    "question": "Browser-based tools improve:",
    "options": [
        "Accessibility",
        "Printer speed",
        "Hard disk size",
        "Battery chemistry"
    ],
    "answer": "Accessibility"
},

{
    "question": "Which technology makes browser-based AI possible?",
    "options": [
        "Cloud computing",
        "Floppy disks",
        "VHS tapes",
        "CDs"
    ],
    "answer": "Cloud computing"
},

{
    "question": "Students should save important work:",
    "options": [
        "Regularly",
        "Never",
        "Only after exams",
        "Once a year"
    ],
    "answer": "Regularly"
},

{
    "question": "Browser-based platforms usually support:",
    "options": [
        "Collaboration",
        "Hardware repair",
        "BIOS updates",
        "Chip manufacturing"
    ],
    "answer": "Collaboration"
},

{
    "question": "Most browser-based AI tools are updated by:",
    "options": [
        "Service providers",
        "End users",
        "Internet cables",
        "Printers"
    ],
    "answer": "Service providers"
},

{
    "question": "Which feature helps access the same work from multiple devices?",
    "options": [
        "Cloud storage",
        "USB cables",
        "Local DVDs",
        "CD-ROM"
    ],
    "answer": "Cloud storage"
},

{
    "question": "Browser-based development reduces dependency on:",
    "options": [
        "High-end local hardware",
        "Electricity",
        "Internet",
        "Accounts"
    ],
    "answer": "High-end local hardware"
},

{
    "question": "AI tools in the browser generally provide:",
    "options": [
        "Easy onboarding",
        "Hardware assembly",
        "Chip fabrication",
        "Mechanical design"
    ],
    "answer": "Easy onboarding"
},

{
    "question": "Modern AI education emphasizes:",
    "options": [
        "Practical learning",
        "Memorization only",
        "No exercises",
        "Offline-only learning"
    ],
    "answer": "Practical learning"
},

{
    "question": "A browser-based editor is useful because it:",
    "options": [
        "Requires little setup",
        "Needs special hardware",
        "Cannot save files",
        "Only works offline"
    ],
    "answer": "Requires little setup"
},

{
    "question": "The cloud enables:",
    "options": [
        "Remote computing",
        "Local-only computing",
        "Hardware replacement",
        "BIOS programming"
    ],
    "answer": "Remote computing"
},

{
    "question": "Which is an important digital skill?",
    "options": [
        "Navigating browser-based tools",
        "Repairing CPUs",
        "Welding",
        "Plumbing"
    ],
    "answer": "Navigating browser-based tools"
},

{
    "question": "Browser applications are generally accessed using:",
    "options": [
        "URLs",
        "HDMI cables",
        "USB ports",
        "Power adapters"
    ],
    "answer": "URLs"
},

{
    "question": "AI platforms often include:",
    "options": [
        "User dashboards",
        "Engine oil",
        "Car batteries",
        "BIOS chips"
    ],
    "answer": "User dashboards"
},

{
    "question": "Which statement is TRUE?",
    "options": [
        "Browser-based tools make AI more accessible.",
        "Browsers require programming chips.",
        "Browsers cannot access AI.",
        "Cloud computing is offline."
    ],
    "answer": "Browser-based tools make AI more accessible."
},

{
    "question": "Online AI services commonly use:",
    "options": [
        "Secure login systems",
        "Fax machines",
        "CD players",
        "Typewriters"
    ],
    "answer": "Secure login systems"
},

{
    "question": "Browser-based learning supports:",
    "options": [
        "Flexibility",
        "Less accessibility",
        "Hardware dependence",
        "Offline-only access"
    ],
    "answer": "Flexibility"
},

{
    "question": "Cloud services help by:",
    "options": [
        "Synchronizing data",
        "Deleting browsers",
        "Replacing monitors",
        "Increasing keyboard size"
    ],
    "answer": "Synchronizing data"
},

{
    "question": "Which is a common browser feature?",
    "options": [
        "Tabs",
        "CPU overclocking",
        "RAM expansion",
        "BIOS flashing"
    ],
    "answer": "Tabs"
},

{
    "question": "Students should keep browsers:",
    "options": [
        "Updated",
        "Uninstalled",
        "Outdated forever",
        "Disabled"
    ],
    "answer": "Updated"
},

{
    "question": "Browser-based AI tools typically offer:",
    "options": [
        "Cross-device access",
        "Printer repair",
        "Hard disk replacement",
        "Network cables"
    ],
    "answer": "Cross-device access"
},

{
    "question": "The browser acts as the interface between:",
    "options": [
        "Users and online services",
        "CPU and RAM",
        "Mouse and keyboard",
        "Monitor and speakers"
    ],
    "answer": "Users and online services"
},

{
    "question": "Cloud-hosted AI models execute primarily on:",
    "options": [
        "Provider-managed servers",
        "Your keyboard",
        "USB drives",
        "Local printers"
    ],
    "answer": "Provider-managed servers"
},

{
    "question": "Browser-first learning enables students to:",
    "options": [
        "Focus on concepts before complex setup",
        "Avoid learning AI",
        "Replace programming languages",
        "Build processors"
    ],
    "answer": "Focus on concepts before complex setup"
},

{
    "question": "Which practice improves security when using online tools?",
    "options": [
        "Using strong passwords",
        "Sharing passwords publicly",
        "Ignoring updates",
        "Using the same password everywhere"
    ],
    "answer": "Using strong passwords"
},

{
    "question": "Browser-based AI platforms are popular because they are:",
    "options": [
        "Convenient and accessible",
        "Hardware-dependent",
        "Offline-only",
        "Difficult to use"
    ],
    "answer": "Convenient and accessible"
},

{
    "question": "The Foundations module emphasizes:",
    "options": [
        "Building essential skills before advanced topics",
        "Skipping the basics",
        "Hardware repair",
        "Database administration"
    ],
    "answer": "Building essential skills before advanced topics"
},

{
    "question": "The main outcome of Module 2 is that students can confidently:",
    "options": [
        "Use browser-based tools as the foundation for learning AI",
        "Build operating systems",
        "Design CPUs",
        "Assemble servers from scratch"
    ],
    "answer": "Use browser-based tools as the foundation for learning AI"
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