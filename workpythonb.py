import streamlit as st
import random

class PythonQuizApp:
    def __init__(self):
        # Initialize quiz variables in session state
        if 'questions' not in st.session_state:
            st.session_state.questions = self.load_questions()
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'user_answers' not in st.session_state:
            st.session_state.user_answers = []
        if 'shuffled_indices' not in st.session_state:
            st.session_state.shuffled_indices = list(range(len(st.session_state.questions)))
            random.shuffle(st.session_state.shuffled_indices)
        if 'selected_option' not in st.session_state:
            st.session_state.selected_option = None
        
        # Show welcome screen if not started
        if 'quiz_started' not in st.session_state:
            st.session_state.quiz_started = False
            self.create_welcome_screen()
        elif not st.session_state.quiz_started:
            self.create_welcome_screen()
        else:
            self.show_question()
    
    def load_questions(self):
        questions = [
            {
                "question": "301. Who developed Python Programming Language?",
                "options": ["a) Wick van Rossum", "b) Rasmus Lerdorf", "c) Guido van Rossum", "d) Niene Stom"],
                "answer": "c",
                "explanation": "Python was designed by Guido van Rossum."
            },
            {
                "question": "2. Which type of Programming does Python support?",
                "options": ["a) object-oriented programming", "b) structured programming", "c) functional programming", "d) all of the mentioned"],
                "answer": "d",
                "explanation": "Python supports OOP, structured, and functional programming."
            },
            {
                "question": "3. Is Python case sensitive when dealing with identifiers?",
                "options": ["a) no", "b) yes", "c) machine dependent", "d) none of the mentioned"],
                "answer": "b",
                "explanation": "Case is always significant in Python identifiers."
            },
            {
                "question": "4. Which of the following is the correct extension of the Python file?",
                "options": ["a) .python", "b) .pl", "c) .py", "d) .p"],
                "answer": "c",
                "explanation": "Python files use .py extension."
            },
            # ... (include all the other questions from the original code)
            # I'm truncating the list here for brevity, but you should include all 80 questions
            {
                "question": "80. Can users transparently use cloud resources?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Users don't need to know implementation details."
            }
        ]
        return questions

    def create_welcome_screen(self):
        st.title("Python Quiz Challenge")
        st.markdown("""
            This quiz contains 80 questions about Python programming and cloud computing.
            You'll get detailed feedback after completing the quiz.
            
            Click Start to begin!
        """)
        
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.rerun()
    
    def show_question(self):
        # Get current question data
        question_idx = st.session_state.shuffled_indices[st.session_state.current_question]
        question_data = st.session_state.questions[question_idx]
        
        st.title(f"Question {st.session_state.current_question + 1} of {len(st.session_state.questions)}")
        st.subheader(question_data["question"])
        
        # Display options as radio buttons
        option_labels = [opt[0] for opt in question_data["options"]]
        options_text = [opt[3:] for opt in question_data["options"]]
        
        selected = st.radio(
            "Select your answer:",
            options_text,
            index=None,
            key=f"question_{st.session_state.current_question}"
        )
        
        st.session_state.selected_option = selected
        
        col1, col2, col3 = st.columns([1,1,1])
        
        # Navigation buttons
        if st.session_state.current_question > 0:
            if col1.button("Previous"):
                self.prev_question()
        
        if st.session_state.current_question < len(st.session_state.questions) - 1:
            if col2.button("Next"):
                self.next_question()
        else:
            if col2.button("Submit"):
                self.next_question()
        
        if col3.button("Quit"):
            st.session_state.quiz_started = False
            st.rerun()
    
    def prev_question(self):
        if st.session_state.current_question > 0:
            st.session_state.current_question -= 1
            st.rerun()
    
    def next_question(self):
        if st.session_state.selected_option is None:
            st.warning("Please select an answer!")
            return
        
        # Get the selected option letter (a, b, c, etc.)
        selected_answer = None
        question_data = st.session_state.questions[
            st.session_state.shuffled_indices[st.session_state.current_question]
        ]
        
        for opt in question_data["options"]:
            if st.session_state.selected_option in opt:
                selected_answer = opt[0].lower()
                break
        
        # Check answer and store result
        is_correct = (selected_answer == question_data["answer"])
        st.session_state.user_answers.append({
            "question": question_data["question"],
            "user_answer": selected_answer,
            "correct_answer": question_data["answer"],
            "is_correct": is_correct,
            "explanation": question_data["explanation"]
        })
        
        if is_correct:
            st.session_state.score += 1
        
        # Move to next question or show results
        if st.session_state.current_question < len(st.session_state.questions) - 1:
            st.session_state.current_question += 1
            st.session_state.selected_option = None
            st.rerun()
        else:
            self.show_results()
    
    def show_results(self):
        st.title("Quiz Results")
        
        # Calculate score
        score_percent = (st.session_state.score / len(st.session_state.questions)) * 100
        
        st.subheader(f"Your score: {st.session_state.score}/{len(st.session_state.questions)} ({score_percent:.1f}%)")
        
        # Detailed feedback
        st.subheader("Detailed Feedback:")
        
        for i, answer in enumerate(st.session_state.user_answers):
            with st.expander(f"Question {i+1}: {answer['question']}"):
                if answer['is_correct']:
                    st.success("Your answer: CORRECT")
                else:
                    st.error("Your answer: INCORRECT")
                    st.write(f"You selected: {answer['user_answer'].upper()}")
                    st.write(f"Correct answer: {answer['correct_answer'].upper()}")
                
                st.write(f"Explanation: {answer['explanation']}")
        
        # Restart or quit buttons
        col1, col2 = st.columns([1,1])
        
        if col1.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.user_answers = []
            st.session_state.selected_option = None
            random.shuffle(st.session_state.shuffled_indices)
            st.rerun()
        
        if col2.button("Quit"):
            st.session_state.quiz_started = False
            st.rerun()

# Run the app
if __name__ == "__main__":
    app = PythonQuizApp()