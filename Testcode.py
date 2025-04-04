import streamlit as st

st.markdown('<h1 style="color:blue">Prepared by Devan Das Mehrani AI Student</h1>', unsafe_allow_html=True)

st.title("Python Quiz (451-500)")
st.write("Select a question range from the tabs below:")

# Define all questions organized by range
questions = {
    "451-460": [
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
        }
    ],
    "460-470": [
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
        }
    ],
    "470-480": [
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
        }
    ],
    "480-490": [
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
        }
    ],
    "490-500": [
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
}

# Create tabs for each question range
tabs = st.tabs(list(questions.keys()))

for tab, (range_name, q_list) in zip(tabs, questions.items()):
    with tab:
        st.header(f"Questions {range_name}")
        for i, q in enumerate(q_list, 1):
            with st.expander(f"Question {int(range_name[:3]) + i - 1}"):
                st.write(q["question"])
                if "```python" in q["question"]:
                    st.code(q["question"].split("```python")[1].split("```")[0], language="python")
                
                selected = st.radio(
                    "Select an option:",
                    q["options"],
                    key=f"{range_name}_{i}"
                )
                
                if st.button("Check Answer", key=f"btn_{range_name}_{i}"):
                    if any(selected.startswith(ans[:1]) for ans in q["answer"].split(" and ")):
                        st.success("Correct!")
                    else:
                        st.error("Incorrect!")
                    st.write(f"**Answer:** {q['answer']}")
                    st.write(f"**Explanation:** {q['explanation']}")
