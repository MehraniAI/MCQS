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
    # Questions 51-60
    {
        "question": "51: What does the del statement do in Python?",
        "options": ["a) Deletes a variable.", "b) Deletes an element from a list.", "c) Deletes a file.", "d) Deletes a class."],
        "answer": "a) Deletes a variable."
    },
    {
        "question": "52: What is the output of the following code?\nx = 5\ny = x\nx = 10\nprint(y)",
        "options": ["a) 5", "b) 10", "c) Error", "d) None"],
        "answer": "a) 5"
    },
    {
        "question": "53: Which of the following is true about Python's global keyword?",
        "options": ["a) It declares a variable inside a function as global.", "b) It declares a variable outside a function as global.", "c) It declares a variable as constant.", "d) It declares a variable as local to a function."],
        "answer": "a) It declares a variable inside a function as global."
    },
    {
        "question": "54: How do you check the type of a variable in Python?",
        "options": ["a) typeof(variable)", "b) variable.type()", "c) type(variable)", "d) variable.__type__()"],
        "answer": "c) type(variable)"
    },
    {
        "question": "55: What will be the output of the following code?\nx = \"Hello\"\ny = 3\nprint(x * y)",
        "options": ["a) HelloHelloHello", "b) Hello3", "c) HelloHelloHelloHello", "d) Error"],
        "answer": "a) HelloHelloHello"
    },
    {
        "question": "56: Which of the following data types is immutable in Python?",
        "options": ["a) list", "b) set", "c) tuple", "d) dictionary"],
        "answer": "c) tuple"
    },
    {
        "question": "57: What is the output of the following code?\nx = 5\ndef func():\n    global x\n    x = 10\nfunc()\nprint(x)",
        "options": ["a) 5", "b) 10", "c) Error", "d) None"],
        "answer": "b) 10"
    },
    {
        "question": "58: What does the zip function in Python do?",
        "options": ["a) Combines two lists into a dictionary.", "b) Creates an iterator that aggregates elements from two or more iterables.", "c) Unzips a list into separate elements.", "d) Sorts elements in a list."],
        "answer": "b) Creates an iterator that aggregates elements from two or more iterables."
    },
    {
        "question": "59: What will be the output of the following code?\ndef foo(a, b):\n    return a + b\n\nprint(foo(1, 2, 3))",
        "options": ["a) 3", "b) 6", "c) Error", "d) None"],
        "answer": "c) Error"
    },
    {
        "question": "60: Which of the following is used to iterate over a sequence of numbers in Python?",
        "options": ["a) for i in range(10):", "b) for i in 1 to 10:", "c) for i = 1 to 10:", "d) for i from 1 to 10:"],
        "answer": "a) for i in range(10):"
    },
    # Questions 61-70
    {
        "question": "61: What is the output of the following code?\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
        "options": ["a) [1, 2, 3]", "b) [1, 2, 3, 4]", "c) [4, 1, 2, 3]", "d) Error"],
        "answer": "b) [1, 2, 3, 4]"
    },
    {
        "question": "62: How do you convert a string \"123\" to a float in Python?",
        "options": ["a) float(\"123\")", "b) convert_float(\"123\")", "c) 123.0", "d) str_to_float(\"123\")"],
        "answer": "a) float(\"123\")"
    },
    {
        "question": "63: Which of the following statements about Python's pass statement is true?",
        "options": ["a) It must be used in every loop.", "b) It terminates the program.", "c) It is used to indicate the end of a function.", "d) It is a null operation."],
        "answer": "d) It is a null operation."
    },
    {
        "question": "64: What will be the output of the following code?\ndef func(x, y=2, z=3):\n    return x * y * z\nprint(func(2, z=4))",
        "options": ["a) 16", "b) 12", "c) 24", "d) 8"],
        "answer": "a) 16"
    },
    {
        "question": "65: How do you check if an object has an attribute in Python?",
        "options": ["a) object.has_attr('attribute')", "b) attribute in object", "c) hasattr(object, 'attribute')", "d) object.attribute_exists('attribute')"],
        "answer": "c) hasattr(object, 'attribute')"
    },
    {
        "question": "66: What is the purpose of the __init__ method in Python classes?",
        "options": ["a) To initialize the object's attributes.", "b) To define private methods.", "c) To finalize the class definition.", "d) To create a new instance of the class."],
        "answer": "a) To initialize the object's attributes."
    },
    {
        "question": "67: What does the return statement do in a function in Python?",
        "options": ["a) Ends the execution of the function and returns a value.", "b) Prints a value to the console.", "c) Raises an exception.", "d) Calls another function."],
        "answer": "a) Ends the execution of the function and returns a value."
    },
    {
        "question": "68: What will be the output of the following code?\nx = [1, 2, 3]\ny = x\nx = [4, 5, 6]\nprint(y)",
        "options": ["a) [1, 2, 3]", "b) [4, 5, 6]", "c) [1, 2, 3, 4, 5, 6]", "d) Error"],
        "answer": "a) [1, 2, 3]"
    },
    {
        "question": "69: Which of the following is used to comment multiple lines in Python?",
        "options": ["a) /* */", "b) <!-- -->", "c) ''' '''", "d) //"],
        "answer": "c) ''' '''"
    },
    {
        "question": "70: What does the is operator do in Python?",
        "options": ["a) Checks if two objects have the same value.", "b) Checks if two objects are identical (refer to the same object).", "c) Checks if two objects are not identical.", "d) Checks if two objects have the same type."],
        "answer": "b) Checks if two objects are identical (refer to the same object)."
    },
    # Questions 71-80
    {
        "question": "71: What will be the output of the following code?\ndef outer():\n    x = 1\n    def inner():\n        nonlocal x\n        x = 2\n    inner()\n    return x\nprint(outer())",
        "options": ["a) 1", "b) 2", "c) Error", "d) None"],
        "answer": "b) 2"
    },
    {
        "question": "72: What is the output of the following code?\ndef func(x, y):\n    return x / y\nprint(func(5, 2))",
        "options": ["a) 2.5", "b) 2", "c) 2.0", "d) 3"],
        "answer": "a) 2.5"
    },
    {
        "question": "73: What does the any function do in Python?",
        "options": ["a) Checks if all elements in an iterable are true.", "b) Checks if all elements in an iterable are false.", "c) Checks if any element in an iterable is true.", "d) Checks if any element in an iterable is false."],
        "answer": "c) Checks if any element in an iterable is true."
    },
    {
        "question": "74: What is the output of the following code?\ndef func(a, b, c=1, d=2):\n    return a + b + c + d\nprint(func(1, 2))",
        "options": ["a) 6", "b) 4", "c) 3", "d) Error"],
        "answer": "a) 6"
    },
    {
        "question": "75: Which of the following statements is true about Python's assert statement?",
        "options": ["a) It raises an exception unconditionally.", "b) It is used for debugging purposes.", "c) It checks if a condition is false.", "d) It is used to define assertions."],
        "answer": "b) It is used for debugging purposes."
    },
    {
        "question": "76: What will be the output of the following code?\nx = [1, 2, 3]\ny = x[:]\ny.append(4)\nprint(x)",
        "options": ["a) [1, 2, 3]", "b) [1, 2, 3, 4]", "c) [4, 1, 2, 3]", "d) Error"],
        "answer": "a) [1, 2, 3]"
    },
    {
        "question": "77: How do you convert a tuple (1, 2, 3) to a list in Python?",
        "options": ["a) list(1, 2, 3)", "b) tuple_to_list((1, 2, 3))", "c) convert_tuple((1, 2, 3))", "d) list((1, 2, 3))"],
        "answer": "d) list((1, 2, 3))"
    },
    {
        "question": "78: What does the len() function do in Python?",
        "options": ["a) Returns the length of an integer.", "b) Returns the length of a string.", "c) Returns the length of an object.", "d) Returns the length of a list or tuple."],
        "answer": "d) Returns the length of a list or tuple."
    },
    {
        "question": "79: What is the output of the following code?\nx = 5\nif x > 10:\n    print(\"Greater than 10\")\nelif x > 3:\n    print(\"Greater than 3\")\nelse:\n    print(\"Less than or equal to 3\")",
        "options": ["a) Greater than 10", "b) Greater than 3", "c) Less than or equal to 3", "d) No output"],
        "answer": "b) Greater than 3"
    },
    {
        "question": "80: Which of the following is a correct way to open a file data.txt in Python?",
        "options": ["a) file = open(\"data.txt\", \"r\")", "b) file = open(\"data.txt\", \"read\")", "c) file = open(\"data.txt\", mode=\"r\")", "d) file = open(\"data.txt\")"],
        "answer": "a) file = open(\"data.txt\", \"r\")"
    },
    # Questions 81-90
    {
        "question": "81: What will be the output of the following code?\nx = [1, 2, 3]\ny = [4, 5]\nz = x + y\nprint(z)",
        "options": ["a) [1, 2, 3, 4, 5]", "b) [[1, 2, 3], [4, 5]]", "c) [1, 2, 3, [4, 5]]", "d) Error"],
        "answer": "a) [1, 2, 3, 4, 5]"
    },
    {
        "question": "82: How do you remove the last element from a list my_list in Python?",
        "options": ["a) my_list.remove_last()", "b) my_list.pop()", "c) my_list.delete(-1)", "d) my_list.remove(-1)"],
        "answer": "b) my_list.pop()"
    },
    {
        "question": "83: What is the output of the following code?\ndef func(x):\n    return x * 2\n\nnums = [1, 2, 3, 4]\ndoubled = map(func, nums)\nprint(list(doubled))",
        "options": ["a) [2, 4, 6, 8]", "b) [1, 4, 9, 16]", "c) [2, 3, 4, 5]", "d) [1, 2, 3, 4]"],
        "answer": "a) [2, 4, 6, 8]"
    },
    {
        "question": "84: What does the sorted() function do in Python?",
        "options": ["a) Sorts a list in descending order.", "b) Sorts a list in ascending order.", "c) Returns the smallest element in a list.", "d) Reverses the elements in a list."],
        "answer": "b) Sorts a list in ascending order."
    },
    {
        "question": "85: What is the output of the following code?\nx = 10\nwhile x > 0:\n    print(x)\n    x -= 2",
        "options": ["a) 10 8 6 4 2", "b) 10 9 8 7 6 5 4 3 2 1", "c) 10 8 6 4 2 0", "d) 10 8 6 4 2 0 -2"],
        "answer": "a) 10 8 6 4 2"
    },
    {
        "question": "86: How do you convert a list [1, 2, 3] to a tuple in Python?",
        "options": ["a) tuple([1, 2, 3])", "b) (1, 2, 3)", "c) convert_tuple([1, 2, 3])", "d) list_to_tuple([1, 2, 3])"],
        "answer": "a) tuple([1, 2, 3])"
    },
    {
        "question": "87: What does the continue statement do in Python?",
        "options": ["a) Exits the current loop.", "b) Skips the remaining code in the current iteration of a loop and jumps to the next iteration.", "c) Ends the program.", "d) Breaks out of the loop completely."],
        "answer": "b) Skips the remaining code in the current iteration of a loop and jumps to the next iteration."
    },
    {
        "question": "88: What will be the output of the following code?\ndef func(x=1, y=2):\n    return x * y\nprint(func(y=3))",
        "options": ["a) 6", "b) 3", "c) 9", "d) 2"],
        "answer": "a) 6"
    },
    {
        "question": "89: What is the purpose of the __doc__ attribute in Python?",
        "options": ["a) It stores the documentation string of a function or module.", "b) It is used to document variables.", "c) It is used to define private methods.", "d) It is used to define class attributes."],
        "answer": "a) It stores the documentation string of a function or module."
    },
    {
        "question": "90: What will be the output of the following code?\nx = 10\nif x > 5:\n    print(\"Hello\")\nelse:\n    print(\"Hi\")",
        "options": ["a) Hello", "b) Hi", "c) Hello Hi", "d) No output"],
        "answer": "a) Hello"
    },
    # Questions 91-100
    {
        "question": "91: Which of the following data types is mutable in Python?",
        "options": ["a) int", "b) float", "c) tuple", "d) list"],
        "answer": "d) list"
    },
    {
        "question": "92: What does the break statement do in Python?",
        "options": ["a) Ends the current iteration of a loop and continues with the next iteration.", "b) Ends the current loop and resumes execution at the next statement after the loop.", "c) Terminates the program.", "d) Skips the current iteration of a loop."],
        "answer": "b) Ends the current loop and resumes execution at the next statement after the loop."
    },
    {
        "question": "93: How can you convert a string \"123\" to an integer in Python?",
        "options": ["a) int(\"123\")", "b) integer(\"123\")", "c) convert(\"123\")", "d) str_to_int(\"123\")"],
        "answer": "a) int(\"123\")"
    },
    {
        "question": "94: Which of the following is a correct way to define a function in Python that takes two parameters a and b?",
        "options": ["a) def function(a, b):", "b) function(a, b):", "c) def function(a b):", "d) define function(a, b):"],
        "answer": "a) def function(a, b):"
    },
    {
        "question": "95: What is the output of the following code?\ndef greet(name, msg=\"Good morning!\"):\n    print(\"Hello\", name + ', ' + msg)\ngreet(\"Alice\")",
        "options": ["a) Hello Alice, Good morning!", "b) Hello Alice", "c) Error", "d) None"],
        "answer": "a) Hello Alice, Good morning!"
    },
    {
        "question": "96: Which of the following statements about Python's lambda function is true?",
        "options": ["a) It can contain multiple expressions.", "b) It can have a return statement.", "c) It is used to define anonymous functions.", "d) It can be used to create classes."],
        "answer": "c) It is used to define anonymous functions."
    },
    {
        "question": "97: What will be the output of the following code?\nx = 5\ny = 2\nprint(x // y)",
        "options": ["a) 2.5", "b) 2", "c) 2.0", "d) 3"],
        "answer": "b) 2"
    },
    {
        "question": "98: What does the format() method do in Python?",
        "options": ["a) Formats a string into uppercase letters.", "b) Formats a string into lowercase letters.", "c) Formats a string based on a format string and arguments.", "d) Formats a string into title case."],
        "answer": "c) Formats a string based on a format string and arguments."
    },
    {
        "question": "99: What is the purpose of the pass statement in Python?",
        "options": ["a) To break out of a loop.", "b) To skip the current iteration of a loop.", "c) To define an empty function or class.", "d) To handle exceptions."],
        "answer": "c) To define an empty function or class."
    },
    {
        "question": "100: Which of the following statements about Python's zip() function is true?",
        "options": ["a) It combines two dictionaries into one.", "b) It sorts a list in descending order.", "c) It creates an iterator that aggregates elements from two or more iterables.", "d) It removes duplicates from a list."],
        "answer": "c) It creates an iterator that aggregates elements from two or more iterables."
    }
]
        return questions

    def create_welcome_screen(self):
        st.title("Python Quiz Challenge")
        st.markdown("""
            This quiz contains 50 questions about Python programming organized in sections.
            
            **Sections:**
            - Questions 51-60: Python Basics
            - Questions 61-70: Data Structures
            - Questions 71-80: Functions and Classes
            - Questions 81-90: Advanced Concepts
            - Questions 91-100: Miscellaneous
            
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