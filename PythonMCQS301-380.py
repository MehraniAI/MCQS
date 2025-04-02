import streamlit as st
import random
import time

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
            # Questions 301-310
            {
                "question": "301. Who developed Python Programming Language?",
                "options": ["a) Wick van Rossum", "b) Rasmus Lerdorf", "c) Guido van Rossum", "d) Niene Stom"],
                "answer": "c",
                "explanation": "Python was designed by Guido van Rossum."
            },
            {
                "question": "302. Which type of Programming does Python support?",
                "options": ["a) object-oriented programming", "b) structured programming", "c) functional programming", "d) all of the mentioned"],
                "answer": "d",
                "explanation": "Python supports OOP, structured, and functional programming."
            },
            {
                "question": "303. Is Python case sensitive when dealing with identifiers?",
                "options": ["a) no", "b) yes", "c) machine dependent", "d) none of the mentioned"],
                "answer": "b",
                "explanation": "Case is always significant in Python identifiers."
            },
            {
                "question": "304. Which of the following is the correct extension of the Python file?",
                "options": ["a) .python", "b) .pl", "c) .py", "d) .p"],
                "answer": "c",
                "explanation": "Python files use .py extension."
            },
            {
                "question": "305. Is Python code compiled or interpreted?",
                "options": ["a) Python code is both compiled and interpreted", "b) Python code is neither compiled nor interpreted", "c) Python code is only compiled", "d) Python code is only interpreted"],
                "answer": "a",
                "explanation": "Python is first compiled to bytecode which is then interpreted."
            },
            {
                "question": "306. All keywords in Python are in _________",
                "options": ["a) Capitalized", "b) lower case", "c) UPPER CASE", "d) None of the mentioned"],
                "answer": "d",
                "explanation": "Only True, False and None are capitalized."
            },
            {
                "question": "307. What will be the value of the following Python expression? 4 + 3 % 5",
                "options": ["a) 7", "b) 2", "c) 4", "d) 1"],
                "answer": "a",
                "explanation": "% has higher precedence than +, so 3%5=3, then 4+3=7."
            },
            {
                "question": "308. Which of the following is used to define a block of code in Python language?",
                "options": ["a) Indentation", "b) Key", "c) Brackets", "d) All of the mentioned"],
                "answer": "a",
                "explanation": "Python uses indentation to define code blocks."
            },
            {
                "question": "309. Which keyword is used for function in Python language?",
                "options": ["a) Function", "b) def", "c) Fun", "d) Define"],
                "answer": "b",
                "explanation": "The 'def' keyword is used to define functions."
            },
            {
                "question": "310. Which character is used for single-line comments in Python?",
                "options": ["a) //", "b) #", "c) !", "d) /*"],
                "answer": "b",
                "explanation": "Python uses # for single-line comments."
            },
            
            # Questions 311-320
            {
                "question": "311. What will be the output of: i=1\nwhile True:\n    if i%3==0:break\n    print(i)\n    i+=1",
                "options": ["a) 1 2 3", "b) error", "c) 1 2", "d) none"],
                "answer": "b",
                "explanation": "There's a syntax error due to space in +=."
            },
            {
                "question": "312. Which function helps find the Python version?",
                "options": ["a) sys.version(1)", "b) sys.version(0)", "c) sys.version()", "d) sys.version"],
                "answer": "d",
                "explanation": "sys.version gives the Python version."
            },
            {
                "question": "313. Python's anonymous functions are called?",
                "options": ["a) pi", "b) anonymous", "c) lambda", "d) none"],
                "answer": "c",
                "explanation": "Lambda functions are anonymous."
            },
            {
                "question": "314. What is Python's order of precedence?",
                "options": ["a) Exponential, Parentheses, Mul, Div, Add, Sub", 
                           "b) Exponential, Parentheses, Div, Mul, Add, Sub",
                           "c) Parentheses, Exponential, Mul, Add, Div, Sub",
                           "d) Parentheses, Exponential, Mul, Div, Add, Sub"],
                "answer": "d",
                "explanation": "Remember PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction."
            },
            {
                "question": "315. What is the output of x=1; x<<2?",
                "options": ["a) 4", "b) 2", "c) 1", "d) 8"],
                "answer": "a",
                "explanation": "Bitwise left shift by 2 multiplies by 4."
            },
            {
                "question": "316. What does pip stand for?",
                "options": ["a) Pip Installs Python", "b) Pip Installs Packages", "c) Preferred Installer Program", "d) All"],
                "answer": "c",
                "explanation": "pip is the Preferred Installer Program."
            },
            {
                "question": "317. What's true about Python variable names?",
                "options": ["a) Only _ and & allowed", "b) Unlimited length", "c) Private need __", "d) None"],
                "answer": "b",
                "explanation": "Variable names can be any length."
            },
            {
                "question": "318. What are the values of: 2**(3**2), (2**3)**2, 2**3**2?",
                "options": ["a) 512, 64, 512", "b) 512, 512, 512", "c) 64, 512, 64", "d) 64, 64, 64"],
                "answer": "a",
                "explanation": "** is right-associative."
            },
            {
                "question": "319. Which is truncation division operator?",
                "options": ["a) |", "b) //", "c) /", "d) %"],
                "answer": "b",
                "explanation": "// does floor division."
            },
            {
                "question": "320. What does filter(bool, [1,0,2,0,'hello','',[]]) return?",
                "options": ["a) [1,0,2,'hello','',[]]", "b) Error", "c) [1,2,'hello']", "d) [1,0,2,0,'hello','',[]]"],
                "answer": "c",
                "explanation": "filter keeps only truthy values."
            },
            
            # Questions 321-330
            {
                "question": "321. Which is a built-in function?",
                "options": ["a) factorial()", "b) print()", "c) seed()", "d) sqrt()"],
                "answer": "b",
                "explanation": "print() is built-in, others need imports."
            },
            {
                "question": "322. What does id() do?",
                "options": ["a) Checks if object has id", "b) Returns object identity", "c) All", "d) None"],
                "answer": "b",
                "explanation": "id() returns object's memory address."
            },
            {
                "question": "323. How many parameters can the shown decorator handle?",
                "options": ["a) Any number", "b) 0", "c) 1", "d) 2"],
                "answer": "a",
                "explanation": "Decorator uses *args and **kwargs."
            },
            {
                "question": "324. What is min(max(False,-3,-4), 2,7)?",
                "options": ["a) -4", "b) -3", "c) 2", "d) False"],
                "answer": "d",
                "explanation": "max returns 0 (False), min is 0."
            },
            {
                "question": "325. Which is not a core Python data type?",
                "options": ["a) Tuples", "b) Lists", "c) Class", "d) Dictionary"],
                "answer": "c",
                "explanation": "Class is user-defined."
            },
            {
                "question": "326. What does print(\"%.2f\"%56.236) output?",
                "options": ["a) 56.236", "b) 56.23", "c) 56.0000", "d) 56.24"],
                "answer": "d",
                "explanation": "Rounds to 2 decimal places."
            },
            {
                "question": "327. What are Python packages?",
                "options": ["a) Set of main modules", "b) Folder of modules", "c) Files with Python code", "d) Programs using modules"],
                "answer": "b",
                "explanation": "Packages are folders with modules."
            },
            {
                "question": "328. What is len([\"hello\",2,4,6])?",
                "options": ["a) Error", "b) 6", "c) 4", "d) 3"],
                "answer": "c",
                "explanation": "Counts the 4 elements."
            },
            {
                "question": "329. What prints when looping over 'abcd' with upper()?",
                "options": ["a) a\nB\nC\nD", "b) a b c d", "c) error", "d) A\nB\nC\nD"],
                "answer": "d",
                "explanation": "Prints each character uppercased."
            },
            {
                "question": "330. Python's namespace search order is?",
                "options": ["a) Built-in → Global → Local", "b) Built-in → Local → Global", 
                           "c) Local → Global → Built-in", "d) Global → Local → Built-in"],
                "answer": "c",
                "explanation": "LEGB rule: Local, Enclosing, Global, Built-in."
            },
            
            # Questions 331-340
            {
                "question": "331. What prints for [1,2,3,4][::-1]?",
                "options": ["a) 4 3 2 1", "b) error", "c) 1 2 3 4", "d) none"],
                "answer": "a",
                "explanation": "[::-1] reverses the list."
            },
            {
                "question": "332. What is \"a\"+\"bc\"?",
                "options": ["a) bc", "b) abc", "c) a", "d) bca"],
                "answer": "b",
                "explanation": "String concatenation."
            },
            {
                "question": "333. Which function is called by format()?",
                "options": ["a) str()", "b) format()", "c) __str__()", "d) __format__()"],
                "answer": "c",
                "explanation": "format() calls __str__() by default."
            },
            {
                "question": "334. Which is not a Python keyword?",
                "options": ["a) pass", "b) eval", "c) assert", "d) nonlocal"],
                "answer": "b",
                "explanation": "eval is a built-in function."
            },
            {
                "question": "335. What prints for temp.id in the shown class?",
                "options": ["a) 12", "b) 224", "c) None", "d) Error"],
                "answer": "a",
                "explanation": "Instance attribute remains 12."
            },
            {
                "question": "336. What is the output of the shown list modification?",
                "options": ["a) Error", "b) None", "c) False", "d) True"],
                "answer": "d",
                "explanation": "Same object modified, same id."
            },
            {
                "question": "337. Which module parses command line options?",
                "options": ["a) getarg", "b) getopt", "c) main", "d) os"],
                "answer": "b",
                "explanation": "getopt handles command line args."
            },
            {
                "question": "338. What is the final set after z operations?",
                "options": ["a) {'a','c','p','q','s','n'}", "b) {'abc','p','q','san'}", 
                           "c) {'a','b','c','p','q','san'}", "d) {'a','b','c',['p','q'],'san}"],
                "answer": "c",
                "explanation": "Sets contain unique elements."
            },
            {
                "question": "339. Which arithmetic operator can't be used with strings?",
                "options": ["a) *", "b) -", "c) +", "d) All"],
                "answer": "b",
                "explanation": "Subtraction isn't defined for strings."
            },
            {
                "question": "340. What does \"abc. DEF\".capitalize() return?",
                "options": ["a) Abc. def", "b) abc. def", "c) Abc. Def", "d) ABC. DEF"],
                "answer": "a",
                "explanation": "First letter uppercase, rest lowercase."
            },
            
            # Questions 341-350
            {
                "question": "341. How to create an empty set?",
                "options": ["a) ()", "b) []", "c) {}", "d) set()"],
                "answer": "d",
                "explanation": "{} makes dict, set() makes set."
            },
            {
                "question": "342. What is the value of 'result' after list operations?",
                "options": ["a) [1,3,5,7,8]", "b) [1,7,8]", "c) [1,2,4,7,8]", "d) error"],
                "answer": "a",
                "explanation": "Contains elements unique to each list."
            },
            {
                "question": "343. How to add element to list?",
                "options": ["a) list1.addEnd(5)", "b) list1.addLast(5)", "c) list1.append(5)", "d) list1.add(5)"],
                "answer": "c",
                "explanation": "append() adds to end of list."
            },
            {
                "question": "344. What prints with center(6)?",
                "options": ["a) *  abcde *", "b) *abcde *", "c) * abcde*", "d) * abcde  *"],
                "answer": "b",
                "explanation": "Right-padded when even length."
            },
            {
                "question": "345. What prints after list modification?",
                "options": ["a) [1,4]", "b) [1,3,4]", "c) [4,3]", "d) [1,3]"],
                "answer": "c",
                "explanation": "Both variables reference same list."
            },
            {
                "question": "346. What's true about functions?",
                "options": ["a) No modularity", "b) Can't create custom", "c) Reusable code", "d) All"],
                "answer": "c",
                "explanation": "Functions allow code reuse."
            },
            {
                "question": "347. How to get value 6 from matrix A?",
                "options": ["a) A[2][1]", "b) A[1][2]", "c) A[3][2]", "d) A[2][3]"],
                "answer": "b",
                "explanation": "Row 1 (2nd), Column 2 (3rd)."
            },
            {
                "question": "348. Maximum identifier length?",
                "options": ["a) 79", "b) 31", "c) 63", "d) None"],
                "answer": "d",
                "explanation": "No fixed limit."
            },
            {
                "question": "349. What prints in the while-else loop?",
                "options": ["a) error", "b) 0 1 2 0", "c) 0 1 2", "d) none"],
                "answer": "c",
                "explanation": "Else doesn't run after break."
            },
            {
                "question": "350. What prints when looping over 'abcd' indices?",
                "options": ["a) error", "b) 1 2 3 4", "c) a b c d", "d) 0 1 2 3"],
                "answer": "d",
                "explanation": "range(len(x)) gives indices 0-3."
            },
            
            # Questions 351-360
            {
                "question": "351. Python function types are?",
                "options": ["a) System/Custom", "b) Built-in/User-defined", "c) Internal/External", "d) User/System"],
                "answer": "b",
                "explanation": "Built-in and user-defined functions."
            },
            {
                "question": "352. What is len(mylist) after addItem?",
                "options": ["a) 5", "b) 8", "c) 2", "d) 1"],
                "answer": "a",
                "explanation": "Appends 1, making length 5."
            },
            {
                "question": "353. Which is a tuple?",
                "options": ["a) {1,2,3}", "b) {}", "c) [1,2,3]", "d) (1,2,3)"],
                "answer": "d",
                "explanation": "Tuples use parentheses."
            },
            {
                "question": "354. What is 'a' in z where z=set('abc$de')?",
                "options": ["a) Error", "b) True", "c) False", "d) No output"],
                "answer": "b",
                "explanation": "'a' is in the set."
            },
            {
                "question": "355. What is round(4.576)?",
                "options": ["a) 4", "b) 4.6", "c) 5", "d) 4.5"],
                "answer": "c",
                "explanation": "Rounds to nearest integer."
            },
            {
                "question": "356. What's true about docstrings?",
                "options": ["a) Required", "b) Access via __doc__", "c) Documents code", "d) All"],
                "answer": "d",
                "explanation": "All statements are correct."
            },
            {
                "question": "357. What prints with format and tuple?",
                "options": ["a) Hello ('foo','bin')", "b) Error", "c) Hello foo and bin", "d) None"],
                "answer": "c",
                "explanation": "Accesses tuple elements by index."
            },
            {
                "question": "358. What is print(math.pow(3,2))?",
                "options": ["a) 9.0", "b) None", "c) 9", "d) None"],
                "answer": "a",
                "explanation": "math.pow() returns float."
            },
            {
                "question": "359. What does id() return?",
                "options": ["a) Checks id", "b) Object identity", "c) None", "d) All"],
                "answer": "b",
                "explanation": "Returns unique object identifier."
            },
            {
                "question": "360. What prints with map/str/join?",
                "options": ["a) 01", "b) [0] [1]", "c) ('01')", "d) ('[0] [1]',)"],
                "answer": "d",
                "explanation": "Creates a tuple with one string element."
            },
            
            # Questions 361-370 (Cloud Computing)
            {
                "question": "361. Which cloud model is outside corporate firewall?",
                "options": ["A. Public", "B. Private", "C. Hybrid", "D. Industry"],
                "answer": "a",
                "explanation": "Public cloud is externally hosted."
            },
            {
                "question": "362. Desktop cloud for employees is?",
                "options": ["A. Public", "B. Private", "C. Government", "D. Hybrid"],
                "answer": "b",
                "explanation": "Private cloud is for internal use."
            },
            {
                "question": "363. What refers to cloud infrastructure location?",
                "options": ["A. Service", "B. Deployment", "C. Application", "D. None"],
                "answer": "b",
                "explanation": "Deployment model refers to location."
            },
            {
                "question": "364. What's true about on-demand self-service?",
                "options": ["A. No provider contact needed", "B. Users request resources", 
                           "C. Providers just prepare", "D. Users solve all problems"],
                "answer": "b",
                "explanation": "Users can provision resources themselves."
            },
            {
                "question": "365. Incorrect statement about cloud and IoT?",
                "options": ["A. Cloud needed for IoT data", "B. Cloud enables IoT", 
                           "C. Cloud provides IoT storage", "D. Without cloud IoT inefficient"],
                "answer": "a",
                "explanation": "IoT can work without cloud (edge computing)."
            },
            {
                "question": "366. Which is not an AI element?",
                "options": ["A. Big data", "B. Cognitive analysis", "C. Computing power", "D. Scenario"],
                "answer": "b",
                "explanation": "Cognitive analysis is an application, not element."
            },
            {
                "question": "367. Correct cloud architecture order?",
                "options": ["A. Infra → Mgmt → Pool → Service", 
                           "B. Infra → Service → Mgmt → Pool",
                           "C. Infra → Pool → Mgmt → Service",
                           "D. Pool → Infra → Mgmt → Service"],
                "answer": "c",
                "explanation": "Bottom-up: Infrastructure → Resource Pool → Management → Services."
            },
            {
                "question": "368. How cloud affects CAPEX/OPEX?",
                "options": ["A. Shifts CAPEX to OPEX", "B. Shifts OPEX to CAPEX", 
                           "C. Increases CAPEX", "D. None"],
                "answer": "a",
                "explanation": "Cloud converts capital expenses to operational."
            },
            {
                "question": "369. Which is not a compute service?",
                "options": ["A. ECS", "B. BMS", "C. OBS", "D. IMS"],
                "answer": "c",
                "explanation": "OBS is object storage, not compute."
            },
            {
                "question": "370. Which leases basic resources?",
                "options": ["A. IaaS", "B. PaaS", "C. SaaS", "D. DaaS"],
                "answer": "a",
                "explanation": "IaaS provides fundamental resources."
            },
            
            # Questions 371-380
            {
                "question": "371. What to consider before cloud adoption?",
                "options": ["A. Cost", "B. Data sensitivity", "C. Migration difficulty", "D. All"],
                "answer": "d",
                "explanation": "All factors are important."
            },
            {
                "question": "372. Cloud 1.0 era features?",
                "options": ["A. Agile dev", "B. Virtualization products", 
                           "C. Automated services", "D. Resource utilization"],
                "answer": "b",
                "explanation": "Early cloud focused on virtualization."
            },
            {
                "question": "373. What's true about broad network access?",
                "options": ["A. Multiple devices", "B. Anytime access", 
                           "C. Status monitoring", "D. All"],
                "answer": "d",
                "explanation": "All describe broad network access."
            },
            {
                "question": "374. Will edge computing replace cloud?",
                "options": ["A. True", "B. False"],
                "answer": "b",
                "explanation": "They complement each other."
            },
            {
                "question": "375. Can containers package software?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Containers standardize deployment."
            },
            {
                "question": "376. Are cloud-native apps cloud-based?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Designed specifically for cloud."
            },
            {
                "question": "377. Is hybrid cloud a mix of public/private?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Combines both deployment models."
            },
            {
                "question": "378. Are KVM and Xen virtualization solutions?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Both are open-source hypervisors."
            },
            {
                "question": "379. Is cloud computing network-dependent?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Requires network connectivity."
            },
            {
                "question": "380. Can users transparently use cloud resources?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Users don't need to know implementation details."
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
        This quiz contains 80 questions about Python programming and cloud computing (Questions 301-380).
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