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

        # Questions 731-740
        {
            "question": "731. Which of these is a valid dictionary key?",
            "options": [
                "a) `[1, 2]`",
                "b) `{\"key\": \"value\"}`",
                "c) `(1, 2)`",
                "d) All of the above"
            ],
            "answer": "c) `(1, 2)` *(Only immutable types can be keys)*",
            "explanation": "Dictionary keys must be immutable (unchangeable) types. Lists and dictionaries are mutable, while tuples are immutable."
        },
        {
            "question": "732. What does this list comprehension do: `[x**2 for x in range(5)]`?",
            "options": [
                "a) Creates `[0, 1, 4, 9, 16]`",
                "b) Creates `[1, 4, 9, 16, 25]`",
                "c) Squares all numbers in a list called `x`",
                "d) Raises an error"
            ],
            "answer": "a) Creates `[0, 1, 4, 9, 16]`",
            "explanation": "The comprehension squares each number in range(5) which is [0,1,2,3,4], resulting in [0,1,4,9,16]."
        },
        {
            "question": "733. How do you create a dictionary from two lists `keys` and `values`?",
            "options": [
                "a) `dict(keys, values)`",
                "b) `dict(zip(keys, values))`",
                "c) `{keys: values}`",
                "d) `map(dict, keys, values)`"
            ],
            "answer": "b) `dict(zip(keys, values))`",
            "explanation": "zip() pairs elements from both lists, and dict() converts those pairs into key-value pairs."
        },
        {
            "question": "734. What is the output of `(1, 2, 3)[1]`?",
            "options": [
                "a) `1`",
                "b) `2`",
                "c) `(2)`",
                "d) Error"
            ],
            "answer": "b) `2`",
            "explanation": "Tuple indexing is 0-based, so index 1 refers to the second element which is 2."
        },
        {
            "question": "735. Which method would you use to count occurrences of \"apple\" in a list?",
            "options": [
                "a) `list.count(\"apple\")`",
                "b) `list.find(\"apple\")`",
                "c) `list.index(\"apple\")`",
                "d) `len(list[\"apple\"])`"
            ],
            "answer": "a) `list.count(\"apple\")`",
            "explanation": "The count() method returns the number of times the specified value appears in the list."
        },
        {
            "question": "736. What does this dictionary comprehension do: `{k:v*2 for k,v in {\"a\":1, \"b\":2}.items()}`?",
            "options": [
                "a) Doubles the keys",
                "b) Doubles the values",
                "c) Creates two copies of each item",
                "d) Filters out odd values"
            ],
            "answer": "b) Doubles the values",
            "explanation": "The comprehension iterates through each key-value pair and creates a new dictionary with the same keys but values multiplied by 2."
        },
        {
            "question": "737. How would you add \"orange\" to this list: `fruits = [\"apple\", \"banana\"]`?",
            "options": [
                "a) `fruits.append(\"orange\")`",
                "b) `fruits += \"orange\"`",
                "c) `fruits.insert(\"orange\")`",
                "d) All of the above"
            ],
            "answer": "a) `fruits.append(\"orange\")`",
            "explanation": "append() adds an item to the end of the list. The other options either have syntax errors or don't do what's intended."
        },
        {
            "question": "738. What is the safest way to get a value from a dictionary with a default if key doesn't exist?",
            "options": [
                "a) `dict[key] or default`",
                "b) `dict.get(key, default)`",
                "c) `dict.fetch(key, default)`",
                "d) `if key in dict: dict[key] else default`"
            ],
            "answer": "b) `dict.get(key, default)`",
            "explanation": "get() method returns the value for key if key is in the dictionary, else default. This prevents KeyError exceptions."
        },
        {
            "question": "739. How would you merge two dictionaries `dict1` and `dict2`?",
            "options": [
                "a) `dict1 + dict2`",
                "b) `dict1.update(dict2)`",
                "c) `dict1.join(dict2)`",
                "d) `merge(dict1, dict2)`"
            ],
            "answer": "b) `dict1.update(dict2)`",
            "explanation": "update() merges the keys and values of dict2 into dict1, overwriting values if keys already exist."
        },
        {
            "question": "740. What is the result of `len({\"a\":1, \"b\":2, \"c\":3})`?",
            "options": [
                "a) `6`",
                "b) `3`",
                "c) `1`",
                "d) `{\"a\":1, \"b\":2, \"c\":3}`"
            ],
            "answer": "b) `3` *(Counts key-value pairs)*",
            "explanation": "len() on a dictionary returns the number of key-value pairs, which is 3 in this case."
        },
        
        # Questions 741-750
        {
            "question": "741. Which operation would you use to check if \"apple\" exists in a list?",
            "options": [
                "a) `\"apple\" in list`",
                "b) `list.contains(\"apple\")`",
                "c) `list.exists(\"apple\")`",
                "d) `\"apple\" == list`"
            ],
            "answer": "a) `\"apple\" in list`",
            "explanation": "The 'in' operator checks for membership in Python sequences like lists, tuples, and strings."
        },
        {
            "question": "742. Which of these is NOT a characteristic of Python sets?",
            "options": [
                "a) Ordered",
                "b) Unindexed",
                "c) Mutable",
                "d) Contains unique elements"
            ],
            "answer": "a) Ordered",
            "explanation": "Sets are unordered collections. While they are mutable and contain unique elements, they don't maintain insertion order (until Python 3.7+ where they maintain insertion order as an implementation detail)."
        },
        {
            "question": "743. How do you create an empty set in Python?",
            "options": [
                "a) `{}`",
                "b) `set()`",
                "c) `[]`",
                "d) `()`"
            ],
            "answer": "b) `set()` *(Note: `{}` creates an empty dictionary)*",
            "explanation": "Empty curly braces {} create an empty dictionary. To create an empty set, you must use set()."
        },
        {
            "question": "744. What happens when you try to add a duplicate element to a set?",
            "options": [
                "a) Raises an error",
                "b) Replaces the existing element",
                "c) Silently ignores it",
                "d) Creates a list of duplicates"
            ],
            "answer": "c) Silently ignores it",
            "explanation": "Sets only contain unique elements. Adding a duplicate element has no effect on the set."
        },
        {
            "question": "745. Which operation returns elements in either set but not both?",
            "options": [
                "a) `union()`",
                "b) `intersection()`",
                "c) `difference()`",
                "d) `symmetric_difference()`"
            ],
            "answer": "d) `symmetric_difference()`",
            "explanation": "Symmetric difference returns elements that are in either set but not in their intersection."
        },
        {
            "question": "746. What is the main difference between `remove()` and `discard()`?",
            "options": [
                "a) `remove()` returns the deleted item",
                "b) `discard()` works with frozen sets",
                "c) `remove()` raises error if element doesn't exist",
                "d) `discard()` is faster"
            ],
            "answer": "c) `remove()` raises error if element doesn't exist",
            "explanation": "Both methods remove elements, but remove() raises KeyError if the element is not found, while discard() does nothing."
        },
        {
            "question": "747. What makes frozensets different from regular sets?",
            "options": [
                "a) They maintain insertion order",
                "b) They are immutable",
                "c) They can contain duplicates",
                "d) They are indexed"
            ],
            "answer": "b) They are immutable",
            "explanation": "Frozensets are immutable versions of sets. Once created, they cannot be modified."
        },
        {
            "question": "748. Why can't lists be elements of a set?",
            "options": [
                "a) Lists are too large",
                "b) Lists are mutable and unhashable",
                "c) Lists can contain duplicates",
                "d) Python syntax restriction"
            ],
            "answer": "b) Lists are mutable and unhashable",
            "explanation": "Set elements must be hashable (immutable). Since lists can be modified, they cannot be hashed and thus can't be set elements."
        },
        {
            "question": "749. What is the time complexity of set membership tests (`in` operator)?",
            "options": [
                "a) O(1)",
                "b) O(n)",
                "c) O(log n)",
                "d) O(n²)"
            ],
            "answer": "a) O(1) *(Due to hashing)*",
            "explanation": "Sets use hash tables, allowing average case O(1) membership tests."
        },
        {
            "question": "750. Which of these can be used as a dictionary key?",
            "options": [
                "a) `{1, 2, 3}`",
                "b) `frozenset({1, 2, 3})`",
                "c) `[1, 2, 3]`",
                "d) `{\"a\": 1}`"
            ],
            "answer": "b) `frozenset({1, 2, 3})` *(Only immutable/hashable types can be keys)*",
            "explanation": "Dictionary keys must be immutable. While regular sets are mutable, frozensets are immutable and can be used as keys."
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
        This quiz contains 20 questions about Python string methods (Questions 731-750).
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