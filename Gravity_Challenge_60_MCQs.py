import streamlit as st

st.set_page_config(page_title="Gravity Challenge", page_icon="🚀")

st.title("🚀 Gravity Challenge Quiz")
st.write("Answer all 60 MCQs. Your results will appear at the end.")

QUESTIONS = [{'number': 1,
  'section': 'AI Fluency',
  'question': 'A student asks AI to brainstorm ideas for a project, then works with AI to improve '
              'the ideas, and finally allows an AI agent to independently organize research tasks. '
              'Which sequence correctly describes these three uses?',
  'options': {'A': 'Augmentation → Automation → Agency',
              'B': 'Automation → Augmentation → Agency',
              'C': 'Agency → Automation → Augmentation',
              'D': 'Automation → Agency → Traditional prompting'},
  'answer': 'B'},
 {'number': 2,
  'section': 'AI Fluency',
  'question': 'A manager defines the task, explains the expected result, checks the quality of the '
              'output, and takes responsibility for its use. Which AI Fluency framework does this '
              'represent?',
  'options': {'A': 'Delegation, Description, Discernment, Diligence',
              'B': 'Design, Development, Delivery, Deployment',
              'C': 'Data, Decision, Direction, Documentation',
              'D': 'Delegation, Development, Discovery, Distribution'},
  'answer': 'A'},
 {'number': 3,
  'section': 'AI Fluency',
  'question': 'An AI assistant produces a polished report but includes statistics that cannot be '
              'found in the supplied documents. What should the reviewer do first?',
  'options': {'A': 'Accept the report because it looks professional',
              'B': 'Check the statistics against the original sources',
              'C': 'Ask AI to make the report more persuasive',
              'D': 'Remove the references and publish it'},
  'answer': 'B'},
 {'number': 4,
  'section': 'AI Fluency',
  'question': 'A teacher uses AI to create lesson materials but wants to ensure students still '
              'develop independent thinking. Which approach is best?',
  'options': {'A': 'Allow AI to complete all student assignments',
              'B': 'Use AI to support explanations while students demonstrate their own '
                   'understanding',
              'C': 'Replace classroom discussions with AI-generated summaries',
              'D': "Let AI decide each student's final academic grade"},
  'answer': 'B'},
 {'number': 5,
  'section': 'AI Fluency',
  'question': 'An employee spends 30 minutes correcting an AI output that would have taken 15 '
              'minutes to create manually. Which evaluation is most relevant?',
  'options': {'A': 'Product quality',
              'B': 'Process effectiveness',
              'C': 'Platform popularity',
              'D': 'Model creativity'},
  'answer': 'B'},
 {'number': 6,
  'section': 'AI Fluency',
  'question': 'An AI assistant provides a correct answer but reaches it using an incorrect '
              'assumption. What should the reviewer examine?',
  'options': {'A': 'Only the final answer',
              'B': 'The justification, assumptions, and evidence',
              'C': 'The formatting and writing style',
              'D': 'The number of paragraphs'},
  'answer': 'B'},
 {'number': 7,
  'section': 'AI Fluency',
  'question': 'A company wants AI to perform repetitive calculations while employees retain '
              'responsibility for interpreting the results. Which approach is most appropriate?',
  'options': {'A': 'Agency',
              'B': 'Automation',
              'C': 'Independent decision-making',
              'D': 'Unrestricted delegation'},
  'answer': 'B'},
 {'number': 8,
  'section': 'AI Fluency',
  'question': 'An AI assistant gives confident answers even when the available information is '
              'incomplete. Which skill helps identify this problem?',
  'options': {'A': 'Discernment', 'B': 'Automation', 'C': 'Distribution', 'D': 'Formatting'},
  'answer': 'A'},
 {'number': 9,
  'section': 'AI Fluency',
  'question': 'A team wants to use AI for a task affecting many customers. What should happen '
              'before deployment?',
  'options': {'A': 'Publish the AI output immediately',
              'B': 'Check risks, data, approval, and disclosure requirements',
              'C': 'Remove human review to improve speed',
              'D': 'Give the AI unrestricted authority'},
  'answer': 'B'},
 {'number': 10,
  'section': 'AI Fluency',
  'question': 'A user receives a weak first response from AI. What is the best next step?',
  'options': {'A': 'Abandon the task immediately',
              'B': 'Explain what is missing and refine the direction',
              'C': 'Accept the response without checking',
              'D': 'Change to an unrelated task'},
  'answer': 'B'},
 {'number': 11,
  'section': 'AI Fluency',
  'question': 'A company evaluates an AI tutor. Every answer is factually correct, but students '
              'are learning less than before. Which evaluation has been neglected?',
  'options': {'A': 'Product evaluation',
              'B': 'Performance evaluation',
              'C': 'Formatting evaluation',
              'D': 'Data storage evaluation'},
  'answer': 'B'},
 {'number': 12,
  'section': 'AI Fluency',
  'question': 'An employee uses AI to create a document and then checks whether it is accurate, '
              'appropriate, and safe to publish. Which principle is demonstrated?',
  'options': {'A': 'Diligence', 'B': 'Automation', 'C': 'Delegation', 'D': 'Platform awareness'},
  'answer': 'A'},
 {'number': 13,
  'section': 'Delegation & Prompting',
  'question': 'A manager asks AI to compare two vendor proposals but provides no evaluation '
              'criteria. What is the main weakness?',
  'options': {'A': 'The AI may choose irrelevant criteria',
              'B': 'The AI cannot read documents',
              'C': 'The AI must always refuse comparisons',
              'D': 'The task requires no context'},
  'answer': 'A'},
 {'number': 14,
  'section': 'Delegation & Prompting',
  'question': 'A manager wants AI to prepare a comparison report. Which instruction provides the '
              'strongest delegation brief?',
  'options': {'A': 'Compare these vendors and choose the best one',
              'B': 'Review the proposals using my criteria, cite supporting sections, flag missing '
                   'information, and prepare a comparison table for my review',
              'C': 'Write a persuasive report supporting Vendor A',
              'D': 'Make a decision using whichever factors seem important'},
  'answer': 'B'},
 {'number': 15,
  'section': 'Delegation & Prompting',
  'question': 'An AI assistant is asked to send a customer email. The user only wants a draft, not '
              'an actual message sent. Which constraint should be included?',
  'options': {'A': 'Send the email automatically',
              'B': 'Draft the email only; do not send it',
              'C': 'Choose the recipient independently',
              'D': 'Delete the original customer message'},
  'answer': 'B'},
 {'number': 16,
  'section': 'Delegation & Prompting',
  'question': 'A user gives AI a broad goal but no audience, format, or constraints. What is the '
              'most likely result?',
  'options': {'A': 'A perfectly tailored response',
              'B': 'An output based on assumptions',
              'C': 'A guaranteed factual report',
              'D': 'An automatically approved decision'},
  'answer': 'B'},
 {'number': 17,
  'section': 'Delegation & Prompting',
  'question': 'A project owner delegates research to an AI agent. Which activity must remain with '
              'the human owner?',
  'options': {'A': 'Defining the expected outcome',
              'B': 'Checking important findings',
              'C': 'Accepting responsibility for the final decision',
              'D': 'All of the above'},
  'answer': 'D'},
 {'number': 18,
  'section': 'Delegation & Prompting',
  'question': 'An employee asks AI to create a financial report and says, “Use any numbers you '
              'need.” What is the biggest risk?',
  'options': {'A': 'The report may be too short',
              'B': 'The AI may invent or assume figures',
              'C': 'The report may use too many headings',
              'D': 'The report may take less time'},
  'answer': 'B'},
 {'number': 19,
  'section': 'Delegation & Prompting',
  'question': 'A user wants AI to summarize a document without adding outside information. Which '
              'instruction is strongest?',
  'options': {'A': 'Make the summary more interesting using your knowledge',
              'B': 'Use only the attached document and identify anything it does not state',
              'C': 'Add relevant facts from the internet',
              'D': 'Fill missing details with reasonable assumptions'},
  'answer': 'B'},
 {'number': 20,
  'section': 'Delegation & Prompting',
  'question': 'An AI agent is asked to book a meeting, but the user has not authorized it to send '
              'invitations. What should the agent do?',
  'options': {'A': 'Send invitations anyway',
              'B': 'Prepare the proposed meeting details for approval',
              'C': 'Choose attendees independently',
              'D': 'Cancel all existing meetings'},
  'answer': 'B'},
 {'number': 21,
  'section': 'Delegation & Prompting',
  'question': 'A user receives an incomplete first draft. Which response best follows the '
              'refinement loop?',
  'options': {'A': 'Reject the entire task',
              'B': 'Identify the missing parts and give specific revision instructions',
              'C': 'Ask the AI to repeat the same response',
              'D': 'Publish the draft immediately'},
  'answer': 'B'},
 {'number': 22,
  'section': 'Delegation & Prompting',
  'question': 'A manager wants AI to analyze customer feedback. Which deliverable is easiest to '
              'verify?',
  'options': {'A': 'A general statement that customers are unhappy',
              'B': 'A table showing themes, supporting comments, and limitations',
              'C': 'A confident recommendation without evidence',
              'D': 'A report containing only AI opinions'},
  'answer': 'B'},
 {'number': 23,
  'section': 'Delegation & Prompting',
  'question': 'A user delegates a task but does not specify what the AI is allowed to decide '
              'independently. Which part of the delegation brief is missing?',
  'options': {'A': 'Context', 'B': 'Authority', 'C': 'Deliverable', 'D': 'Outcome'},
  'answer': 'B'},
 {'number': 24,
  'section': 'Delegation & Prompting',
  'question': 'An AI assistant prepares a report that meets the requested format but contains '
              'unsupported conclusions. What should happen before acceptance?',
  'options': {'A': 'Check the evidence and revise the conclusions',
              'B': 'Accept it because the format is correct',
              'C': 'Remove all supporting documents',
              'D': 'Forward it without review'},
  'answer': 'A'},
 {'number': 25,
  'section': 'Workflow Design & Diagnosis',
  'question': 'A company wants to automate a process involving customer applications. Some '
              'applications contain missing information and others require special approval. What '
              'is the safest design?',
  'options': {'A': 'Automatically approve every application',
              'B': 'Separate standard cases from exceptions requiring human review',
              'C': 'Reject every incomplete application without explanation',
              'D': 'Let AI invent missing information'},
  'answer': 'B'},
 {'number': 26,
  'section': 'Workflow Design & Diagnosis',
  'question': 'An AI system repeatedly makes errors because the source spreadsheet contains '
              'inconsistent records. What should the team address first?',
  'options': {'A': 'The spreadsheet and input quality',
              'B': "The report's font size",
              'C': "The AI's response length",
              'D': 'The dashboard colour scheme'},
  'answer': 'A'},
 {'number': 27,
  'section': 'Workflow Design & Diagnosis',
  'question': 'A team wants to improve an inefficient workflow using AI. What should it identify '
              'first?',
  'options': {'A': 'The most expensive AI model',
              'B': 'The actual problem, current process, and desired outcome',
              'C': 'The number of AI tools available',
              'D': 'The colour of the user interface'},
  'answer': 'B'},
 {'number': 28,
  'section': 'Workflow Design & Diagnosis',
  'question': 'An AI assistant creates a report and then automatically sends it to external '
              'customers. What is the main design concern?',
  'options': {'A': 'The report may contain too many pages',
              'B': 'There is no approval gate before an external action',
              'C': 'The assistant uses a computer',
              'D': 'The workflow contains multiple steps'},
  'answer': 'B'},
 {'number': 29,
  'section': 'Workflow Design & Diagnosis',
  'question': 'A workflow works correctly for normal applications but fails when an application '
              'contains unusual information. What improvement is most appropriate?',
  'options': {'A': 'Remove all exception checks',
              'B': 'Define exception-handling rules and escalation paths',
              'C': 'Allow the AI to make every decision',
              'D': 'Ignore unusual applications'},
  'answer': 'B'},
 {'number': 30,
  'section': 'Workflow Design & Diagnosis',
  'question': 'A manager wants to measure whether an AI workflow is successful. Which measure is '
              'strongest?',
  'options': {'A': 'Number of prompts entered',
              'B': 'Accuracy, time saved, error rate, and impact on users',
              'C': 'Number of AI tools installed',
              'D': 'Length of the generated report'},
  'answer': 'B'},
 {'number': 31,
  'section': 'Workflow Design & Diagnosis',
  'question': 'An AI assistant is asked to process records but sometimes skips entries. What '
              'should the team introduce?',
  'options': {'A': 'A verification step that checks the processed records against the original '
                   'list',
              'B': 'A more colourful report',
              'C': 'A longer welcome message',
              'D': 'An instruction to work faster'},
  'answer': 'A'},
 {'number': 32,
  'section': 'Workflow Design & Diagnosis',
  'question': 'A workflow includes several repetitive steps, but one step involves approving '
              'sensitive requests. What is the best design?',
  'options': {'A': 'Automate every step without restrictions',
              'B': 'Automate repetitive work and retain human approval for sensitive decisions',
              'C': 'Remove the approval step',
              'D': 'Allow the AI to approve requests based on confidence'},
  'answer': 'B'},
 {'number': 33,
  'section': 'Workflow Design & Diagnosis',
  'question': 'A team changes its AI model but continues using the same workflow without testing '
              'it. What is the main problem?',
  'options': {'A': 'Model changes may affect workflow performance',
              'B': 'Models always produce identical results',
              'C': 'Testing is unnecessary after deployment',
              'D': 'Workflow rules cannot be changed'},
  'answer': 'A'},
 {'number': 34,
  'section': 'Workflow Design & Diagnosis',
  'question': 'An AI system performs a task successfully in a small trial but produces '
              'inconsistent results at larger scale. What should the team examine?',
  'options': {'A': 'Performance across different cases and users',
              'B': 'Only the first successful result',
              'C': "The system's logo",
              'D': 'The number of people in the office'},
  'answer': 'A'},
 {'number': 35,
  'section': 'Workflow Design & Diagnosis',
  'question': 'A workflow saves time but increases the number of incorrect customer records. How '
              'should the team respond?',
  'options': {'A': 'Keep it because speed improved',
              'B': 'Reassess the workflow using both efficiency and accuracy',
              'C': 'Hide the errors from management',
              'D': 'Increase automation without investigation'},
  'answer': 'B'},
 {'number': 36,
  'section': 'Workflow Design & Diagnosis',
  'question': 'A manager discovers that an AI workflow has no named owner. What should happen?',
  'options': {'A': 'Continue using it without changes',
              'B': 'Assign an accountable owner before relying on it',
              'C': 'Allow the AI to become its own owner',
              'D': 'Remove all monitoring'},
  'answer': 'B'},
 {'number': 37,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'An employee uploads a confidential company document to an AI tool because the tool '
              'says it does not train on user data. What must the employee check?',
  'options': {'A': 'Whether the tool has a dark mode',
              'B': 'Whether the data route is approved for that information',
              'C': 'Whether the document is short',
              'D': 'Whether the AI can summarize quickly'},
  'answer': 'B'},
 {'number': 38,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'A user replaces customer names with identification codes but keeps the code-mapping '
              'key. How should this data be described?',
  'options': {'A': 'Fully anonymous',
              'B': 'Pseudonymised',
              'C': 'Public information',
              'D': 'Automatically safe to share'},
  'answer': 'B'},
 {'number': 39,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'An AI assistant recommends rejecting a customer application. The employee says, “A '
              'human will review it later.” What is the strongest safeguard?',
  'options': {'A': 'Review after the decision has already been sent',
              'B': 'Define who reviews what and when, before the decision becomes final',
              'C': 'Allow the AI to send the rejection automatically',
              'D': 'Remove the review process'},
  'answer': 'B'},
 {'number': 40,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'A company uses an AI-generated ranking system to shortlist applicants. What '
              'fairness check is important?',
  'options': {'A': 'Check who is included and excluded and whether the criteria are fair',
              'B': 'Check only the total number of applicants',
              'C': 'Use the ranking without review',
              'D': 'Hide the ranking criteria'},
  'answer': 'A'},
 {'number': 41,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'A connected AI tool reads a document containing hidden instructions to reveal '
              'private information. What is the main risk?',
  'options': {'A': 'Prompt injection through untrusted content',
              'B': 'Slow internet speed',
              'C': 'Incorrect document formatting',
              'D': 'Low screen resolution'},
  'answer': 'A'},
 {'number': 42,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'An employee accidentally shares confidential information with an unapproved AI '
              'service. What should happen first?',
  'options': {'A': 'Delete the conversation to hide the mistake',
              'B': 'Stop further sharing and follow the incident reporting process',
              'C': 'Continue using the service',
              'D': 'Ignore the incident'},
  'answer': 'B'},
 {'number': 43,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'A team approved an AI workflow last year. Since then, the model, data, and audience '
              'have changed. What should the team do?',
  'options': {'A': 'Assume the old approval still applies',
              'B': 'Reassess the workflow because important conditions changed',
              'C': 'Remove all documentation',
              'D': "Increase the system's permissions"},
  'answer': 'B'},
 {'number': 44,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'A manager says that using incognito mode makes uploading confidential data safe. '
              'What is the correct response?',
  'options': {'A': 'Incognito mode guarantees data protection',
              'B': 'Incognito mode does not replace an approved data route',
              'C': 'Incognito mode removes all privacy risks',
              'D': 'Incognito mode automatically anonymizes documents'},
  'answer': 'B'},
 {'number': 45,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'A company uses AI to prepare reports that affect employees. Which people should be '
              'considered in the risk assessment?',
  'options': {'A': 'Only the employees who operate the AI',
              'B': 'Everyone potentially affected, including people who never see the report',
              'C': 'Only senior management',
              'D': 'Only the AI development team'},
  'answer': 'B'},
 {'number': 46,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'A manager discovers that an AI tool has access to more company data than its task '
              'requires. What is the best control?',
  'options': {'A': 'Keep all access because it may be useful later',
              'B': 'Limit access to the smallest necessary scope',
              'C': 'Give the tool administrator permissions',
              'D': 'Disable all security checks'},
  'answer': 'B'},
 {'number': 47,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'A report contains a possible policy violation identified by AI. What should the '
              'employee do?',
  'options': {'A': 'Let AI issue the final punishment',
              'B': 'Escalate the finding to the appropriate human reviewer',
              'C': 'Remove the finding from the report',
              'D': 'Automatically close the case'},
  'answer': 'B'},
 {'number': 48,
  'section': 'Governance, Risk & Responsible Use',
  'question': 'A company wants to document the risks of an AI workflow. Which record is most '
              'complete?',
  'options': {'A': 'Only the name of the AI tool',
              'B': 'Data, capability, affected people, evidence, owner, and residual risk',
              'C': 'Only the date the workflow started',
              'D': 'Only the number of users'},
  'answer': 'B'},
 {'number': 49,
  'section': 'Skills & Connectors',
  'question': 'A team installs a shared AI skill created by another department. What should it do '
              'before enabling it?',
  'options': {'A': 'Trust it because it was created internally',
              'B': 'Review its source, reach, fit, outside content, and actions',
              'C': 'Give it full access immediately',
              'D': 'Assume it cannot affect connected tools'},
  'answer': 'B'},
 {'number': 50,
  'section': 'Skills & Connectors',
  'question': 'An employee connects a cloud drive to an AI assistant and expects it to understand '
              "the company's reporting format. What is the misunderstanding?",
  'options': {'A': 'A connector provides access, not necessarily instructions or methods',
              'B': 'A connector automatically creates a reporting policy',
              'C': 'A connector replaces all skills',
              'D': 'A connector guarantees correct formatting'},
  'answer': 'A'},
 {'number': 51,
  'section': 'Skills & Connectors',
  'question': 'A skill never activates even when the employee expects it to. What should the '
              'employee inspect first?',
  'options': {'A': "The skill's description and trigger wording",
              'B': "The computer's wallpaper",
              'C': 'The size of the monitor',
              'D': "The employee's typing speed"},
  'answer': 'A'},
 {'number': 52,
  'section': 'Skills & Connectors',
  'question': 'An AI skill contains hidden instructions that could send data to an outside '
              'service. What is the best response?',
  'options': {'A': 'Enable it because it is only a text file',
              'B': 'Inspect the skill and its instructions before enabling it',
              'C': 'Give it access to every connected service',
              'D': 'Ignore the instructions'},
  'answer': 'B'},
 {'number': 53,
  'section': 'Skills & Connectors',
  'question': 'A connector has permission to edit and delete company files, although the task only '
              'requires reading them. What should the administrator do?',
  'options': {'A': 'Keep all permissions enabled',
              'B': 'Start with read-only access and the smallest necessary scope',
              'C': 'Give it more permissions',
              'D': 'Disable all monitoring'},
  'answer': 'B'},
 {'number': 54,
  'section': 'Skills & Connectors',
  'question': 'An AI assistant used to follow a skill correctly, but performance becomes worse as '
              'the conversation grows longer. What is a reasonable diagnostic step?',
  'options': {'A': 'Start a fresh conversation',
              'B': 'Immediately delete the skill',
              'C': 'Grant additional permissions',
              'D': 'Replace every instruction with a shorter one'},
  'answer': 'A'},
 {'number': 55,
  'section': 'Skills & Connectors',
  'question': 'A skill repeatedly produces the same error because a precise calculation step is '
              'unreliable. What is the best improvement?',
  'options': {'A': 'Keep rephrasing the same instruction forever',
              'B': 'Move the exact calculation into a reliable script',
              'C': 'Remove the calculation',
              'D': 'Allow the AI to guess the result'},
  'answer': 'B'},
 {'number': 56,
  'section': 'Skills & Connectors',
  'question': 'A user wants to move an AI skill between different platforms. Which statement is '
              'most accurate?',
  'options': {'A': 'Every platform supports identical setup and behaviour',
              'B': 'The skill file may travel, but platform setup can differ',
              'C': 'All custom assistants transfer automatically',
              'D': 'Connectors and skills are always interchangeable'},
  'answer': 'B'},
 {'number': 57,
  'section': 'Skills & Connectors',
  'question': 'A team connects an AI assistant to a document repository. What should it verify?',
  'options': {'A': 'Whether the assistant can access the required documents and only the permitted '
                   'scope',
              'B': 'Whether the repository has attractive icons',
              'C': 'Whether all files are public',
              'D': 'Whether the assistant can delete documents'},
  'answer': 'A'},
 {'number': 58,
  'section': 'Skills & Connectors',
  'question': 'An AI skill is useful but can take actions through connected tools. What should the '
              'team evaluate?',
  'options': {'A': 'Only how well the skill is written',
              'B': 'Its source, reach, suitability, external content, and possible actions',
              'C': 'Only the number of lines in its file',
              'D': 'Only its creation date'},
  'answer': 'B'},
 {'number': 59,
  'section': 'Skills & Connectors',
  'question': 'A user wants an AI assistant to access files but not change them. Which permission '
              'is most appropriate?',
  'options': {'A': 'Full administrator access',
              'B': 'Read-only access',
              'C': 'Read and delete access',
              'D': 'Unrestricted write access'},
  'answer': 'B'},
 {'number': 60,
  'section': 'Skills & Connectors',
  'question': 'A company wants to introduce an AI skill and connector into a sensitive workflow. '
              'Which approach is strongest?',
  'options': {'A': 'Enable both immediately and test after deployment',
              'B': 'Review the skill, limit connector permissions, test the workflow, and monitor '
                   'its actions',
              'C': 'Trust internal tools without checking them',
              'D': 'Give the AI full authority to reduce human involvement'},
  'answer': 'B'}]

if "current" not in st.session_state:
    st.session_state.current = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "submitted" not in st.session_state:
    st.session_state.submitted = False

total = len(QUESTIONS)
q = QUESTIONS[st.session_state.current]

if not st.session_state.submitted:

    st.progress((st.session_state.current + 1) / total)

    st.subheader(
        f"Question {st.session_state.current + 1} of {total}"
    )

    st.markdown(f"### {q['question']}")

    options = q["options"]

    selected = st.radio(
        "Choose your answer:",
        list(options.keys()),
        format_func=lambda x: f"{x}. {options[x]}",
        index=(
            list(options.keys()).index(
                st.session_state.answers[st.session_state.current]
            )
            if st.session_state.current in st.session_state.answers
            else None
        ),
        key=f"question_{st.session_state.current}"
    )

    if selected:
        st.session_state.answers[st.session_state.current] = selected

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Previous", disabled=st.session_state.current == 0):
            st.session_state.current -= 1
            st.rerun()

    with col2:
        if st.session_state.current < total - 1:
            if st.button("Next ➡"):
                st.session_state.current += 1
                st.rerun()
        else:
            if st.button("Submit Quiz ✅"):
                if len(st.session_state.answers) == total:
                    st.session_state.submitted = True
                    st.rerun()
                else:
                    st.warning("Please answer all questions first.")

else:
    score = 0

    for i, question in enumerate(QUESTIONS):
        if st.session_state.answers.get(i) == question["answer"]:
            score += 1

    percentage = (score / total) * 100

    st.success("Quiz Completed!")

    st.metric("Your Score", f"{score}/{total}")
    st.metric("Percentage", f"{percentage:.2f}%")

    if percentage >= 80:
        st.balloons()
        st.success("Excellent work! 🚀")
    elif percentage >= 50:
        st.info("Good effort! Keep practising.")
    else:
        st.warning("Keep learning and try again!")

    st.header("📋 Answer Review")

    for i, question in enumerate(QUESTIONS):
        user_answer = st.session_state.answers.get(i)
        correct_answer = question["answer"]

        st.markdown(f"### Question {i + 1}")
        st.write(question["question"])

        if user_answer == correct_answer:
            st.success(f"Correct: {correct_answer}")
        else:
            st.error(f"Your answer: {user_answer}")
            st.success(f"Correct answer: {correct_answer}")

        st.divider()

    if st.button("🔄 Restart Quiz"):
        st.session_state.current = 0
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.rerun()