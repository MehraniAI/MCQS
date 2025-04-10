import streamlit as st
import random
import time

st.markdown('<h1 style="color:blue">Prepared by Devan Das Mehrani AI Student</h1>', unsafe_allow_html=True)

class PythonQuizApp:
    def __init__(self):
        self.questions = self.load_questions()
        if 'current_question' not in st.session_state:
            self.initialize_session_state()
        
    def initialize_session_state(self):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.user_answers = []
        st.session_state.shuffled_indices = list(range(len(self.questions)))
        random.shuffle(st.session_state.shuffled_indices)
        st.session_state.time_per_question = 60  # 1 minute per question
        st.session_state.start_time = time.time()
        st.session_state.timer_expired = False

    def load_questions(self):
        questions = [
            # Question 651-700 
            {
        "question": "651. What happens if you try to `del` a variable that doesn’t exist?",
        "options": [
            "a) It silently does nothing",
            "b) It raises a `NameError`",
            "c) It returns `False`",
            "d) It creates the variable"
        ],
        "answer": "b) It raises a `NameError`"
    },
    {
        "question": "652. Which of the following is NOT a valid way to create a string in Python?",
        "options": [
            "a) `my_str = 'Hello'`",
            "b) `my_str = \"Hello\"`",
            "c) `my_str = '''Hello'''`",
            "d) `my_str = (Hello)`"
        ],
        "answer": "d) `my_str = (Hello)`"
    },
    {
        "question": "653. What does it mean that Python strings are immutable?",
        "options": [
            "a) They cannot be changed after creation",
            "b) They can only contain numeric characters",
            "c) They automatically convert to uppercase",
            "d) They can be modified in-place"
        ],
        "answer": "a) They cannot be changed after creation"
    },
    {
        "question": "654. What is the output of: `print(r'Hello\\tWorld')`?",
        "options": [
            "a) Hello    World",
            "b) Hello\\tWorld",
            "c) Hello\nWorld",
            "d) Error"
        ],
        "answer": "b) Hello\\tWorld"
    },
    {
        "question": "655. Which string creation method allows for multi-line strings?",
        "options": [
            "a) Single quotes",
            "b) Double quotes",
            "c) Triple quotes",
            "d) Raw strings"
        ],
        "answer": "c) Triple quotes"
    },
    {
        "question": "656. What does the `\\b` escape sequence do?",
        "options": [
            "a) Inserts a tab",
            "b) Inserts a backspace",
            "c) Inserts a backslash",
            "d) Inserts a newline"
        ],
        "answer": "b) Inserts a backspace"
    },
    {
        "question": "657. Which escape sequence would you use to include a double quote inside a double-quoted string?",
        "options": [
            "a) `\\'`",
            "b) `\\\"`",
            "c) `\\\\`",
            "d) `\\n`"
        ],
        "answer": "b) `\\\"`"
    },
    {
        "question": "658. What is the output of: `'Hello' + 'World'`?",
        "options": [
            "a) 'Hello World'",
            "b) 'HelloWorld'",
            "c) 'Hello+World'",
            "d) Error"
        ],
        "answer": "b) 'HelloWorld'"
    },
    {
        "question": "659. What does `'Hello'[1]` return?",
        "options": [
            "a) 'H'",
            "b) 'e'",
            "c) 'l'",
            "d) 'o'"
        ],
        "answer": "b) 'e'"
    },
    {
        #Questions 660-670

        "question": "660. What is the output of: `'Hello World!'[7:]`?",
        "options": [
            "a) 'World!'",
            "b) 'World'",
            "c) 'orld!'",
            "d) 'Hello'"
        ],
        "answer": "a) 'World!'"
    },
    {
        "question": "661. What does `len(\" Python \")` return?",
        "options": [
            "a) 6",
            "b) 7",
            "c) 8",
            "d) 9"
        ],
        "answer": "c) 8"
    },
    {
        "question": "662. What does `'hello'.upper()` return?",
        "options": [
            "a) 'HELLO'",
            "b) 'Hello'",
            "c) 'hello'",
            "d) Error"
        ],
        "answer": "a) 'HELLO'"
    },
    {
        "question": "663. What is the output of: `'Hello World'.split('l')`?",
        "options": [
            "a) ['He', '', 'o Wor', 'd']",
            "b) ['Hello', 'World']",
            "c) ['H', 'e', 'l', 'l', 'o']",
            "d) Error"
        ],
        "answer": "a) ['He', '', 'o Wor', 'd']"
    },
    {
        "question": "664. What does `','.join(['a', 'b', 'c'])` return?",
        "options": [
            "a) 'a,b,c'",
            "b) 'a b c'",
            "c) 'a, b, c'",
            "d) ['a,b,c']"
        ],
        "answer": "a) 'a,b,c'"
    },
    {
        "question": "665. What is the output of: `'hello'.find('l')`?",
        "options": [
            "a) 1",
            "b) 2",
            "c) 3",
            "d) -1"
        ],
        "answer": "b) 2"
    },
    {
        "question": "666. What does `'hello hello'.count('he')` return?",
        "options": [
            "a) 1",
            "b) 2",
            "c) 0",
            "d) 5"
        ],
        "answer": "b) 2"
    },
    {
        "question": "667. Which string formatting method was introduced in Python 3.6?",
        "options": [
            "a) %-formatting",
            "b) str.format()",
            "c) f-strings",
            "d) Template strings"
        ],
        "answer": "c) f-strings"
    },
    {
        "question": "668. What is the output of: `f\"2 + 2 = {2+2}\"`?",
        "options": [
            "a) '2 + 2 = 4'",
            "b) '2 + 2 = {2+2}'",
            "c) '4 = 4'",
            "d) Error"
        ],
        "answer": "a) '2 + 2 = 4'"
    },
    {
        "question": "669. Which placeholder would you use for a floating-point number with 2 decimal places using %-formatting?",
        "options": [
            "a) `%d`",
            "b) `%f`",
            "c) `%.2f`",
            "d) `%s`"
        ],
        "answer": "c) `%.2f`"
    },
    {
        "question": "670. What is the output of:\n```python\na = \"hello\"\nb = \"hello\"\nprint(a is b)\n```",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "a) True"
    },
    {
        #Questions 671-680

        "question": "671. Which strings are typically NOT automatically interned in Python?",
        "options": [
            "a) Short strings",
            "b) Strings that look like identifiers",
            "c) Very long strings",
            "d) Strings containing only digits"
        ],
        "answer": "c) Very long strings"
    },
    {
        "question": "672. What is the output of: `'apple' < 'banana'`?",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "a) True"
    },
    {
        "question": "673. What is the output of: `'A' > 'a'`?",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "b) False"
    },
    {
        "question": "674. What is the output of: `int(3.9)`?",
        "options": [
            "a) 3",
            "b) 4",
            "c) 3.0",
            "d) Error"
        ],
        "answer": "a) 3"
    },
    {
        "question": "675. What is the output of: `str(True)`?",
        "options": [
            "a) '1'",
            "b) 'True'",
            "c) True",
            "d) Error"
        ],
        "answer": "b) 'True'"
    },
    {
        "question": "676. What is the output of: `bool(\"\")`?",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "b) False"
    },
    {
        "question": "677. What is the output of: `'Hi' * 3`?",
        "options": [
            "a) 'HiHiHi'",
            "b) 'Hi Hi Hi'",
            "c) 'Hi3'",
            "d) Error"
        ],
        "answer": "a) 'HiHiHi'"
    },
    {
        "question": "678. What is the output of:\n```python\ns = 'hello'\nprint(s.replace('l', 'x'))\n```",
        "options": [
            "a) 'hexxo'",
            "b) 'hexo'",
            "c) 'hxxo'",
            "d) 'hello'"
        ],
        "answer": "a) 'hexxo'"
    },
    {
        "question": "679. What is the output of: `'hello'.title()`?",
        "options": [
            "a) 'HELLO'",
            "b) 'Hello'",
            "c) 'hello'",
            "d) 'H e l l o'"
        ],
        "answer": "b) 'Hello'"
    },
    {
        "question": "680. Which method would you use to remove whitespace from both ends of a string?",
        "options": [
            "a) `trim()`",
            "b) `strip()`",
            "c) `clean()`",
            "d) `remove()`"
        ],
        "answer": "b) `strip()`"
    },
    {
        #Question 681-690

        "question": "681. What is the output of: `'hello'.isalpha()`?",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "a) True"
    },
    {
        "question": "682. How can you create a multi-line string in Python?",
        "options": [
            "a) Using single quotes",
            "b) Using double quotes",
            "c) Using triple quotes",
            "d) Using square brackets"
        ],
        "answer": "c) Using triple quotes"
    },
    {
        "question": "683. What is the output of `print(r\"Hello\\nWorld\")`?",
        "options": [
            "a) `Hello\nWorld`",
            "b) `Hello\\nWorld`",
            "c) `Hello World`",
            "d) `rHello World`"
        ],
        "answer": "b) `Hello\\nWorld`"
    },
    {
        "question": "684. Which escape sequence represents a tab character?",
        "options": [
            "a) `\\n`",
            "b) `\\t`",
            "c) `\\b`",
            "d) `\\\\`"
        ],
        "answer": "b) `\\t`"
    },
    {
        "question": "685. What does `my_string[7:]` do?",
        "options": [
            "a) Returns the first 7 characters",
            "b) Returns characters from index 7 to the end",
            "c) Returns the last 7 characters",
            "d) Raises an error"
        ],
        "answer": "b) Returns characters from index 7 to the end"
    },
    {
        "question": "686. How do you convert a string to uppercase?",
        "options": [
            "a) `my_string.toUpper()`",
            "b) `my_string.upper()`",
            "c) `upper(my_string)`",
            "d) `my_string.capitalize()`"
        ],
        "answer": "b) `my_string.upper()`"
    },
    {
        "question": "687. What is the output of `\"Hello, World!\".split(\"l\")`?",
        "options": [
            "a) `[\"He\", \"\", \"o, Wor\", \"d!\"]`",
            "b) `[\"Hello\", \"World\"]`",
            "c) `[\"H\", \"e\", \"l\", \"l\", \"o\"]`",
            "d) `[\"Hel\", \"lo, Wor\", \"d!\"]`"
        ],
        "answer": "a) `[\"He\", \"\", \"o, Wor\", \"d!\"]`"
    },
    {
        "question": "688. Which method joins a list of strings into a single string?",
        "options": [
            "a) `concat()`",
            "b) `merge()`",
            "c) `join()`",
            "d) `combine()`"
        ],
        "answer": "c) `join()`"
    },
    {
        "question": "689. What does `\"hello\".count(\"l\")` return?",
        "options": [
            "a) 1",
            "b) 2",
            "c) 3",
            "d) 0"
        ],
        "answer": "b) 2"
    },
    {
        "question": "690. Which operator is used for string repetition?",
        "options": [
            "a) `+`",
            "b) `*`",
            "c) ``",
            "d) `//`"
        ],
        "answer": "b) `*`"
    },
    {
        #Questons 691-700
        
        "question": "691. What is the result of `\"apple\" < \"banana\"`?",
        "options": [
            "a) `True`",
            "b) `False`",
            "c) `None`",
            "d) `Error`"
        ],
        "answer": "a) `True`"
    },
    {
        "question": "692. Which function converts an integer to a string?",
        "options": [
            "a) `int()`",
            "b) `float()`",
            "c) `str()`",
            "d) `chr()`"
        ],
        "answer": "c) `str()`"
    },
    {
        "question": "693. What does `\"123abc\".isnumeric()` return?",
        "options": [
            "a) `True`",
            "b) `False`",
            "c) `None`",
            "d) `Error`"
        ],
        "answer": "b) `False`"
    },
    {
        "question": "694. Which method checks if a string starts with a specific substring?",
        "options": [
            "a) `startswith()`",
            "b) `beginwith()`",
            "c) `checkprefix()`",
            "d) `firstmatch()`"
        ],
        "answer": "a) `startswith()`"
    },
    {
        "question": "695. What is the output of `\"-\".join([\"A\", \"B\", \"C\"])`?",
        "options": [
            "a) `\"A-B-C\"`",
            "b) `\"A B C\"`",
            "c) `\"ABC\"`",
            "d) `[\"A\", \"B\", \"C\"]`"
        ],
        "answer": "a) `\"A-B-C\"`"
    },
    {
        "question": "696. How do you replace \"cat\" with \"dog\" in `\"I love cats\"`?",
        "options": [
            "a) `replace(\"cat\", \"dog\")`",
            "b) `swap(\"cat\", \"dog\")`",
            "c) `substitute(\"cat\", \"dog\")`",
            "d) `change(\"cat\", \"dog\")`"
        ],
        "answer": "a) `replace(\"cat\", \"dog\")`"
    },
    {
        "question": "697. What is string interning in Python?",
        "options": [
            "a) Storing only one copy of each unique string to save memory",
            "b) Converting strings to integers",
            "c) A method to reverse strings",
            "d) A way to encrypt strings"
        ],
        "answer": "a) Storing only one copy of each unique string to save memory"
    },
    {
        "question": "698. Which strings are automatically interned?",
        "options": [
            "a) All strings",
            "b) Only strings longer than 20 characters",
            "c) Short strings and identifiers",
            "d) Only strings containing numbers"
        ],
        "answer": "c) Short strings and identifiers"
    },
    {
        "question": "699. What does `sys.intern()` do?",
        "options": [
            "a) Deletes a string from memory",
            "b) Manually interns a string",
            "c) Converts a string to lowercase",
            "d) Checks if a string is numeric"
        ],
        "answer": "b) Manually interns a string"
    },
    {
        "question": "700. What is the output of `\"Python\" * 3`?",
        "options": [
            "a) `\"PythonPythonPython\"`",
            "b) `\"Python 3\"`",
            "c) `\"PythonPython\"`",
            "d) `Error`"
        ],
        "answer": "a) `\"PythonPythonPython\"`"
    }
       ]
        return questions

    def display_timer(self):
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.time_per_question - int(elapsed_time))
        
        mins, secs = divmod(remaining_time, 60)
        timer_text = f"⏱️ Time remaining: {mins:02d}:{secs:02d}"
        
        if remaining_time <= 0 and not st.session_state.timer_expired:
            st.session_state.timer_expired = True
            st.rerun()
        
        return remaining_time, timer_text

    def show_welcome_screen(self):
        st.title("Python String Methods Quiz")
        st.write("""
        This quiz contains 50 questions about Python string methods (Questions 651-700).
        You'll have 1 minute to answer each question.
        """)
        
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.rerun()

    def show_question(self):
        st.title("Python String Methods Quiz")
        
        # Display timer
        remaining_time, timer_text = self.display_timer()
        st.write(timer_text)
        
        if remaining_time <= 0:
            self.handle_time_expired()
            return
        
        # Get current question data
        question_data = self.questions[
            st.session_state.shuffled_indices[st.session_state.current_question]
        ]
        
        # Display question
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(self.questions)} (Q{651 + st.session_state.current_question})")
        st.write(question_data["question"])
        
        # Display options
        if 'user_answer' not in st.session_state:
            st.session_state.user_answer = None
        
        for option in question_data["options"]:
            if st.button(option, key=option):
                st.session_state.user_answer = option[0].lower()
        
        # Navigation buttons
        col1, col2, col3 = st.columns(3)
        
        if st.session_state.current_question > 0:
            if col1.button("Previous"):
                st.session_state.current_question -= 1
                st.session_state.user_answer = None
                st.session_state.start_time = time.time()
                st.session_state.timer_expired = False
                st.rerun()
        
        if st.session_state.current_question < len(self.questions) - 1:
            if col2.button("Next"):
                if st.session_state.user_answer is None:
                    st.warning("Please select an answer!")
                else:
                    self.record_answer(question_data)
                    st.session_state.current_question += 1
                    st.session_state.user_answer = None
                    st.session_state.start_time = time.time()
                    st.session_state.timer_expired = False
                    st.rerun()
        else:
            if col2.button("Submit"):
                if st.session_state.user_answer is None:
                    st.warning("Please select an answer!")
                else:
                    self.record_answer(question_data)
                    st.session_state.quiz_completed = True
                    st.rerun()
        
        if col3.button("Quit"):
            st.session_state.quiz_started = False
            st.rerun()

    def handle_time_expired(self):
        question_data = self.questions[
            st.session_state.shuffled_indices[st.session_state.current_question]
        ]
        
        self.record_answer(question_data, expired=True)
        
        if st.session_state.current_question < len(self.questions) - 1:
            st.session_state.current_question += 1
            st.session_state.user_answer = None
            st.session_state.start_time = time.time()
            st.session_state.timer_expired = False
            st.rerun()
        else:
            st.session_state.quiz_completed = True
            st.rerun()

    def record_answer(self, question_data, expired=False):
        if expired:
            user_answer = None
            is_correct = False
        else:
            user_answer = st.session_state.user_answer
            is_correct = (user_answer == question_data["answer"])
        
        st.session_state.user_answers.append({
            "question": question_data["question"],
            "user_answer": user_answer,
            "correct_answer": question_data["answer"],
            "is_correct": is_correct,
            "explanation": question_data["explanation"],
            "time_expired": expired
        })
        
        if is_correct:
            st.session_state.score += 1

    def show_results(self):
        st.title("Quiz Results")
        
        # Calculate score
        score_percent = (st.session_state.score / len(self.questions)) * 100
        
        # Display summary
        st.subheader(f"Your score: {st.session_state.score}/{len(self.questions)} ({score_percent:.1f}%)")
        
        # Detailed feedback
        st.subheader("Detailed Feedback:")
        
        for i, answer in enumerate(st.session_state.user_answers):
            with st.expander(f"Question {651 + i}: {answer['question']}"):
                if answer['time_expired']:
                    st.error("Time expired - no answer submitted")
                elif answer['is_correct']:
                    st.success("Your answer: CORRECT")
                else:
                    st.error("Your answer: INCORRECT")
                    if answer['user_answer']:
                        st.write(f"You selected: {answer['user_answer'].upper()}")
                    st.write(f"Correct answer: {answer['correct_answer'].upper()}")
                
                st.write(f"Explanation: {answer['explanation']}")
        
        # Restart button
        if st.button("Restart Quiz"):
            self.initialize_session_state()
            st.session_state.quiz_started = True
            st.session_state.quiz_completed = False
            st.rerun()

    def run(self):
        if 'quiz_started' not in st.session_state:
            st.session_state.quiz_started = False
        if 'quiz_completed' not in st.session_state:
            st.session_state.quiz_completed = False
        
        if not st.session_state.quiz_started:
            self.show_welcome_screen()
        elif not st.session_state.quiz_completed:
            self.show_question()
        else:
            self.show_results()

if __name__ == "__main__":
    app = PythonQuizApp()
    app.run()