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

{    
    "question": "What is a Digital FTE?",
    "options": [
        "Digital Full-Time Employee",
        "Digital File Transfer Engine",
        "Data Function Tool Engine",
        "Distributed Task Executor"
    ],
    "answer": "Digital Full-Time Employee",
    "explanation": "Digital FTE stands for Digital Full-Time Employee. It is an AI-powered digital worker that performs tasks traditionally done by humans, helping organizations improve efficiency and productivity."
},

{
    "question": "What is the 10-80-10 model?",
    "options": [
        "Human executes all work",
        "Human directs, AI executes, Human verifies",
        "AI directs, Human executes",
        "AI performs everything"
    ],
    "answer": "Human directs, AI executes, Human verifies",
    "explanation": "The 10-80-10 model means humans provide the direction (10%), AI performs most of the work (80%), and humans verify and improve the final output (10%)."
},

{
    "question": "In the 10-80-10 model, who performs the 80%?",
    "options": [
        "Customer",
        "Manager",
        "AI",
        "Developer"
    ],
    "answer": "AI",
    "explanation": "The AI performs the majority (80%) of the work after receiving clear instructions from the human."
},

{
    "question": "The final 10% represents:",
    "options": [
        "Deployment",
        "Coding",
        "Verification",
        "Marketing"
    ],
    "answer": "Verification",
    "explanation": "The last 10% is verification, where humans check, correct, and approve the AI's work before it is used."
},

{
    "question": "Agent Factory primarily promotes:",
    "options": [
        "Traditional programming",
        "AI-Native Development",
        "Hardware engineering",
        "Networking"
    ],
    "answer": "AI-Native Development",
    "explanation": "Agent Factory encourages AI-Native Development, where AI is integrated into the workflow from the beginning instead of being added later."
},

{
    "question": "AI-Native means:",
    "options": [
        "AI integrated from the beginning",
        "AI added later",
        "No AI used",
        "Manual workflows"
    ],
    "answer": "AI integrated from the beginning",
    "explanation": "AI-Native means designing systems and workflows with AI as a core part from the start."
},

{
    "question": "Human value in AI workflows mainly comes from:",
    "options": [
        "Typing speed",
        "Judgment and direction",
        "RAM size",
        "Internet speed"
    ],
    "answer": "Judgment and direction",
    "explanation": "Humans contribute by making decisions, giving instructions, and using critical thinking, while AI performs repetitive tasks."
},

{
    "question": "Digital FTEs are used to:",
    "options": [
        "Scale knowledge work",
        "Increase storage",
        "Improve hardware",
        "Manage networks"
    ],
    "answer": "Scale knowledge work",
    "explanation": "Digital FTEs allow organizations to complete more knowledge-based work efficiently without hiring additional employees."
},

{
    "question": "What improves AI output quality most?",
    "options": [
        "Better monitor",
        "More RAM",
        "Better context",
        "Faster keyboard"
    ],
    "answer": "Better context",
    "explanation": "Providing detailed and relevant context helps AI generate more accurate and useful responses."
},

{
    "question": "AI should be viewed as:",
    "options": [
        "Perfect intelligence",
        "A collaborator",
        "A replacement for thinking",
        "A database"
    ],
    "answer": "A collaborator",
    "explanation": "AI is most effective when used as a partner that assists humans, not as a replacement for human judgment."
},

{
    "question": "Why is verification necessary?",
    "options": [
        "AI can hallucinate",
        "AI is slow",
        "AI lacks storage",
        "AI lacks internet"
    ],
    "answer": "AI can hallucinate",
    "explanation": "AI may generate incorrect or made-up information, so humans must verify its responses before relying on them."
},

{
    "question": "Which is NOT part of 10-80-10?",
    "options": [
        "Direct",
        "Execute",
        "Verify",
        "Ignore"
    ],
    "answer": "Ignore",
    "explanation": "The 10-80-10 model consists of directing, AI execution, and verification. Ignoring the results is not part of the process."
},

{
    "question": "AI excels at:",
    "options": [
        "Scaling repetitive work",
        "Perfect truth",
        "Legal decisions",
        "Human emotions"
    ],
    "answer": "Scaling repetitive work",
    "explanation": "AI is excellent at performing repetitive tasks quickly and consistently but still requires human oversight."
},

{
    "question": "Context engineering refers to:",
    "options": [
        "Building CPUs",
        "Managing information given to AI",
        "Creating hardware",
        "Installing browsers"
    ],
    "answer": "Managing information given to AI",
    "explanation": "Context engineering involves organizing and providing the right information so AI can produce better results."
},

{
    "question": "Human-AI collaboration combines:",
    "options": [
        "Human judgment + AI scale",
        "Human speed + AI emotions",
        "Human memory + AI hardware",
        "Human coding + AI networking"
    ],
    "answer": "Human judgment + AI scale",
    "explanation": "Humans contribute decision-making and creativity, while AI provides speed, automation, and scalability."
},

{
    "question": "Agent Factory emphasizes:",
    "options": [
        "Outcome-focused work",
        "Syntax memorization",
        "Hardware design",
        "Networking"
    ],
    "answer": "Outcome-focused work",
    "explanation": "Agent Factory focuses on achieving successful outcomes instead of memorizing programming syntax."
},

{
    "question": "Digital FTEs help organizations:",
    "options": [
        "Scale operations",
        "Reduce storage",
        "Replace databases",
        "Increase electricity"
    ],
    "answer": "Scale operations",
    "explanation": "Digital FTEs allow businesses to expand operations efficiently by automating routine tasks."
},

{
    "question": "AI-generated work should always be:",
    "options": [
        "Verified",
        "Ignored",
        "Deleted",
        "Trusted blindly"
    ],
    "answer": "Verified",
    "explanation": "Humans should always review AI-generated work because AI can make mistakes or produce inaccurate information."
},

{
    "question": "Which skill becomes more important in AI?",
    "options": [
        "Problem definition",
        "Typing speed",
        "Keyboard shortcuts",
        "Hardware assembly"
    ],
    "answer": "Problem definition",
    "explanation": "Clearly defining the problem helps AI produce more accurate and relevant solutions."
},

{
    "question": "The most important takeaway from Orientation is:",
    "options": [
        "Humans direct AI",
        "AI replaces humans",
        "Coding disappears",
        "Browsers are obsolete"
    ],
    "answer": "Humans direct AI",
    "explanation": "The key message is that humans remain responsible for giving direction while AI assists in completing the work."
},

{
    "question": "What does the first 10% in the 10-80-10 model represent?",
    "options": [
        "Verification",
        "Direction",
        "Execution",
        "Deployment"
    ],
    "answer": "Direction",
    "explanation": "The first 10% involves humans setting goals, providing instructions, and defining the task for AI."
},

{
    "question": "What does the 80% in the 10-80-10 model represent?",
    "options": [
        "Human review",
        "Planning",
        "AI execution",
        "Testing"
    ],
    "answer": "AI execution",
    "explanation": "The middle 80% is the work performed by AI based on the instructions provided by humans."
},

{
    "question": "What does the final 10% in the 10-80-10 model represent?",
    "options": [
        "Prompting",
        "Coding",
        "Verification",
        "Training"
    ],
    "answer": "Verification",
    "explanation": "After AI completes the work, humans verify its accuracy, quality, and correctness."
},

{
    "question": "Digital FTEs are designed to augment:",
    "options": [
        "Knowledge workers",
        "Networks",
        "Hardware",
        "Databases"
    ],
    "answer": "Knowledge workers",
    "explanation": "Digital FTEs assist knowledge workers by automating repetitive tasks, allowing humans to focus on higher-level thinking."
},

{
    "question": "The main goal of AI-Native Development is:",
    "options": [
        "More hardware",
        "Better outcomes",
        "More coding",
        "Less automation"
    ],
    "answer": "Better outcomes",
    "explanation": "AI-Native Development aims to achieve better business and project outcomes by integrating AI into workflows from the beginning."
},

{
    "question": "What should humans primarily provide to AI?",
    "options": [
        "Storage",
        "Bandwidth",
        "Direction",
        "Electricity"
    ],
    "answer": "Direction",
    "explanation": "Humans are responsible for providing clear goals, instructions, and context so AI can perform tasks effectively."
},

{
    "question": "Which capability makes AI valuable for organizations?",
    "options": [
        "Monitor size",
        "Scalability",
        "Mouse speed",
        "CPU color"
    ],
    "answer": "Scalability",
    "explanation": "Scalability allows AI to perform the same tasks for many users or projects quickly and consistently, making it valuable for organizations."
},

{
    "question": "AI can help increase:",
    "options": [
        "Productivity",
        "Screen brightness",
        "Electricity",
        "Hardware weight"
    ],
    "answer": "Productivity",
    "explanation": "AI automates repetitive tasks, allowing people to complete more work in less time and improving productivity."
},

{
    "question": "What is the most important human responsibility when using AI?",
    "options": [
        "Networking",
        "Typing",
        "Verification",
        "Hardware setup"
    ],
    "answer": "Verification",
    "explanation": "Humans must verify AI-generated work because AI can sometimes produce incorrect or misleading information."
},

{
    "question": "AI systems should be treated as:",
    "options": [
        "Perfect experts",
        "Assistants",
        "Managers",
        "Databases"
    ],
    "answer": "Assistants",
    "explanation": "AI should be treated as an assistant that supports human work, not as a replacement for human thinking or decision-making."
},

{
    "question": "Human judgment is important because AI can:",
    "options": [
        "Make mistakes",
        "Use RAM",
        "Open browsers",
        "Connect networks"
    ],
    "answer": "Make mistakes",
    "explanation": "AI is powerful but not perfect. Humans must use their judgment to detect and correct AI errors."
},

{
    "question": "What helps AI produce better results?",
    "options": [
        "Quality context",
        "Expensive keyboard",
        "Large monitor",
        "Faster mouse"
    ],
    "answer": "Quality context",
    "explanation": "Providing clear instructions and relevant information helps AI generate more accurate and useful responses."
},

{
    "question": "Which approach is encouraged by Agent Factory?",
    "options": [
        "Experimentation",
        "Avoiding AI",
        "Manual repetition",
        "Hardware repair"
    ],
    "answer": "Experimentation",
    "explanation": "Agent Factory encourages users to experiment with AI, learn from results, and continuously improve their workflows."
},

{
    "question": "AI-Native workflows focus on:",
    "options": [
        "Outcomes",
        "Syntax",
        "Hardware",
        "Networking"
    ],
    "answer": "Outcomes",
    "explanation": "AI-Native workflows prioritize achieving the best results rather than focusing only on coding syntax."
},

{
    "question": "Digital FTEs can help businesses:",
    "options": [
        "Scale work",
        "Reduce electricity",
        "Replace internet",
        "Increase heat"
    ],
    "answer": "Scale work",
    "explanation": "Digital FTEs enable businesses to complete more work efficiently without increasing the number of human employees."
},

{
    "question": "What is one risk of AI-generated content?",
    "options": [
        "Hallucinations",
        "Monitor damage",
        "Keyboard failure",
        "CPU melting"
    ],
    "answer": "Hallucinations",
    "explanation": "AI hallucinations occur when AI generates information that sounds correct but is actually false or made up."
},

{
    "question": "Humans should always review AI outputs before:",
    "options": [
        "Using them",
        "Typing",
        "Saving files",
        "Opening browsers"
    ],
    "answer": "Using them",
    "explanation": "Reviewing AI output ensures that it is accurate, complete, and suitable before it is used."
},

{
    "question": "What does AI-Native Development encourage?",
    "options": [
        "Working with AI from the start",
        "Ignoring AI",
        "Manual coding only",
        "Hardware assembly"
    ],
    "answer": "Working with AI from the start",
    "explanation": "AI-Native Development encourages integrating AI into projects from the beginning instead of adding it later."
},

{
    "question": "Which quality is most valuable in AI collaboration?",
    "options": [
        "Clear thinking",
        "Fast typing",
        "Large monitor",
        "Gaming skills"
    ],
    "answer": "Clear thinking",
    "explanation": "Clear thinking helps humans create better prompts, make better decisions, and effectively guide AI."
},

{
    "question": "The purpose of context engineering is to:",
    "options": [
        "Provide useful information",
        "Build hardware",
        "Install software",
        "Upgrade networks"
    ],
    "answer": "Provide useful information",
    "explanation": "Context engineering means supplying AI with the right information so it can produce accurate and relevant responses."
},

{
    "question": "AI works best when given:",
    "options": [
        "Clear objectives",
        "Random tasks",
        "No instructions",
        "Contradictions"
    ],
    "answer": "Clear objectives",
    "explanation": "AI performs best when it receives specific goals, detailed instructions, and clear expectations."
},

{
    "question": "The future workplace is expected to involve:",
    "options": [
        "Human-AI collaboration",
        "No technology",
        "Only humans",
        "Only robots"
    ],
    "answer": "Human-AI collaboration",
    "explanation": "Future workplaces are expected to combine human creativity and judgment with AI's speed and efficiency."
},

{
    "question": "AI can help automate:",
    "options": [
        "Repetitive tasks",
        "Human emotions",
        "Electricity generation",
        "Weather"
    ],
    "answer": "Repetitive tasks",
    "explanation": "AI is especially useful for automating repetitive and routine tasks, allowing humans to focus on more important work."
},

{
    "question": "What remains uniquely human in AI workflows?",
    "options": [
        "Judgment",
        "Token prediction",
        "Automation",
        "Scaling"
    ],
    "answer": "Judgment",
    "explanation": "Humans provide reasoning, ethics, creativity, and judgment, which AI cannot fully replace."
},

{
    "question": "Organizations use Digital FTEs to improve:",
    "options": [
        "Efficiency",
        "Screen size",
        "Power cables",
        "Keyboards"
    ],
    "answer": "Efficiency",
    "explanation": "Digital FTEs improve efficiency by completing repetitive tasks quickly and accurately."
},

{
    "question": "AI output quality depends heavily on:",
    "options": [
        "Input quality",
        "Monitor size",
        "Mouse sensitivity",
        "Desk size"
    ],
    "answer": "Input quality",
    "explanation": "The quality of AI responses depends greatly on the quality of the prompts and information provided by the user."
},

{
    "question": "The orientation promotes a mindset of:",
    "options": [
        "Learning and experimentation",
        "Avoiding change",
        "Manual work only",
        "Hardware upgrades"
    ],
    "answer": "Learning and experimentation",
    "explanation": "The orientation encourages continuous learning, trying new AI techniques, and improving through experimentation."
},

{
    "question": "AI should support humans rather than:",
    "options": [
        "Replace judgment",
        "Increase productivity",
        "Assist work",
        "Provide ideas"
    ],
    "answer": "Replace judgment",
    "explanation": "AI should assist humans in their work but should never replace human judgment and decision-making."
},

{
    "question": "A successful AI workflow combines:",
    "options": [
        "Human oversight and AI execution",
        "AI only",
        "Humans only",
        "Hardware only"
    ],
    "answer": "Human oversight and AI execution",
    "explanation": "The best AI workflows combine AI's speed with human oversight to ensure accurate, reliable, and high-quality results."
},


    {
    "question": "The key lesson of Orientation Presentation is:",
    "options": [
        "Humans lead, AI assists",
        "AI replaces everyone",
        "Hardware is everything",
        "Coding is obsolete"
    ],
    "answer": "Humans lead, AI assists",
    "explanation": "The main message is that humans remain in control by providing direction and judgment, while AI acts as a powerful assistant."
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