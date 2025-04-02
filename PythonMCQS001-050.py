import streamlit as st
import random

st.markdown('<h1 style="color:blue">Prepared by Devan Das Mehrani AI Student</h1>', unsafe_allow_html=True)

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
        if 'current_section' not in st.session_state:
            st.session_state.current_section = 0
        
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
            # Questions 1-10
            {
                "question": "1. Which of the following is true about Python?",
                "options": [
                    "a) Python is a compiled language.",
                    "b) Python is a high-level language.",
                    "c) Python is primarily used for numeric computations.",
                    "d) Python is suitable only for web development."
                ],
                "answer": "b",
                "explanation": "Python is a high-level, interpreted language that's used for many purposes beyond just web development."
            },
            {
                "question": "2. What is the output of the following code snippet?\nx = 5\ny = 2\nprint(x // y)",
                "options": ["a) 2.5", "b) 2", "c) 2.0", "d) 3"],
                "answer": "b",
                "explanation": "The // operator performs floor division, returning the largest integer less than or equal to the result."
            },
            {
                "question": "3. Which of the following statements about Python's lists is correct?",
                "options": [
                    "a) Lists in Python are always homogeneous.",
                    "b) Lists are immutable.",
                    "c) Lists can contain elements of different data types.",
                    "d) Lists cannot be nested."
                ],
                "answer": "c",
                "explanation": "Python lists can contain elements of different types and can be nested."
            },
            {
                "question": "4. What is the purpose of the __init__ method in Python classes?",
                "options": [
                    "a) To initialize the class variables.",
                    "b) To create a new instance of the class.",
                    "c) To define private methods.",
                    "d) To finalize the class definition."
                ],
                "answer": "a",
                "explanation": "__init__ is the constructor method that initializes an object's state."
            },
            {
                "question": "5. Which of the following is an advantage of using Python?",
                "options": [
                    "a) Python is a low-performance language.",
                    "b) Python code is not readable.",
                    "c) Python has a large standard library.",
                    "d) Python is not suitable for scientific computing."
                ],
                "answer": "c",
                "explanation": "Python's extensive standard library is one of its main advantages."
            },
            {
                "question": "6. What will be the output of the following code?\ndef foo(a, b=2, c=3):\n    print(a, b, c)\nfoo(1, c=4)",
                "options": ["a) 1 2 3", "b) 1 2 4", "c) 1 4 3", "d) 1 3 4"],
                "answer": "b",
                "explanation": "The function uses default b=2 and overrides c with 4."
            },
            {
                "question": "7. What does the pass statement do in Python?",
                "options": [
                    "a) It terminates the execution of a loop.",
                    "b) It is used to skip the current iteration of a loop.",
                    "c) It is used to raise an exception.",
                    "d) It is used as a placeholder indicating 'do nothing'."
                ],
                "answer": "d",
                "explanation": "pass is a null operation used when syntax requires a statement but no action is needed."
            },
            {
                "question": "8. Which of the following is a correct way to open and read from a file named data.txt in Python?",
                "options": [
                    "a) file = open('data.txt', 'r')",
                    "b) file = open('data.txt', 'w')",
                    "c) file = open('data.txt', 'a')",
                    "d) file = open('data.txt', 'x')"
                ],
                "answer": "a",
                "explanation": "The 'r' mode opens a file for reading."
            },
            {
                "question": "9. What is the output of the following code?\nnumbers = [1, 2, 3, 4, 5]\nprint(numbers[10:])",
                "options": ["a) []", "b) [5]", "c) [1, 2, 3, 4, 5]", "d) Error: Index out of range"],
                "answer": "a",
                "explanation": "Slicing beyond list bounds returns an empty list rather than raising an error."
            },
            {
                "question": "10. What does the import this statement do in Python?",
                "options": [
                    "a) Imports all modules in the current directory.",
                    "b) Imports the Python Enhancement Proposals (PEPs).",
                    "c) Prints the Zen of Python.",
                    "d) Prints the Python version information."
                ],
                "answer": "c",
                "explanation": "import this prints Tim Peters' 'Zen of Python'."
            },
            
            # Questions 11-20
            {
                "question": "11. What will be the output of the following code?\nx = 10\nif x > 5:\n    print('Hello')\nelse:\n    print('Hi')",
                "options": ["a) Hello", "b) Hi", "c) Hello Hi", "d) No output"],
                "answer": "a",
                "explanation": "Since 10 > 5, the if condition is true and 'Hello' is printed."
            },
            {
                "question": "12. Which of the following data types is mutable in Python?",
                "options": ["a) int", "b) float", "c) tuple", "d) list"],
                "answer": "d",
                "explanation": "Lists are mutable (can be changed after creation), unlike tuples."
            },
            {
                "question": "13. What does the break statement do in Python?",
                "options": [
                    "a) Ends the current iteration of a loop and continues with the next iteration.",
                    "b) Ends the current loop and resumes execution at the next statement after the loop.",
                    "c) Terminates the program.",
                    "d) Skips the current iteration of a loop."
                ],
                "answer": "b",
                "explanation": "break exits the nearest enclosing loop."
            },
            {
                "question": "14. How can you convert a string '123' to an integer in Python?",
                "options": ["a) int('123')", "b) integer('123')", "c) convert('123')", "d) str_to_int('123')"],
                "answer": "a",
                "explanation": "The int() function converts strings to integers."
            },
            {
                "question": "15. Which of the following is a correct way to define a function in Python that takes two parameters a and b?",
                "options": [
                    "a) def function(a, b):",
                    "b) function(a, b):",
                    "c) def function(a b):",
                    "d) define function(a, b):"
                ],
                "answer": "a",
                "explanation": "Functions are defined using the def keyword followed by parameters in parentheses."
            },
            {
                "question": "16. What will be the output of the following code?\ndef func(x, y=[]):\n    y.append(x)\n    return y\nprint(func(1))\nprint(func(2))",
                "options": ["a) [1], [2]", "b) [1, 2], [2]", "c) [1], [1, 2]", "d) [1, 2], [1, 2]"],
                "answer": "d",
                "explanation": "Default arguments are evaluated only once when the function is defined, not each call."
            },
            {
                "question": "17. What is the output of 2 ** 3 ** 2 in Python?",
                "options": ["a) 64", "b) 512", "c) 576", "d) 12"],
                "answer": "b",
                "explanation": "Exponentiation is right-associative, so 2**(3**2) = 2^9 = 512."
            },
            {
                "question": "18. Which of the following statements about Python dictionaries is correct?",
                "options": [
                    "a) Dictionaries are ordered collections.",
                    "b) Dictionary keys must be immutable.",
                    "c) Dictionaries can only store integer keys.",
                    "d) Dictionaries cannot be nested."
                ],
                "answer": "b",
                "explanation": "Dictionary keys must be immutable types (strings, numbers, tuples)."
            },
            {
                "question": "19. What is the output of the following code?\nnums = [1, 2, 3, 4]\nsquares = map(lambda x: x**2, nums)\nprint(list(squares))",
                "options": ["a) [1, 4, 9, 16]", "b) [1, 2, 3, 4]", "c) [2, 4, 6, 8]", "d) [1, 3, 5, 7]"],
                "answer": "a",
                "explanation": "map applies the lambda function to each element, squaring them."
            },
            {
                "question": "20. What will be the output of the following code?\nx = 10\ny = 5\nz = x if x > y else y\nprint(z)",
                "options": ["a) 10", "b) 5", "c) True", "d) False"],
                "answer": "a",
                "explanation": "This is a ternary operator that returns x when x > y, which is true here."
            },
            
            # Questions 21-30
            {
                "question": "21. What is the purpose of self in Python class methods?",
                "options": [
                    "a) It refers to the class itself.",
                    "b) It is a keyword used to denote a private method.",
                    "c) It represents the instance of the class.",
                    "d) It is used to inherit from another class."
                ],
                "answer": "c",
                "explanation": "self refers to the instance of the class (by convention, not a keyword)."
            },
            {
                "question": "22. What does the not in operator do in Python?",
                "options": [
                    "a) Checks if a value is not present in a list.",
                    "b) Performs bitwise NOT operation.",
                    "c) Checks if a value is not equal to another value.",
                    "d) Checks if a substring is not in a string."
                ],
                "answer": "a",
                "explanation": "not in checks for absence of an element in a container."
            },
            {
                "question": "23. What will be the output of the following code?\nnums = [1, 2, 3, 4, 5]\nprint(nums[-2])",
                "options": ["a) 1", "b) 2", "c) 4", "d) 5"],
                "answer": "c",
                "explanation": "Negative indices count from the end (-1 is last, -2 is second last, etc.)."
            },
            {
                "question": "24. How can you check the number of items in a list my_list in Python?",
                "options": ["a) my_list.count()", "b) my_list.size()", "c) len(my_list)", "d) my_list.length()"],
                "answer": "c",
                "explanation": "The len() function returns the number of items in a container."
            },
            {
                "question": "25. What is the purpose of the finally block in a Python try-except-finally statement?",
                "options": [
                    "a) It always runs before the try block.",
                    "b) It runs only if an exception occurs.",
                    "c) It runs regardless of whether an exception occurs or not.",
                    "d) It is used to handle specific exceptions."
                ],
                "answer": "c",
                "explanation": "finally blocks always execute, making them good for cleanup code."
            },
            {
                "question": "26. Which of the following statements about Python's pass statement is correct?",
                "options": [
                    "a) It must be used in every loop.",
                    "b) It terminates the program.",
                    "c) It is used to indicate the end of a function.",
                    "d) It is a null operation."
                ],
                "answer": "d",
                "explanation": "pass is a null operation that does nothing when executed."
            },
            {
                "question": "27. What will be the output of the following code?\ndef my_func(x):\n    return 2 * x\nresult = my_func(5)\nprint(result)",
                "options": ["a) 10", "b) 5", "c) 2", "d) 25"],
                "answer": "a",
                "explanation": "The function doubles its input, so 5 * 2 = 10."
            },
            {
                "question": "28. Which of the following is a correct way to remove an element from a list my_list in Python?",
                "options": [
                    "a) my_list.delete(element)",
                    "b) my_list.remove(element)",
                    "c) my_list.pop(element)",
                    "d) my_list.erase(element)"
                ],
                "answer": "b",
                "explanation": "remove() deletes the first occurrence of the specified value."
            },
            {
                "question": "29. What does the __str__ method do in Python?",
                "options": [
                    "a) Converts an object to a string.",
                    "b) Returns the length of a string.",
                    "c) Concatenates two strings.",
                    "d) Checks if two strings are equal."
                ],
                "answer": "a",
                "explanation": "__str__ provides the informal string representation of an object."
            },
            {
                "question": "30. What will be the output of the following code?\na = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
                "options": ["a) [1, 2, 3]", "b) [1, 2, 3, 4]", "c) [1, 2, 4]", "d) Error"],
                "answer": "b",
                "explanation": "Both variables reference the same list object, so modifying one affects the other."
            },
            
            # Questions 31-40
            {
                "question": "31. What is the output of the following code?\ndef foo():\n    try:\n        return 1\n    finally:\n        return 2\nprint(foo())",
                "options": ["a) 1", "b) 2", "c) 1 2", "d) 2 1"],
                "answer": "b",
                "explanation": "finally blocks execute even during a return, and can override the return value."
            },
            {
                "question": "32. Which of the following is true about Python's lambda functions?",
                "options": [
                    "a) They can contain multiple expressions.",
                    "b) They can have a variable number of arguments.",
                    "c) They can contain statements like return.",
                    "d) They are used for defining classes."
                ],
                "answer": "b",
                "explanation": "Lambda functions can take any number of arguments but only one expression."
            },
            {
                "question": "33. What does the extend method do on a list in Python?",
                "options": [
                    "a) Adds an element to the end of the list.",
                    "b) Adds two lists together.",
                    "c) Replaces an element at a specific index.",
                    "d) Adds elements from another list to the end of the list."
                ],
                "answer": "d",
                "explanation": "extend() adds all elements of an iterable to the list."
            },
            {
                "question": "34. What will be the output of the following code?\nx = [1, 2, 3]\ny = x.copy()\ny.append(4)\nprint(x)",
                "options": ["a) [1, 2, 3]", "b) [1, 2, 3, 4]", "c) [1, 4, 2, 3]", "d) Error"],
                "answer": "a",
                "explanation": "copy() creates a new list, so changes to y don't affect x."
            },
            {
                "question": "35. Which of the following is a correct way to create a set in Python?",
                "options": [
                    "a) my_set = {1, 2, 3}",
                    "b) my_set = [1, 2, 3]",
                    "c) my_set = (1, 2, 3)",
                    "d) my_set = {1, 2, 3, 3}"
                ],
                "answer": "a",
                "explanation": "Sets are created with curly braces {} (without colons for key-value pairs)."
            },
            {
                "question": "36. How do you create a dictionary in Python?",
                "options": [
                    "a) my_dict = [key: value, key2: value2]",
                    "b) my_dict = (key: value, key2: value2)",
                    "c) my_dict = {key: value, key2: value2}",
                    "d) my_dict = {key = value, key2 = value2}"
                ],
                "answer": "c",
                "explanation": "Dictionaries use curly braces with key:value pairs."
            },
            {
                "question": "37. What will be the output of the following code?\nmy_dict = {'a': 1, 'b': 2, 'c': 3}\nprint(my_dict.get('d', 4))",
                "options": ["a) 1", "b) 3", "c) 4", "d) None"],
                "answer": "c",
                "explanation": "get() returns the default value (4) when the key isn't found."
            },
            {
                "question": "38. Which of the following statements about Python's with statement is true?",
                "options": [
                    "a) It is used to create a class.",
                    "b) It is used for exception handling.",
                    "c) It is used to simplify try-except-finally blocks.",
                    "d) It is used to define functions."
                ],
                "answer": "c",
                "explanation": "with simplifies resource management (files, locks) by automatically handling setup/teardown."
            },
            {
                "question": "39. What is the output of the following code?\nfor i in range(3):\n    print(i)\nelse:\n    print('Done')",
                "options": ["a) 0 1 2", "b) 0 1 2 Done", "c) Done 0 1 2", "d) 0 1 Done 2"],
                "answer": "b",
                "explanation": "The else clause executes after the loop completes normally (without break)."
            },
            {
                "question": "40. How do you add an element to the end of a list in Python?",
                "options": ["a) my_list.add(element)", "b) my_list.append(element)", "c) my_list.insert(element)", "d) my_list.push(element)"],
                "answer": "b",
                "explanation": "append() adds a single element to the end of the list."
            },
            
            # Questions 41-50
            {
                "question": "41. What is the output of the following code?\ndef add(x, y):\n    return x + y\nprint(add('Hello', 'World'))",
                "options": ["a) HelloWorld", "b) Hello World", "c) Error", "d) None"],
                "answer": "a",
                "explanation": "The + operator concatenates strings."
            },
            {
                "question": "42. Which of the following is used to define a block of code in Python?",
                "options": ["a) Curly braces {}", "b) Parentheses ()", "c) Indentation", "d) Square brackets []"],
                "answer": "c",
                "explanation": "Python uses indentation to define code blocks."
            },
            {
                "question": "43. How do you declare a variable x with the value 10 in Python?",
                "options": ["a) int x = 10", "b) x := 10", "c) let x = 10", "d) x = 10"],
                "answer": "d",
                "explanation": "Python variables are declared by simple assignment."
            },
            {
                "question": "44. What will be the output of the following code?\na = [1, 2, 3]\nb = a[:]\nb.append(4)\nprint(a)",
                "options": ["a) [1, 2, 3]", "b) [1, 2, 3, 4]", "c) [4, 1, 2, 3]", "d) Error"],
                "answer": "a",
                "explanation": "Slicing [:] creates a shallow copy, so changes to b don't affect a."
            },
            {
                "question": "45. Which of the following is not a valid keyword in Python?",
                "options": ["a) finally", "b) raise", "c) assert", "d) repeat"],
                "answer": "d",
                "explanation": "repeat is not a Python keyword."
            },
            {
                "question": "46. What is the output of the following code?\nx = 'Python'\nprint(x[1:4])",
                "options": ["a) Pyt", "b) yth", "c) ytho", "d) ytho"],
                "answer": "b",
                "explanation": "Slicing from index 1 to 4 (exclusive) gives 'yth'."
            },
            {
                "question": "47. How do you convert a list to a tuple in Python?",
                "options": ["a) tuple(list)", "b) convert(list)", "c) list_to_tuple(list)", "d) tuple_convert(list)"],
                "answer": "a",
                "explanation": "The tuple() constructor converts iterables to tuples."
            },
            {
                "question": "48. Which of the following is true about Python's garbage collection?",
                "options": [
                    "a) It uses a mark-and-sweep algorithm.",
                    "b) It uses reference counting.",
                    "c) It requires manual memory management.",
                    "d) It does not exist in Python."
                ],
                "answer": "b",
                "explanation": "Python primarily uses reference counting with cycle detection."
            },
            {
                "question": "49. What will be the output of the following code?\na = (1, 2)\nb = (3, 4)\nprint(a + b)",
                "options": ["a) (1, 2)", "b) (3, 4)", "c) (1, 2, 3, 4)", "d) Error"],
                "answer": "c",
                "explanation": "The + operator concatenates tuples."
            },
            {
                "question": "50. How do you check if a key exists in a dictionary in Python?",
                "options": ["a) key in my_dict", "b) my_dict.has_key(key)", "c) key.exists(my_dict)", "d) my_dict.key_exists(key)"],
                "answer": "a",
                "explanation": "The in operator checks for key existence in dictionaries."
            }
        ]
        return questions

    def create_welcome_screen(self):
        st.title("Python Quiz Challenge")
        st.markdown("""
            This quiz contains 50 questions about Python programming organized in sections.
            
            **Sections:**
            - Questions 1-10: Python Basics
            - Questions 11-20: Data Structures
            - Questions 21-30: Functions and Classes
            - Questions 31-40: Advanced Concepts
            - Questions 41-50: Miscellaneous
            
            You'll get detailed feedback after completing each section.
            
            Click Start to begin!
        """)
        
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.session_state.current_section = 0
            st.rerun()
    
    def show_question(self):
        # Determine current section (0=1-10, 1=11-20, etc.)
        section_start = st.session_state.current_section * 10
        section_end = section_start + 9
        
        # Get current question data
        question_idx = st.session_state.shuffled_indices[st.session_state.current_question]
        question_data = st.session_state.questions[question_idx]
        
        st.title(f"Section {st.session_state.current_section + 1}: Questions {section_start + 1}-{section_end + 1}")
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(st.session_state.questions)}")
        st.markdown(f"**{question_data['question']}**")
        
        # Display options as radio buttons
        selected = st.radio(
            "Select your answer:",
            question_data["options"],
            index=None,
            key=f"question_{st.session_state.current_question}"
        )
        
        st.session_state.selected_option = selected
        
        col1, col2, col3 = st.columns([1,1,1])
        
        # Navigation buttons
        if st.session_state.current_question > section_start:
            if col1.button("Previous"):
                self.prev_question()
        
        if st.session_state.current_question < section_end:
            if col2.button("Next"):
                self.next_question()
        else:
            if col2.button("Submit Section"):
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
            if st.session_state.selected_option == opt:
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
        section_end = (st.session_state.current_section * 10) + 9
        if st.session_state.current_question < section_end:
            st.session_state.current_question += 1
            st.session_state.selected_option = None
            st.rerun()
        else:
            self.show_section_results()
    
    def show_section_results(self):
        st.title(f"Section {st.session_state.current_section + 1} Results")
        
        # Calculate section score
        section_start = st.session_state.current_section * 10
        section_end = section_start + 9
        section_answers = st.session_state.user_answers[section_start:section_end + 1]
        section_score = sum(1 for ans in section_answers if ans["is_correct"])
        
        st.subheader(f"Your score: {section_score}/10 ({section_score * 10}%)")
        
        # Detailed feedback
        st.subheader("Detailed Feedback:")
        
        for i, answer in enumerate(section_answers, start=section_start + 1):
            with st.expander(f"Question {i}: {answer['question']}"):
                if answer['is_correct']:
                    st.success("✅ Your answer: CORRECT")
                else:
                    st.error("❌ Your answer: INCORRECT")
                    st.write(f"You selected: {answer['user_answer'].upper()}")
                    st.write(f"Correct answer: {answer['correct_answer'].upper()}")
                
                st.write(f"**Explanation:** {answer['explanation']}")
        
        # Move to next section or final results
        if st.session_state.current_section < 4:  # 5 sections (0-4)
            if st.button("Continue to Next Section"):
                st.session_state.current_section += 1
                st.session_state.current_question = st.session_state.current_section * 10
                st.session_state.selected_option = None
                st.rerun()
        else:
            self.show_final_results()
    
    def show_final_results(self):
        st.title("Quiz Completed!")
        
        # Calculate final score
        final_score = st.session_state.score
        total_questions = len(st.session_state.questions)
        score_percent = (final_score / total_questions) * 100
        
        st.subheader(f"Final Score: {final_score}/{total_questions} ({score_percent:.1f}%)")
        
        # Section breakdown
        st.subheader("Section Performance:")
        cols = st.columns(5)
        for i in range(5):
            section_start = i * 10
            section_end = section_start + 9
            section_answers = st.session_state.user_answers[section_start:section_end + 1]
            section_score = sum(1 for ans in section_answers if ans["is_correct"])
            
            cols[i].metric(
                label=f"Section {i+1}",
                value=f"{section_score}/10",
                delta=f"{section_score * 10}%"
            )
        
        # Restart or quit buttons
        col1, col2 = st.columns([1,1])
        
        if col1.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.user_answers = []
            st.session_state.selected_option = None
            st.session_state.current_section = 0
            random.shuffle(st.session_state.shuffled_indices)
            st.rerun()
        
        if col2.button("Quit"):
            st.session_state.quiz_started = False
            st.rerun()

# Run the app
if __name__ == "__main__":
    app = PythonQuizApp()