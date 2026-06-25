
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
    "question": "What does AI stand for?",
    "options": [
        "Automated Intelligence",
        "Artificial Intelligence",
        "Artificial Integration",
        "Automated Interface"
    ],
    "answer": "Artificial Intelligence"
},

{
    "question": "What is a Large Language Model (LLM)?",
    "options": [
        "A computer monitor",
        "A model trained on large amounts of text",
        "A database server",
        "A web browser"
    ],
    "answer": "A model trained on large amounts of text"
},

{
    "question": "What are tokens in AI?",
    "options": [
        "Internet cables",
        "Units of text processed by a model",
        "Images only",
        "Databases"
    ],
    "answer": "Units of text processed by a model"
},

{
    "question": "What is a context window?",
    "options": [
        "Browser window size",
        "Amount of information AI can consider at once",
        "RAM capacity",
        "Monitor resolution"
    ],
    "answer": "Amount of information AI can consider at once"
},

{
    "question": "Training is the process where:",
    "options": [
        "Users chat with AI",
        "Models learn patterns from data",
        "Browsers load websites",
        "Servers shut down"
    ],
    "answer": "Models learn patterns from data"
},

{
    "question": "Inference refers to:",
    "options": [
        "Model deployment and generating responses",
        "Building hardware",
        "Creating datasets only",
        "Installing software"
    ],
    "answer": "Model deployment and generating responses"
},

{
    "question": "AI models primarily predict:",
    "options": [
        "Weather only",
        "The next likely token",
        "Hardware failures",
        "Electricity usage"
    ],
    "answer": "The next likely token"
},

{
    "question": "What is a hallucination in AI?",
    "options": [
        "Perfect prediction",
        "Confidently generated incorrect information",
        "Hardware malfunction",
        "Slow internet"
    ],
    "answer": "Confidently generated incorrect information"
},

{
    "question": "Which statement is true?",
    "options": [
        "AI always knows facts",
        "AI can make mistakes",
        "AI is never wrong",
        "AI understands everything"
    ],
    "answer": "AI can make mistakes"
},

{
    "question": "What is an embedding?",
    "options": [
        "A keyboard shortcut",
        "Numerical representation of information",
        "Network protocol",
        "Browser plugin"
    ],
    "answer": "Numerical representation of information"
},

{
    "question": "RAG stands for:",
    "options": [
        "Retrieval-Augmented Generation",
        "Random AI Generator",
        "Recursive Agent Group",
        "Rapid Algorithm Grid"
    ],
    "answer": "Retrieval-Augmented Generation"
},

{
    "question": "Why use RAG?",
    "options": [
        "To access relevant knowledge beyond training data",
        "To increase monitor size",
        "To reduce internet speed",
        "To remove context"
    ],
    "answer": "To access relevant knowledge beyond training data"
},

{
    "question": "Fine-tuning means:",
    "options": [
        "Additional training for specific tasks",
        "Browser optimization",
        "Hardware replacement",
        "Database deletion"
    ],
    "answer": "Additional training for specific tasks"
},

{
    "question": "What is an AI agent?",
    "options": [
        "A system that can take actions toward goals",
        "A CPU component",
        "A browser tab",
        "A database server"
    ],
    "answer": "A system that can take actions toward goals"
},

{
    "question": "How is an agent different from a chatbot?",
    "options": [
        "Agents can use tools and perform actions",
        "No difference exists",
        "Agents are hardware devices",
        "Chatbots are always smarter"
    ],
    "answer": "Agents can use tools and perform actions"
},

{
    "question": "What powers modern generative AI?",
    "options": [
        "Neural networks",
        "Fax machines",
        "Printers",
        "Modems"
    ],
    "answer": "Neural networks"
},

{
    "question": "AI reasoning models attempt to:",
    "options": [
        "Improve problem-solving abilities",
        "Replace electricity",
        "Increase screen brightness",
        "Remove data"
    ],
    "answer": "Improve problem-solving abilities"
},

{
    "question": "AI learns patterns primarily from:",
    "options": [
        "Training data",
        "Keyboard layouts",
        "Monitor size",
        "Routers"
    ],
    "answer": "Training data"
},

{
    "question": "Which is NOT guaranteed by AI?",
    "options": [
        "Speed",
        "Perfect accuracy",
        "Scalability",
        "Automation"
    ],
    "answer": "Perfect accuracy"
},

{
    "question": "Multi-agent systems involve:",
    "options": [
        "Multiple AI agents working together",
        "Multiple monitors",
        "Multiple networks",
        "Multiple browsers"
    ],
    "answer": "Multiple AI agents working together"
},

# 21-50 True/False

{"question":"AI is primarily statistical.","options":["True","False"],"answer":"True"},
{"question":"Tokens are units of text.","options":["True","False"],"answer":"True"},
{"question":"Context windows affect memory.","options":["True","False"],"answer":"True"},
{"question":"Hallucinations can occur.","options":["True","False"],"answer":"True"},
{"question":"Training happens before deployment.","options":["True","False"],"answer":"True"},
{"question":"Inference generates outputs.","options":["True","False"],"answer":"True"},
{"question":"Embeddings represent meaning numerically.","options":["True","False"],"answer":"True"},
{"question":"RAG retrieves external information.","options":["True","False"],"answer":"True"},
{"question":"Fine-tuning specializes models.","options":["True","False"],"answer":"True"},
{"question":"Agents can use tools.","options":["True","False"],"answer":"True"},
{"question":"AI always tells the truth.","options":["True","False"],"answer":"False"},
{"question":"AI models predict likely tokens.","options":["True","False"],"answer":"True"},
{"question":"Neural networks are central to modern AI.","options":["True","False"],"answer":"True"},
{"question":"Multi-agent systems use multiple agents.","options":["True","False"],"answer":"True"},
{"question":"AI has limitations.","options":["True","False"],"answer":"True"},
{"question":"LLM means Large Language Model.","options":["True","False"],"answer":"True"},
{"question":"AI understands reality exactly like humans.","options":["True","False"],"answer":"False"},
{"question":"Context affects responses.","options":["True","False"],"answer":"True"},
{"question":"AI can summarize information.","options":["True","False"],"answer":"True"},
{"question":"AI can reason perfectly.","options":["True","False"],"answer":"False"},
{"question":"Training teaches patterns.","options":["True","False"],"answer":"True"},
{"question":"Inference uses trained models.","options":["True","False"],"answer":"True"},
{"question":"RAG improves access to current information.","options":["True","False"],"answer":"True"},
{"question":"Embeddings support semantic search.","options":["True","False"],"answer":"True"},
{"question":"Agents can automate tasks.","options":["True","False"],"answer":"True"},
{"question":"AI can help with coding.","options":["True","False"],"answer":"True"},
{"question":"Hallucinations require verification.","options":["True","False"],"answer":"True"},
{"question":"AI productivity depends on context quality.","options":["True","False"],"answer":"True"},
{"question":"Human oversight remains important.","options":["True","False"],"answer":"True"},
{"question":"AI systems can be wrong.","options":["True","False"],"answer":"True"}

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
