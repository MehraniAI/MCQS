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
        "question": "651. What happens if you try to `del` a variable that doesn't exist?",
        "options": [
            "a) It silently does nothing",
            "b) It raises a `NameError`",
            "c) It returns `False`",
            "d) It creates the variable"
        ],
        "answer": "b) It raises a `NameError`",
        "explanation": "In Python, trying to delete a variable that doesn't exist raises a NameError. Python doesn't silently ignore this operation because it's considered a programmer error that should be addressed."
    },
    {
        "question": "652. Which of the following is NOT a valid way to create a string in Python?",
        "options": [
            "a) `my_str = 'Hello'`",
            "b) `my_str = \"Hello\"`",
            "c) `my_str = '''Hello'''`",
            "d) `my_str = (Hello)`"
        ],
        "answer": "d) `my_str = (Hello)`",
        "explanation": "Option d is invalid because it tries to create a string without quotes. In Python, strings must be enclosed in quotes (single, double, or triple). The parentheses alone don't create a string."
    },
    {
        "question": "653. What does it mean that Python strings are immutable?",
        "options": [
            "a) They cannot be changed after creation",
            "b) They can only contain numeric characters",
            "c) They automatically convert to uppercase",
            "d) They can be modified in-place"
        ],
        "answer": "a) They cannot be changed after creation",
        "explanation": "String immutability in Python means once a string is created, its contents cannot be changed. Any operation that appears to modify a string actually creates a new string object."
    },
    {
        "question": "654. What is the output of: `print(r'Hello\\tWorld')`?",
        "options": [
            "a) Hello    World",
            "b) Hello\\tWorld",
            "c) Hello\nWorld",
            "d) Error"
        ],
        "answer": "b) Hello\\tWorld",
        "explanation": "The 'r' prefix creates a raw string where escape sequences are not processed. So \\t is treated as literal characters, not as a tab."
    },
    {
        "question": "655. Which string creation method allows for multi-line strings?",
        "options": [
            "a) Single quotes",
            "b) Double quotes",
            "c) Triple quotes",
            "d) Raw strings"
        ],
        "answer": "c) Triple quotes",
        "explanation": "Triple quotes (''' or \"\"\") allow strings to span multiple lines. Single and double quotes require explicit line continuation characters (\\)."
    },
    {
        "question": "656. What does the `\\b` escape sequence do?",
        "options": [
            "a) Inserts a tab",
            "b) Inserts a backspace",
            "c) Inserts a backslash",
            "d) Inserts a newline"
        ],
        "answer": "b) Inserts a backspace",
        "explanation": "The \\b escape sequence represents a backspace character. When printed, it moves the cursor back one space (though the effect may not be visible in all output contexts)."
    },
    {
        "question": "657. Which escape sequence would you use to include a double quote inside a double-quoted string?",
        "options": [
            "a) `\\'`",
            "b) `\\\"`",
            "c) `\\\\`",
            "d) `\\n`"
        ],
        "answer": "b) `\\\"`",
        "explanation": "To include a double quote inside a double-quoted string, you need to escape it with a backslash (\\\"). This tells Python to treat it as a literal character rather than the string delimiter."
    },
    {
        "question": "658. What is the output of: `'Hello' + 'World'`?",
        "options": [
            "a) 'Hello World'",
            "b) 'HelloWorld'",
            "c) 'Hello+World'",
            "d) Error"
        ],
        "answer": "b) 'HelloWorld'",
        "explanation": "The + operator concatenates strings without adding any extra characters. To get a space between words, you would need to explicitly include it: 'Hello ' + 'World'."
    },
    {
        "question": "659. What does `'Hello'[1]` return?",
        "options": [
            "a) 'H'",
            "b) 'e'",
            "c) 'l'",
            "d) 'o'"
        ],
        "answer": "b) 'e'",
        "explanation": "Python uses zero-based indexing, so index 1 refers to the second character in the string. 'H' is at index 0, 'e' at 1, 'l' at 2 and 3, and 'o' at 4."
    },
    {
        "question": "660. What is the output of: `'Hello World!'[7:]`?",
        "options": [
            "a) 'World!'",
            "b) 'World'",
            "c) 'orld!'",
            "d) 'Hello'"
        ],
        "answer": "a) 'World!'",
        "explanation": "The slice [7:] means 'from index 7 to the end'. Counting spaces (which are characters), 'W' is at position 7, so the slice returns 'World!'."
    },
    {
        "question": "661. What does `len(\" Python \")` return?",
        "options": [
            "a) 6",
            "b) 7",
            "c) 8",
            "d) 9"
        ],
        "answer": "c) 8",
        "explanation": "The len() function counts all characters in the string, including spaces. There's one space before 'Python' and one after, plus 6 letters, totaling 8 characters."
    },
    {
        "question": "662. What does `'hello'.upper()` return?",
        "options": [
            "a) 'HELLO'",
            "b) 'Hello'",
            "c) 'hello'",
            "d) Error"
        ],
        "answer": "a) 'HELLO'",
        "explanation": "The upper() method converts all lowercase characters in a string to uppercase. It doesn't modify the original string (strings are immutable) but returns a new string."
    },
    {
        "question": "663. What is the output of: `'Hello World'.split('l')`?",
        "options": [
            "a) ['He', '', 'o Wor', 'd']",
            "b) ['Hello', 'World']",
            "c) ['H', 'e', 'l', 'l', 'o']",
            "d) Error"
        ],
        "answer": "a) ['He', '', 'o Wor', 'd']",
        "explanation": "split('l') splits the string at each 'l' character. The empty string between two 'l's becomes an empty string in the list. The split includes all parts before, between, and after the 'l's."
    },
    {
        "question": "664. What does `','.join(['a', 'b', 'c'])` return?",
        "options": [
            "a) 'a,b,c'",
            "b) 'a b c'",
            "c) 'a, b, c'",
            "d) ['a,b,c']"
        ],
        "answer": "a) 'a,b,c'",
        "explanation": "The join() method combines the elements of the list into a single string, with the string it's called on (',') inserted between each element. Note it's called on the delimiter string, not the list."
    },
    {
        "question": "665. What is the output of: `'hello'.find('l')`?",
        "options": [
            "a) 1",
            "b) 2",
            "c) 3",
            "d) -1"
        ],
        "answer": "b) 2",
        "explanation": "find() returns the index of the first occurrence of the substring. The first 'l' is at index 2 (remember Python uses zero-based indexing: h=0, e=1, l=2)."
    },
    {
        "question": "666. What does `'hello hello'.count('he')` return?",
        "options": [
            "a) 1",
            "b) 2",
            "c) 0",
            "d) 5"
        ],
        "answer": "b) 2",
        "explanation": "count() returns the number of non-overlapping occurrences of the substring. 'he' appears at the start of both 'hello's in the string."
    },
    {
        "question": "667. Which string formatting method was introduced in Python 3.6?",
        "options": [
            "a) %-formatting",
            "b) str.format()",
            "c) f-strings",
            "d) Template strings"
        ],
        "answer": "c) f-strings",
        "explanation": "f-strings (formatted string literals) were introduced in Python 3.6. They provide a concise way to embed expressions inside string literals using {expression} syntax."
    },
    {
        "question": "668. What is the output of: `f\"2 + 2 = {2+2}\"`?",
        "options": [
            "a) '2 + 2 = 4'",
            "b) '2 + 2 = {2+2}'",
            "c) '4 = 4'",
            "d) Error"
        ],
        "answer": "a) '2 + 2 = 4'",
        "explanation": "In an f-string, expressions inside {} are evaluated at runtime. Here 2+2 evaluates to 4, resulting in the string '2 + 2 = 4'."
    },
    {
        "question": "669. Which placeholder would you use for a floating-point number with 2 decimal places using %-formatting?",
        "options": [
            "a) `%d`",
            "b) `%f`",
            "c) `%.2f`",
            "d) `%s`"
        ],
        "answer": "c) `%.2f`",
        "explanation": "In %-formatting, %.2f formats a float with 2 decimal places. %d is for integers, %f defaults to 6 decimals, and %s is for strings."
    },
    {
        "question": "670. What is the output of:\n```python\na = \"hello\"\nb = \"hello\"\nprint(a is b)\n```",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "a) True",
        "explanation": "Due to Python's string interning, identical string literals may refer to the same object in memory. The 'is' operator checks object identity, so this often returns True for small strings, though this is an implementation detail."
    },
    {
        "question": "671. Which strings are typically NOT automatically interned in Python?",
        "options": [
            "a) Short strings",
            "b) Strings that look like identifiers",
            "c) Very long strings",
            "d) Strings containing only digits"
        ],
        "answer": "c) Very long strings",
        "explanation": "Python automatically interns (stores only one copy of) small strings and strings that look like identifiers for optimization. Very long strings are typically not interned automatically to save memory."
    },
    {
        "question": "672. What is the output of: `'apple' < 'banana'`?",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "a) True",
        "explanation": "String comparison in Python is lexicographical (like dictionary order). 'a' comes before 'b' in the alphabet, so 'apple' is considered less than 'banana'."
    },
    {
        "question": "673. What is the output of: `'A' > 'a'`?",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "b) False",
        "explanation": "In Python, uppercase letters have lower Unicode values than lowercase letters. So 'A' (65) is less than 'a' (97), making the comparison False."
    },
    {
        "question": "674. What is the output of: `int(3.9)`?",
        "options": [
            "a) 3",
            "b) 4",
            "c) 3.0",
            "d) Error"
        ],
        "answer": "a) 3",
        "explanation": "int() truncates towards zero when converting from float. It doesn't round, so 3.9 becomes 3. This is different from round(3.9) which would return 4."
    },
    {
        "question": "675. What is the output of: `str(True)`?",
        "options": [
            "a) '1'",
            "b) 'True'",
            "c) True",
            "d) Error"
        ],
        "answer": "b) 'True'",
        "explanation": "The str() function converts a boolean to its string representation. True becomes 'True' (note the quotes indicating it's now a string), not the numeric value 1."
    },
    {
        "question": "676. What is the output of: `bool(\"\")`?",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "b) False",
        "explanation": "In Python, empty sequences (including empty strings) are considered False in a boolean context. Non-empty strings are True."
    },
    {
        "question": "677. What is the output of: `'Hi' * 3`?",
        "options": [
            "a) 'HiHiHi'",
            "b) 'Hi Hi Hi'",
            "c) 'Hi3'",
            "d) Error"
        ],
        "answer": "a) 'HiHiHi'",
        "explanation": "The * operator when used with a string and integer performs repetition. The string is concatenated with itself the specified number of times."
    },
    {
        "question": "678. What is the output of:\n```python\ns = 'hello'\nprint(s.replace('l', 'x'))\n```",
        "options": [
            "a) 'hexxo'",
            "b) 'hexo'",
            "c) 'hxxo'",
            "d) 'hello'"
        ],
        "answer": "a) 'hexxo'",
        "explanation": "replace() replaces all occurrences of the first argument with the second. Both 'l's in 'hello' are replaced with 'x's, resulting in 'hexxo'."
    },
    {
        "question": "679. What is the output of: `'hello'.title()`?",
        "options": [
            "a) 'HELLO'",
            "b) 'Hello'",
            "c) 'hello'",
            "d) 'H e l l o'"
        ],
        "answer": "b) 'Hello'",
        "explanation": "title() capitalizes the first character of each word in the string. For a single word, it's equivalent to capitalize(), making the first letter uppercase and the rest lowercase."
    },
    {
        "question": "680. Which method would you use to remove whitespace from both ends of a string?",
        "options": [
            "a) `trim()`",
            "b) `strip()`",
            "c) `clean()`",
            "d) `remove()`"
        ],
        "answer": "b) `strip()`",
        "explanation": "strip() removes leading and trailing whitespace (spaces, tabs, newlines). Python doesn't have a trim() method (though some other languages do). lstrip() and rstrip() remove from left or right only."
    },
    {
        "question": "681. What is the output of: `'hello'.isalpha()`?",
        "options": [
            "a) True",
            "b) False",
            "c) Error",
            "d) None"
        ],
        "answer": "a) True",
        "explanation": "isalpha() returns True if all characters in the string are alphabetic and there is at least one character. 'hello' contains only letters, so it returns True."
    },
    {
        "question": "682. How can you create a multi-line string in Python?",
        "options": [
            "a) Using single quotes",
            "b) Using double quotes",
            "c) Using triple quotes",
            "d) Using square brackets"
        ],
        "answer": "c) Using triple quotes",
        "explanation": "Triple quotes (''' or \"\"\") allow strings to span multiple lines without needing explicit line continuation characters. Single and double quotes require \\n for newlines."
    },
    {
        "question": "683. What is the output of `print(r\"Hello\\nWorld\")`?",
        "options": [
            "a) `Hello\nWorld`",
            "b) `Hello\\nWorld`",
            "c) `Hello World`",
            "d) `rHello World`"
        ],
        "answer": "b) `Hello\\nWorld`",
        "explanation": "The 'r' prefix creates a raw string where backslashes are treated as literal characters. So \\n is not interpreted as a newline but printed as two characters."
    },
    {
        "question": "684. Which escape sequence represents a tab character?",
        "options": [
            "a) `\\n`",
            "b) `\\t`",
            "c) `\\b`",
            "d) `\\\\`"
        ],
        "answer": "b) `\\t`",
        "explanation": "\\t represents a tab character. \\n is newline, \\b is backspace, and \\\\ is a literal backslash."
    },
    {
        "question": "685. What does `my_string[7:]` do?",
        "options": [
            "a) Returns the first 7 characters",
            "b) Returns characters from index 7 to the end",
            "c) Returns the last 7 characters",
            "d) Raises an error"
        ],
        "answer": "b) Returns characters from index 7 to the end",
        "explanation": "Slicing with [7:] means 'from index 7 to the end'. To get the first 7 characters you'd use [:7], and for the last 7 you'd use [-7:]."
    },
    {
        "question": "686. How do you convert a string to uppercase?",
        "options": [
            "a) `my_string.toUpper()`",
            "b) `my_string.upper()`",
            "c) `upper(my_string)`",
            "d) `my_string.capitalize()`"
        ],
        "answer": "b) `my_string.upper()`",
        "explanation": "upper() is the correct string method to convert to uppercase. capitalize() only capitalizes the first character, and Python doesn't have toUpper()."
    },
    {
        "question": "687. What is the output of `\"Hello, World!\".split(\"l\")`?",
        "options": [
            "a) `[\"He\", \"\", \"o, Wor\", \"d!\"]`",
            "b) `[\"Hello\", \"World\"]`",
            "c) `[\"H\", \"e\", \"l\", \"l\", \"o\"]`",
            "d) `[\"Hel\", \"lo, Wor\", \"d!\"]`"
        ],
        "answer": "a) `[\"He\", \"\", \"o, Wor\", \"d!\"]`",
        "explanation": "split('l') splits at each 'l'. Between two 'l's there's an empty string. The split includes all parts before, between, and after the 'l's."
    },
    {
        "question": "688. Which method joins a list of strings into a single string?",
        "options": [
            "a) `concat()`",
            "b) `merge()`",
            "c) `join()`",
            "d) `combine()`"
        ],
        "answer": "c) `join()`",
        "explanation": "join() is called on the delimiter string and takes a sequence of strings to join. For example: ', '.join(['a', 'b']) gives 'a, b'."
    },
    {
        "question": "689. What does `\"hello\".count(\"l\")` return?",
        "options": [
            "a) 1",
            "b) 2",
            "c) 3",
            "d) 0"
        ],
        "answer": "b) 2",
        "explanation": "count() returns the number of non-overlapping occurrences of the substring. 'hello' contains two 'l' characters."
    },
    {
        "question": "690. Which operator is used for string repetition?",
        "options": [
            "a) `+`",
            "b) `*`",
            "c) ``",
            "d) `//`"
        ],
        "answer": "b) `*`",
        "explanation": "The * operator, when used with a string and integer, performs string repetition. For example: 'hi' * 3 gives 'hihihi'."
    },
    {
        "question": "691. What is the result of `\"apple\" < \"banana\"`?",
        "options": [
            "a) `True`",
            "b) `False`",
            "c) `None`",
            "d) `Error`"
        ],
        "answer": "a) `True`",
        "explanation": "String comparison is lexicographical (like dictionary order). 'a' comes before 'b', so 'apple' is considered less than 'banana' regardless of length."
    },
    {
        "question": "692. Which function converts an integer to a string?",
        "options": [
            "a) `int()`",
            "b) `float()`",
            "c) `str()`",
            "d) `chr()`"
        ],
        "answer": "c) `str()`",
        "explanation": "str() converts its argument to a string representation. int() converts to integer, float() to floating-point number, and chr() returns the Unicode character for an integer."
    },
    {
        "question": "693. What does `\"123abc\".isnumeric()` return?",
        "options": [
            "a) `True`",
            "b) `False`",
            "c) `None`",
            "d) `Error`"
        ],
        "answer": "b) `False`",
        "explanation": "isnumeric() returns True only if all characters in the string are numeric. Since 'abc' are letters, it returns False."
    },
    {
        "question": "694. Which method checks if a string starts with a specific substring?",
        "options": [
            "a) `startswith()`",
            "b) `beginwith()`",
            "c) `checkprefix()`",
            "d) `firstmatch()`"
        ],
        "answer": "a) `startswith()`",
        "explanation": "startswith() checks if the string begins with the specified substring. There is no beginwith() method in Python."
    },
    {
        "question": "695. What is the output of `\"-\".join([\"A\", \"B\", \"C\"])`?",
        "options": [
            "a) `\"A-B-C\"`",
            "b) `\"A B C\"`",
            "c) `\"ABC\"`",
            "d) `[\"A\", \"B\", \"C\"]`"
        ],
        "answer": "a) `\"A-B-C\"`",
        "explanation": "join() combines the list elements into a string with the specified separator ('-') between them. Note that join() is called on the separator string."
    },
    {
        "question": "696. How do you replace \"cat\" with \"dog\" in `\"I love cats\"`?",
        "options": [
            "a) `replace(\"cat\", \"dog\")`",
            "b) `swap(\"cat\", \"dog\")`",
            "c) `substitute(\"cat\", \"dog\")`",
            "d) `change(\"cat\", \"dog\")`"
        ],
        "answer": "a) `replace(\"cat\", \"dog\")`",
        "explanation": "The replace() method replaces occurrences of the first argument with the second. For example: \"I love cats\".replace(\"cat\", \"dog\") gives \"I love dogs\"."
    },
    {
        "question": "697. What is string interning in Python?",
        "options": [
            "a) Storing only one copy of each unique string to save memory",
            "b) Converting strings to integers",
            "c) A method to reverse strings",
            "d) A way to encrypt strings"
        ],
        "answer": "a) Storing only one copy of each unique string to save memory",
        "explanation": "String interning is an optimization where Python stores only one copy of each distinct string value. This is done automatically for small strings and can be forced with sys.intern()."
    },
    {
        "question": "698. Which strings are automatically interned?",
        "options": [
            "a) All strings",
            "b) Only strings longer than 20 characters",
            "c) Short strings and identifiers",
            "d) Only strings containing numbers"
        ],
        "answer": "c) Short strings and identifiers",
        "explanation": "Python automatically interns small strings and strings that look like identifiers (variable names, function names, etc.) for optimization. Very long strings are typically not interned."
    },
    {
        "question": "699. What does `sys.intern()` do?",
        "options": [
            "a) Deletes a string from memory",
            "b) Manually interns a string",
            "c) Converts a string to lowercase",
            "d) Checks if a string is numeric"
        ],
        "answer": "b) Manually interns a string",
        "explanation": "sys.intern() forces a string to be interned, which can be useful for optimization when you know you'll be comparing the same string many times."
    },
    {
        "question": "700. What is the output of `\"Python\" * 3`?",
        "options": [
            "a) `\"PythonPythonPython\"`",
            "b) `\"Python 3\"`",
            "c) `\"PythonPython\"`",
            "d) `Error`"
        ],
        "answer": "a) `\"PythonPythonPython\"`",
        "explanation": "The * operator with a string and integer performs string repetition. The string is concatenated with itself the specified number of times."
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
            is_correct = (user_answer == question_data["answer"][0].lower())
        
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