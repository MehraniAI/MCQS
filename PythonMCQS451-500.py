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
            # Question 451-460 
            {
            "question": "451. What is the output of:\n```python\ndef f(x):\n    return x * 2\nprint(f(3))\n```",
            "options": ["a) 6", "b) 3", "c) 9", "d) Error"],
            "answer": "a) 6",
            "explanation": "The function doubles the input (3*2=6)."
            },
            {
            "question": "452. What does `return` without a value do?",
            "options": ["a) Returns `None`", "b) Raises an error", "c) Returns `0`", "d) Nothing"],
            "answer": "a) Returns `None`",
            "explanation": "A function with no return statement or just `return` returns None."
            },
            {
            "question": "453. What is a lambda function?",
            "options": ["a) An anonymous function", "b) A named function", "c) A recursive function", "d) None"],
            "answer": "a) An anonymous function",
            "explanation": "Lambda functions are small anonymous functions defined with the lambda keyword."
            },
            {
            "question": "454. What is the output of:\n```python\ndef f(x, y=2):\n    return x * y\nprint(f(3))\n```",
            "options": ["a) 6", "b) 5", "c) Error", "d) 3"],
            "answer": "a) 6",
            "explanation": "The default y=2 is used (3*2=6)."
            },
            {
            "question": "455. Which is not a function definition?",
            "options": [
                "a) def f(): pass",
                "b) f = lambda x: x",
                "c) function f() { }",
                "d) def f(x): return x"
            ],
            "answer": "c) function f() { }",
            "explanation": "This is JavaScript syntax, not Python."
            },
            {
            "question": "456. What is the output of print('Hi', 'Bye', sep='--')?",
            "options": ["a) Hi--Bye", "b) Hi Bye", "c) Hi,Bye", "d) Error"],
            "answer": "a) Hi--Bye",
            "explanation": "sep='--' specifies the separator between arguments."
            },
            {
            "question": "457. What does end='' do in print()?",
            "options": ["a) Prevents a newline", "b) Adds a space", "c) Ends the program", "d) None"],
            "answer": "a) Prevents a newline",
            "explanation": "end='' replaces the default newline with an empty string."
            },
            {
            "question": "458. What is the output of print(print(1))?",
            "options": ["a) 1 followed by None", "b) 1", "c) Error", "d) 1 1"],
            "answer": "a) 1 followed by None",
            "explanation": "The inner print(1) prints 1 and returns None, which is printed by the outer print."
            },
            {
            "question": "459. Which is not a valid print statement?",
            "options": [
                "a) print('Hi')",
                "b) print 'Hi' (Python 2)",
                "c) print(1, 2, 3)",
                "d) print x (Python 3)"
            ],
            "answer": "d) print x (Python 3)",
            "explanation": "Python 3 requires parentheses for print."
            },
            {
            "question": "460. What is the output of print(f'{2+3}')?",
            "options": ["a) 5", "b) 2+3", "c) {5}", "d) Error"],
            "answer": "a) 5",
            "explanation": "f-strings evaluate expressions inside curly braces."
            },

            # Question 461-470
            {
            "question": "461. What does os.getcwd() return?",
            "options": ["a) Current working directory", "b) List of files", "c) Environment variables", "d) None"],
            "answer": "a) Current working directory",
            "explanation": "getcwd() returns the current working directory path."
            },
            {
            "question": "462. Which function renames a file?",
            "options": ["a) os.rename()", "b) os.remove()", "c) os.listdir()", "d) os.mkdir()"],
            "answer": "a) os.rename()",
            "explanation": "os.rename() renames files or directories."
            },
            {
            "question": "463. What does os.path.join('a', 'b') return?",
            "options": ["a) 'a/b' (OS-dependent separator)", "b) 'a b'", "c) 'ab'", "d) Error"],
            "answer": "a) 'a/b' (OS-dependent separator)",
            "explanation": "os.path.join() creates paths with the correct separator for the OS."
            },
            {
            "question": "464. Which checks if a file exists?",
            "options": ["a) os.path.exists()", "b) os.path.isfile()", "c) Both", "d) None"],
            "answer": "c) Both",
            "explanation": "exists() checks for any path, isfile() specifically checks for files."
            },
            {
            "question": "465. What does os.environ contain?",
            "options": ["a) Environment variables", "b) Command-line arguments", "c) File paths", "d) None"],
            "answer": "a) Environment variables",
            "explanation": "os.environ is a dictionary of environment variables."
            },
            {
            "question": "466. What is Streamlit primarily used for?",
            "options": ["a) Web scraping", "b) Data visualization & web apps", "c) Game development", "d) None"],
            "answer": "b) Data visualization & web apps",
            "explanation": "Streamlit is for creating data apps quickly."
            },
            {
            "question": "467. Which command runs a Streamlit app?",
            "options": ["a) streamlit run app.py", "b) python app.py", "c) flask run", "d) None"],
            "answer": "a) streamlit run app.py",
            "explanation": "This is the standard way to run Streamlit apps."
            },
            {
            "question": "468. Which function creates a slider in Streamlit?",
            "options": ["a) st.slider()", "b) st.input()", "c) st.range()", "d) None"],
            "answer": "a) st.slider()",
            "explanation": "st.slider() creates interactive slider widgets."
            },
            {
            "question": "469. What is the output of print([1, 2, 3][1:])?",
            "options": ["a) [1, 2]", "b) [2, 3]", "c) [1, 2, 3]", "d) [1]"],
            "answer": "b) [2, 3]",
            "explanation": "Slicing from index 1 to end."
            },
            {
            "question": "470. How do you add an element 4 to the end of a list lst?",
            "options": ["a) lst.append(4)", "b) lst.add(4)", "c) lst.insert(4)", "d) lst += 4"],
            "answer": "a) lst.append(4)",
            "explanation": "append() adds to the end of a list."
            },

            # Question 471-480 
            {
            "question": "471. Which method removes the last element from a list?",
            "options": ["a) lst.remove()", "b) lst.pop()", "c) lst.delete()", "d) lst.clear()"],
            "answer": "b) lst.pop()",
            "explanation": "pop() removes and returns the last item by default."
            },
            {
            "question": "472. What is the key difference between a list and a tuple?",
            "options": [
                "a) Lists are mutable, tuples are immutable",
                "b) Tuples can store only integers",
                "c) Lists are faster than tuples",
                "d) Tuples use curly braces"
            ],
            "answer": "a) Lists are mutable, tuples are immutable",
            "explanation": "The main difference is mutability."
            },
            {
            "question": "473. How do you create a tuple with a single element?",
            "options": ["a) t = (1)", "b) t = 1,", "c) t = (1,)", "d) t = [1]"],
            "answer": "c) t = (1,)",
            "explanation": "The comma makes it a tuple, not just parentheses."
            },
            {
            "question": "474. What is the output of print((1, 2) + (3, 4))?",
            "options": ["a) (1, 2, 3, 4)", "b) (4, 6)", "c) [1, 2, 3, 4]", "d) Error"],
            "answer": "a) (1, 2, 3, 4)",
            "explanation": "Tuples can be concatenated with +."
            },
            {
            "question": "475. Which of the following is not a property of a set?",
            "options": ["a) Unordered", "b) Mutable", "c) Allows duplicate elements", "d) Uses {}"],
            "answer": "c) Allows duplicate elements",
            "explanation": "Sets automatically remove duplicates."
            },
            {
            "question": "476. What is the output of print({1, 2, 2, 3})?",
            "options": ["a) {1, 2, 2, 3}", "b) {1, 2, 3}", "c) {2}", "d) Error"],
            "answer": "b) {1, 2, 3}",
            "explanation": "Sets remove duplicate values."
            },
            {
            "question": "477. Which operation returns the intersection of two sets A and B?",
            "options": ["a) A | B", "b) A & B", "c) A - B", "d) A ^ B"],
            "answer": "b) A & B",
            "explanation": "& returns elements common to both sets."
            },
            {
            "question": "478. How do you access the value for the key 'age' in a dictionary d?",
            "options": ["a) d['age']", "b) d.get('age')", "c) d('age')", "d) Both a and b"],
            "answer": "d) Both a and b",
            "explanation": "Both square brackets and get() work."
            },
            {
            "question": "479. Which method removes all items from a dictionary?",
            "options": ["a) d.clear()", "b) d.delete()", "c) d.remove()", "d) d.pop()"],
            "answer": "a) d.clear()",
            "explanation": "clear() empties the dictionary."
            },
            {
            "question": "480. What is the output of print({'a': 1, 'b': 2}.get('c', 3))?",
            "options": ["a) 1", "b) 2", "c) 3", "d) None"],
            "answer": "c) 3",
            "explanation": "get() returns the default (3) when key doesn't exist."
            },

            # Question 481-490
            {
            "question": "481. What is the output of 'hello'.upper()?",
            "options": ["a) 'HELLO'", "b) 'Hello'", "c) 'hello'", "d) 'hElLo'"],
            "answer": "a) 'HELLO'",
            "explanation": "upper() converts to uppercase."
            },
            {
            "question": "482. How do you split a string s into a list of words?",
            "options": ["a) s.split()", "b) s.join()", "c) s.slice()", "d) s.split(' ')"],
            "answer": "a) s.split()",
            "explanation": "split() divides by whitespace by default."
            },
            {
            "question": "483. What does 'abc'.replace('b', 'x') return?",
            "options": ["a) 'axc'", "b) 'abc'", "c) 'axb'", "d) 'xbx'"],
            "answer": "a) 'axc'",
            "explanation": "replace() substitutes characters."
            },
            {
            "question": "484. What is a parameter in Python?",
            "options": [
                "a) A value passed to a function",
                "b) A variable in the function definition",
                "c) A return value",
                "d) A built-in function"
            ],
            "answer": "b) A variable in the function definition",
            "explanation": "Parameters are the function's variable placeholders."
            },
            {
            "question": "485. What is the output of:\n```python\ndef greet(name='World'):\n    print(f'Hello, {name}')\ngreet()\n```",
            "options": ["a) Hello, name", "b) Hello, World", "c) Error", "d) Hello,"],
            "answer": "b) Hello, World",
            "explanation": "Default parameter 'World' is used."
            },
            {
            "question": "486. Which type of argument is passed in func(a=1, b=2)?",
            "options": ["a) Positional", "b) Keyword", "c) Default", "d) Variable-length"],
            "answer": "b) Keyword",
            "explanation": "Arguments passed with names are keyword arguments."
            },
            {
            "question": "487. What is the output of:\n```python\nx = 10\nif x > 5:\n    print('A')\nelif x > 8:\n    print('B')\nelse:\n    print('C')\n```",
            "options": ["a) A", "b) B", "c) C", "d) A B"],
            "answer": "a) A",
            "explanation": "First true condition (x>5) executes."
            },
            {
            "question": "488. Which operator checks for equality?",
            "options": ["a) =", "b) ==", "c) ===", "d) !="],
            "answer": "b) ==",
            "explanation": "== is the equality comparison operator."
            },
            {
            "question": "489. What is the output of print(not True and False)?",
            "options": ["a) True", "b) False", "c) Error", "d) None"],
            "answer": "b) False",
            "explanation": "not True is False, and False and False is False."
            },
            {
            "question": "490. How do you define a function in Python?",
            "options": [
                "a) function my_func():",
                "b) def my_func():",
                "c) define my_func():",
                "d) func my_func():"
            ],
            "answer": "b) def my_func():",
            "explanation": "Functions are defined with the def keyword."
            },

            # Question 491-500
            {
            "question": "491. What is the output of:\n```python\ndef square(x):\n    return x * x\nprint(square(4))\n```",
            "options": ["a) 4", "b) 8", "c) 16", "d) Error"],
            "answer": "c) 16",
            "explanation": "4 squared is 16."
            },
            {
            "question": "492. What keyword is used to return a value from a function?",
            "options": ["a) break", "b) return", "c) yield", "d) exit"],
            "answer": "b) return",
            "explanation": "return sends a value back from a function."
            },
            {
            "question": "493. What does print('Hi', end=' ') do?",
            "options": [
                "a) Prints 'Hi' with a space at the end",
                "b) Prints 'Hi' and exits",
                "c) Prints 'Hi' with a newline",
                "d) Error"
            ],
            "answer": "a) Prints 'Hi' with a space at the end",
            "explanation": "end=' ' replaces the default newline with a space."
            },
            {
            "question": "494. What is the output of print(1, 2, 3, sep='-')?",
            "options": ["a) 1-2-3", "b) 1 2 3", "c) 1,2,3", "d) 123"],
            "answer": "a) 1-2-3",
            "explanation": "sep='-' specifies the separator between items."
            },
            {
            "question": "495. Which parameter is used to separate items in print()?",
            "options": ["a) end", "b) sep", "c) delim", "d) split"],
            "answer": "b) sep",
            "explanation": "sep controls the separator between arguments."
            },
            {
            "question": "496. Which os method lists files in a directory?",
            "options": ["a) os.listdir()", "b) os.files()", "c) os.scandir()", "d) os.getcwd()"],
            "answer": "a) os.listdir()",
            "explanation": "listdir() returns directory contents."
            },
            {
            "question": "497. What does os.path.join('dir', 'file.txt') do?",
            "options": [
                "a) Combines paths with OS-specific separators",
                "b) Deletes a file",
                "c) Checks if a file exists",
                "d) Renames a file"
            ],
            "answer": "a) Combines paths with OS-specific separators",
            "explanation": "join() creates proper path strings."
            },
            {
            "question": "498. How do you get the current working directory?",
            "options": [
                "a) os.cwd()",
                "b) os.getcwd()",
                "c) os.current_dir()",
                "d) os.path.cwd()"
            ],
            "answer": "b) os.getcwd()",
            "explanation": "getcwd() returns the current working directory."
            },
            {
            "question": "499. What is Streamlit primarily used for?",
            "options": [
                "a) Web scraping",
                "b) Data visualization and creating web apps",
                "c) Game development",
                "d) Machine learning training"
            ],
            "answer": "b) Data visualization and creating web apps",
            "explanation": "Streamlit specializes in data apps."
            },
            {
            "question": "500. How do you run a Streamlit app?",
            "options": [
                "a) python app.py",
                "b) streamlit run app.py",
                "c) flask run",
                "d) run streamlit app.py"
            ],
            "answer": "b) streamlit run app.py",
            "explanation": "This is the standard Streamlit command."
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
        st.title("Python Quiz Challenge")
        st.write("""
        This quiz contains 50 questions about Python programming and cloud computing (Questions 451-500).
        You'll have 1 minute to answer each question.
        """)
        
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.rerun()

    def show_question(self):
        st.title("Python Quiz")
        
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
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(self.questions)} (Q{451 + st.session_state.current_question + 1})")
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
            with st.expander(f"Question {451 + i + 1}: {answer['question']}"):
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