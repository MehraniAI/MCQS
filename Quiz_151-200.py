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
    "answer": "Giving AI sufficient context to achieve a goal",
    "explanation": "Modern prompting focuses on providing clear context so AI can produce accurate results."
},

{
    "question": "What is Context Engineering?",
    "options": [
        "Building CPUs",
        "Designing and supplying the right information to AI",
        "Installing browsers",
        "Creating databases"
    ],
    "answer": "Designing and supplying the right information to AI",
    "explanation": "Context engineering means structuring input so AI understands the task properly."
},

{
    "question": "Which produces better results?",
    "options": [
        "Vague requests",
        "Clear specifications",
        "Random instructions",
        "Short commands only"
    ],
    "answer": "Clear specifications",
    "explanation": "Clear instructions reduce confusion and improve AI output quality."
},

{
    "question": "A specification should include:",
    "options": [
        "Goals and requirements",
        "Keyboard settings",
        "Screen size",
        "Browser version"
    ],
    "answer": "Goals and requirements",
    "explanation": "Good specs define what needs to be done and expected outcomes."
},

{
    "question": "What is role prompting?",
    "options": [
        "Giving AI a specific role or perspective",
        "Installing permissions",
        "Creating user accounts",
        "Database access"
    ],
    "answer": "Giving AI a specific role or perspective",
    "explanation": "Role prompting helps AI respond like an expert in a specific field."
},

{
    "question": "Which is a good role prompt?",
    "options": [
        "Act as a senior software architect.",
        "Use electricity.",
        "Increase RAM.",
        "Open BIOS."
    ],
    "answer": "Act as a senior software architect.",
    "explanation": "Role prompts guide tone, style, and expertise level."
},

{
    "question": "Why provide examples?",
    "options": [
        "To reduce clarity",
        "To demonstrate expected output format",
        "To slow AI down",
        "To increase token costs"
    ],
    "answer": "To demonstrate expected output format",
    "explanation": "Examples help AI understand exactly what output is expected."
},

{
    "question": "Structured output means:",
    "options": [
        "Organized response format",
        "Random text generation",
        "Browser settings",
        "Hardware configuration"
    ],
    "answer": "Organized response format",
    "explanation": "Structured outputs like JSON make responses predictable and usable."
},

{
    "question": "Which output is more reliable?",
    "options": [
        "Defined JSON structure",
        "Unspecified format",
        "Random paragraphs",
        "Mixed formatting"
    ],
    "answer": "Defined JSON structure",
    "explanation": "Structured formats reduce errors in data processing."
},

{
    "question": "What improves AI performance most?",
    "options": [
        "Better context",
        "Better monitor",
        "Faster mouse",
        "Larger keyboard"
    ],
    "answer": "Better context",
    "explanation": "AI performance depends heavily on quality of input context."
},

{
    "question": "AI should be given:",
    "options": [
        "Constraints",
        "Confusion",
        "Contradictions",
        "Random data"
    ],
    "answer": "Constraints",
    "explanation": "Constraints help AI stay focused on the required output."
},

{
    "question": "Constraints help AI:",
    "options": [
        "Produce targeted outputs",
        "Become slower",
        "Forget context",
        "Avoid reasoning"
    ],
    "answer": "Produce targeted outputs",
    "explanation": "Constraints narrow down possibilities and improve accuracy."
},

{
    "question": "A good prompt usually contains:",
    "options": [
        "Objective",
        "Context",
        "Constraints",
        "All of the above"
    ],
    "answer": "All of the above",
    "explanation": "Strong prompts combine goal, context, and rules."
},

{
    "question": "Iteration means:",
    "options": [
        "Refining prompts and outputs",
        "Restarting computers",
        "Formatting disks",
        "Reinstalling browsers"
    ],
    "answer": "Refining prompts and outputs",
    "explanation": "Iteration improves results step by step."
},

{
    "question": "Prompt evaluation helps:",
    "options": [
        "Measure quality",
        "Reduce quality",
        "Remove context",
        "Disable AI"
    ],
    "answer": "Measure quality",
    "explanation": "Evaluation helps improve prompt effectiveness."
},

{
    "question": "What is a system instruction?",
    "options": [
        "High-level guidance for AI behavior",
        "A motherboard component",
        "A browser extension",
        "A monitor setting"
    ],
    "answer": "High-level guidance for AI behavior",
    "explanation": "System instructions define how AI should behave overall."
},

{
    "question": "Modern prompting focuses more on:",
    "options": [
        "Collaboration",
        "Trick questions",
        "Hidden commands",
        "Keyword stuffing"
    ],
    "answer": "Collaboration",
    "explanation": "AI is now used as a collaborator, not just a tool."
},

{
    "question": "Why specify audience?",
    "options": [
        "To tailor communication",
        "To reduce accuracy",
        "To confuse AI",
        "To increase latency"
    ],
    "answer": "To tailor communication",
    "explanation": "Audience helps AI adjust tone and complexity."
},

{
    "question": "Which prompt is better?",
    "options": [
        "Explain AI.",
        "Explain AI to a 12-year-old using simple examples.",
        "AI",
        "Tell me something."
    ],
    "answer": "Explain AI to a 12-year-old using simple examples.",
    "explanation": "Specific prompts produce clearer and better responses."
},

{
    "question": "AI agents benefit from:",
    "options": [
        "Clear instructions",
        "Ambiguity",
        "Missing requirements",
        "No goals"
    ],
    "answer": "Clear instructions",
    "explanation": "Agents need structured goals to act correctly."
},

{
    "question": "Context is often more important than wording.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Meaning depends more on context than exact phrasing."
},

{
    "question": "Examples improve output quality.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Examples guide AI toward expected structure."
},

{
    "question": "Specifications reduce ambiguity.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Clear specs remove confusion in instructions."
},

{
    "question": "Constraints are useful.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "They help AI stay focused and controlled."
},

{
    "question": "Structured outputs improve reliability.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Structured formats reduce randomness."
},

{
    "question": "AI should be given goals.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Goals guide AI behavior toward results."
},

{
    "question": "Iteration improves results.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Repeated refinement improves performance."
},

{
    "question": "Prompt evaluation is valuable.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Evaluation helps identify weak prompts."
},

{
    "question": "Role prompting can improve performance.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Roles guide tone and expertise."
},

{
    "question": "Audience matters.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Different audiences need different explanations."
},

{
    "question": "Vague prompts usually perform better.",
    "options": ["True", "False"],
    "answer": "False",
    "explanation": "Vague prompts reduce accuracy."
},

{
    "question": "Context Engineering is important.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "It improves AI understanding significantly."
},

{
    "question": "Specifications help AI understand tasks.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Specs clearly define expectations."
},

{
    "question": "Examples clarify expectations.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Examples remove confusion."
},

{
    "question": "AI works best without requirements.",
    "options": ["True", "False"],
    "answer": "False",
    "explanation": "Requirements improve output quality."
},

{
    "question": "Goal clarity improves outputs.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Clear goals lead to better results."
},

{
    "question": "Constraints guide behavior.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Constraints control output direction."
},

{
    "question": "JSON is an example of structured output.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "JSON is widely used structured format."
},

{
    "question": "AI can follow specifications.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Models can follow structured instructions."
},

{
    "question": "Context quality matters.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Better context = better AI response."
},

{
    "question": "Good prompts reduce ambiguity.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Clear prompts reduce confusion."
},

{
    "question": "AI agents need instructions.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Agents require clear tasks."
},

{
    "question": "Prompt refinement is useful.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Refining improves accuracy."
},

{
    "question": "Examples are valuable.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Examples guide output formatting."
},

{
    "question": "Audience definition helps communication.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "It adjusts complexity and tone."
},

{
    "question": "Specifications define requirements.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Specs describe what must be done."
},

{
    "question": "Iteration is part of prompting.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Prompting improves through repetition."
},

{
    "question": "Role prompting can provide expertise framing.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Roles simulate expert behavior."
},

{
    "question": "Structured outputs are useful for automation.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Machines can easily process structured data."
},

{
    "question": "Prompting is becoming more about Context Engineering.",
    "options": ["True", "False"],
    "answer": "True",
    "explanation": "Modern AI focuses more on context than keywords."
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