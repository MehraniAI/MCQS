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
            # Questions 401-410 
            {
            "question": "401. Which of the following is mutable in Python?",
            "options": ["a) Tuple", "b) String", "c) List", "d) Set"],
            "answer": "c) List and d) Set",
            "explanation": "Lists and sets are mutable (can be changed after creation), while tuples and strings are immutable."
            },
            {
            "question": "402. What is the output of the following code?\n```python\nt = (1, 2, [3, 4])\nt[2][0] = 5\nprint(t)\n```",
            "options": ["a) (1, 2, [3, 4])", "b) (1, 2, [5, 4])", "c) Error (Tuples are immutable)", "d) (1, 2, 5, 4)"],
            "answer": "b) (1, 2, [5, 4])",
            "explanation": "A tuple is immutable, but its inner list is mutable."
            },
            {
            "question": "403. Which method removes an item from a dictionary and returns its value?",
            "options": ["a) pop()", "b) remove()", "c) delete()", "d) clear()"],
            "answer": "a) pop()",
            "explanation": "pop() removes and returns the value for a given key."
            },
            {
            "question": "404. What is the output of print('Hello' * 2)?",
            "options": ["a) HelloHello", "b) 'Hello' * 2", "c) TypeError", "d) Hello 2"],
            "answer": "a) HelloHello",
            "explanation": "Strings can be multiplied to repeat them."
            },
            {
            "question": "405. What is the difference between parameters and arguments?",
            "options": [
                "a) Parameters are passed to a function, while arguments are defined in the function.",
                "b) Parameters are defined in the function, while arguments are passed to the function.",
                "c) They are the same.",
                "d) Arguments are used in def, while parameters are used in print."
            ],
            "answer": "b) Parameters are placeholders in function definitions, while arguments are actual values passed.",
            "explanation": "Parameters are the variables in the function definition, arguments are the values you pass when calling the function."
            },
            {
            "question": "406. Which keyword is used to define a function in Python?",
            "options": ["a) function", "b) def", "c) lambda", "d) func"],
            "answer": "b) def",
            "explanation": "Functions are defined using the 'def' keyword."
            },
            {
            "question": "407. What does os.path.join() do?",
            "options": [
                "a) Joins two strings with a slash.",
                "b) Joins path components in an OS-independent way.",
                "c) Joins lists into a string.",
                "d) Joins dictionaries."
            ],
            "answer": "b) It joins path components correctly for the operating system.",
            "explanation": "os.path.join() safely joins paths using the correct separator for the OS."
            },
            {
            "question": "408. What is the output of print(3 > 2 > 1)?",
            "options": ["a) True", "b) False", "c) Error", "d) None"],
            "answer": "a) True",
            "explanation": "This is equivalent to (3 > 2) and (2 > 1), which is True."
            },
            {
            "question": "409. Which data structure does not allow duplicates?",
            "options": ["a) List", "b) Tuple", "c) Set", "d) Dictionary (keys)"],
            "answer": "c) Set and d) Dictionary keys",
            "explanation": "Both sets and dictionary keys enforce uniqueness."
            },
            {
            "question": "410. What is Streamlit primarily used for?",
            "options": [
                "a) Web scraping",
                "b) Data visualization and creating web apps",
                "c) Game development",
                "d) Machine learning model training"
            ],
            "answer": "b) Streamlit is used to create interactive web apps for data science.",
            "explanation": "Streamlit is a popular framework for building data apps quickly."
            },

            # Question 411-420
            {
            "question": "411. What does print('Python'.replace('P', 'J')) output?",
            "options": ["a) Python", "b) Jython", "c) Error", "d) P"],
            "answer": "b) Jython",
            "explanation": "replace() substitutes 'P' with 'J'."
            },
            {
            "question": "412. Which of the following is a valid dictionary?",
            "options": [
                "a) {1: 'A', 'B': 2}",
                "b) {[1]: 'A'} (Invalid: Lists cannot be keys.)",
                "c) {{1}: 'A'} (Invalid: Sets cannot be keys.)",
                "d) {(1,): 'A'} (Valid: Tuples can be keys.)"
            ],
            "answer": "a) and d)",
            "explanation": "Dictionary keys must be immutable - tuples are allowed but lists and sets are not."
            },
            {
            "question": "413. What does if not False: evaluate to?",
            "options": ["a) True", "b) False", "c) Error", "d) None"],
            "answer": "a) True",
            "explanation": "not False equals True."
            },
            {
            "question": "414. What is the purpose of sys.argv?",
            "options": [
                "a) To store function arguments",
                "b) To pass command-line arguments to a script",
                "c) To define parameters",
                "d) To handle exceptions"
            ],
            "answer": "b) It stores command-line arguments passed to a Python script.",
            "explanation": "sys.argv is a list of command-line arguments."
            },
            {
            "question": "415. Which method checks if a key exists in a dictionary?",
            "options": [
                "a) has_key() (Python 2 only)",
                "b) in operator",
                "c) contains()",
                "d) exists()"
            ],
            "answer": "b) in (e.g., if 'key' in my_dict:)",
            "explanation": "The 'in' operator checks for key existence."
            },
            {
            "question": "416. Which of the following creates an empty list in Python?",
            "options": ["a) list = []", "b) list = list()", "c) Both a and b", "d) list = {}"],
            "answer": "c) Both a and b",
            "explanation": "Both [] and list() create empty lists."
            },
            {
            "question": "417. What is the output of [1, 2, 3] + [4, 5]?",
            "options": ["a) [1, 2, 3, 4, 5]", "b) [5, 7, 3]", "c) [1, 2, 7]", "d) Error"],
            "answer": "a) [1, 2, 3, 4, 5]",
            "explanation": "The + operator concatenates lists."
            },
            {
            "question": "418. Which method removes the last element from a list?",
            "options": ["a) list.remove()", "b) list.pop()", "c) list.delete()", "d) list.clear()"],
            "answer": "b) list.pop()",
            "explanation": "pop() removes and returns the last item by default."
            },
            {
            "question": "419. What does list[::-1] do?",
            "options": ["a) Reverses the list", "b) Sorts the list", "c) Removes duplicates", "d) Creates a copy"],
            "answer": "a) Reverses the list",
            "explanation": "Slicing with [::-1] creates a reversed copy."
            },
            {
            "question": "420. Which is not a valid list operation?",
            "options": [
                "a) list.append(5)",
                "b) list.insert(0, 5)",
                "c) list.add(5)",
                "d) list.extend([5])"
            ],
            "answer": "c) list.add(5)",
            "explanation": "add() is not a list method - it's used with sets."
            },

            # Question 421-430
            {
            "question": "421. How is a tuple defined?",
            "options": ["a) t = (1, 2, 3)", "b) t = tuple([1, 2, 3])", "c) Both a and b", "d) t = {1, 2, 3}"],
            "answer": "c) Both a and b",
            "explanation": "Tuples can be created using parentheses or the tuple() constructor."
            },
            {
            "question": "422. Tuples are:",
            "options": ["a) Mutable", "b) Immutable", "c) Both", "d) None"],
            "answer": "b) Immutable",
            "explanation": "Tuples cannot be changed after creation (immutable)."
            },
            {
            "question": "423. What is the output of (1, 2) + (3,)?",
            "options": ["a) (1, 2, 3)", "b) (4, 2)", "c) Error", "d) (1, 5)"],
            "answer": "a) (1, 2, 3)",
            "explanation": "Tuples can be concatenated with the + operator."
            },
            {
            "question": "424. Which is not a tuple?",
            "options": ["a) (1)", "b) (1,)", "c) tuple()", "d) (1, 2)"],
            "answer": "a) (1)",
            "explanation": "A single value in parentheses is not a tuple (needs a comma)."
            },
            {
            "question": "425. What does len((1, 2, 3)) return?",
            "options": ["a) 3", "b) 6", "c) 1", "d) Error"],
            "answer": "a) 3",
            "explanation": "len() returns the number of elements in the tuple."
            },
            {
            "question": "426. Which creates an empty set?",
            "options": ["a) s = {}", "b) s = set()", "c) Both", "d) None"],
            "answer": "b) s = set()",
            "explanation": "{} creates an empty dictionary, not a set."
            },
            {
            "question": "427. What is the output of {1, 2, 2, 3}?",
            "options": ["a) {1, 2, 3}", "b) {1, 2, 2, 3}", "c) {2}", "d) Error"],
            "answer": "a) {1, 2, 3}",
            "explanation": "Sets automatically remove duplicate values."
            },
            {
            "question": "428. Which operation finds common elements in two sets?",
            "options": ["a) set1 + set2", "b) set1.union(set2)", "c) set1.intersection(set2)", "d) set1.difference(set2)"],
            "answer": "c) set1.intersection(set2)",
            "explanation": "intersection() returns elements common to both sets."
            },
            {
            "question": "429. What does set1.discard(5) do?",
            "options": ["a) Removes 5 if present", "b) Raises an error if 5 is missing", "c) Adds 5", "d) None"],
            "answer": "a) Removes 5 if present",
            "explanation": "discard() removes an element without raising an error if missing."
            },
            {
            "question": "430. Which is not a set operation?",
            "options": ["a) | (Union)", "b) & (Intersection)", "c) - (Difference)", "d) + (Concatenation)"],
            "answer": "d) + (Concatenation)",
            "explanation": "Sets use |, &, - for operations, not +."
            },
            # Question 431-440
            {
            "question": "431. How is a dictionary defined?",
            "options": ["a) d = {'key': 'value'}", "b) d = dict(key='value')", "c) Both", "d) None"],
            "answer": "c) Both",
            "explanation": "Dictionaries can be created with curly braces or dict()."
            },
            {
            "question": "432. What is the output of d.get('missing_key', 'default')?",
            "options": ["a) None", "b) 'default'", "c) Error", "d) 'missing_key'"],
            "answer": "b) 'default'",
            "explanation": "get() returns the default value if key doesn't exist."
            },
            {
            "question": "433. Which method returns all keys in a dictionary?",
            "options": ["a) d.keys()", "b) d.items()", "c) d.values()", "d) All"],
            "answer": "a) d.keys()",
            "explanation": "keys() returns a view of all dictionary keys."
            },
            {
            "question": "434. What does d.pop('key') do?",
            "options": ["a) Removes and returns the value for 'key'", "b) Deletes the dictionary", "c) Adds a new key", "d) None"],
            "answer": "a) Removes and returns the value for 'key'",
            "explanation": "pop() removes the key and returns its value."
            },
            {
            "question": "435. Which is not a valid dictionary key?",
            "options": ["a) 1", "b) 'name'", "c) [1, 2]", "d) (1, 2)"],
            "answer": "c) [1, 2]",
            "explanation": "Dictionary keys must be immutable (lists are mutable)."
            },
            {
            "question": "436. What is the output of 'hello'.upper()?",
            "options": ["a) 'HELLO'", "b) 'hello'", "c) 'Hello'", "d) Error"],
            "answer": "a) 'HELLO'",
            "explanation": "upper() converts all characters to uppercase."
            },
            {
            "question": "437. Which method splits a string into a list?",
            "options": ["a) str.split()", "b) str.join()", "c) str.strip()", "d) str.replace()"],
            "answer": "a) str.split()",
            "explanation": "split() divides a string into a list based on a delimiter."
            },
            {
            "question": "438. What does 'abc'[::-1] return?",
            "options": ["a) 'cba'", "b) 'abc'", "c) ''", "d) Error"],
            "answer": "a) 'cba'",
            "explanation": "[::-1] reverses the string."
            },
            {
            "question": "439. Which checks if a string contains only digits?",
            "options": ["a) str.isdigit()", "b) str.isalpha()", "c) str.isalnum()", "d) str.lower()"],
            "answer": "a) str.isdigit()",
            "explanation": "isdigit() returns True if all characters are digits."
            },
            {
            "question": "440. What is the output of 'a' + 'b'?",
            "options": ["a) 'ab'", "b) 'a b'", "c) 'a+b'", "d) Error"],
            "answer": "a) 'ab'",
            "explanation": "+ concatenates strings."
            },
            # Question 441-450
            {
            "question": "441. What is a parameter?",
            "options": [
                "a) A value passed to a function",
                "b) A variable in a function definition",
                "c) A return value",
                "d) None"
            ],
            "answer": "b) A variable in a function definition",
            "explanation": "Parameters are the placeholders in function definitions."
            },
            {
            "question": "442. What is an argument?",
            "options": [
                "a) A value passed to a function",
                "b) A variable in a function definition",
                "c) A keyword",
                "d) None"
            ],
            "answer": "a) A value passed to a function",
            "explanation": "Arguments are the actual values passed when calling a function."
            },
            {
            "question": "443. Which is a default argument?",
            "options": ["a) def f(x=1):", "b) def f(x):", "c) def f(*args):", "d) def f(**kwargs):"],
            "answer": "a) def f(x=1):",
            "explanation": "x=1 is a default argument with a default value of 1."
            },
            {
            "question": "444. What does *args represent?",
            "options": [
                "a) Keyword arguments",
                "b) Variable-length positional arguments",
                "c) Mandatory arguments",
                "d) None"
            ],
            "answer": "b) Variable-length positional arguments",
            "explanation": "*args collects extra positional arguments as a tuple."
            },
            {
            "question": "445. What does **kwargs represent?",
            "options": [
                "a) Keyword arguments",
                "b) Positional arguments",
                "c) Required arguments",
                "d) None"
            ],
            "answer": "a) Keyword arguments",
            "explanation": "**kwargs collects extra keyword arguments as a dictionary."
            },
            {
            "question": "446. What is the output of if 0: print('Yes') else: print('No')?",
            "options": ["a) Yes", "b) No", "c) Error", "d) None"],
            "answer": "b) No",
            "explanation": "0 is falsy in Python, so the else clause executes."
            },
            {
            "question": "447. Which is equivalent to if x > 5 and x < 10?",
            "options": ["a) if 5 < x < 10", "b) if x in range(6, 10)", "c) Both", "d) None"],
            "answer": "a) if 5 < x < 10",
            "explanation": "Python allows chained comparisons."
            },
            {
            "question": "448. What does elif stand for?",
            "options": ["a) Else if", "b) End if", "c) Exit if", "d) None"],
            "answer": "a) Else if",
            "explanation": "elif is short for 'else if'."
            },
            {
            "question": "449. What is the output of print('Hi') if True else print('Bye')?",
            "options": ["a) Hi", "b) Bye", "c) Both", "d) Error"],
            "answer": "a) Hi",
            "explanation": "This ternary expression prints 'Hi' since the condition is True."
            },
            {
            "question": "450. Which is not a valid condition?",
            "options": ["a) if x == 5:", "b) if x = 5:", "c) if x in [1, 2, 3]:", "d) if x > 5:"],
            "answer": "b) if x = 5:",
            "explanation": "= is assignment, not comparison (use == instead)."
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
        This quiz contains 50 questions about Python programming and cloud computing (Questions 401-450).
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
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(self.questions)} (Q{300 + st.session_state.current_question + 1})")
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
            with st.expander(f"Question {300 + i + 1}: {answer['question']}"):
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
