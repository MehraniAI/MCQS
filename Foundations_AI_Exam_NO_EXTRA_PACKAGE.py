# PANAVERSITY CERTIFIED ASSOCIATE FOUNDATIONS
# Futuristic AI-themed, 10-section / 200-question examination simulator
# Install: python -m pip install streamlit
# The timer has a built-in fallback; streamlit-autorefresh is optional.
# Run:     streamlit run Foundations_AI_Exam.py

import time
import streamlit as st

def st_autorefresh(interval=1000, limit=None, key=None):
        time.sleep(interval / 1000)
        st.rerun()


st.set_page_config(
    page_title="Panaversity AI Examination",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SECTIONS = [
  {
    "title": "Just Delegate It",
    "questions": [
      {
        "question": "(Cross-platform) A finance manager hands AI a quarterly budget variance report to summarise. Which first step best follows the delegation habit?",
        "options": {
          "A": "Write a short brief naming the job, the audience and the format, then check the result against the report.",
          "B": "Paste the report with the word \"summarise\" and accept whatever comes back.",
          "C": "Let the AI decide who the audience is and how long the summary should be.",
          "D": "Skip the brief because the report is short."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A financial analyst repeats the same job eleven times, adding one more line to the written brief each time. What is the purpose?",
        "options": {
          "A": "To make the prompt longer so the AI works harder.",
          "B": "To test whether the AI gets bored of repeating a task.",
          "C": "To avoid ever having to read the output.",
          "D": "To see which added line actually improves the result."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A company doctor asks AI to draft a staff wellness reminder. What must happen before it is sent?",
        "options": {
          "A": "Nothing, because AI drafts are always medically safe.",
          "B": "The administrator formats it and sends it without reading.",
          "C": "The doctor checks every health statement against approved clinical guidance.",
          "D": "The AI is asked once whether it is sure."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) What is a Delegation Record?",
        "options": {
          "A": "A log of how many hours the AI tool was used.",
          "B": "A one-page record of the job, the brief, what was checked and what was accepted or rejected.",
          "C": "A legal contract signed with the AI vendor.",
          "D": "A list of employees who are not allowed to use AI."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) An HR administrator delegates meeting minutes to AI. Which brief is strongest?",
        "options": {
          "A": "Purpose, audience, length, tone and the exact notes to be used.",
          "B": "\"Write good minutes.\"",
          "C": "The meeting date only.",
          "D": "A request to sound professional, nothing else."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A manager finds a figure in an AI draft that does not appear in the source file. What should the manager do?",
        "options": {
          "A": "Keep it, because AI numbers are usually close enough.",
          "B": "Delete the whole draft and stop using AI.",
          "C": "Ask the AI to confirm it and trust the confirmation.",
          "D": "Trace the figure to the source, correct it and note the issue before using the draft."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which task is the best first candidate to delegate to AI?",
        "options": {
          "A": "A decision about a colleague's salary.",
          "B": "A job you do not understand well enough to judge.",
          "C": "A low-risk, repeatable job of your own, such as a weekly status email.",
          "D": "A task involving a client's private records."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A budget officer's brief gets a generic answer. What is the most useful fix?",
        "options": {
          "A": "Repeat the same brief in capital letters.",
          "B": "Add what a good result looks like, such as format, length and an example.",
          "C": "Switch tools until one gives a better answer by chance.",
          "D": "Remove all details so the AI has freedom."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) An administrator delegates scheduling emails to AI. Who is answerable for the emails once they are sent?",
        "options": {
          "A": "The administrator who delegated and sent them.",
          "B": "The AI vendor.",
          "C": "The AI tool itself.",
          "D": "No one, because AI wrote them."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) How should a financial analyst check an AI summary of a spreadsheet?",
        "options": {
          "A": "Ask the AI to rate its own accuracy.",
          "B": "Check only the first sentence.",
          "C": "Judge it by how confident it sounds.",
          "D": "Compare its key numbers and claims with the original data."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Why does the course ask you to delegate a job of your own?",
        "options": {
          "A": "Because AI cannot work on other people's jobs.",
          "B": "Because it is cheaper than delegating a colleague's job.",
          "C": "Because you know the work well enough to judge whether the result is right.",
          "D": "Because your own jobs are always easy."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A procurement manager sees a polished vendor comparison from AI. What is the correct response?",
        "options": {
          "A": "Accept it, since polished work is usually correct.",
          "B": "Check it before accepting, however good it looks.",
          "C": "Send it to the vendor for approval.",
          "D": "Accept it if it is longer than one page."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What does a written brief let a team lead do that a casual chat does not?",
        "options": {
          "A": "Repeat the job, hand it to others and see where it went wrong.",
          "B": "Avoid having to review any output.",
          "C": "Guarantee that the AI never errs.",
          "D": "Make the AI remember the team permanently."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) After AI returns a result, what is the next habit in the course?",
        "options": {
          "A": "Forward it immediately to save time.",
          "B": "Ask the AI for a longer version.",
          "C": "Store it without reading.",
          "D": "Check it against what you asked for and against the source."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which of these does NOT belong in a good brief?",
        "options": {
          "A": "The job to be done.",
          "B": "The intended audience.",
          "C": "A promise that you will accept the first answer.",
          "D": "The required format."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A company doctor gets different answers each time the same job is run. What helps most?",
        "options": {
          "A": "Run it ten times and pick the longest answer.",
          "B": "Tighten the brief with clearer constraints and an example.",
          "C": "Remove the example from the brief.",
          "D": "Assume the first answer is always right."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) When should a financial analyst stop adding lines to the brief?",
        "options": {
          "A": "When the result meets the success criteria and passes the checks.",
          "B": "When the brief reaches a fixed word count.",
          "C": "When the AI says it is finished.",
          "D": "Never; briefs must always keep growing."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A manager rejects an AI draft. What is the best note for the Delegation Record?",
        "options": {
          "A": "Only that the AI was bad.",
          "B": "Nothing, since rejected work is not recorded.",
          "C": "The name of the tool in capital letters.",
          "D": "What was wrong and which brief line would prevent it next time."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A budget meeting is tomorrow. An administrator is tempted to skip checking the AI-prepared handout. What does the course say?",
        "options": {
          "A": "Skip it, because deadlines excuse checking.",
          "B": "Ask a colleague to check only the title.",
          "C": "Check it anyway; the habit applies most when time is short.",
          "D": "Print it and check later."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A procurement officer delegated a vendor shortlist to AI. Who signs off on the final shortlist?",
        "options": {
          "A": "The AI, because it prepared it.",
          "B": "The officer, after checking the work.",
          "C": "The vendor being shortlisted.",
          "D": "Whoever opens the file first."
        },
        "answer": "B"
      }
    ]
  },
  {
    "title": "What AI Actually Is",
    "questions": [
      {
        "question": "(Cross-platform) A manager asks why an AI tool gave a confident but wrong answer. What is the best explanation?",
        "options": {
          "A": "It looked the fact up and the database was broken.",
          "B": "It generates likely-sounding text and can produce fluent errors.",
          "C": "It deliberately lied to the manager.",
          "D": "It was tired after many requests."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What does a language model do at its core?",
        "options": {
          "A": "Predicts the next piece of text based on patterns learned in training.",
          "B": "Stores a copy of every web page and retrieves it.",
          "C": "Thinks and feels like a human colleague.",
          "D": "Runs a spreadsheet engine behind the chat."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A financial analyst asks for a market figure from last week and the AI gives an outdated number. Why can this happen?",
        "options": {
          "A": "AI deletes new data automatically.",
          "B": "The analyst's account is blocked.",
          "C": "Numbers are never stored in AI.",
          "D": "Models have a training cutoff and may lack recent data unless they search."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) What is a hallucination in AI?",
        "options": {
          "A": "A screen glitch while the tool loads.",
          "B": "An image the user uploaded.",
          "C": "A confident output that is invented or false.",
          "D": "A hidden setting for creativity."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A company doctor notices the AI invented a medical reference. What does this show?",
        "options": {
          "A": "AI references are always real if formatted properly.",
          "B": "Citations and facts must be verified because AI can fabricate them.",
          "C": "The reference was probably correct but old.",
          "D": "Doctors should never read AI outputs."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Why do surprises from AI stop looking like magic or malfunction once you know how it works?",
        "options": {
          "A": "Because they follow from a pattern-predicting machine, not a mind or a bug.",
          "B": "Because the surprises are always errors in the code.",
          "C": "Because the AI is reading your mind.",
          "D": "Because the vendor manually edits each answer."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) What is a context window?",
        "options": {
          "A": "The browser window the chat opens in.",
          "B": "The time the tool stays logged in.",
          "C": "A list of the user's saved files.",
          "D": "The amount of text the model can consider at once in a conversation."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) An administrator pastes a 300-page file and the AI misses an early detail. What is a likely cause?",
        "options": {
          "A": "The AI refuses to read page one.",
          "B": "PDF files are unreadable by every AI.",
          "C": "The input may exceed or strain the context the model can handle well.",
          "D": "The detail was too important to include."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A manager says, \"The AI understands our company like an employee.\" What is the most accurate correction?",
        "options": {
          "A": "It has worked in the company for years.",
          "B": "It only knows what it was trained on and what you give it in the chat.",
          "C": "It keeps a private file on every employee.",
          "D": "It automatically reads internal servers."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Why can the same question get different answers on different runs?",
        "options": {
          "A": "Output is generated with some randomness, so wording and details can vary.",
          "B": "The AI changes its mind to annoy users.",
          "C": "The server stores a different answer per day.",
          "D": "Only the first answer is ever real."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A financial analyst wants an exact calculation of a large budget. What is the safer approach?",
        "options": {
          "A": "Trust mental arithmetic from the chat text.",
          "B": "Round all numbers before asking.",
          "C": "Ask the AI three times and average the guesses.",
          "D": "Have AI run the code or calculator and verify the result."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) What is training data?",
        "options": {
          "A": "The messages typed by one user in one session.",
          "B": "A manual written by the vendor's lawyers.",
          "C": "The large body of text and other material a model learned patterns from.",
          "D": "The model's password list."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A doctor asks whether AI \"knows\" a patient's condition. What is true?",
        "options": {
          "A": "It has access to every hospital record.",
          "B": "It has no knowledge of the patient beyond what is typed into the chat.",
          "C": "It diagnoses with certainty.",
          "D": "It remembers all patients from earlier chats forever."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which statement about AI tools is correct?",
        "options": {
          "A": "They can be very useful drafters, yet they still need human checking.",
          "B": "They are always right when the answer is long.",
          "C": "They are always wrong on factual topics.",
          "D": "They never need clear instructions."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A manager sees the AI apologise and change its answer when challenged, though the first answer was right. What does this suggest?",
        "options": {
          "A": "The first answer was definitely wrong.",
          "B": "The AI has become more accurate.",
          "C": "Challenging an AI always improves it.",
          "D": "AI can bend to pressure, so users should verify instead of relying on agreement."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) What is the difference between a chat assistant and a search engine?",
        "options": {
          "A": "There is no difference.",
          "B": "A search engine writes drafts; a chat assistant lists websites.",
          "C": "A chat assistant generates new text; a search engine finds existing pages.",
          "D": "A chat assistant only works offline."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) Why can an AI sound confident even when it is unsure?",
        "options": {
          "A": "Confidence means it checked three sources.",
          "B": "Fluent wording is a feature of how text is generated, not proof of accuracy.",
          "C": "It is programmed to be right.",
          "D": "It measures certainty out loud."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) A finance team lead wants current exchange rates inside an AI chat. What helps?",
        "options": {
          "A": "Use a tool with search or a connected data source and verify the source.",
          "B": "Assume the model memorised today's rates.",
          "C": "Guess and ask the AI to agree.",
          "D": "Avoid dates in the question."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) What does it mean that an AI model is \"general-purpose\"?",
        "options": {
          "A": "It is certified for every profession.",
          "B": "It is guaranteed correct in every field.",
          "C": "It works only for coding.",
          "D": "It can attempt many kinds of tasks, with varying reliability."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which description best fits what a manager should expect from AI?",
        "options": {
          "A": "A replacement for all human review.",
          "B": "A tool that cannot produce text.",
          "C": "A fast, fallible assistant whose work needs review.",
          "D": "A colleague who is legally accountable."
        },
        "answer": "C"
      }
    ]
  },
  {
    "title": "AI Fluency (The 4Ds)",
    "questions": [
      {
        "question": "(Cross-platform) What are the four habits in the AI Fluency framework?",
        "options": {
          "A": "Design, Debug, Deploy and Deliver.",
          "B": "Draft, Dispatch, Decide and Discard.",
          "C": "Delegation, Description, Discernment and Diligence.",
          "D": "Data, Display, Document and Distribute."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A financial analyst decides which parts of a quarterly report AI should draft and which parts she will do herself. Which D is this?",
        "options": {
          "A": "Description.",
          "B": "Delegation.",
          "C": "Discernment.",
          "D": "Diligence."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) An administrator tells AI the audience, tone and length for a staff memo. Which D is this?",
        "options": {
          "A": "Description.",
          "B": "Delegation.",
          "C": "Discernment.",
          "D": "Diligence."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A manager reads an AI draft and judges whether it is accurate, useful and appropriate. Which D is this?",
        "options": {
          "A": "Delegation.",
          "B": "Description.",
          "C": "Diligence.",
          "D": "Discernment."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A company doctor takes responsibility for an AI-assisted wellness notice and discloses the AI help where needed. Which D is this?",
        "options": {
          "A": "Description.",
          "B": "Delegation.",
          "C": "Diligence.",
          "D": "Discernment."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) Under Delegation, which task should a budget officer be most careful about handing to AI?",
        "options": {
          "A": "A first draft of a routine email.",
          "B": "A decision with serious consequences that needs human accountability.",
          "C": "A brainstorm of agenda items.",
          "D": "A reformatting of meeting notes."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which is the strongest example of good Description?",
        "options": {
          "A": "\"Write a 150-word update for finance staff, neutral tone, using the attached figures only.\"",
          "B": "\"Write something about the budget.\"",
          "C": "\"Make it good.\"",
          "D": "\"Do what you did last time.\""
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) An analyst notices an AI summary skipped a key risk in the report. Which D caught the problem?",
        "options": {
          "A": "Delegation.",
          "B": "Description.",
          "C": "None; AI never skips anything.",
          "D": "Discernment."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Who owns the final result of AI-assisted work, according to Diligence?",
        "options": {
          "A": "The AI vendor.",
          "B": "The AI model.",
          "C": "The person who uses and shares it.",
          "D": "Nobody until it is audited."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A manager forwards an AI-written report with an error, saying \"the AI wrote it.\" What is wrong with this?",
        "options": {
          "A": "Nothing; AI is accountable for its writing.",
          "B": "Ownership stays with the manager, so checking was part of the job.",
          "C": "The report should have been longer.",
          "D": "Managers should never forward reports."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which question belongs to Discernment?",
        "options": {
          "A": "Is this output accurate, relevant and fit for the purpose?",
          "B": "How can I make this prompt shorter?",
          "C": "Which tool is the cheapest?",
          "D": "How fast did the tool answer?"
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) An administrator gives AI a vague request and receives a vague draft. Which D should improve?",
        "options": {
          "A": "Diligence.",
          "B": "Delegation only.",
          "C": "Discernment only.",
          "D": "Description."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which action supports Diligence?",
        "options": {
          "A": "Hiding AI use from everyone.",
          "B": "Pasting confidential files into any tool.",
          "C": "Being transparent about AI use and protecting sensitive data.",
          "D": "Skipping review to meet a deadline."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A finance team asks AI to compare three vendors, and the AI mixes up two prices. What habit prevents harm?",
        "options": {
          "A": "Description: write a longer prompt next time.",
          "B": "Discernment: check the prices against the quotes.",
          "C": "Delegation: give the job to a second AI.",
          "D": "None; mix-ups are normal."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Why is Delegation described as the first of the four habits?",
        "options": {
          "A": "Because deciding what to hand over shapes everything that follows.",
          "B": "Because it is the easiest to forget.",
          "C": "Because tools force it first.",
          "D": "Because it costs nothing."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A doctor wants AI to draft patient education text. What is the best Delegation choice?",
        "options": {
          "A": "Let AI decide the treatment advice.",
          "B": "Skip human review to save time.",
          "C": "Use AI only for the final signature.",
          "D": "Use AI for a first draft and keep clinical judgement and approval with the doctor."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which is an example of poor Discernment?",
        "options": {
          "A": "Comparing an answer with the source document.",
          "B": "Asking for the reasoning and verifying it.",
          "C": "Accepting an AI answer because it sounds confident.",
          "D": "Checking dates and names."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A manager gives AI the budget file, the audience and a format, then reviews and signs the result. Which habits did the manager use?",
        "options": {
          "A": "Only Delegation.",
          "B": "All four: Delegation, Description, Discernment and Diligence.",
          "C": "Only Description.",
          "D": "None of them."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What does the 4Ds framework mainly help a professional decide?",
        "options": {
          "A": "Whether AI helps, and how to use it responsibly.",
          "B": "Which AI brand to buy.",
          "C": "How to avoid reading outputs.",
          "D": "How to hide AI use."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) An administrator found a policy error in an AI draft after it had been emailed. Which D should be strengthened first?",
        "options": {
          "A": "Only Description, with longer prompts.",
          "B": "Only Delegation, by never using AI again.",
          "C": "None; errors after sending are fine.",
          "D": "Discernment and Diligence: review before sending and own the outcome."
        },
        "answer": "D"
      }
    ]
  },
  {
    "title": "AI Prompting",
    "questions": [
      {
        "question": "(Cross-platform) A finance manager wants a summary of a budget report. Which prompt is best?",
        "options": {
          "A": "\"Summarise this.\"",
          "B": "\"Budget.\"",
          "C": "\"Tell me everything about money.\"",
          "D": "\"Summarise the attached Q3 budget report in five bullets for the board, flagging overspends.\""
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which element most improves a prompt for a financial analyst's forecast memo?",
        "options": {
          "A": "Adding polite greetings only.",
          "B": "Writing it entirely in capitals.",
          "C": "Stating the role, task, context, format and constraints.",
          "D": "Making it as short as possible."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A company doctor wants a clear staff health notice. What should the prompt include?",
        "options": {
          "A": "Only the word \"health\".",
          "B": "The audience, reading level, tone and the approved facts to use.",
          "C": "A request to invent statistics.",
          "D": "No context so the AI is unbiased."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Why give an AI an example of the output you want?",
        "options": {
          "A": "It shows the format and style more clearly than a description alone.",
          "B": "It makes the AI slower on purpose.",
          "C": "It replaces the need for a task.",
          "D": "It guarantees perfect accuracy."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) An administrator's first answer is close but too long. What is the best next prompt?",
        "options": {
          "A": "\"Wrong. Redo.\"",
          "B": "Start a new chat and paste nothing.",
          "C": "\"Be better.\"",
          "D": "\"Shorten this to 120 words and keep the three action items.\""
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) What does giving the AI a role, such as \"act as a payroll administrator\", mainly do?",
        "options": {
          "A": "Gives it legal authority.",
          "B": "Lets it access payroll systems.",
          "C": "Sets the perspective and vocabulary of the answer.",
          "D": "Makes the answer factually certain."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A manager needs a table of vendor costs. Which instruction is clearest?",
        "options": {
          "A": "\"Show me something visual.\"",
          "B": "\"Return a table with columns Vendor, Unit Cost and Delivery Time.\"",
          "C": "\"Put it nicely.\"",
          "D": "\"Make a list or a table, whichever.\""
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What is iterating on a prompt?",
        "options": {
          "A": "Refining the request in steps based on what came back.",
          "B": "Copying the same prompt into five tools.",
          "C": "Deleting the chat to start over each time.",
          "D": "Asking the AI to guess your intent."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A financial analyst wants the AI to use only the pasted data. Which line helps?",
        "options": {
          "A": "\"Use whatever you know.\"",
          "B": "\"Estimate anything missing.\"",
          "C": "\"Be creative with numbers.\"",
          "D": "\"Use only the figures below; if something is missing, say so.\""
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Why tell the AI what to do when information is missing?",
        "options": {
          "A": "It makes the answer longer.",
          "B": "It hides errors.",
          "C": "It reduces guessing and invented details.",
          "D": "It changes the tool's price."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A budget officer's prompt contains three unrelated tasks, and the answer is messy. What is the best fix?",
        "options": {
          "A": "Add five more tasks.",
          "B": "Split them into separate, focused prompts.",
          "C": "Remove the audience.",
          "D": "Ask the AI to pick a favourite."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which constraint is useful when drafting an email to a client?",
        "options": {
          "A": "Word limit, tone and the one action you want taken.",
          "B": "A request to be as vague as possible.",
          "C": "The AI's favourite colour.",
          "D": "A blank subject line."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A doctor wants plain language for patients. What should the prompt say?",
        "options": {
          "A": "\"Make it smart.\"",
          "B": "\"Use the hardest terms available.\"",
          "C": "\"Write like a textbook.\"",
          "D": "\"Explain at a Grade 7 reading level without medical jargon.\""
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which approach helps the AI check its own draft?",
        "options": {
          "A": "Ask it only to repeat itself.",
          "B": "Tell it that it is always right.",
          "C": "Ask it to review the answer against your criteria and list gaps.",
          "D": "Remove the criteria."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A manager's prompt gets a surprising answer. What is the best first move?",
        "options": {
          "A": "Blame the AI and quit.",
          "B": "Reread the prompt for missing context or ambiguity.",
          "C": "Delete all prior messages and give up.",
          "D": "Add more adjectives."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What is the benefit of stating the audience in a prompt?",
        "options": {
          "A": "The AI can match depth, tone and vocabulary to that reader.",
          "B": "It makes the AI remember the reader forever.",
          "C": "It prevents all errors.",
          "D": "It changes the model's training."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A finance team wants consistent monthly reports. What helps most?",
        "options": {
          "A": "Typing a new prompt from scratch each month.",
          "B": "Changing tools every month.",
          "C": "Asking for different formats each time.",
          "D": "Saving a tested prompt template and reusing it."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) An administrator pastes meeting notes and asks for action items. What detail should be added?",
        "options": {
          "A": "A request for jokes.",
          "B": "A random font name.",
          "C": "Who owns each item and the due dates.",
          "D": "Nothing, since lists are enough."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) Which is a sign of a weak prompt?",
        "options": {
          "A": "It names the format and length.",
          "B": "It leaves the goal, audience and format for the AI to guess.",
          "C": "It supplies the data to be used.",
          "D": "It states what to avoid."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Why ask the AI to explain its reasoning or sources?",
        "options": {
          "A": "It gives you something concrete to check.",
          "B": "It proves the answer is correct.",
          "C": "It removes the need to review.",
          "D": "It makes the answer private."
        },
        "answer": "A"
      }
    ]
  },
  {
    "title": "Markdown In, HTML Out",
    "questions": [
      {
        "question": "(Cross-platform) What is Markdown?",
        "options": {
          "A": "A simple plain-text way to mark headings, lists and emphasis.",
          "B": "A spreadsheet formula language.",
          "C": "A type of image file.",
          "D": "A password manager."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A manager writes a report in plain text and wants a heading. Which Markdown line creates a top-level heading?",
        "options": {
          "A": "== Quarterly Budget Report ==",
          "B": "<<Quarterly Budget Report>>",
          "C": "@@ Quarterly Budget Report",
          "D": "# Quarterly Budget Report"
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which Markdown makes a word bold?",
        "options": {
          "A": "//approved//",
          "B": "~~approved~~",
          "C": "**approved**",
          "D": "##approved##"
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) How is a bulleted list written in Markdown?",
        "options": {
          "A": "Start each line with a colon.",
          "B": "Start each line with a dash and a space.",
          "C": "Write the items in one long line.",
          "D": "Surround them with square brackets."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What is HTML mainly used for?",
        "options": {
          "A": "Structuring and displaying content in web pages.",
          "B": "Running payroll calculations.",
          "C": "Encrypting email.",
          "D": "Storing databases."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A financial analyst asks AI for a one-page summary she can open in a browser. Which output format fits?",
        "options": {
          "A": "A voice recording.",
          "B": "A zipped image.",
          "C": "A password list.",
          "D": "An HTML file."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Why do the book's agents work so well with Markdown?",
        "options": {
          "A": "It cannot contain text.",
          "B": "It only works on one operating system.",
          "C": "It is simple, readable text that both people and AI handle easily.",
          "D": "It needs a paid licence."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) Which Markdown creates a numbered list?",
        "options": {
          "A": "* * * Review budget",
          "B": "1. Review budget 2. Approve spend",
          "C": "[1] [2] Review budget",
          "D": "# Review # Approve"
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) An administrator wants a link in a Markdown note. Which syntax is correct?",
        "options": {
          "A": "[Company policy](https://example.com/policy)",
          "B": "{Company policy}(https://example.com/policy)",
          "C": "<<Company policy>>https://example.com/policy",
          "D": "Company policy->link"
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) What does the HTML tag <h1> usually represent?",
        "options": {
          "A": "A paragraph break.",
          "B": "An image.",
          "C": "A table row.",
          "D": "The main heading of a page."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A doctor wants to share a formatted wellness handout that opens on any device. What is the best AI request?",
        "options": {
          "A": "\"Make it a secret file.\"",
          "B": "\"Send it as a spreadsheet macro.\"",
          "C": "\"Convert this Markdown handout to a clean HTML page.\"",
          "D": "\"Compress it to nothing.\""
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) What does the HTML tag <p> mark?",
        "options": {
          "A": "A password field.",
          "B": "A paragraph.",
          "C": "A page break between files.",
          "D": "A picture."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which is an advantage of writing the draft in Markdown first?",
        "options": {
          "A": "You can focus on content and convert it to other formats afterwards.",
          "B": "It forces you to use a mouse.",
          "C": "It deletes formatting errors on its own.",
          "D": "It locks the text from edits."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A manager's table in Markdown uses pipes. What does a pipe (|) do?",
        "options": {
          "A": "Deletes a row.",
          "B": "Starts a heading.",
          "C": "Marks a comment.",
          "D": "Separates the columns of a table."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) What is the safest way to check an AI-generated HTML page before sharing?",
        "options": {
          "A": "Send it without opening it.",
          "B": "Assume the AI's layout is perfect.",
          "C": "Open it in a browser and read it for errors and wrong content.",
          "D": "Check only the file name."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) Which tag pair creates an unordered list in HTML?",
        "options": {
          "A": "<table> with <p> items.",
          "B": "<ul> with <li> items.",
          "C": "<head> with <body> items.",
          "D": "<a> with <img> items."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) A financial analyst wants the number 2026 shown in italics in Markdown. Which is correct?",
        "options": {
          "A": "*2026*",
          "B": "!!2026!!",
          "C": "((2026))",
          "D": "$$2026$$"
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) Why is it useful to learn both Markdown and HTML?",
        "options": {
          "A": "They are required to log in to AI tools.",
          "B": "They replace spreadsheets.",
          "C": "They prevent hallucinations.",
          "D": "They are the two simple document languages agents commonly read and write."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) An administrator wants a page title in the browser tab. Where is it set in HTML?",
        "options": {
          "A": "In a <p> tag inside <body>.",
          "B": "In a comment line.",
          "C": "In the <title> tag inside <head>.",
          "D": "It cannot be set."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) What does \"Markdown in, HTML out\" mean in practice?",
        "options": {
          "A": "Type HTML and receive audio.",
          "B": "Write or give AI simple Markdown and receive a finished web page in HTML.",
          "C": "Give images and receive passwords.",
          "D": "Write Word files and lose all formatting."
        },
        "answer": "B"
      }
    ]
  },
  {
    "title": "Code You Never Write",
    "questions": [
      {
        "question": "(Cross-platform) A financial analyst has never coded but needs 500 expense rows totalled by department. What is the best approach?",
        "options": {
          "A": "Learn a programming language for a year first.",
          "B": "Describe the task to AI, let it write and run the code, then check the totals.",
          "C": "Total the rows by eye and hope.",
          "D": "Ask AI for a guess without the data."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What does the course say about code AI writes for you?",
        "options": {
          "A": "You still need to check that it ran and produced the right result.",
          "B": "It is always correct if it runs.",
          "C": "It never needs testing.",
          "D": "It should be hidden from the team."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A manager asks AI to clean a messy contact list. Which step best verifies the result?",
        "options": {
          "A": "Trust the first row only.",
          "B": "Delete the original file immediately.",
          "C": "Assume no rows changed.",
          "D": "Compare a sample of rows before and after and check the row counts."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Why keep a copy of the original file before running AI-written code on it?",
        "options": {
          "A": "To make the code run faster.",
          "B": "To hide the changes.",
          "C": "So an error can be undone.",
          "D": "Because AI cannot read originals."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) An administrator wants to rename 200 files by date. Which request is clearest?",
        "options": {
          "A": "\"Fix my files.\"",
          "B": "\"Write a script to rename these files as YYYY-MM-DD_name and show me a preview first.\"",
          "C": "\"Do something with dates.\"",
          "D": "\"Rename everything randomly.\""
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What does it mean to ask AI to run code rather than only write it?",
        "options": {
          "A": "The tool executes the code and returns real results, not just text.",
          "B": "The AI types faster.",
          "C": "The code is saved for the vendor.",
          "D": "The AI deletes your files."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A budget officer sees AI report \"Done\" after a script. What should she do?",
        "options": {
          "A": "Accept it, because the word Done is enough.",
          "B": "Ask the AI to say Done again.",
          "C": "Close the file.",
          "D": "Open the output and check that it matches what she asked for."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which task suits \"code you never write\"?",
        "options": {
          "A": "Deciding who to promote.",
          "B": "Judging a patient's condition.",
          "C": "Repeating a calculation across thousands of rows.",
          "D": "Signing a contract."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A company doctor wants a chart of anonymised monthly clinic visits. What should be checked?",
        "options": {
          "A": "Only that the colours look nice.",
          "B": "That the chart's numbers match the source data and the labels are right.",
          "C": "That the chart is large.",
          "D": "Nothing, as charts are always right."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What is a safe first step when AI offers code that modifies many files?",
        "options": {
          "A": "Run it on a small test copy first.",
          "B": "Run it on the whole company drive.",
          "C": "Run it without reading any output.",
          "D": "Disable backups first."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A financial analyst gets an error message after AI's code ran. What is a good next move?",
        "options": {
          "A": "Ignore the message.",
          "B": "Delete the data.",
          "C": "Switch to another job.",
          "D": "Paste the error back to the AI, and ask for a fix with an explanation."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Why ask AI to explain in plain words what its code does?",
        "options": {
          "A": "So the code becomes shorter.",
          "B": "So the code needs no testing.",
          "C": "So you can check that it matches your intent before relying on it.",
          "D": "To avoid reading results."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A manager asks for a summary table from a CSV file. Which detail should be in the request?",
        "options": {
          "A": "Only the word \"table\".",
          "B": "Which columns to group by, what to total and the output format.",
          "C": "A request to be creative.",
          "D": "The AI's preferred layout."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which risk should a non-coder watch for in AI-written code?",
        "options": {
          "A": "It may quietly do something different from what was intended.",
          "B": "It always refuses to run.",
          "C": "It cannot handle numbers.",
          "D": "It deletes itself."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) An administrator wants to merge three attendance sheets. What check proves nothing was lost?",
        "options": {
          "A": "Check the file's colour.",
          "B": "Count only the first sheet.",
          "C": "Skip checks if it opens.",
          "D": "Compare the combined row count with the sum of the originals."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) What is a script?",
        "options": {
          "A": "A type of spreadsheet chart.",
          "B": "A meeting agenda.",
          "C": "A short program that automates a task.",
          "D": "A security badge."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A manager wants the same report built every Monday. What helps?",
        "options": {
          "A": "Rewrite everything every Monday.",
          "B": "Save the working script or instructions and re-run them.",
          "C": "Ask a different tool each week.",
          "D": "Avoid keeping any record."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) A doctor's file contains personal patient details. Before using AI to run code on it, what must be considered?",
        "options": {
          "A": "Whether the data may be placed in that tool at all.",
          "B": "Whether the code is long.",
          "C": "Whether the file has a nice name.",
          "D": "Nothing; code tools are exempt."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) What is the main idea of \"Code You Never Write\"?",
        "options": {
          "A": "Never look at any results.",
          "B": "Avoid computers entirely.",
          "C": "Hide code from your team.",
          "D": "Get AI to write, run and check code so you can focus on the outcome."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A budget officer's AI-run script gives a total that looks far too high. What is the correct response?",
        "options": {
          "A": "Use the total because the script ran.",
          "B": "Increase the budget to match.",
          "C": "Investigate, test against a manual sample and correct before using it.",
          "D": "Delete the file."
        },
        "answer": "C"
      }
    ]
  },
  {
    "title": "Skills & Connectors",
    "questions": [
      {
        "question": "(Cross-platform) What is a skill in an AI assistant?",
        "options": {
          "A": "A certificate the AI earns from a university.",
          "B": "A password for the chat.",
          "C": "A saved set of instructions that teaches the AI how to do a task your way.",
          "D": "A paid upgrade with no instructions."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) What is a connector?",
        "options": {
          "A": "A cable between two laptops.",
          "B": "A safe link that lets the AI reach your real apps and data.",
          "C": "A file format for slides.",
          "D": "A tool that deletes chat history."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) A finance manager teaches AI the exact layout of the monthly variance report once. Which feature fits?",
        "options": {
          "A": "A skill.",
          "B": "A hallucination.",
          "C": "A context window.",
          "D": "A screenshot."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) An administrator wants AI to read calendar entries to schedule meetings. What is needed?",
        "options": {
          "A": "Pasting the manager's password into the chat.",
          "B": "A printed calendar.",
          "C": "No access, because AI guesses availability.",
          "D": "A connector to the calendar, granted with appropriate permission."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Why are the skills you build described as portable?",
        "options": {
          "A": "They only work in one tab.",
          "B": "They disappear after one chat.",
          "C": "They travel with you to other tools, from the browser to desktop agents.",
          "D": "They are locked to one vendor forever."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A financial analyst plans to connect AI to the accounting system. What is the safest principle?",
        "options": {
          "A": "Grant full admin rights for convenience.",
          "B": "Grant the minimum access needed, and prefer read-only where possible.",
          "C": "Share one login across the team.",
          "D": "Skip approval from IT."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) A company doctor wants a skill for drafting staff notices in the clinic's approved tone. Which content belongs in the skill?",
        "options": {
          "A": "Tone rules, structure and approved wording; not patient records.",
          "B": "Patient names and diagnoses.",
          "C": "Personal passwords.",
          "D": "Random jokes."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) Before turning on a new connector, what should a manager check?",
        "options": {
          "A": "Only the connector's logo.",
          "B": "Whether a friend uses it.",
          "C": "How colourful its settings page is.",
          "D": "What data it can reach and whether policy allows it."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A skill gives different results than expected. What is the best fix?",
        "options": {
          "A": "Delete all your files.",
          "B": "Assume skills cannot be changed.",
          "C": "Review and refine the skill's instructions and test again.",
          "D": "Add contradictory rules."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) Which is a good candidate for a skill?",
        "options": {
          "A": "A one-time unrelated question.",
          "B": "A recurring task with a consistent method, such as a weekly status report.",
          "C": "A secret decision with no steps.",
          "D": "A task nobody understands."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) An administrator wants a connector to send emails automatically. What is the key risk?",
        "options": {
          "A": "Messages may go out wrongly without review.",
          "B": "Emails become impossible to read.",
          "C": "The inbox stops working.",
          "D": "The AI gets tired."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) What should you do with a connector you no longer need?",
        "options": {
          "A": "Leave it on forever.",
          "B": "Share it with everyone.",
          "C": "Rename it.",
          "D": "Turn it off or remove access."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A budget officer wants AI to pull figures from a shared drive. What improves trust in the result?",
        "options": {
          "A": "Accept them because a connector was used.",
          "B": "Delete the file.",
          "C": "Check the figures against the actual file the connector read.",
          "D": "Avoid asking for sources."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) How is a skill different from a one-off prompt?",
        "options": {
          "A": "A skill can never be edited.",
          "B": "A skill is saved and reusable; a prompt is typed for one moment.",
          "C": "A prompt is permanent.",
          "D": "They are identical."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) A financial analyst shares a skill with her team. What should she include?",
        "options": {
          "A": "Clear instructions, an example and notes on checks required.",
          "B": "Her private credentials.",
          "C": "Only the skill's name.",
          "D": "Nothing, since skills explain themselves."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) What does a connector add that pasting text into chat does not?",
        "options": {
          "A": "A guarantee that AI never errs.",
          "B": "A way to avoid permissions.",
          "C": "Automatic legal approval.",
          "D": "Direct, controlled access to live apps or data."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A manager asks if a skill can replace human review. What is correct?",
        "options": {
          "A": "Yes, skills are always right.",
          "B": "Yes, if the skill is long.",
          "C": "No; it improves consistency, but you still check the result.",
          "D": "Only on weekends."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A company doctor's clinic uses a connector to a scheduling app. Which data decision is wise?",
        "options": {
          "A": "Give it every record in the system.",
          "B": "Limit it to appointment times and exclude clinical notes.",
          "C": "Give it the doctor's password.",
          "D": "Disable logging."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Why test a new skill on a low-risk example first?",
        "options": {
          "A": "To see whether it behaves as intended before relying on it.",
          "B": "To make it expire.",
          "C": "To prove the AI is perfect.",
          "D": "To avoid writing instructions."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) Which statement about skills and connectors is accurate?",
        "options": {
          "A": "Skills give access; connectors give instructions.",
          "B": "Both remove the need for judgement.",
          "C": "Both are the same as prompts typed once.",
          "D": "Skills teach how to do the work; connectors give access to the places the work lives."
        },
        "answer": "D"
      }
    ]
  },
  {
    "title": "How to Think in the AI Era",
    "questions": [
      {
        "question": "(Cross-platform) A manager is deciding whether to use AI for a task. What is the first question to ask?",
        "options": {
          "A": "Which AI is the newest?",
          "B": "Can AI make it longer?",
          "C": "Is everyone else using it?",
          "D": "Is this the kind of problem AI is good at, and can I check the result?"
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Which problem is a poor fit for AI alone?",
        "options": {
          "A": "Drafting a first-pass agenda.",
          "B": "Reformatting notes into bullets.",
          "C": "A decision needing personal accountability and sensitive judgement, such as a disciplinary outcome.",
          "D": "Brainstorming slogan ideas."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A financial analyst frames the problem: \"What decision will this analysis support, and for whom?\" Why?",
        "options": {
          "A": "It makes the AI cheaper.",
          "B": "A clear problem frame guides what to ask AI and how to judge the answer.",
          "C": "It removes the need for data.",
          "D": "It guarantees approval."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) An administrator spends hours prompting AI for a task that takes five minutes by hand. What does the course suggest?",
        "options": {
          "A": "Sometimes not using AI is the right call.",
          "B": "Use AI regardless.",
          "C": "Add more prompts.",
          "D": "Blame the tool."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A company doctor wants to know when AI is useful. Which description is best?",
        "options": {
          "A": "Useful for final clinical decisions.",
          "B": "Useful for replacing professional licences.",
          "C": "Useful only for images.",
          "D": "Useful for drafting, summarising and exploring, where a human can verify the output."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A budget officer is unsure what the real problem is. What should she do before asking AI?",
        "options": {
          "A": "Ask AI to guess the goal.",
          "B": "Skip planning to save time.",
          "C": "Write down the goal, constraints and what a good outcome looks like.",
          "D": "Start with the longest prompt possible."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) Why is judgement described as the skill you keep using after the others become second nature?",
        "options": {
          "A": "Because tools keep changing the names of features.",
          "B": "Because deciding when and how to use AI never becomes automatic.",
          "C": "Because judgement is only for managers.",
          "D": "Because other skills are not important."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) A manager considers AI for a task where mistakes are costly and hard to detect. What is a sensible approach?",
        "options": {
          "A": "Use AI only for support, with strong human review, or avoid it.",
          "B": "Trust it fully for speed.",
          "C": "Skip review to meet a deadline.",
          "D": "Share the data publicly for feedback."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) What does breaking a big problem into smaller parts help with?",
        "options": {
          "A": "You avoid doing any work.",
          "B": "You make the problem unsolvable.",
          "C": "You need fewer details.",
          "D": "You can decide which parts suit AI and which need a person."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A financial analyst receives an AI-generated forecast without assumptions. What is the best step?",
        "options": {
          "A": "Present it as certain.",
          "B": "Delete the assumptions from the report.",
          "C": "Ask for the assumptions and test them against known facts.",
          "D": "Round the forecast up."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) Which question helps decide whether to reach for AI?",
        "options": {
          "A": "Is the weather good?",
          "B": "What would happen if the output were wrong?",
          "C": "Is the tool free this week?",
          "D": "Is the file name short?"
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) An administrator is asked to \"use AI for everything\". What is the better stance?",
        "options": {
          "A": "Match the tool to the task and use judgement each time.",
          "B": "Use AI for every task regardless.",
          "C": "Never use AI.",
          "D": "Only use it on Fridays."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) Why does framing matter so much?",
        "options": {
          "A": "Framing is only for artists.",
          "B": "AI always corrects the frame.",
          "C": "It affects only the font.",
          "D": "A badly framed problem produces confident answers to the wrong question."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A manager wants AI to decide who gets a budget increase. What is the most accurate view?",
        "options": {
          "A": "AI should decide alone.",
          "B": "A random pick is fairer.",
          "C": "AI can organise information, but the decision and fairness review remain human.",
          "D": "Fairness is not relevant."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A company doctor asks for a list of possible wellness topics. Why is this a good AI use?",
        "options": {
          "A": "It requires patient records.",
          "B": "It is exploratory and low-risk, and the doctor can screen every idea.",
          "C": "It cannot be checked.",
          "D": "It must be final."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which of these shows good AI-era thinking?",
        "options": {
          "A": "Keeping ownership of the goal and the outcome while using AI for the legwork.",
          "B": "Handing over the goal as well.",
          "C": "Ignoring the output quality.",
          "D": "Believing AI is neutral and flawless."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A finance team has a rare, one-off, high-stakes negotiation. What is the best role for AI?",
        "options": {
          "A": "Negotiate on behalf of the team alone.",
          "B": "Sign the final agreement.",
          "C": "Replace the legal reviewer.",
          "D": "Prepare options and questions, while the team leads the decision."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) What is a sign that AI is helping rather than hurting?",
        "options": {
          "A": "You stop reading the output.",
          "B": "You cannot explain the result.",
          "C": "You save time and the output still passes your checks.",
          "D": "Errors are found later by others."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) An administrator keeps rewriting prompts without progress. What is a sensible pause point?",
        "options": {
          "A": "Add more rewrites forever.",
          "B": "Step back and re-frame the problem or do part of the work manually.",
          "C": "Hide the problem.",
          "D": "Switch the deadline."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which belongs to \"how to think\" rather than \"how to click\"?",
        "options": {
          "A": "Deciding what is worth delegating and how to verify it.",
          "B": "Finding the upload button.",
          "C": "Choosing a theme colour.",
          "D": "Resizing the window."
        },
        "answer": "A"
      }
    ]
  },
  {
    "title": "Workflow Design & Diagnosis",
    "questions": [
      {
        "question": "(Cross-platform) A finance manager maps a workflow step by step and decides who owns each step. Which three questions guide the ownership decision?",
        "options": {
          "A": "Can it be undone, what does an error cost, and who is answerable.",
          "B": "How fast, how long, and how colourful.",
          "C": "Who is cheapest, who is newest, and who is oldest.",
          "D": "Which tool, which colour, and which day."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) In a payment-approval workflow, a step cannot be reversed once the money is sent. What does this suggest?",
        "options": {
          "A": "Let AI send it automatically.",
          "B": "Remove all checks.",
          "C": "Do it at the end of the month.",
          "D": "Keep a human responsible and require review before that step."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) An administrator's AI step drafts a meeting reminder that can be edited before sending. Which factor applies?",
        "options": {
          "A": "It must never involve AI.",
          "B": "It is irreversible.",
          "C": "It is easily undone and low cost if wrong, so more automation is acceptable.",
          "D": "It needs legal sign-off."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A company doctor's workflow includes drafting a general wellness newsletter. Who is answerable for what is published?",
        "options": {
          "A": "The AI.",
          "B": "A named person, such as the doctor or the communications owner.",
          "C": "Nobody.",
          "D": "The reader."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What is the value of writing a workflow out step by step?",
        "options": {
          "A": "It makes hidden steps and owners visible so they can be assigned.",
          "B": "It makes the workflow faster by itself.",
          "C": "It replaces the need for owners.",
          "D": "It hides risks."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A budget workflow starts producing wrong totals. What is the right first move?",
        "options": {
          "A": "Replace the whole team.",
          "B": "Blame the AI at once.",
          "C": "Ignore it until month end.",
          "D": "Diagnose where in the steps the error enters rather than guessing."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A financial analyst notes that a wrong forecast would cost the company a large contract. How should this step be handled?",
        "options": {
          "A": "Automate it fully for speed.",
          "B": "Remove the review step.",
          "C": "Treat it as high-cost, with strong human review and a clear owner.",
          "D": "Leave the owner unspecified."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) What does \"say what the workflow actually does without overstating it\" mean?",
        "options": {
          "A": "Claim the workflow is fully automatic.",
          "B": "Describe the real role of AI and humans accurately, without exaggerating automation.",
          "C": "Hide the human checks.",
          "D": "Avoid describing any steps."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) An HR administrator's onboarding workflow has an AI-written welcome letter. Which question helps assign ownership?",
        "options": {
          "A": "Who is answerable if the letter contains an error?",
          "B": "Which font is used?",
          "C": "How long is the letter?",
          "D": "What time was it written?"
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) What is the final product of the Workflow Design course?",
        "options": {
          "A": "A long report nobody reads.",
          "B": "A tool licence.",
          "C": "A private note only the author understands.",
          "D": "A one-page map that somebody else could run."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A step in the workflow is easily reversible and low cost, yet it has no owner. What is the correct fix?",
        "options": {
          "A": "Leave it unowned.",
          "B": "Delete the step.",
          "C": "Assign an owner anyway, because someone must be answerable.",
          "D": "Wait for an error."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A manager's team gets inconsistent outputs from an AI step. Which diagnosis is useful?",
        "options": {
          "A": "Assume the AI is broken permanently.",
          "B": "Check the inputs, the instructions and the review step for gaps.",
          "C": "Remove all instructions.",
          "D": "Increase the deadline."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which step is the best candidate for tighter human control?",
        "options": {
          "A": "Releasing a salary payment to a supplier.",
          "B": "Drafting a thank-you note.",
          "C": "Suggesting meeting times.",
          "D": "Tidying a list."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A financial analyst says, \"AI does the whole reporting process.\" In truth she reviews every figure. What is the better statement?",
        "options": {
          "A": "AI does everything with no checks.",
          "B": "The report writes itself.",
          "C": "No one is involved.",
          "D": "AI drafts the report, and I verify the figures before release."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) What is the benefit of mapping the review step explicitly?",
        "options": {
          "A": "It removes the need for AI.",
          "B": "It adds delay without value.",
          "C": "It ensures errors are caught before they reach anyone affected.",
          "D": "It hides the owner."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) In diagnosis, what should you do before changing the workflow?",
        "options": {
          "A": "Change every step at once.",
          "B": "Identify the step where the problem begins.",
          "C": "Ignore the evidence.",
          "D": "Add more AI tools."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) A company doctor's team uses AI to sort routine appointment requests. A wrong sort is easily corrected. Which design is suitable?",
        "options": {
          "A": "AI sorts, a person spot-checks and any urgent request goes to a human.",
          "B": "AI decides alone for all cases.",
          "C": "No checks at all.",
          "D": "Everything is manual forever."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) Why is \"who is answerable\" a separate question from \"who does the work\"?",
        "options": {
          "A": "They are always the same.",
          "B": "Answerability does not matter.",
          "C": "Only vendors answer.",
          "D": "The one doing a step may be AI, but a person must still answer for the outcome."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A procurement workflow has a step that cannot be undone and costs a lot if wrong. What should the design include?",
        "options": {
          "A": "Full automation.",
          "B": "A hidden step.",
          "C": "A human decision-maker and a documented approval.",
          "D": "No record."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) How can a team test whether its workflow map is clear?",
        "options": {
          "A": "Keep the map secret.",
          "B": "Ask someone else to run it from the map alone.",
          "C": "Make it longer.",
          "D": "Remove the owners."
        },
        "answer": "B"
      }
    ]
  },
  {
    "title": "Governance, Risk & Responsible Use",
    "questions": [
      {
        "question": "(Cross-platform) A free AI tool's terms allow the vendor to train on user inputs. A marketing associate wants to brainstorm slogans from product information that is already public. What should the associate do?",
        "options": {
          "A": "Use any free tool without thinking, since the info is public.",
          "B": "Check that policy allows this tool for public material, and keep internal data out.",
          "C": "Refuse to use any AI at all.",
          "D": "Paste internal pricing to improve the results."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What are the four questions to run before AI does real work?",
        "options": {
          "A": "Can AI do this task, can this data go in, can I turn this tool on, and could this affect someone unfairly.",
          "B": "Is it fast, cheap, popular and colourful.",
          "C": "Who owns it, who pays, who laughs and who leaves.",
          "D": "Which brand, which price, which day and which place."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A company doctor wants to paste patient notes into a public AI chat. Which question stops this first?",
        "options": {
          "A": "Can I make it longer?",
          "B": "Is the tool free?",
          "C": "Is the tool fast?",
          "D": "Can this data go in?"
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A finance manager wants to upload confidential payroll data to an unapproved AI tool. What is the right action?",
        "options": {
          "A": "Upload it quickly before anyone notices.",
          "B": "Remove the file name and upload it.",
          "C": "Do not; use only a tool approved for that data class, or ask IT and compliance.",
          "D": "Ask the AI if it is allowed."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) An administrator finds a new AI browser extension and wants to switch it on at work. Which question applies?",
        "options": {
          "A": "Is the logo attractive?",
          "B": "Can I turn this tool on, under company policy?",
          "C": "Does it have good reviews only?",
          "D": "Is it new?"
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) A manager wants AI to rank job applicants and reject the bottom half. What is the key governance concern?",
        "options": {
          "A": "It could affect people unfairly, so human review and bias checks are needed.",
          "B": "It will take too long.",
          "C": "It will cost too much.",
          "D": "The applicants may be bored."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A financial analyst asks AI to prepare a draft of public market commentary. Which question is most satisfied?",
        "options": {
          "A": "None; drafts cannot be checked.",
          "B": "The data is private.",
          "C": "The tool is banned.",
          "D": "Can AI do this task? Yes, as a draft, with human checks."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) What does a free tool that trains on user inputs imply for sensitive data?",
        "options": {
          "A": "All data is safe.",
          "B": "Only public data is dangerous.",
          "C": "Sensitive or internal data should stay out of that tool.",
          "D": "Nothing, as vendors never keep inputs."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A company doctor drafts general health tips using only public guidance and an approved tool. Which is acceptable?",
        "options": {
          "A": "No, AI can never be used by doctors.",
          "B": "Yes, provided the doctor reviews the output and owns it.",
          "C": "Yes, without review.",
          "D": "Yes, if patient names are added."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) What does the course say the Governance record is for?",
        "options": {
          "A": "A one-page record you fill in for a workflow you own.",
          "B": "A public announcement.",
          "C": "A list of banned words.",
          "D": "An AI vendor's invoice."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A budget officer wants to use client names in a prompt to an enterprise tool covered by company contract. What should she confirm?",
        "options": {
          "A": "That the tool is free.",
          "B": "That the AI will not mention it.",
          "C": "That nobody is watching.",
          "D": "That the approved tool and policy permit that data class."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) An HR manager wants AI to summarise exit interviews. Which risk deserves attention?",
        "options": {
          "A": "Whether the summary is too short.",
          "B": "Whether the font is neat.",
          "C": "Personal, sensitive information and possible unfair conclusions about individuals.",
          "D": "Whether the tool has a logo."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A marketing associate is told the company bans a certain free AI tool. What should the associate do?",
        "options": {
          "A": "Use it on a personal phone.",
          "B": "Follow the policy and use an approved alternative or request an exception.",
          "C": "Ignore the ban for public material.",
          "D": "Use it and delete the chat."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) When is it acceptable to rely on a vendor's privacy settings alone?",
        "options": {
          "A": "Not by themselves; also check company policy and the data class involved.",
          "B": "Always; settings guarantee safety.",
          "C": "Never read any settings.",
          "D": "Only when the tool is free."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) A manager says, \"AI made the decision, not me.\" Under responsible use, what is correct?",
        "options": {
          "A": "The AI vendor is answerable.",
          "B": "No one is answerable.",
          "C": "The customer is answerable.",
          "D": "The manager remains answerable for the decision."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) A financial analyst plans to use AI-generated figures in an audit report. What is required?",
        "options": {
          "A": "Nothing, since AI is accurate.",
          "B": "Removal of all sources.",
          "C": "Verification of the figures and clear ownership of the report.",
          "D": "A disclaimer instead of checking."
        },
        "answer": "C"
      },
      {
        "question": "(Cross-platform) A company doctor's admin wants to use AI to schedule appointments. What should be limited?",
        "options": {
          "A": "The calendar.",
          "B": "Access to clinical details that scheduling does not need.",
          "C": "The reminders.",
          "D": "The clinic phone number."
        },
        "answer": "B"
      },
      {
        "question": "(Cross-platform) Which sequence best reflects the four governance questions?",
        "options": {
          "A": "Task fit, data, tool permission, then fairness impact.",
          "B": "Colour, size, price, then brand.",
          "C": "Speed, speed, speed, then speed.",
          "D": "Fairness only."
        },
        "answer": "A"
      },
      {
        "question": "(Cross-platform) An administrator accidentally pasted internal data into an unapproved tool. What is the best response?",
        "options": {
          "A": "Hide it and hope no one notices.",
          "B": "Paste more data to compare.",
          "C": "Blame a colleague.",
          "D": "Report it promptly through the proper channel so the risk can be handled."
        },
        "answer": "D"
      },
      {
        "question": "(Cross-platform) Why does the governance course make the other nine courses safe to use at work?",
        "options": {
          "A": "It removes all rules.",
          "B": "It replaces the need for judgement.",
          "C": "It adds checks on task, data, tool and fairness before real work begins.",
          "D": "It guarantees there will be no errors."
        },
        "answer": "C"
      }
    ]
  }
]
TOTAL_SECTIONS = len(SECTIONS)
QUESTIONS_PER_SECTION = 20
SECONDS_PER_QUESTION = 60
TOTAL_QUESTIONS = TOTAL_SECTIONS * QUESTIONS_PER_SECTION

# ---------- FUTURISTIC THEME ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
:root { --cyan:#42e8ff; --blue:#4b8dff; --violet:#a56bff; --ink:#eaf4ff; }
html, body, [data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at 12% 8%, #172b54 0%, #0b1225 38%, #070b16 100%);
    color:var(--ink); font-family:'Inter',sans-serif;
}
[data-testid="stHeader"] { background:rgba(0,0,0,0); }
[data-testid="stAppViewContainer"] > .main { background:transparent; }
.block-container { max-width:1250px; padding-top:1.5rem; padding-bottom:3rem; }
[data-testid="stSidebar"] { background:#0b1429; border-right:1px solid #25395d; }
[data-testid="stMetric"] { background:rgba(21,39,72,.72); border:1px solid #29466f; padding:15px 18px; border-radius:16px; }
[data-testid="stMetricLabel"] { color:#9db7d8 !important; }
[data-testid="stMetricValue"] { color:#f4f9ff !important; }
.stProgress > div > div > div > div { background:linear-gradient(90deg,var(--cyan),var(--blue),var(--violet)); }
div.stButton > button { border-radius:12px; min-height:3rem; border:1px solid #3b6092; background:linear-gradient(100deg,#1764a8,#5942a7); color:white; font-weight:700; transition:all .2s ease; }
div.stButton > button:hover { border-color:var(--cyan); box-shadow:0 0 20px #42e8ff44; transform:translateY(-1px); color:white; }
div[data-testid="stRadio"] label { background:rgba(18,34,62,.75); border:1px solid #29466f; border-radius:12px; padding:12px 15px; margin:7px 0; width:100%; }
div[data-testid="stRadio"] label:hover { border-color:var(--cyan); background:#162b4b; }
[data-testid="stExpander"] { background:rgba(15,29,54,.85); border:1px solid #29466f; border-radius:13px; }
.exam-hero { padding:34px; border-radius:24px; border:1px solid #31527d; background:linear-gradient(125deg,rgba(16,46,82,.96),rgba(37,25,76,.92)); box-shadow:0 18px 55px #0006; position:relative; overflow:hidden; }
.eyebrow { color:#5ceaff; letter-spacing:3px; font-size:12px; font-weight:800; }
.hero-title { color:white; font-size:clamp(30px,5vw,54px); line-height:1.08; font-weight:900; margin:12px 0; }
.hero-sub { color:#b9cbe5; font-size:16px; max-width:760px; }
.panel { background:rgba(14,27,51,.88); border:1px solid #29466f; border-radius:20px; padding:22px; box-shadow:0 12px 35px #0003; }
/* MCQ ANSWER OPTIONS */
div[data-testid="stRadio"] [role="radiogroup"] label {
    background: #F1F6FF !important;
    border: 2px solid #83A9DF !important;
    border-radius: 12px !important;
    padding: 13px 16px !important;
    margin: 8px 0 !important;
}

div[data-testid="stRadio"] [role="radiogroup"] label,
div[data-testid="stRadio"] [role="radiogroup"] label * {
    color: #10213B !important;
    font-weight: 600 !important;
    opacity: 1 !important;
}

div[data-testid="stRadio"] [role="radiogroup"] label:hover {
    background: #DCEAFF !important;
    border-color: #42E8FF !important;
}

div[data-testid="stRadio"] > label {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}
.section-chip { display:inline-block; padding:7px 13px; border-radius:30px; color:#72edff; background:#123958; border:1px solid #286b8a; font-weight:700; font-size:13px; }
.timer { color:#5ceaff; font-size:30px; font-weight:900; text-align:right; }
.timer-low { color:#ff8585; }
.muted { color:#9eb3d1; }
.robot-watermark { position:fixed; right:-35px; bottom:-80px; width:min(42vw,520px); opacity:.075; z-index:0; pointer-events:none; }
footer {visibility:hidden;}
</style>
<div class="robot-watermark">
<svg viewBox="0 0 500 560" xmlns="http://www.w3.org/2000/svg">
 <g fill="none" stroke="#65eaff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round">
  <path d="M250 48v55M220 48h60"/><circle cx="250" cy="34" r="13" fill="#65eaff"/>
  <rect x="85" y="105" width="330" height="260" rx="62"/><path d="M85 190H45v95h40M415 190h40v95h-40"/>
  <rect x="140" y="175" width="75" height="55" rx="22"/><rect x="285" y="175" width="75" height="55" rx="22"/>
  <path d="M170 285q80 65 160 0M250 365v80M160 445h180M185 445l-45 75M315 445l45 75"/>
  <path d="M85 140L35 105M415 140l50-35M105 365l-55 60M395 365l60 60"/>
  <circle cx="250" cy="310" r="8" fill="#65eaff"/>
 </g>
 <g fill="#65eaff"><circle cx="55" cy="55" r="5"/><circle cx="440" cy="45" r="7"/><circle cx="30" cy="330" r="6"/><circle cx="470" cy="350" r="5"/></g>
</svg></div>
""", unsafe_allow_html=True)


def init_state():
    defaults = {
        "page": "welcome",
        "section_index": 0,
        "question_index": 0,
        "answers": {},
        "question_started_at": None,
        "attempt_id": 0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def section_answers(section_index):
    return st.session_state.answers.get(str(section_index), {})


def save_answer(section_index, question_index, selected, timed_out=False):
    section_data = st.session_state.answers.setdefault(str(section_index), {})
    section_data[str(question_index)] = {"selected": selected, "timed_out": timed_out}


def score_section(section_index):
    score = 0
    responses = section_answers(section_index)
    for qi, question in enumerate(SECTIONS[section_index]["questions"]):
        response = responses.get(str(qi), {})
        if response.get("selected") == question["answer"]:
            score += 1
    return score


def start_section(section_index):
    st.session_state.section_index = section_index
    st.session_state.question_index = 0
    st.session_state.question_started_at = time.time()
    st.session_state.page = "quiz"
    st.rerun()


def advance_question():
    si = st.session_state.section_index
    qi = st.session_state.question_index
    if qi + 1 >= QUESTIONS_PER_SECTION:
        st.session_state.page = "section_result"
        st.session_state.question_started_at = None
    else:
        st.session_state.question_index += 1
        st.session_state.question_started_at = time.time()
    st.rerun()


def render_brand_header():
    st.markdown("<div class='eyebrow'>PANAVERSITY • CERTIFIED ASSOCIATE</div>", unsafe_allow_html=True)


def render_section_result(section_index):
    section = SECTIONS[section_index]
    score = score_section(section_index)
    percent = score * 5
    st.markdown(f"<div class='eyebrow'>EXAMINATION COMPLETE • SECTION {section_index + 1}</div>", unsafe_allow_html=True)
    st.markdown(f"# 🏆 {section['title']} — Result")
    a, b, c = st.columns(3)
    a.metric("Section score", f"{score} / 20")
    b.metric("Percentage", f"{percent}%")
    c.metric("Correct answers", str(score))
    st.progress(score / 20)
    st.markdown("### Answer review")
    responses = section_answers(section_index)
    for qi, question in enumerate(section["questions"]):
        response = responses.get(str(qi), {})
        selected = response.get("selected")
        correct = question["answer"]
        ok = selected == correct
        label = f"Question {qi + 1}  •  " + ("✅ Correct" if ok else "❌ Incorrect / unanswered")
        with st.expander(label):
            st.markdown(f"**{question['question']}**")
            for letter, option in question["options"].items():
                if letter == correct:
                    st.success(f"{letter}. {option} — Correct answer")
                elif letter == selected:
                    st.error(f"{letter}. {option} — Your answer")
                else:
                    st.write(f"{letter}. {option}")
    st.divider()
    if section_index < TOTAL_SECTIONS - 1:
        if st.button(f"🚀 Continue to Section {section_index + 2}", type="primary", use_container_width=True):
            start_section(section_index + 1)
    else:
        st.success("All ten sections are complete. Your overall examination result is ready.")
        if st.button("🏆 View All Sections Result", type="primary", use_container_width=True):
            st.session_state.page = "all_result"
            st.rerun()


def render_all_results():
    st.markdown("<div class='eyebrow'>FINAL EXAMINATION REPORT</div>", unsafe_allow_html=True)
    st.markdown("# 🏆 All Sections Result")
    total = sum(score_section(i) for i in range(TOTAL_SECTIONS))
    percent = total / TOTAL_QUESTIONS * 100
    a, b, c = st.columns(3)
    a.metric("Final score", f"{total} / {TOTAL_QUESTIONS}")
    b.metric("Overall percentage", f"{percent:.1f}%")
    c.metric("Sections completed", f"{TOTAL_SECTIONS} / {TOTAL_SECTIONS}")
    st.progress(total / TOTAL_QUESTIONS)
    st.markdown("### Section-by-section performance")
    for i, section in enumerate(SECTIONS):
        score = score_section(i)
        with st.container(border=True):
            left, right = st.columns([4, 1])
            left.markdown(f"**{i + 1:02d}. {section['title']}**")
            right.markdown(f"**{score}/20 · {score*5}%**")
            st.progress(score / 20)
    if percent >= 90:
        st.success("Outstanding performance. Excellent command of the course material!")
    elif percent >= 75:
        st.success("Strong performance. Review the missed questions to sharpen your knowledge.")
    elif percent >= 50:
        st.warning("Good attempt. Revisit the weaker sections and practise again.")
    else:
        st.info("Keep learning and practising. Every attempt helps you improve.")
    if st.button("🔄 Restart Full Examination", type="primary", use_container_width=True):
        st.session_state.page = "welcome"
        st.session_state.section_index = 0
        st.session_state.question_index = 0
        st.session_state.answers = {}
        st.session_state.question_started_at = None
        st.session_state.attempt_id += 1
        st.rerun()


init_state()
render_brand_header()

# ---------- WELCOME ----------
if st.session_state.page == "welcome":
    st.markdown("""
    <div class="exam-hero">
      <div class="eyebrow">AI-POWERED LEARNING • EXAM SIMULATOR</div>
      <div class="hero-title">Foundations<br>Knowledge Challenge</div>
      <div class="hero-sub">A focused 10-section examination covering AI fluency, prompting, delegation, workflows, tools and responsible AI use.</div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns(3)
    c1.metric("Sections", "10")
    c2.metric("Total questions", "200")
    c3.metric("Time per question", "60 sec")
    st.markdown("### Examination roadmap")
    for i, section in enumerate(SECTIONS):
        st.markdown(f"<div class='panel' style='padding:13px 18px;margin:8px 0'><span class='section-chip'>SECTION {i+1:02d}</span> &nbsp; <b>{section['title']}</b> <span class='muted' style='float:right'>20 questions</span></div>", unsafe_allow_html=True)
    st.info("Each section has its own result screen. Your answers are revealed only after you finish that section. The final combined report appears after Section 10.")
    if st.button("⚡ Begin Examination — Section 1", type="primary", use_container_width=True):
        start_section(0)
    st.stop()

# ---------- QUIZ ----------
if st.session_state.page == "quiz":
    si = st.session_state.section_index
    qi = st.session_state.question_index
    section = SECTIONS[si]
    question = section["questions"][qi]
    if st.session_state.question_started_at is None:
        st.session_state.question_started_at = time.time()

    elapsed = time.time() - st.session_state.question_started_at
    remaining = max(0, SECONDS_PER_QUESTION - int(elapsed))

    top1, top2 = st.columns([3, 1])
    top1.markdown(f"## Section {si+1} / {TOTAL_SECTIONS}: {section['title']}")
    top1.markdown(f"<span class='section-chip'>QUESTION {qi+1} OF {QUESTIONS_PER_SECTION}</span>", unsafe_allow_html=True)
    top2.markdown(f"<div class='timer {'timer-low' if remaining <= 10 else ''}'>{remaining:02d}<span style='font-size:14px'> SEC LEFT</span></div>", unsafe_allow_html=True)
    st.progress((qi + 1) / QUESTIONS_PER_SECTION)

    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown(f"<div class='eyebrow'>SELECT THE BEST ANSWER</div><div class='question-title'>{question['question']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    radio_key = f"choice_{st.session_state.attempt_id}_{si}_{qi}"
    selected = st.radio(
        "Choose one answer:",
        options=list(question["options"].keys()),
        format_func=lambda letter: f"{letter}. {question['options'][letter]}",
        index=None,
        key=radio_key,
        label_visibility="visible",
    )

    col_a, col_b = st.columns([3, 1])
    with col_a:
        if st.button("Submit Answer  →", type="primary", use_container_width=True, disabled=(selected is None)):
            save_answer(si, qi, selected)
            advance_question()
    with col_b:
        if st.button("Skip", use_container_width=True):
            save_answer(si, qi, None)
            advance_question()

    # Refresh the countdown once per second. The fallback works even when
    # streamlit-autorefresh is not installed. Do not refresh after timeout.
    if remaining > 0:
        st_autorefresh(
            interval=1000,
            limit=None,
            key=f"timer_{st.session_state.attempt_id}_{si}_{qi}",
        )
    if remaining <= 0:
        save_answer(si, qi, None, timed_out=True)
        advance_question()
    st.caption("Your answer is not shown as correct or incorrect until this section is complete.")
    st.stop()

# ---------- SECTION RESULT ----------
if st.session_state.page == "section_result":
    render_section_result(st.session_state.section_index)
    st.stop()

# ---------- FINAL RESULT ----------
if st.session_state.page == "all_result":
    render_all_results()
    st.stop()
