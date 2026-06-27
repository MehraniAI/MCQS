
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

textarea {
    color: white !important;
    -webkit-text-fill-color: white !important;
}
</style>
""", unsafe_allow_html=True)

QUESTIONS = [
    
# ---------------- QUESTIONS ----------------
# 101–150 MCQs with explanations

{
    "question": "What does NLP stand for in AI?",
    "options": [
        "Natural Language Processing",
        "Neural Learning Program",
        "New Logic Protocol",
        "Network Language Parser"
    ],
    "answer": "Natural Language Processing",
    "explanation": "NLP is a branch of AI that helps computers understand and process human language."
},
{
    "question": "Which part of AI focuses on image recognition?",
    "options": [
        "Computer Vision",
        "Data Mining",
        "Web Development",
        "System Design"
    ],
    "answer": "Computer Vision",
    "explanation": "Computer Vision enables machines to interpret and analyze images and videos."
},
{
    "question": "What is supervised learning?",
    "options": [
        "Learning with labeled data",
        "Learning without any data",
        "Learning through hardware",
        "Random guessing"
    ],
    "answer": "Learning with labeled data",
    "explanation": "In supervised learning, models are trained using input-output labeled examples."
},
{
    "question": "What is unsupervised learning?",
    "options": [
        "Learning from unlabeled data",
        "Learning with teacher",
        "Learning only from images",
        "Learning using rules only"
    ],
    "answer": "Learning from unlabeled data",
    "explanation": "The model finds patterns in data without labeled answers."
},
{
    "question": "Which algorithm is commonly used for classification?",
    "options": [
        "Decision Tree",
        "Linear Keyboard",
        "File System",
        "HTTP Protocol"
    ],
    "answer": "Decision Tree",
    "explanation": "Decision trees split data into branches to classify outcomes."
},
{
    "question": "What is overfitting in AI?",
    "options": [
        "Model performs well on training but poorly on new data",
        "Model deletes data",
        "Model stops working",
        "Model becomes hardware"
    ],
    "answer": "Model performs well on training but poorly on new data",
    "explanation": "Overfitting happens when a model memorizes training data instead of learning general patterns."
},
{
    "question": "What is underfitting?",
    "options": [
        "Model is too simple to learn patterns",
        "Model is too large",
        "Model is perfect",
        "Model is overtrained"
    ],
    "answer": "Model is too simple to learn patterns",
    "explanation": "Underfitting happens when the model cannot capture patterns in the data."
},
{
    "question": "Which function is used to reduce error in training?",
    "options": [
        "Loss function",
        "Print function",
        "Input function",
        "Display function"
    ],
    "answer": "Loss function",
    "explanation": "Loss function measures how wrong the model’s predictions are."
},
{
    "question": "What is gradient descent used for?",
    "options": [
        "Optimizing model parameters",
        "Increasing data size",
        "Deleting datasets",
        "Running browsers"
    ],
    "answer": "Optimizing model parameters",
    "explanation": "Gradient descent adjusts model weights to minimize error."
},
{
    "question": "Which layer is used in neural networks?",
    "options": [
        "Input layer",
        "Output layer",
        "Hidden layer",
        "All of the above"
    ],
    "answer": "All of the above",
    "explanation": "Neural networks consist of input, hidden, and output layers."
},
{
    "question": "What does a neuron in AI simulate?",
    "options": [
        "Human brain cell",
        "CPU fan",
        "Hard disk",
        "Router"
    ],
    "answer": "Human brain cell",
    "explanation": "Artificial neurons are inspired by biological brain neurons."
},
{
    "question": "Which activation function is commonly used?",
    "options": [
        "ReLU",
        "HTML",
        "SQL",
        "HTTP"
    ],
    "answer": "ReLU",
    "explanation": "ReLU is widely used because it helps models learn faster and avoids vanishing gradients."
},
{
    "question": "What is deep learning?",
    "options": [
        "Neural networks with many layers",
        "Simple arithmetic",
        "Database storage",
        "Web hosting"
    ],
    "answer": "Neural networks with many layers",
    "explanation": "Deep learning uses multiple layers to learn complex patterns."
},
{
    "question": "What is a dataset?",
    "options": [
        "Collection of data used for training",
        "A computer chip",
        "A browser extension",
        "A programming language"
    ],
    "answer": "Collection of data used for training",
    "explanation": "Datasets contain structured information used to train AI models."
},
{
    "question": "Which is a real-world AI application?",
    "options": [
        "Voice assistants",
        "Paper notebooks",
        "Mechanical pencils",
        "Manual calculators"
    ],
    "answer": "Voice assistants",
    "explanation": "AI powers tools like Siri, Alexa, and Google Assistant."
},
{
    "question": "What is bias in AI?",
    "options": [
        "Systematic error in predictions",
        "Internet speed",
        "Hardware failure",
        "Power supply"
    ],
    "answer": "Systematic error in predictions",
    "explanation": "Bias happens when training data leads to unfair or skewed results."
},
{
    "question": "What is reinforcement learning?",
    "options": [
        "Learning through rewards and penalties",
        "Learning with books",
        "Learning without data",
        "Learning hardware"
    ],
    "answer": "Learning through rewards and penalties",
    "explanation": "The model improves by receiving feedback (reward/punishment)."
},
{
    "question": "Which is an example of reinforcement learning?",
    "options": [
        "Game-playing AI",
        "Calculator app",
        "Text editor",
        "Browser cache"
    ],
    "answer": "Game-playing AI",
    "explanation": "Game AIs learn strategies by playing and improving over time."
},
{
    "question": "What is a model parameter?",
    "options": [
        "Internal value learned during training",
        "Keyboard key",
        "Screen size",
        "Internet speed"
    ],
    "answer": "Internal value learned during training",
    "explanation": "Parameters are weights adjusted during training."
},
{
    "question": "What is batch processing?",
    "options": [
        "Training data in groups",
        "Single data processing",
        "Deleting data",
        "Printing files"
    ],
    "answer": "Training data in groups",
    "explanation": "Data is processed in batches to improve efficiency."
},
{
    "question": "What is epoch in machine learning?",
    "options": [
        "One full pass through training data",
        "Computer shutdown",
        "Internet cycle",
        "Memory reset"
    ],
    "answer": "One full pass through training data",
    "explanation": "One epoch means the model has seen the entire dataset once."
},
{
    "question": "What is accuracy in AI?",
    "options": [
        "How often model is correct",
        "Model speed",
        "Data size",
        "CPU usage"
    ],
    "answer": "How often model is correct",
    "explanation": "Accuracy measures correct predictions over total predictions."
},
{
    "question": "What is precision in AI?",
    "options": [
        "Correct positive predictions out of predicted positives",
        "Total dataset size",
        "Training speed",
        "Memory usage"
    ],
    "answer": "Correct positive predictions out of predicted positives",
    "explanation": "Precision focuses on correctness of positive predictions."
},
{
    "question": "What is recall in AI?",
    "options": [
        "Correct positives out of actual positives",
        "Model restart",
        "Data storage",
        "Network speed"
    ],
    "answer": "Correct positives out of actual positives",
    "explanation": "Recall measures how many real positives were correctly found."
},
{
    "question": "What is a confusion matrix?",
    "options": [
        "Table showing prediction results",
        "Random data list",
        "Network error log",
        "Memory map"
    ],
    "answer": "Table showing prediction results",
    "explanation": "It compares predicted vs actual results in classification."
},
{
    "question": "What is a feature in machine learning?",
    "options": [
        "Input variable used for prediction",
        "Computer brand",
        "Software license",
        "Browser tab"
    ],
    "answer": "Input variable used for prediction",
    "explanation": "Features are the inputs used by the model to make predictions."
},
{
    "question": "What is feature engineering?",
    "options": [
        "Selecting and transforming data features",
        "Building hardware",
        "Deleting files",
        "Installing apps"
    ],
    "answer": "Selecting and transforming data features",
    "explanation": "It improves model performance by preparing better input data."
},
{
    "question": "What is clustering?",
    "options": [
        "Grouping similar data points",
        "Sorting files alphabetically",
        "Deleting data",
        "Compressing images"
    ],
    "answer": "Grouping similar data points",
    "explanation": "Clustering organizes data into groups based on similarity."
},
{
    "question": "Which is a clustering algorithm?",
    "options": [
        "K-Means",
        "HTTP",
        "HTML",
        "FTP"
    ],
    "answer": "K-Means",
    "explanation": "K-Means groups data into clusters based on distance."
},
{
    "question": "What is regression in AI?",
    "options": [
        "Predicting continuous values",
        "Deleting data",
        "Sorting files",
        "Compiling code"
    ],
    "answer": "Predicting continuous values",
    "explanation": "Regression predicts numerical values like price or temperature."
},
{
    "question": "What is a decision boundary?",
    "options": [
        "Line separating classes in data",
        "Computer border",
        "Network limit",
        "Screen edge"
    ],
    "answer": "Line separating classes in data",
    "explanation": "It divides different categories in classification models."
},
{
    "question": "What is transfer learning?",
    "options": [
        "Using a pre-trained model for new tasks",
        "Deleting old model",
        "Creating hardware",
        "Changing OS"
    ],
    "answer": "Using a pre-trained model for new tasks",
    "explanation": "It saves time by reusing knowledge from existing models."
},
{
    "question": "What is data preprocessing?",
    "options": [
        "Cleaning and preparing data",
        "Deleting model",
        "Printing files",
        "Running OS"
    ],
    "answer": "Cleaning and preparing data",
    "explanation": "Raw data is cleaned before training models."
},
{
    "question": "What is normalization?",
    "options": [
        "Scaling data into a standard range",
        "Deleting files",
        "Encrypting data",
        "Compressing videos"
    ],
    "answer": "Scaling data into a standard range",
    "explanation": "It ensures values are on a similar scale for better learning."
},
{
    "question": "What is a chatbot?",
    "options": [
        "AI system that chats with users",
        "Hardware device",
        "Operating system",
        "Compiler"
    ],
    "answer": "AI system that chats with users",
    "explanation": "Chatbots simulate conversation using AI."
},
{
    "question": "What is the main goal of AI?",
    "options": [
        "Simulate human intelligence",
        "Build hardware",
        "Replace electricity",
        "Increase storage"
    ],
    "answer": "Simulate human intelligence",
    "explanation": "AI aims to mimic human thinking and decision-making."
},
{
    "question": "Which is NOT a type of AI?",
    "options": [
        "Mechanical AI",
        "Narrow AI",
        "General AI",
        "Super AI"
    ],
    "answer": "Mechanical AI",
    "explanation": "Mechanical AI is not a recognized AI category."
},
{
    "question": "What is Narrow AI?",
    "options": [
        "AI designed for specific tasks",
        "AI that knows everything",
        "AI without data",
        "AI hardware only"
    ],
    "answer": "AI designed for specific tasks",
    "explanation": "It is built for one specific task like translation or recognition."
},
{
    "question": "What is General AI?",
    "options": [
        "AI that can perform any intellectual task",
        "AI for games only",
        "AI for images only",
        "AI for databases"
    ],
    "answer": "AI that can perform any intellectual task",
    "explanation": "General AI would think like a human across all tasks."
},
{
    "question": "What is Super AI?",
    "options": [
        "AI smarter than humans",
        "AI for calculators",
        "AI for typing",
        "AI for storage"
    ],
    "answer": "AI smarter than humans",
    "explanation": "Super AI is a hypothetical AI that surpasses human intelligence."
},
{
    "question": "What is a transformer model?",
    "options": [
        "Architecture used in modern LLMs",
        "Electric device",
        "Database type",
        "Browser engine"
    ],
    "answer": "Architecture used in modern LLMs",
    "explanation": "Transformers power models like ChatGPT."
},
{
    "question": "What is attention mechanism?",
    "options": [
        "Focuses on important parts of input",
        "Deletes data",
        "Compresses files",
        "Increases RAM"
    ],
    "answer": "Focuses on important parts of input",
    "explanation": "It helps the model focus on relevant words in a sentence."
},
{
    "question": "Why is data important in AI?",
    "options": [
        "It is used for learning patterns",
        "It increases screen size",
        "It deletes errors",
        "It replaces hardware"
    ],
    "answer": "It is used for learning patterns",
    "explanation": "AI learns from data, so better data = better performance."
}
]

# ---------------- SESSION ----------------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "questions" not in st.session_state:
    st.session_state.questions = random.sample(QUESTIONS, len(QUESTIONS))

# ---------------- HOME ----------------

if st.session_state.page == "home":
    st.title("📚 MCQs Quiz 2026")

    name = st.text_input("Enter Your Name")

    if st.button("Start Quiz"):
        if not name:
            st.warning("Enter your name first!")
            st.stop()

        st.session_state.name = name
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.start_time = time.time()
        st.session_state.page = "quiz"
        st.rerun()

# ---------------- QUIZ ----------------

elif st.session_state.page == "quiz":

    q_index = st.session_state.current_question
    total = len(st.session_state.questions)

    if q_index >= total:
        st.session_state.page = "result"
        st.rerun()

    q = st.session_state.questions[q_index]

    st.title("📚 Quiz")

    st.progress((q_index + 1) / total)

    st.subheader(f"Q{q_index + 1}: {q['question']}")

    selected = st.radio("Choose answer", q["options"])

    if st.button("Next"):
        st.session_state.answers[q_index] = selected

        if selected == q["answer"]:
            st.session_state.score += 1

        st.session_state.current_question += 1
        st.rerun()

# ---------------- RESULT ----------------

elif st.session_state.page == "result":

    total = len(st.session_state.questions)
    score = st.session_state.score
    percent = (score / total) * 100

    st.title("🎉 Result")

    st.metric("Score", f"{score}/{total}")
    st.metric("Percentage", f"{percent:.2f}%")

    if percent >= 50:
        st.success("PASS")
    else:
        st.error("FAIL")

    if st.button("Restart Quiz"):
        st.session_state.page = "home"
        st.rerun()