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
        st.session_state.timer_expired = True

    def load_questions(self):
        questions = [
            # Questions 701-710
            {
                "question": "701. Which string method would you use to check if a string contains only alphabetic characters?",
                "options": [
                    "a) isalpha()",
                    "b) isalnum()",
                    "c) isdigit()",
                    "d) isspace()"
                ],
                "answer": "a",
                "explanation": "The isalpha() method returns True if all characters in the string are alphabetic and there is at least one character."
            },
            {
                "question": "702. What does the string method isalnum() check for?",
                "options": [
                    "a) If all characters are alphabetic",
                    "b) If all characters are numeric",
                    "c) If all characters are alphanumeric",
                    "d) If all characters are ASCII"
                ],
                "answer": "c",
                "explanation": "The isalnum() method returns True if all characters in the string are alphanumeric (either letters or numbers) and there is at least one character."
            },
            {
                "question": "703. Which method would you use to center a string within a specified width?",
                "options": [
                    "a) align()",
                    "b) center()",
                    "c) pad()",
                    "d) justify()"
                ],
                "answer": "b",
                "explanation": "The center() method returns a centered string of length width, padded with spaces or a specified fill character."
            },
            {
                "question": "704. What does the endswith() method do?",
                "options": [
                    "a) Checks if a string ends with a specified suffix",
                    "b) Adds a suffix to the end of a string",
                    "c) Removes whitespace from the end of a string",
                    "d) Returns the last character of a string"
                ],
                "answer": "a",
                "explanation": "The endswith() method returns True if the string ends with the specified suffix, otherwise it returns False."
            },
            {
                "question": "705. What is the purpose of the expandtabs() method?",
                "options": [
                    "a) Expands all tabs in a string to spaces",
                    "b) Converts spaces to tabs",
                    "c) Removes all tabs from a string",
                    "d) Counts the number of tabs in a string"
                ],
                "answer": "a",
                "explanation": "The expandtabs() method returns a copy of the string where all tab characters are replaced by spaces, optionally using the given tabsize (default 8)."
            },
            {
                "question": "706. What does the find() method return if the substring is not found?",
                "options": [
                    "a) None",
                    "b) False",
                    "c) -1",
                    "d) Raises an exception"
                ],
                "answer": "c",
                "explanation": "The find() method returns the lowest index of the substring if found, otherwise it returns -1."
            },
            {
                "question": "707. How does the index() method differ from find()?",
                "options": [
                    "a) index() is case-sensitive while find() is not",
                    "b) index() raises a ValueError if the substring is not found",
                    "c) index() searches from the end of the string",
                    "d) There is no difference"
                ],
                "answer": "b",
                "explanation": "The index() method is similar to find() but raises a ValueError when the substring is not found."
            },
            {
                "question": "708. What does the isdigit() method check for?",
                "options": [
                    "a) If the string contains only digits",
                    "b) If the string contains any digits",
                    "c) If the string can be converted to a digit",
                    "d) If the string represents a valid number"
                ],
                "answer": "a",
                "explanation": "The isdigit() method returns True if all characters in the string are digits and there is at least one character."
            },
            {
                "question": "709. What is the purpose of the islower() method?",
                "options": [
                    "a) Checks if all characters are lowercase",
                    "b) Converts all characters to lowercase",
                    "c) Checks if any character is lowercase",
                    "d) Checks if the string contains letters"
                ],
                "answer": "a",
                "explanation": "The islower() method returns True if all cased characters in the string are lowercase and there is at least one cased character."
            },
            {
                "question": "710. What does the isnumeric() method check for?",
                "options": [
                    "a) If the string contains only numeric characters",
                    "b) If the string can be converted to a number",
                    "c) If the string contains any numbers",
                    "d) If the string represents a valid integer"
                ],
                "answer": "a",
                "explanation": "The isnumeric() method returns True if all characters in the string are numeric characters, and there is at least one character."
            },

            # Questions 711-720
            {
                "question": "711. What is the purpose of the isspace() method?",
                "options": [
                    "a) Checks if the string contains only whitespace characters",
                    "b) Removes whitespace from the string",
                    "c) Counts the number of spaces in the string",
                    "d) Replaces spaces with underscores"
                ],
                "answer": "a",
                "explanation": "The isspace() method returns True if there are only whitespace characters in the string and there is at least one character."
            },
            {
                "question": "712. What does the istitle() method check for?",
                "options": [
                    "a) If the string is a valid Python identifier",
                    "b) If the string follows title case (first letter of each word capitalized)",
                    "c) If the string is all uppercase",
                    "d) If the string can be used as a title"
                ],
                "answer": "b",
                "explanation": "The istitle() method returns True if the string is a titlecased string (first character of each word is uppercase and rest are lowercase)."
            },
            {
                "question": "713. What is the purpose of the isupper() method?",
                "options": [
                    "a) Checks if all characters are uppercase",
                    "b) Converts all characters to uppercase",
                    "c) Checks if any character is uppercase",
                    "d) Checks if the string contains letters"
                ],
                "answer": "a",
                "explanation": "The isupper() method returns True if all cased characters in the string are uppercase and there is at least one cased character."
            },
            {
                "question": "714. What does the join() method do?",
                "options": [
                    "a) Combines two strings together",
                    "b) Joins the elements of an iterable with the string as a separator",
                    "c) Splits a string into parts",
                    "d) Concatenates strings with a space"
                ],
                "answer": "b",
                "explanation": "The join() method takes an iterable (like a list) and joins its elements with the string as a separator between them."
            },
            {
                "question": "715. What is the purpose of the ljust() method?",
                "options": [
                    "a) Justifies text to the left",
                    "b) Returns a left-justified string of given width",
                    "c) Removes whitespace from the left",
                    "d) Aligns numbers to the left"
                ],
                "answer": "b",
                "explanation": "The ljust() method returns the string left-justified in a string of specified length, padded with spaces or a specified character."
            },
            {
                "question": "716. What does the lower() method do?",
                "options": [
                    "a) Returns a copy of the string converted to lowercase",
                    "b) Returns the string with the first letter lowercase",
                    "c) Checks if the string is all lowercase",
                    "d) Converts only vowels to lowercase"
                ],
                "answer": "a",
                "explanation": "The lower() method returns a copy of the string with all cased characters converted to lowercase."
            },
            {
                "question": "717. What is the purpose of the lstrip() method?",
                "options": [
                    "a) Removes leading whitespace",
                    "b) Removes trailing whitespace",
                    "c) Removes all whitespace",
                    "d) Splits the string from the left"
                ],
                "answer": "a",
                "explanation": "The lstrip() method returns a copy of the string with leading whitespace removed."
            },
            {
                "question": "718. What does the partition() method return?",
                "options": [
                    "a) A list of parts split by the separator",
                    "b) A tuple containing the part before, the separator, and the part after",
                    "c) The string divided into equal parts",
                    "d) The string with the separator removed"
                ],
                "answer": "b",
                "explanation": "The partition() method splits the string at the first occurrence of the separator and returns a 3-tuple containing the part before, the separator, and the part after."
            },
            {
                "question": "719. How does rfind() differ from find()?",
                "options": [
                    "a) rfind() searches from the end of the string",
                    "b) rfind() is case-insensitive",
                    "c) rfind() returns a list of all matches",
                    "d) There is no difference"
                ],
                "answer": "a",
                "explanation": "The rfind() method returns the highest index of the substring (searches from the end of the string), while find() returns the lowest index."
            },
            {
                "question": "720. What does the rindex() method do?",
                "options": [
                    "a) Like index() but searches from the end",
                    "b) Reverses the string before searching",
                    "c) Returns a list of all indices",
                    "d) Performs a case-insensitive search"
                ],
                "answer": "a",
                "explanation": "The rindex() method is like index() but returns the highest index where the substring is found (searches from the end)."
            },

            # Questions 721-730
            {
                "question": "721. What is the purpose of the rjust() method?",
                "options": [
                    "a) Justifies text to the right",
                    "b) Returns a right-justified string of given width",
                    "c) Removes whitespace from the right",
                    "d) Aligns numbers to the right"
                ],
                "answer": "b",
                "explanation": "The rjust() method returns the string right-justified in a string of specified length, padded with spaces or a specified character."
            },
            {
                "question": "722. What does the rpartition() method do?",
                "options": [
                    "a) Like partition() but splits from the right",
                    "b) Repeats the partition operation",
                    "c) Returns a reversed partition",
                    "d) Performs multiple partitions"
                ],
                "answer": "a",
                "explanation": "The rpartition() method splits the string at the last occurrence of the separator (working from the right)."
            },
            {
                "question": "723. What is the purpose of the rsplit() method?",
                "options": [
                    "a) Like split() but works from the right",
                    "b) Reverses the string before splitting",
                    "c) Returns a reversed list of splits",
                    "d) Splits only on the rightmost occurrence"
                ],
                "answer": "a",
                "explanation": "The rsplit() method splits the string at the specified separator (working from the right) and returns a list."
            },
            {
                "question": "724. What does the rstrip() method do?",
                "options": [
                    "a) Removes leading whitespace",
                    "b) Removes trailing whitespace",
                    "c) Removes all whitespace",
                    "d) Splits the string from the right"
                ],
                "answer": "b",
                "explanation": "The rstrip() method returns a copy of the string with trailing whitespace removed."
            },
            {
                "question": "725. What is the purpose of the split() method?",
                "options": [
                    "a) Divides the string into a list of substrings",
                    "b) Separates numbers from letters",
                    "c) Splits the string into equal parts",
                    "d) Creates a list of characters"
                ],
                "answer": "a",
                "explanation": "The split() method splits the string at the specified separator and returns a list of substrings."
            },
            {
                "question": "726. What does the splitlines() method do?",
                "options": [
                    "a) Splits the string at line breaks",
                    "b) Removes all line breaks",
                    "c) Counts the number of lines",
                    "d) Joins lines with a separator"
                ],
                "answer": "a",
                "explanation": "The splitlines() method splits the string at line breaks and returns a list of lines."
            },
            {
                "question": "727. What is the purpose of the startswith() method?",
                "options": [
                    "a) Checks if the string starts with a specified prefix",
                    "b) Adds a prefix to the string",
                    "c) Returns the first character",
                    "d) Checks if the string can start a sentence"
                ],
                "answer": "a",
                "explanation": "The startswith() method returns True if the string starts with the specified prefix, otherwise False."
            },
            {
                "question": "728. What does the strip() method do?",
                "options": [
                    "a) Removes leading and trailing whitespace",
                    "b) Removes all whitespace",
                    "c) Splits the string into parts",
                    "d) Returns a stripped-down version"
                ],
                "answer": "a",
                "explanation": "The strip() method returns a copy of the string with both leading and trailing whitespace removed."
            },
            {
                "question": "729. What is the purpose of the swapcase() method?",
                "options": [
                    "a) Swaps the first and last characters",
                    "b) Converts uppercase to lowercase and vice versa",
                    "c) Swaps vowels and consonants",
                    "d) Changes the case randomly"
                ],
                "answer": "b",
                "explanation": "The swapcase() method returns a copy of the string with uppercase characters converted to lowercase and vice versa."
            },
            {
                "question": "730. What does the title() method do?",
                "options": [
                    "a) Returns a titlecased version of the string",
                    "b) Adds a title to the string",
                    "c) Converts the string to uppercase",
                    "d) Capitalizes only the first letter"
                ],
                "answer": "a",
                "explanation": "The title() method returns a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase."
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
        This quiz contains 30 questions about Python string methods (Questions 701-730).
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
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(self.questions)} (Q{701 + st.session_state.current_question})")
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
            with st.expander(f"Question {701 + i}: {answer['question']}"):
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