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
        QUESTIONS = [
            {"q": "1. Which keyword starts a comment in Python?", "options": ["//", "<!--", "#", "/*"], "answer": "#", "explanation": "In Python, comments start with the # symbol."},
            {"q": "2. In name: str = 'Alice', the annotation str is a …", "options": ["run-time type checker", "type hint decorator", "string literal"], "answer": "type hint decorator", "explanation": "The str here is a type hint, indicating the expected type."},
            {"q": "3. Given def area(r: float) -> float: …, what will mypy warn about?", "options": ["Missing return", "Use of float", "Returning a str value", "Using *args"], "answer": "Returning a str value", "explanation": "mypy warns if a function annotated to return float actually returns a str."},
            {"q": "4. Which built-in function reveals the data-type of a variable at run-time?", "options": ["id()", "eval()", "type()", "dir()"], "answer": "type()", "explanation": "type() returns the type of the object passed to it."},
            {"q": "5. What is printed?\n\nx: int = 5\nprint(type(x) is int)", "options": ["'True'", "True", "<class 'int'>", "None"], "answer": "True", "explanation": "type(x) is int checks identity and returns True for built-in types."},
            {"q": "6. Choose the legal variable name:", "options": ["2nd_place", "user-name", "_score", "class"], "answer": "_score", "explanation": "_score is valid; 2nd_place starts with a digit, user-name has -, and class is a keyword."},
            {"q": "7. Dynamic typing in Python means …", "options": ["variable names can re-bind to any object at run-time", "all names must be pre-declared", "types change only on reboot", "values change automatically to str"], "answer": "variable names can re-bind to any object at run-time", "explanation": "Variables in Python are dynamically typed and can point to any object type."},
            {"q": "8. PEP 484 introduced …", "options": ["async/await", "f-strings", "type hints", "dataclasses"], "answer": "type hints", "explanation": "PEP 484 defined standard type hints in Python."},
            {"q": "9. Fill the blank so the function returns an int:\ndef add(a: int, b: int) -> ______:\n    return a + b", "options": ["float", "str", "Any", "int"], "answer": "int", "explanation": "The return annotation should match the returned value's type, which is int."},
            {"q": "10. Which library can enforce hints with run-time checks?", "options": ["random", "typing", "pydantic", "calendar"], "answer": "pydantic", "explanation": "pydantic uses type hints and enforces them at run-time."},
            {"q": "11. What does int('3.9') raise?", "options": ["NameError", "TypeError", "KeyError", "ValueError"], "answer": "ValueError", "explanation": "int() can't convert a string with decimal point, so it raises ValueError."},
            {"q": "12. 'hello'.capitalize() returns …", "options": ["HELLO", "Hello", "hello", "Hello "], "answer": "Hello", "explanation": "capitalize() returns the string with first letter in uppercase and the rest lowercase."},
            {"q": "13. bool('') evaluates to …", "options": ["'False'", "False", "True", "None"], "answer": "False", "explanation": "Empty strings are considered False in Python's truthy/falsy rules."},
            {"q": "14. Which operator concatenates two strings?", "options": ["+", "*", "%", "&"], "answer": "+", "explanation": "The + operator concatenates strings in Python."},
            {"q": "15. Choose the statement that safely converts user = '42' to an integer and hints the result:", "options": ["age = user as int", "age: int = int(user)", "int age = user", "user:int()"], "answer": "age: int = int(user)", "explanation": "This is the correct way to cast and hint the type."},
            {"q": "16. The slice 'Python'[1:4] yields …", "options": ["'Pyt'", "'yth'", "'yth'", "'hon'"], "answer": "'yth'", "explanation": "Slice 1:4 returns characters at index 1, 2, and 3 → 'yth'."},
            {"q": "17. What does str(3.0) return?", "options": ["3", "'3.0'", "'3'", "3.0"], "answer": "'3.0'", "explanation": "str(3.0) converts the float 3.0 into string '3.0'."},
            {"q": "18. Result of 7 // 2 is …", "options": ["3.5", "3.0", "3", "TypeError"], "answer": "3", "explanation": "// performs floor division and returns integer part only."},
            {"q": "19. The keyword not has higher precedence than …", "options": ["and", "is", "==", "or"], "answer": "or", "explanation": "Operator precedence: not > and > or."},
            {"q": "20. Which loop prints numbers 0-4?\nfor i in ______(5):\n    print(i)", "options": ["enumerate", "list", "range", "iter"], "answer": "range", "explanation": "range(5) generates numbers 0 to 4."},
            {"q": "21. How many times does this run?\ncount = 0\nwhile count < 3:\n    count += 1", "options": ["0", "2", "3", "4"], "answer": "3", "explanation": "The loop runs while count is less than 3, so 3 times."},
            {"q": "22. The else clause tied to a for loop executes when …", "options": ["break fires", "continue fires", "the loop ends naturally", "an exception occurs"], "answer": "the loop ends naturally", "explanation": "else on a loop runs only if the loop wasn't terminated by break."},
            {"q": "23. Choose the operator that tests identity, not equality:", "options": ["==", "!=", "is", "in"], "answer": "is", "explanation": "The is operator checks if two names point to the same object."},
            {"q": "24. What prints?\nfor x in [1, 2, 3]:\n    if x % 2 == 0:\n        break\nelse:\n    print('done')", "options": ["done", "2 done", "nothing", "nothing (loop breaks)"], "answer": "nothing (loop breaks)", "explanation": "The loop breaks on x=2, so else does not execute."},
            {"q": "25. Pick the immutable collection:", "options": ["list", "tuple", "dict", "set"], "answer": "tuple", "explanation": "tuple is immutable; list, dict, and set are mutable."},
            {"q": "26. Which statement adds an item to a list in-place?", "options": ["items + [x]", "items.append(x)", "items = items + [x]", "items.extend = x"], "answer": "items.append(x)", "explanation": "append adds an item in-place without creating a new list."},
            {"q": "27. What does {}.get('key') return when 'key' is missing?", "options": ["None", "False", "''", "KeyError"], "answer": "None", "explanation": "dict.get() returns None if the key is not found."},
            {"q": "28. The literal {1, 2, 3} | {3, 4} results in …", "options": ["{1, 2, 3, 4}", "{3}", "{4}", "{1, 2}"], "answer": "{1, 2, 3, 4}", "explanation": "| is the union operator for sets."},
            {"q": "29. Choose the valid way to declare an empty dictionary:", "options": ["{}", "dict()", "[]", "()"], "answer": "{}", "explanation": "{} creates an empty dict; [] is a list, () is tuple."},
            {"q": "30. Which type hint marks a list of integers?", "options": ["list", "list[int]", "List()", "tuple[int]"], "answer": "list[int]", "explanation": "list[int] (or List[int] with from typing) marks a list of ints."},
            {"q": "31. Why use frozenset over set?", "options": ["faster iteration", "supports duplicates", "hashable & immutable", "ordered behaviour"], "answer": "hashable & immutable", "explanation": "frozenset is immutable and can be used as dict keys."},
            {"q": "32. Given scores: dict[str, int], what does the value side accept?", "options": ["'99'", "99", "[99]", "{'99'}"], "answer": "99", "explanation": "dict[str, int] means keys are str, values are int."},
            {"q": "33. Default parameter values are evaluated …", "options": ["once, at function definition time", "each call", "on import", "never"], "answer": "once, at function definition time", "explanation": "Defaults are evaluated only once at function definition."},
            {"q": "34. Which import renames a module?", "options": ["import math.pi as p", "import math as m", "from math import sqrt as math", "import sqrt from math"], "answer": "import math as m", "explanation": "import math as m renames math to m."},
            {"q": "35. __name__ == '__main__' guards allow …", "options": ["code to run only when the file is executed directly", "type checking", "unit tests to fail", "import cycles"], "answer": "code to run only when the file is executed directly", "explanation": "This idiom prevents code from running when the module is imported."},
            {"q": "36. Select the correct type-hinted function that returns nothing:", "options": ["def log(msg: str) -> None: print(msg)", "def log(msg) => None:", "def log(str) -> void:", "def log(msg: str): pass -> None"], "answer": "def log(msg: str) -> None: print(msg)", "explanation": "Functions returning nothing are annotated with -> None."},
            {"q": "37. Which block always executes?", "options": ["try", "except", "else", "finally"], "answer": "finally", "explanation": "finally always runs whether an exception occurred or not."},
            {"q": "38. Identify the pattern that re-raises an exception:\ntry:\n    risky()\nexcept Exception as e:\n    ______", "options": ["e", "pass", "ignore()", "raise"], "answer": "raise", "explanation": "raise (by itself) re-raises the current exception."},
            {"q": "39. What exception is raised by open('nosuch.txt') without error handling?", "options": ["ValueError", "FileNotFoundError", "ImportError", "KeyError"], "answer": "FileNotFoundError", "explanation": "Trying to open a non-existent file raises FileNotFoundError."},
            {"q": "40. In with open('log.txt', 'w') as f:, the mode 'w' means …", "options": ["write (truncate)", "append", "read binary", "update binary"], "answer": "write (truncate)", "explanation": "'w' writes to the file, truncating it first."},
            {"q": "41. After a with block ends, the file object f is …", "options": ["flushed only", "automatically closed", "deleted", "converted to bytes"], "answer": "automatically closed", "explanation": "with automatically closes the file when block exits."},
            {"q": "42. Which method reads the entire file into a single string?", "options": ["readline()", "readlines()", "read()", "iter()"], "answer": "read()", "explanation": "read() returns the entire file contents as a string."},
            {"q": "43. What does import math; math.pi evaluate to (rounded)?", "options": ["2.718", "1.618", "3.141592653589793", "3.14 string"], "answer": "3.141592653589793", "explanation": "math.pi is defined as 3.141592653589793."},
            {"q": "44. Using datetime, which class represents a calendar date only?", "options": ["date", "time", "datetime", "timedelta"], "answer": "date", "explanation": "datetime.date represents date (year, month, day) only."},
            {"q": "45. Choose the correct timedelta construction for '2 hours':", "options": ["timedelta(hours=120)", "timedelta(days=2)", "timedelta(hours=2)", "timedelta(minutes=1200)"], "answer": "timedelta(hours=2)", "explanation": "timedelta(hours=2) represents exactly 2 hours."},
        ]
        return QUESTIONS

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
        This quiz contains 45 questions about Python(simples papers).
        You'll have 1.3 minute to answer each question.
        """)
        
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.rerun()

    def show_question(self):
        st.title("Python Quiz 1st Qurater")
        
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
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(self.questions)}")
        st.write(question_data["q"])
        
        # Display options
        if 'user_answer' not in st.session_state:
            st.session_state.user_answer = None
        
        for option in question_data["options"]:
            if st.button(option, key=option):
                st.session_state.user_answer = option
        
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
            "question": question_data["q"],
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
            with st.expander(f"Question {i + 1}: {answer['question']}"):
                if answer['time_expired']:
                    st.error("Time expired - no answer submitted")
                elif answer['is_correct']:
                    st.success("Your answer: CORRECT")
                else:
                    st.error("Your answer: INCORRECT")
                    if answer['user_answer']:
                        st.write(f"You selected: {answer['user_answer']}")
                    st.write(f"Correct answer: {answer['correct_answer']}")
                
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
