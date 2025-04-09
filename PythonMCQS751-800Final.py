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
    {
        "question": "751. What determines the internal order of elements in a set?",
        "options": [
            "a) Insertion order",
            "b) Hash values",
            "c) Alphabetical order",
            "d) Random assignment"
        ],
        "answer": "b) Hash values *(Though this is implementation detail)*",
        "explanation": "While sets appear unordered, their internal ordering is determined by the hash values of their elements. However, this is an implementation detail and shouldn't be relied upon as it may vary across different Python versions or implementations."
    },
    {
        "question": "752. What does `A.issuperset(B)` check?",
        "options": [
            "a) If A contains all elements of B",
            "b) If B contains all elements of A",
            "c) If A and B have no common elements",
            "d) If A is larger than B"
        ],
        "answer": "a) If A contains all elements of B",
        "explanation": "The `issuperset()` method checks if all elements of set B are present in set A. It returns True if A contains all elements of B, and False otherwise. This is the opposite of `issubset()`."
    },
    {
        "question": "753. Which operator performs set union?",
        "options": [
            "a) `&`",
            "b) `|`",
            "c) `-`",
            "d) `^`"
        ],
        "answer": "b) `|`",
        "explanation": "The pipe `|` operator performs set union, combining all elements from both sets without duplicates. For example, `{1,2} | {2,3}` results in `{1,2,3}`. The `&` operator is for intersection, `-` for difference, and `^` for symmetric difference."
    },
    {
        "question": "754. What does `set1 - set2` return?",
        "options": [
            "a) Elements in set1 not in set2",
            "b) Elements in set2 not in set1",
            "c) Common elements",
            "d) All unique elements"
        ],
        "answer": "a) Elements in set1 not in set2",
        "explanation": "The difference operation (`set1 - set2`) returns a new set containing elements that are in set1 but not in set2. This operation is not symmetric - `set2 - set1` would return elements in set2 but not in set1."
    },
    {
        "question": "755. How do you remove and return an arbitrary set element?",
        "options": [
            "a) `remove()`",
            "b) `discard()`",
            "c) `pop()`",
            "d) `clear()`"
        ],
        "answer": "c) `pop()`",
        "explanation": "The `pop()` method removes and returns an arbitrary element from the set. This is useful when you need to process elements while emptying a set. `remove()` removes a specific element but raises KeyError if not found, while `discard()` removes without raising an error."
    },
    {
        "question": "756. What does `set.update()` do?",
        "options": [
            "a) Returns a new merged set",
            "b) Modifies the set in-place with union",
            "c) Removes all elements",
            "d) Sorts the set"
        ],
        "answer": "b) Modifies the set in-place with union",
        "explanation": "The `update()` method modifies the set in-place by adding elements from other iterables (like sets, lists, etc.). It's equivalent to the `|=` operator. Unlike union operation which returns a new set, `update()` changes the existing set."
    },
    {
        "question": "757. Which is the most efficient way to remove duplicates from a list?",
        "options": [
            "a) `list(set(original_list))`",
            "b) Using a loop to check each element",
            "c) `list(dict.fromkeys(original_list))`",
            "d) Both a and c"
        ],
        "answer": "d) Both a and c",
        "explanation": "Both converting to a set and back (option a) and using `dict.fromkeys()` (option c) are efficient O(n) operations for removing duplicates. The dictionary approach has the added benefit of preserving insertion order (Python 3.7+), while the set approach is slightly faster but doesn't preserve order."
    },
    {
        "question": "758. What does this code do: `len(set1 ^ set2)`?",
        "options": [
            "a) Counts common elements",
            "b) Counts elements in either set but not both",
            "c) Returns the larger set's size",
            "d) Raises an error"
        ],
        "answer": "b) Counts elements in either set but not both",
        "explanation": "The `^` operator performs symmetric difference, returning elements that are in either set but not in both. `len(set1 ^ set2)` counts how many such elements exist. This is useful for finding elements that are unique to each set."
    },
    {
        "question": "759. Which method would you use to check if two sets have no common elements?",
        "options": [
            "a) `isdisjoint()`",
            "b) `issubset()`",
            "c) `intersection()`",
            "d) `difference()`"
        ],
        "answer": "a) `isdisjoint()`",
        "explanation": "The `isdisjoint()` method returns True if the sets have no elements in common. This is more efficient than checking `len(set1 & set2) == 0` because it can return False as soon as it finds any common element."
    },
    {
        "question": "760. What is the result of `frozenset({1,2}) | {3,4}`?",
        "options": [
            "a) `{1,2,3,4}`",
            "b) Error - can't mix types",
            "c) `frozenset({1,2,3,4})`",
            "d) `(1,2,3,4)`"
        ],
        "answer": "a) `{1,2,3,4}` *(Result is a regular set)*",
        "explanation": "When performing operations between a frozenset and a regular set, the result is a regular set. The operation succeeds because frozensets support all set operations. The result contains all elements from both sets."
    },
    {
        "question": "761. Why are sets ideal for membership testing?",
        "options": [
            "a) They maintain order",
            "b) They use hashing for O(1) lookups",
            "c) They can contain any data type",
            "d) They automatically sort elements"
        ],
        "answer": "b) They use hashing for O(1) lookups",
        "explanation": "Sets use hash tables internally, which allows for average O(1) time complexity for membership tests (`in` operator). This is much faster than lists or tuples which require O(n) time for membership testing."
    },
    {
        "question": "762. What is a Python module?",
        "options": [
            "a) A special Python keyword",
            "b) A file containing Python definitions and statements",
            "c) A type of Python loop",
            "d) A Python data structure"
        ],
        "answer": "b) A file containing Python definitions and statements",
        "explanation": "A module in Python is simply a .py file containing Python code (definitions and statements). Modules allow you to organize related code into separate files, making your programs more manageable and reusable."
    },
    {
        "question": "763. Which extension do Python module files have?",
        "options": [
            "a) .pt",
            "b) .py",
            "c) .mod",
            "d) .pym"
        ],
        "answer": "b) .py",
        "explanation": "Python module files use the .py extension. This is the standard file extension for Python source code files. When you import a module, Python looks for files with this extension in the search path."
    },
    {
        "question": "764. What is the correct way to import a module named 'math'?",
        "options": [
            "a) `include math`",
            "b) `import math`",
            "c) `require math`",
            "d) `using math`"
        ],
        "answer": "b) `import math`",
        "explanation": "The correct syntax to import a module in Python is `import module_name`. After importing, you can access the module's contents using dot notation, like `math.sqrt(4)`. The other options show syntax from other languages."
    },
    {
        "question": "765. How can you import only the sqrt function from the math module?",
        "options": [
            "a) `import sqrt from math`",
            "b) `from math import sqrt`",
            "c) `import math.sqrt`",
            "d) `math.import(sqrt)`"
        ],
        "answer": "b) `from math import sqrt`",
        "explanation": "The `from module import name` syntax allows you to import specific names from a module directly into your current namespace. After this import, you can use `sqrt()` directly without the `math.` prefix."
    },
    {
        "question": "766. What is the purpose of the `__init__.py` file in a directory?",
        "options": [
            "a) It makes the directory a Python package",
            "b) It initializes Python on your system",
            "c) It contains documentation for the module",
            "d) It's required for all Python scripts"
        ],
        "answer": "a) It makes the directory a Python package",
        "explanation": "The `__init__.py` file (even if empty) signals to Python that the directory should be treated as a package. This allows you to import modules from the directory. In Python 3.3+, it's not strictly required for implicit namespace packages, but it's still good practice."
    },
    {
        "question": "767. Which of these is NOT a standard Python built-in module?",
        "options": [
            "a) math",
            "b) random",
            "c) pandas",
            "d) os"
        ],
        "answer": "c) pandas *(It's a third-party module)*",
        "explanation": "pandas is a popular third-party module for data analysis, not part of Python's standard library. The math, random, and os modules are all part of Python's standard library and come with Python installations."
    },
    {
        "question": "768. What does `if __name__ == \"__main__\":` do in a Python script?",
        "options": [
            "a) Makes the script run faster",
            "b) Ensures code only runs when the script is executed directly",
            "c) Imports all required modules",
            "d) Creates a new module"
        ],
        "answer": "b) Ensures code only runs when the script is executed directly",
        "explanation": "This idiom checks if the script is being run directly (not imported as a module). Code under this block will only execute when the script is run directly, allowing the file to be both imported as a module and run as a script."
    },
    {
        "question": "769. How can you see all names defined in a module?",
        "options": [
            "a) `help(module)`",
            "b) `module.list()`",
            "c) `dir(module)`",
            "d) `module.names()`"
        ],
        "answer": "c) `dir(module)`",
        "explanation": "The built-in `dir()` function returns a list of names in the current local scope or, when given a module object, returns an alphabetized list of names defined in that module. This includes functions, classes, and variables."
    },
    {
        "question": "770. What is a Python package?",
        "options": [
            "a) A collection of related modules",
            "b) A compressed Python file",
            "c) A Python installation file",
            "d) A type of Python dictionary"
        ],
        "answer": "a) A collection of related modules",
        "explanation": "A Python package is a way of organizing related modules into a directory hierarchy. Packages can contain modules and subpackages, and are typically identified by the presence of an `__init__.py` file in the directory."
    },
    {
        "question": "771. How do you install third-party Python packages?",
        "options": [
            "a) `python get package_name`",
            "b) `pip install package_name`",
            "c) `import package_name`",
            "d) `download package_name`"
        ],
        "answer": "b) `pip install package_name`",
        "explanation": "pip is Python's package installer. The command `pip install package_name` downloads and installs the specified package from the Python Package Index (PyPI). `import` is for using already installed packages, not installing them."
    },
    {
        "question": "772. What is the purpose of the PYTHONPATH environment variable?",
        "options": [
            "a) It stores the path to Python executable",
            "b) It specifies where Python looks for modules to import",
            "c) It contains Python documentation",
            "d) It sets the default Python version"
        ],
        "answer": "b) It specifies where Python looks for modules to import",
        "explanation": "PYTHONPATH is an environment variable that adds additional directories to Python's module search path. When you import a module, Python looks in these directories (after built-ins but before default install locations)."
    },
    {
        "question": "773. Which function would you use to read the documentation of a module?",
        "options": [
            "a) `info()`",
            "b) `help()`",
            "c) `doc()`",
            "d) `describe()`"
        ],
        "answer": "b) `help()`",
        "explanation": "The built-in `help()` function launches Python's interactive help system. When called with a module name (e.g., `help(math)`), it displays documentation about that module's contents."
    },
    {
        "question": "774. What happens if you try to import a non-existent module?",
        "options": [
            "a) Python creates an empty module",
            "b) Raises ImportError",
            "c) Returns None",
            "d) Silently continues execution"
        ],
        "answer": "b) Raises ImportError",
        "explanation": "When Python can't find the module you're trying to import, it raises an ImportError. This helps catch typos or missing dependencies early. You can catch this exception to handle missing modules gracefully."
    },
    {
        "question": "775. How can you reload an already imported module?",
        "options": [
            "a) `reload(module)`",
            "b) `import module again`",
            "c) `from importlib import reload` then `reload(module)`",
            "d) You can't reload modules"
        ],
        "answer": "c) `from importlib import reload` then `reload(module)`",
        "explanation": "In Python 3, you need to use `importlib.reload()` to reload a previously imported module. This is useful during development when you've changed a module and want to test the changes without restarting Python."
    },
    {
        "question": "776. What is the correct way to use an alias when importing a module?",
        "options": [
            "a) `import math as m`",
            "b) `import math -> m`",
            "c) `alias math m`",
            "d) `math = import m`"
        ],
        "answer": "a) `import math as m`",
        "explanation": "The `as` keyword creates an alias for the imported module. After `import math as m`, you can use `m` instead of `math` (e.g., `m.sqrt(4)`). This is commonly used with modules that have long names (like `numpy as np`)."
    },
    {
        "question": "777. What is the purpose of exception handling in Python?",
        "options": [
            "a) To make code run faster",
            "b) To handle errors gracefully and prevent program crashes",
            "c) To create custom data types",
            "d) To skip certain code blocks"
        ],
        "answer": "b) To handle errors gracefully and prevent program crashes",
        "explanation": "Exception handling allows programs to deal with unexpected situations (like file not found or invalid input) without crashing. It separates normal program logic from error handling, making code more robust and maintainable."
    },
    {
        "question": "778. Which keyword is used to test a block of code for errors?",
        "options": [
            "a) `catch`",
            "b) `try`",
            "c) `error`",
            "d) `check`"
        ],
        "answer": "b) `try`",
        "explanation": "The `try` block contains code that might raise exceptions. It must be followed by one or more `except` blocks to handle potential exceptions. This is Python's primary mechanism for catching and handling runtime errors."
    },
    {
        "question": "779. What happens if an exception occurs in the `try` block?",
        "options": [
            "a) The program crashes immediately",
            "b) Execution jumps to the matching `except` block",
            "c) The `else` block executes",
            "d) The `finally` block executes immediately"
        ],
        "answer": "b) Execution jumps to the matching `except` block",
        "explanation": "When an exception occurs in a `try` block, Python looks for a matching `except` block to handle it. If found, execution continues there. If no matching `except` is found, the exception propagates up the call stack."
    },
    {
        "question": "780. Which block is executed if no exceptions occur in the `try` block?",
        "options": [
            "a) `except`",
            "b) `else`",
            "c) `finally`",
            "d) `catch`"
        ],
        "answer": "b) `else`",
        "explanation": "The `else` block in a try-except structure executes only if no exceptions were raised in the `try` block. It's useful for code that should run only when the `try` block succeeds, keeping it separate from the `try` block itself."
    },
    {
        "question": "781. Which block is always executed regardless of whether an exception occurs?",
        "options": [
            "a) `try`",
            "b) `except`",
            "c) `else`",
            "d) `finally`"
        ],
        "answer": "d) `finally`",
        "explanation": "The `finally` block executes whether an exception occurred or not. It's typically used for cleanup actions (like closing files or releasing resources) that should always happen, regardless of success or failure."
    },
    {
        "question": "782. How do you catch a specific exception type?",
        "options": [
            "a) `except Error:`",
            "b) `except Exception:`",
            "c) `except ValueError:`",
            "d) All of the above"
        ],
        "answer": "c) `except ValueError:`",
        "explanation": "You can catch specific exceptions by naming them after `except`. This allows different handling for different error types. Catching specific exceptions is better practice than catching all exceptions (`except Exception:`), as it prevents accidentally masking unexpected errors."
    },
    {
        "question": "783. What is the output of this code?\n```python\ntry:\n    print(10/0)\nexcept ZeroDivisionError:\n    print(\"A\")\nexcept:\n    print(\"B\")\nelse:\n    print(\"C\")\nfinally:\n    print(\"D\")\n```",
        "options": [
            "a) A D",
            "b) B D",
            "c) A C D",
            "d) A B C D"
        ],
        "answer": "a) A D",
        "explanation": "The code raises a ZeroDivisionError, which is caught by the first except block (printing 'A'). The bare except block doesn't run because the exception was already caught. The else block doesn't run because an exception occurred. The finally block always runs (printing 'D')."
    },
    {
        "question": "784. How do you raise a custom exception?",
        "options": [
            "a) `throw CustomError()`",
            "b) `raise CustomError()`",
            "c) `exception CustomError()`",
            "d) `error CustomError()`"
        ],
        "answer": "b) `raise CustomError()`",
        "explanation": "In Python, the `raise` statement is used to trigger exceptions. To raise a custom exception, you would typically define a class that inherits from Exception and then use `raise CustomError()`. This differs from languages like Java that use 'throw'."
    },
    {
        "question": "785. What is the purpose of the `as` keyword in exception handling?",
        "options": [
            "a) To create an alias for the exception",
            "b) To assign the exception to a variable",
            "c) To compare exceptions",
            "d) To ignore the exception"
        ],
        "answer": "b) To assign the exception to a variable",
        "explanation": "The `as` keyword in an except clause assigns the exception object to a variable, allowing you to access its attributes and methods. For example: `except ValueError as e:` lets you examine `e` (like printing `str(e)` to see the error message)."
    },
    {
        "question": "786. Which exception is raised when converting invalid input to a number?",
        "options": [
            "a) `TypeError`",
            "b) `ValueError`",
            "c) `ConversionError`",
            "d) `InputError`"
        ],
        "answer": "b) `ValueError`",
        "explanation": "`ValueError` is raised when a function receives an argument of the correct type but inappropriate value. For example, `int('abc')` raises ValueError because 'abc' is a string (correct type) but can't be converted to an integer (invalid value)."
    },
    {
        "question": "787. How do you create a custom exception class?",
        "options": [
            "a) `class MyError(Exception):`",
            "b) `exception MyError:`",
            "c) `def MyError(Exception):`",
            "d) `new Exception MyError:`"
        ],
        "answer": "a) `class MyError(Exception):`",
        "explanation": "Custom exceptions are created by defining new classes that inherit from Python's base Exception class or one of its subclasses. Typically, the class body is kept simple, often just with a docstring explaining the error."
    },
    {
        "question": "788. What does `NoReturn` from the typing module indicate?",
        "options": [
            "a) The function returns None",
            "b) The function never returns normally",
            "c) The function returns any type",
            "d) The function returns an exception"
        ],
        "answer": "b) The function never returns normally",
        "explanation": "`NoReturn` is a special type annotation indicating a function never returns normally - it either always raises an exception or enters an infinite loop. This is different from returning None, which is a normal return with the value None."
    },
    {
        "question": "789. Which is NOT a good practice for exception handling?",
        "options": [
            "a) Catching specific exceptions",
            "b) Using bare `except:` statements",
            "c) Providing informative error messages",
            "d) Cleaning up resources in `finally`"
        ],
        "answer": "b) Using bare `except:` statements",
        "explanation": "Bare except clauses (without specifying an exception type) catch all exceptions, including system-exiting ones like KeyboardInterrupt. This can mask important errors and make debugging difficult. Always catch specific exceptions when possible."
    },
    {
        "question": "790. What happens if an exception occurs in the `finally` block?",
        "options": [
            "a) It overrides the original exception",
            "b) It's added to the original exception",
            "c) The program crashes immediately",
            "d) It's ignored"
        ],
        "answer": "a) It overrides the original exception",
        "explanation": "If an exception occurs in a finally block, it takes precedence over any exception that might have occurred in the try or except blocks. This means the original exception is lost, which can make debugging difficult - so finally blocks should be kept simple."
    },
    {
        "question": "791. How do you catch multiple exceptions in one block?",
        "options": [
            "a) `except (TypeError, ValueError):`",
            "b) `except TypeError or ValueError:`",
            "c) `catch [TypeError, ValueError]:`",
            "d) `except TypeError, ValueError:`"
        ],
        "answer": "a) `except (TypeError, ValueError):`",
        "explanation": "To catch multiple exception types with the same handler, put them in a tuple after the except keyword. This is cleaner than separate except blocks when the handling is identical. The old syntax (option d) was removed in Python 3."
    },
    {
        "question": "792. When should you use `try-except` for file operations?",
        "options": [
            "a) When the file might not exist",
            "b) When you lack read permissions",
            "c) When the file format is invalid",
            "d) All of the above"
        ],
        "answer": "d) All of the above",
        "explanation": "File operations can fail for many reasons - missing files (FileNotFoundError), permission issues (PermissionError), invalid operations (IOError), etc. Using try-except makes your program robust against these issues. Even format validation can raise exceptions during conversion."
    },
    {
        "question": "793. What is the purpose of `else` in exception handling?",
        "options": [
            "a) To handle the exception",
            "b) To run code when no exception occurs",
            "c) To clean up resources",
            "d) To raise new exceptions"
        ],
        "answer": "b) To run code when no exception occurs",
        "explanation": "The `else` block in try-except executes only if the try block completes without raising any exceptions. It's useful for separating the code that might raise exceptions from code that should only run when no exceptions occur, making the logic clearer."
    },
    {
        "question": "794. Which is equivalent to Java's `throw` in Python?",
        "options": [
            "a) `throws`",
            "b) `raise`",
            "c) `except`",
            "d) `error`"
        ],
        "answer": "b) `raise`",
        "explanation": "Python uses `raise` to trigger exceptions, which is equivalent to Java's `throw`. The syntax is different but the concept is the same - both are used to signal that an exceptional condition has occurred."
    },
    {
        "question": "795. What does this code do?\n```python\ntry:\n    risky_operation()\nexcept Exception as e:\n    log_error(e)\n    raise\n```",
        "options": [
            "a) Logs and ignores the error",
            "b) Logs and re-raises the same error",
            "c) Logs and raises a new error",
            "d) Logs and returns None"
        ],
        "answer": "b) Logs and re-raises the same error",
        "explanation": "The bare `raise` statement inside an except block re-raises the current exception. This pattern is useful when you need to perform some action (like logging) but still want the exception to propagate up the call stack for higher-level handling."
    },
    {
        "question": "796. Why is exception handling important for user input?",
        "options": [
            "a) To make the program faster",
            "b) To handle invalid input gracefully",
            "c) To skip validation",
            "d) To hide errors from users"
        ],
        "answer": "b) To handle invalid input gracefully",
        "explanation": "User input is inherently unpredictable. Exception handling allows programs to validate input and provide helpful feedback when input is invalid, rather than crashing. This improves user experience and makes programs more robust."
    },
    {
        "question": "797. Which function is used to open a file in Python?",
        "options": [
            "a) `file_open()`",
            "b) `open_file()`",
            "c) `open()`",
            "d) `file()`"
        ],
        "answer": "c) `open()`",
        "explanation": "The built-in `open()` function is used to open files in Python. It returns a file object and takes parameters for the filename and mode (like 'r' for read, 'w' for write). It's the standard way to work with files in Python."
    },
    {
        "question": "798. What is the default mode when opening a file?",
        "options": [
            "a) `'w'` (write)",
            "b) `'a'` (append)",
            "c) `'r'` (read)",
            "d) `'x'` (exclusive)"
        ],
        "answer": "c) `'r'` (read)",
        "explanation": "If no mode is specified when calling `open()`, Python defaults to `'r'` (read mode). This opens the file for reading text (in text mode), and raises an error if the file doesn't exist."
    },
    {
        "question": "799. Which mode would you use to write to a file without overwriting existing content?",
        "options": [
            "a) `'w'`",
            "b) `'r+'`",
            "c) `'a'`",
            "d) `'x'`"
        ],
        "answer": "c) `'a'` (append)",
        "explanation": "Append mode (`'a'`) opens the file for writing, but new content is added to the end of the file rather than overwriting existing content. `'w'` would truncate the file, while `'r+'` allows both reading and writing from the start."
    },
    {
        "question": "800. What happens if you open a non-existent file in 'r' mode?",
        "options": [
            "a) The file is created",
            "b) An empty file is created",
            "c) A `FileNotFoundError` occurs",
            "d) The program crashes silently"
        ],
        "answer": "c) A `FileNotFoundError` occurs",
        "explanation": "In read mode (`'r'`), Python expects the file to exist. If it doesn't, a FileNotFoundError is raised. This differs from write (`'w'`) or append (`'a'`) modes, which create the file if it doesn't exist."
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
        This quiz contains 50 questions about Python string methods (Questions 751-800).
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
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(self.questions)} (Q{750 + st.session_state.current_question})")
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
            with st.expander(f"Question {751 + i}: {answer['question']}"):
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