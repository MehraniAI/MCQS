import streamlit as st
import random

st.set_page_config(page_title="PCAO-F Practice Quiz", page_icon="\U0001F9E0", layout="centered")

# ---------------------------------------------------------------------------
# Question bank: 120 original PCAO-F practice questions (auto-generated from
# the source PDF). Each item has: num, domain, question, options (A-D), answer.
# ---------------------------------------------------------------------------
QUESTIONS = [
    {
        "num": 1,
        "domain": 'Prompting & Task Execution',
        "question": 'A user asks an AI assistant to summarize a 40-page policy but does not specify the audience or desired length. What is the best first step?',
        "options": {
            'A': 'Ask for the intended audience and output constraints',
            'B': 'Tell the model to summarize everything in exactly 40 bullets',
            'C': 'Use a random template',
            'D': 'Assume the audience is technical',
        },
        "answer": 'A',
    },
    {
        "num": 2,
        "domain": 'Prompting & Task Execution',
        "question": 'Which prompt is most likely to produce a consistent structured output?',
        "options": {
            'A': 'Give the topic only',
            'B': 'Specify the task, constraints, desired fields, and output format',
            'C': 'Ask the model to be creative',
            'D': 'Repeat the same vague request',
        },
        "answer": 'B',
    },
    {
        "num": 3,
        "domain": 'Prompting & Task Execution',
        "question": 'A prompt contains several independent tasks. What can improve reliability?',
        "options": {
            'A': 'Hide the tasks in one long paragraph',
            'B': 'Break the work into clear steps or stages',
            'C': 'Remove all constraints',
            'D': 'Ask for a guess',
        },
        "answer": 'B',
    },
    {
        "num": 4,
        "domain": 'Prompting & Task Execution',
        "question": 'What is the main purpose of giving an AI an explicit role or perspective?',
        "options": {
            'A': 'Guarantee factual accuracy',
            'B': 'Provide useful context for how the task should be approached',
            'C': 'Increase internet speed',
            'D': 'Prevent all hallucinations',
        },
        "answer": 'B',
    },
    {
        "num": 5,
        "domain": 'Prompting & Task Execution',
        "question": 'Which instruction is most testable?',
        "options": {
            'A': 'Make it excellent',
            'B': 'Make it professional',
            'C': 'Return exactly five bullet points, each under 20 words',
            'D': 'Make it interesting',
        },
        "answer": 'C',
    },
    {
        "num": 6,
        "domain": 'Prompting & Task Execution',
        "question": 'If an AI repeatedly misunderstands a task, which change is most useful?',
        "options": {
            'A': 'Make the prompt shorter at random',
            'B': 'Clarify the objective, constraints, and expected output',
            'C': 'Add unrelated information',
            'D': 'Ask it to try harder',
        },
        "answer": 'B',
    },
    {
        "num": 7,
        "domain": 'Prompting & Task Execution',
        "question": 'Why can examples in a prompt be useful?',
        "options": {
            'A': 'They always guarantee correctness',
            'B': 'They demonstrate the desired pattern or format',
            'C': 'They eliminate the need for evaluation',
            'D': "They increase the model's training data",
        },
        "answer": 'B',
    },
    {
        "num": 8,
        "domain": 'Prompting & Task Execution',
        "question": 'A user wants an AI to extract names, dates, and amounts from invoices. Which instruction is strongest?',
        "options": {
            'A': 'Read these invoices',
            'B': 'Extract useful information',
            'C': "Return name, date, and amount for each invoice in a table; use 'unknown' when absent",
            'D': 'Tell me everything',
        },
        "answer": 'C',
    },
    {
        "num": 9,
        "domain": 'Prompting & Task Execution',
        "question": 'What should you do when an AI response is too broad?',
        "options": {
            'A': 'Add precise scope and boundaries',
            'B': 'Remove the original task',
            'C': 'Accept it without checking',
            'D': 'Ask for unrelated examples',
        },
        "answer": 'A',
    },
    {
        "num": 10,
        "domain": 'Prompting & Task Execution',
        "question": 'Which approach is best for a complex task with dependencies?',
        "options": {
            'A': 'Ask for the final answer without context',
            'B': 'Decompose it into stages and define inputs/outputs',
            'C': 'Use only one-word prompts',
            'D': 'Avoid verification',
        },
        "answer": 'B',
    },
    {
        "num": 11,
        "domain": 'Prompting & Task Execution',
        "question": 'A prompt asks for a legal conclusion from incomplete facts. What should the user do?',
        "options": {
            'A': 'Ask for certainty anyway',
            'B': 'Provide relevant facts and define the limits of the requested analysis',
            'C': 'Tell the model to invent missing facts',
            'D': 'Skip review',
        },
        "answer": 'B',
    },
    {
        "num": 12,
        "domain": 'Prompting & Task Execution',
        "question": 'Which is a useful constraint?',
        "options": {
            'A': 'Be smart',
            'B': 'Do your best',
            'C': 'Use only the supplied data and cite the source field for each claim',
            'D': 'Write something good',
        },
        "answer": 'C',
    },
    {
        "num": 13,
        "domain": 'Prompting & Task Execution',
        "question": 'Why is output format important in automation?',
        "options": {
            'A': 'It makes the model conscious',
            'B': 'Structured output is easier for downstream systems to parse and validate',
            'C': 'It guarantees no errors',
            'D': 'It replaces testing',
        },
        "answer": 'B',
    },
    {
        "num": 14,
        "domain": 'Prompting & Task Execution',
        "question": 'When should an AI task be stopped and clarified before execution?',
        "options": {
            'A': 'When a critical requirement is ambiguous',
            'B': 'Whenever the response is short',
            'C': 'Whenever the model uses a comma',
            'D': 'Never',
        },
        "answer": 'A',
    },
    {
        "num": 15,
        "domain": 'Output Evaluation & Validation',
        "question": 'An AI gives a confident answer with a citation that does not actually support the claim. What is this primarily an example of?',
        "options": {
            'A': 'Successful validation',
            'B': 'A citation mismatch requiring verification',
            'C': 'Perfect grounding',
            'D': 'Model calibration',
        },
        "answer": 'B',
    },
    {
        "num": 16,
        "domain": 'Output Evaluation & Validation',
        "question": 'What is the most important reason to verify high-impact AI outputs?',
        "options": {
            'A': 'AI outputs can be plausible but wrong',
            'B': 'AI cannot produce text',
            'C': 'Verification makes answers longer',
            'D': "It improves the model's training automatically",
        },
        "answer": 'A',
    },
    {
        "num": 17,
        "domain": 'Output Evaluation & Validation',
        "question": 'A model invents a nonexistent study. What is the best response?',
        "options": {
            'A': 'Publish it because it sounds credible',
            'B': 'Verify the study independently and remove unsupported claims',
            'C': 'Add more adjectives',
            'D': 'Ask the model to cite itself',
        },
        "answer": 'B',
    },
    {
        "num": 18,
        "domain": 'Output Evaluation & Validation',
        "question": 'Which evidence is strongest for validating a factual claim?',
        "options": {
            'A': 'A confident tone',
            'B': 'An independently checked authoritative source',
            'C': 'A longer paragraph',
            'D': 'A high temperature setting',
        },
        "answer": 'B',
    },
    {
        "num": 19,
        "domain": 'Output Evaluation & Validation',
        "question": 'What does calibration concern in AI-assisted decisions?',
        "options": {
            'A': 'Whether confidence corresponds reasonably to actual correctness',
            'B': 'Whether the interface is colorful',
            'C': 'Whether the prompt is short',
            'D': 'Whether a model has a logo',
        },
        "answer": 'A',
    },
    {
        "num": 20,
        "domain": 'Output Evaluation & Validation',
        "question": 'A generated spreadsheet total differs from the source ledger. What should happen next?',
        "options": {
            'A': 'Use the AI total because it is faster',
            'B': 'Reconcile the discrepancy against the source data',
            'C': 'Average the two totals',
            'D': 'Delete the source ledger',
        },
        "answer": 'B',
    },
    {
        "num": 21,
        "domain": 'Output Evaluation & Validation',
        "question": 'Which evaluation method is strongest for a recurring workflow?',
        "options": {
            'A': 'Evaluate one random output once',
            'B': 'Define explicit criteria and test representative cases',
            'C': 'Judge by tone only',
            'D': 'Skip evaluation after deployment',
        },
        "answer": 'B',
    },
    {
        "num": 22,
        "domain": 'Output Evaluation & Validation',
        "question": 'Why are edge cases important in AI evaluation?',
        "options": {
            'A': 'They reveal failure modes that common examples may miss',
            'B': 'They make the model larger',
            'C': 'They guarantee success',
            'D': 'They remove the need for users',
        },
        "answer": 'A',
    },
    {
        "num": 23,
        "domain": 'Output Evaluation & Validation',
        "question": 'An AI summarizes a report and omits a critical exception. What should the reviewer check?',
        "options": {
            'A': 'Only grammar',
            'B': 'Completeness against the source and the task requirements',
            'C': 'Font size',
            'D': 'Word count only',
        },
        "answer": 'B',
    },
    {
        "num": 24,
        "domain": 'Output Evaluation & Validation',
        "question": 'What is a good human-in-the-loop trigger?',
        "options": {
            'A': 'Every trivial response',
            'B': 'A defined condition where errors are costly or uncertainty is material',
            'C': 'Never review anything',
            'D': 'Review only outputs with emojis',
        },
        "answer": 'B',
    },
    {
        "num": 25,
        "domain": 'Output Evaluation & Validation',
        "question": 'Which statement about fluent AI text is correct?',
        "options": {
            'A': 'Fluency is evidence of correctness',
            'B': 'Fluency alone does not establish factual accuracy',
            'C': 'Fluency prevents hallucinations',
            'D': 'Fluency replaces source checking',
        },
        "answer": 'B',
    },
    {
        "num": 26,
        "domain": 'Output Evaluation & Validation',
        "question": 'A model extracts customer IDs and sometimes swaps two digits. What is an appropriate validation check?',
        "options": {
            'A': 'Compare extracted IDs with the source using deterministic checks',
            'B': 'Accept every output',
            'C': 'Ask for more adjectives',
            'D': 'Change the font',
        },
        "answer": 'A',
    },
    {
        "num": 27,
        "domain": 'Output Evaluation & Validation',
        "question": 'What is a benchmark useful for?',
        "options": {
            'A': 'Comparing system performance against defined tasks or criteria',
            'B': 'Guaranteeing future performance',
            'C': 'Replacing all user judgment',
            'D': 'Making prompts private',
        },
        "answer": 'A',
    },
    {
        "num": 28,
        "domain": 'Output Evaluation & Validation',
        "question": "If an AI recommendation affects a person's eligibility for a critical service, what is generally appropriate?",
        "options": {
            'A': 'Automate without oversight',
            'B': 'Use stronger validation and appropriate human review',
            'C': 'Hide the recommendation',
            'D': 'Treat confidence as proof',
        },
        "answer": 'B',
    },
    {
        "num": 29,
        "domain": 'Output Evaluation & Validation',
        "question": 'Which is the best way to test whether a summary preserves key meaning?',
        "options": {
            'A': 'Compare it against source claims and required points',
            'B': 'Count adjectives',
            'C': 'Measure paragraph length only',
            'D': 'Ask the model whether it is correct',
        },
        "answer": 'A',
    },
    {
        "num": 30,
        "domain": 'Output Evaluation & Validation',
        "question": 'What is a false positive in a classification workflow?',
        "options": {
            'A': 'The system flags something that should not have been flagged',
            'B': 'The system misses a true case',
            'C': 'The system is offline',
            'D': 'The user changes the password',
        },
        "answer": 'A',
    },
    {
        "num": 31,
        "domain": 'Output Evaluation & Validation',
        "question": 'What is a false negative?',
        "options": {
            'A': 'A correct case is incorrectly flagged',
            'B': 'A true case is missed',
            'C': 'A response is too long',
            'D': 'A model returns JSON',
        },
        "answer": 'B',
    },
    {
        "num": 32,
        "domain": 'Output Evaluation & Validation',
        "question": 'Why should evaluation data resemble real use?',
        "options": {
            'A': 'It makes testing more representative of actual failure modes',
            'B': 'It makes models smarter automatically',
            'C': 'It avoids all edge cases',
            'D': 'It removes privacy obligations',
        },
        "answer": 'A',
    },
    {
        "num": 33,
        "domain": 'Output Evaluation & Validation',
        "question": "A model's answer is unsupported but happens to be correct. Is that enough for a high-stakes workflow?",
        "options": {
            'A': 'Yes, correctness by chance is sufficient',
            'B': 'No; the process still needs reliable evidence and validation',
            'C': 'Yes, if the answer is fluent',
            'D': 'Only if the prompt is long',
        },
        "answer": 'B',
    },
    {
        "num": 34,
        "domain": 'Output Evaluation & Validation',
        "question": 'What is the best response to uncertainty in a high-impact AI output?',
        "options": {
            'A': 'Hide it',
            'B': "Expose or route uncertainty according to the workflow's review policy",
            'C': 'Convert it to certainty',
            'D': 'Ignore it',
        },
        "answer": 'B',
    },
    {
        "num": 35,
        "domain": 'Output Evaluation & Validation',
        "question": 'Why can multiple independent checks be useful?',
        "options": {
            'A': 'They can catch different classes of errors',
            'B': 'They guarantee zero errors',
            'C': 'They eliminate source data',
            'D': 'They reduce accountability',
        },
        "answer": 'A',
    },
    {
        "num": 36,
        "domain": 'Output Evaluation & Validation',
        "question": 'A generated answer conflicts with a trusted internal record. Which should be preferred for a factual business decision?',
        "options": {
            'A': 'The generated answer',
            'B': 'The trusted record, unless verified evidence establishes otherwise',
            'C': 'Whichever is longer',
            'D': 'Whichever sounds more confident',
        },
        "answer": 'B',
    },
    {
        "num": 37,
        "domain": 'Output Evaluation & Validation',
        "question": 'What is a useful acceptance criterion for an extraction system?',
        "options": {
            'A': 'It should be good',
            'B': 'Required fields must be present and match source values within defined rules',
            'C': 'It should sound natural',
            'D': 'It should be creative',
        },
        "answer": 'B',
    },
    {
        "num": 38,
        "domain": 'Output Evaluation & Validation',
        "question": 'When is human review especially important?',
        "options": {
            'A': 'When consequences of error are significant or the task is outside validated scope',
            'B': 'When the output is one sentence',
            'C': 'Only on weekends',
            'D': 'Never',
        },
        "answer": 'A',
    },
    {
        "num": 39,
        "domain": 'Output Evaluation & Validation',
        "question": "A model passes a benchmark but fails on your organization's real data. What does this demonstrate?",
        "options": {
            'A': 'Benchmark performance does not guarantee task-specific performance',
            'B': 'Benchmarks are always useless',
            'C': 'Your data must be wrong',
            'D': 'The model is necessarily broken',
        },
        "answer": 'A',
    },
    {
        "num": 40,
        "domain": 'Product & Model Selection',
        "question": 'When selecting a model for a task, which trade-off should be considered?',
        "options": {
            'A': 'Quality, latency, cost, context needs, and task requirements',
            'B': 'Brand color only',
            'C': 'Number of buttons',
            'D': 'Logo design',
        },
        "answer": 'A',
    },
    {
        "num": 41,
        "domain": 'Product & Model Selection',
        "question": 'A simple classification task has strict latency requirements. Which choice is often reasonable?',
        "options": {
            'A': 'Use the most expensive model regardless of need',
            'B': 'Choose a sufficiently capable lower-latency model and validate it',
            'C': 'Use no model',
            'D': 'Increase prompt length indefinitely',
        },
        "answer": 'B',
    },
    {
        "num": 42,
        "domain": 'Product & Model Selection',
        "question": 'Why might a larger model be unnecessary?',
        "options": {
            'A': 'The task may not require its additional capability',
            'B': 'Large models cannot generate text',
            'C': 'Smaller models are always more accurate',
            'D': 'Cost never matters',
        },
        "answer": 'A',
    },
    {
        "num": 43,
        "domain": 'Product & Model Selection',
        "question": 'What does context length describe?',
        "options": {
            'A': 'How much input/context a model can process within its limits',
            'B': 'How many users can log in',
            'C': 'The number of GPUs in a company',
            'D': 'How long a company has existed',
        },
        "answer": 'A',
    },
    {
        "num": 44,
        "domain": 'Product & Model Selection',
        "question": 'Why can repeatedly extending a long conversation be undesirable?',
        "options": {
            'A': 'Irrelevant or stale context can accumulate and increase complexity or cost',
            'B': 'Models stop working after five messages',
            'C': 'It always improves accuracy',
            'D': 'It deletes the system prompt',
        },
        "answer": 'A',
    },
    {
        "num": 45,
        "domain": 'Product & Model Selection',
        "question": 'What should guide the choice between a fast model and a more capable model?',
        "options": {
            'A': 'The actual quality and latency requirements of the task',
            'B': 'Personal preference only',
            'C': 'Model name length',
            'D': 'The number of vowels in the name',
        },
        "answer": 'A',
    },
    {
        "num": 46,
        "domain": 'Product & Model Selection',
        "question": 'If two models meet quality requirements, what is a sensible tie-breaker?',
        "options": {
            'A': 'Consider cost, latency, reliability, and operational constraints',
            'B': 'Choose randomly',
            'C': 'Choose the newest logo',
            'D': 'Use both without testing',
        },
        "answer": 'A',
    },
    {
        "num": 47,
        "domain": 'Product & Model Selection',
        "question": 'Why should model selection be tested on representative workloads?',
        "options": {
            'A': 'Model rankings can differ by task',
            'B': 'All models behave identically',
            'C': "Testing changes the model's training",
            'D': 'It eliminates governance',
        },
        "answer": 'A',
    },
    {
        "num": 48,
        "domain": 'Product & Model Selection',
        "question": 'What is vendor neutrality in AI practice?',
        "options": {
            'A': 'Designing decisions and concepts so they are not unnecessarily tied to one vendor',
            'B': 'Never using vendors',
            'C': 'Using only open-source software',
            'D': 'Avoiding documentation',
        },
        "answer": 'A',
    },
    {
        "num": 49,
        "domain": 'Product & Model Selection',
        "question": 'A workflow needs image understanding but the selected model only supports text. What is the primary issue?',
        "options": {
            'A': 'Capability mismatch',
            'B': 'Prompt formatting',
            'C': 'Human resources',
            'D': 'File naming',
        },
        "answer": 'A',
    },
    {
        "num": 50,
        "domain": 'Product & Model Selection',
        "question": 'What should be checked before adopting a new AI product in an organization?',
        "options": {
            'A': 'Capabilities, limitations, security, privacy, cost, and fit for purpose',
            'B': 'Only the marketing page',
            'C': 'Only the logo',
            'D': 'Only the demo',
        },
        "answer": 'A',
    },
    {
        "num": 51,
        "domain": 'Product & Model Selection',
        "question": "Why is 'best model' an incomplete question?",
        "options": {
            'A': 'Best depends on the task, constraints, and evaluation criteria',
            'B': 'There is only one AI model',
            'C': 'Models cannot be compared',
            'D': 'The question is illegal',
        },
        "answer": 'A',
    },
    {
        "num": 52,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'A workflow begins with an email, extracts fields, checks policy, and creates a draft response. What should be designed first?',
        "options": {
            'A': 'The workflow stages, inputs, outputs, and decision points',
            'B': 'The color of the interface',
            'C': 'A random prompt',
            'D': 'The final logo',
        },
        "answer": 'A',
    },
    {
        "num": 53,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'Which task is most suitable for deterministic logic rather than an LLM?',
        "options": {
            'A': 'Checking whether an invoice total equals the sum of line items',
            'B': 'Writing a nuanced explanation',
            'C': 'Brainstorming slogans',
            'D': 'Summarizing an interview',
        },
        "answer": 'A',
    },
    {
        "num": 54,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'Why combine AI with deterministic validation?',
        "options": {
            'A': 'AI handles flexible language while deterministic checks enforce precise rules',
            'B': 'It makes AI conscious',
            'C': 'It eliminates all errors',
            'D': 'It removes the need for data',
        },
        "answer": 'A',
    },
    {
        "num": 55,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'A workflow has an AI step followed by an irreversible financial action. What is prudent?',
        "options": {
            'A': 'Add validation and an appropriate approval gate before the irreversible action',
            'B': 'Let the model act without checks',
            'C': 'Remove all logs',
            'D': 'Increase creativity',
        },
        "answer": 'A',
    },
    {
        "num": 56,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'What is a useful workflow boundary?',
        "options": {
            'A': 'A clear definition of what the AI may do and where control returns to a person or system',
            'B': 'No limits',
            'C': 'Only a visual border',
            'D': 'A longer prompt',
        },
        "answer": 'A',
    },
    {
        "num": 57,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'A workflow repeatedly fails because the AI receives inconsistent input formats. What is a strong fix?',
        "options": {
            'A': 'Normalize or validate inputs before the AI step',
            'B': 'Ask the model to guess',
            'C': 'Delete input validation',
            'D': 'Add emojis',
        },
        "answer": 'A',
    },
    {
        "num": 58,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'What does a human approval gate accomplish?',
        "options": {
            'A': 'It requires a designated person to review before a defined consequential action',
            'B': 'It guarantees the model is correct',
            'C': 'It trains the model automatically',
            'D': 'It removes accountability',
        },
        "answer": 'A',
    },
    {
        "num": 59,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'Why should workflow failure modes be mapped?',
        "options": {
            'A': 'To identify where errors can occur and what controls are needed',
            'B': 'To make diagrams prettier',
            'C': 'To avoid testing',
            'D': 'To increase token usage',
        },
        "answer": 'A',
    },
    {
        "num": 60,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'A workflow uses AI to draft customer replies but sends nothing automatically. What risk is reduced?',
        "options": {
            'A': 'Unreviewed AI text reaching customers',
            'B': 'All privacy risk',
            'C': 'All hallucinations',
            'D': 'All operational cost',
        },
        "answer": 'A',
    },
    {
        "num": 61,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'What is idempotency useful for in automated workflows?',
        "options": {
            'A': 'Preventing repeated execution from causing unintended duplicate effects',
            'B': 'Improving grammar',
            'C': 'Increasing model creativity',
            'D': 'Changing a prompt',
        },
        "answer": 'A',
    },
    {
        "num": 62,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'A process is slow because a model is called three times for information that could be cached. What is an optimization?',
        "options": {
            'A': 'Cache stable results where appropriate',
            'B': 'Add more calls',
            'C': 'Disable monitoring',
            'D': 'Increase randomness',
        },
        "answer": 'A',
    },
    {
        "num": 63,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'Which design is generally more robust?',
        "options": {
            'A': 'Explicit stages with validation and clear failure handling',
            'B': 'One giant opaque step',
            'C': 'No logging',
            'D': 'No constraints',
        },
        "answer": 'A',
    },
    {
        "num": 64,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'What is a fallback path?',
        "options": {
            'A': 'A defined alternative when the primary AI or tool step cannot safely complete',
            'B': 'A backup color',
            'C': 'A second logo',
            'D': 'A longer prompt',
        },
        "answer": 'A',
    },
    {
        "num": 65,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'When should a task be handed to an engineer?',
        "options": {
            'A': 'When required integrations, security controls, reliability, or custom logic exceed no-code capabilities',
            'B': 'Whenever a response has punctuation',
            'C': 'Never',
            'D': 'Only when the model is slow',
        },
        "answer": 'A',
    },
    {
        "num": 66,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'What should a workflow owner define before deployment?',
        "options": {
            'A': 'Success criteria, failure handling, permissions, review points, and monitoring',
            'B': 'Only the prompt',
            'C': 'Only the interface',
            'D': 'Only the model name',
        },
        "answer": 'A',
    },
    {
        "num": 67,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'A workflow has a low-risk AI drafting step and a high-risk approval step. Where should stricter controls concentrate?',
        "options": {
            'A': 'Around the high-risk approval and consequential action',
            'B': 'Only around the drafting font',
            'C': 'Nowhere',
            'D': 'Only in the welcome screen',
        },
        "answer": 'A',
    },
    {
        "num": 68,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'What is a single point of failure in a workflow?',
        "options": {
            'A': 'A component whose failure can stop the entire process',
            'B': 'A successful output',
            'C': 'A user guide',
            'D': 'A prompt example',
        },
        "answer": 'A',
    },
    {
        "num": 69,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'Why separate AI generation from action execution?',
        "options": {
            'A': 'It allows output validation before side effects occur',
            'B': 'It makes models larger',
            'C': 'It guarantees no hallucinations',
            'D': 'It removes the need for permissions',
        },
        "answer": 'A',
    },
    {
        "num": 70,
        "domain": 'Workflow Integration & Solution Design',
        "question": 'What should happen when an AI workflow encounters an input outside its validated scope?',
        "options": {
            'A': 'Stop, route to fallback, or request human handling according to policy',
            'B': 'Guess silently',
            'C': 'Act anyway',
            'D': 'Delete the input',
        },
        "answer": 'A',
    },
    {
        "num": 71,
        "domain": 'Configuration & Knowledge Management',
        "question": 'What is the purpose of system-level instructions in an AI workflow?',
        "options": {
            'A': 'Set persistent behavior, boundaries, and operating rules',
            'B': 'Store passwords',
            'C': 'Guarantee truth',
            'D': 'Increase screen resolution',
        },
        "answer": 'A',
    },
    {
        "num": 72,
        "domain": 'Configuration & Knowledge Management',
        "question": 'Why is grounding useful?',
        "options": {
            'A': 'It provides relevant source material for the model to use when generating an answer',
            'B': 'It guarantees no errors',
            'C': 'It eliminates permissions',
            'D': 'It replaces evaluation',
        },
        "answer": 'A',
    },
    {
        "num": 73,
        "domain": 'Configuration & Knowledge Management',
        "question": 'A knowledge base contains outdated policies. What is the primary risk?',
        "options": {
            'A': 'The AI may produce answers based on stale information',
            'B': 'The model becomes faster',
            'C': 'The UI changes color',
            'D': 'The prompt becomes shorter',
        },
        "answer": 'A',
    },
    {
        "num": 74,
        "domain": 'Configuration & Knowledge Management',
        "question": 'What is retrieval intended to do in a knowledge workflow?',
        "options": {
            'A': 'Find relevant information from an available corpus for the current task',
            'B': 'Train every model from scratch',
            'C': 'Delete documents',
            'D': 'Guarantee a legal conclusion',
        },
        "answer": 'A',
    },
    {
        "num": 75,
        "domain": 'Configuration & Knowledge Management',
        "question": 'Why should knowledge sources have ownership and update processes?',
        "options": {
            'A': 'To keep information current and accountable',
            'B': 'To make prompts longer',
            'C': 'To avoid all automation',
            'D': 'To increase hallucinations',
        },
        "answer": 'A',
    },
    {
        "num": 76,
        "domain": 'Configuration & Knowledge Management',
        "question": 'A user asks an AI to answer only from an internal handbook. What is a useful instruction?',
        "options": {
            'A': 'Explicitly restrict the answer to the supplied handbook and identify when information is absent',
            'B': 'Tell it to use any source',
            'C': 'Ask it to invent missing policy',
            'D': 'Remove the handbook',
        },
        "answer": 'A',
    },
    {
        "num": 77,
        "domain": 'Configuration & Knowledge Management',
        "question": 'What is context management?',
        "options": {
            'A': 'Selecting, organizing, and maintaining relevant information supplied to an AI task',
            'B': 'Changing screen brightness',
            'C': 'Deleting all instructions',
            'D': 'Increasing network speed',
        },
        "answer": 'A',
    },
    {
        "num": 78,
        "domain": 'Configuration & Knowledge Management',
        "question": 'Why can too much context reduce usefulness?',
        "options": {
            'A': 'Irrelevant or conflicting information can distract or confuse the task',
            'B': 'Models cannot read more than one word',
            'C': 'It always improves accuracy',
            'D': 'It deletes the output',
        },
        "answer": 'A',
    },
    {
        "num": 79,
        "domain": 'Configuration & Knowledge Management',
        "question": 'Which source should normally receive stronger trust in a policy-answering workflow?',
        "options": {
            'A': 'The current authoritative policy repository',
            'B': 'An anonymous social post',
            'C': 'A random old screenshot',
            'D': 'An unverified summary',
        },
        "answer": 'A',
    },
    {
        "num": 80,
        "domain": 'Configuration & Knowledge Management',
        "question": 'What should happen when two knowledge sources conflict?',
        "options": {
            'A': 'Resolve the conflict using source authority, recency, and policy rules',
            'B': 'Pick the longer document',
            'C': 'Pick randomly',
            'D': 'Hide the conflict',
        },
        "answer": 'A',
    },
    {
        "num": 81,
        "domain": 'Configuration & Knowledge Management',
        "question": 'What is a connector generally used for?',
        "options": {
            'A': 'Giving an AI workflow controlled access to an external system or data source',
            'B': 'Changing model weights',
            'C': 'Printing documents',
            'D': 'Replacing all permissions',
        },
        "answer": 'A',
    },
    {
        "num": 82,
        "domain": 'Configuration & Knowledge Management',
        "question": 'Why should connector permissions be scoped narrowly?',
        "options": {
            'A': 'To reduce unnecessary access and limit potential impact',
            'B': 'To make prompts prettier',
            'C': 'To guarantee perfect output',
            'D': 'To increase token usage',
        },
        "answer": 'A',
    },
    {
        "num": 83,
        "domain": 'Configuration & Knowledge Management',
        "question": 'A knowledge document contains confidential information. What should be considered before making it available to an AI system?',
        "options": {
            'A': 'Access controls, privacy, purpose, retention, and applicable policy',
            'B': 'Only document length',
            'C': 'Only formatting',
            'D': 'Only spelling',
        },
        "answer": 'A',
    },
    {
        "num": 84,
        "domain": 'Configuration & Knowledge Management',
        "question": 'What is a good practice for changing a production AI configuration?',
        "options": {
            'A': 'Use versioning, testing, and a controlled change process',
            'B': 'Change it silently',
            'C': 'Delete the old configuration',
            'D': 'Skip validation',
        },
        "answer": 'A',
    },
    {
        "num": 85,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'What is the principle of least privilege?',
        "options": {
            'A': 'Give a system only the access required for its task',
            'B': 'Give every system administrator access',
            'C': 'Remove all permissions',
            'D': 'Allow unrestricted browsing',
        },
        "answer": 'A',
    },
    {
        "num": 86,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'Why is personal data a governance concern in AI workflows?',
        "options": {
            'A': 'Its collection and use may create privacy, security, legal, and ethical obligations',
            'B': 'Personal data is always public',
            'C': 'AI cannot process it',
            'D': 'It improves accuracy automatically',
        },
        "answer": 'A',
    },
    {
        "num": 87,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'What should happen before putting sensitive organizational data into an AI service?',
        "options": {
            'A': 'Check approved-use policy, data handling, permissions, and contractual/privacy requirements',
            'B': 'Upload it immediately',
            'C': 'Assume every service is approved',
            'D': 'Remove all audit logs',
        },
        "answer": 'A',
    },
    {
        "num": 88,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'What is a useful audit trail?',
        "options": {
            'A': 'A record of relevant actions, decisions, inputs/outputs, and approvals appropriate to the workflow',
            'B': 'A list of model colors',
            'C': 'A copy of every password',
            'D': 'A random screenshot',
        },
        "answer": 'A',
    },
    {
        "num": 89,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'Why should AI-generated decisions be attributable to a responsible owner in consequential workflows?',
        "options": {
            'A': 'Someone must be accountable for how the system is used and acted upon',
            'B': 'AI becomes conscious',
            'C': 'It prevents all mistakes',
            'D': 'It removes human responsibility',
        },
        "answer": 'A',
    },
    {
        "num": 90,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'What is data minimization?',
        "options": {
            'A': 'Collecting or exposing only the data necessary for the stated purpose',
            'B': 'Collecting everything',
            'C': 'Deleting all data immediately',
            'D': 'Using the largest dataset possible',
        },
        "answer": 'A',
    },
    {
        "num": 91,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'An employee wants to paste a confidential client contract into a public AI tool. What is the best response?',
        "options": {
            'A': 'Check whether the tool and data use are authorized before sharing',
            'B': 'Paste it anyway',
            'C': 'Remove the client name only and assume it is safe',
            'D': 'Post it publicly first',
        },
        "answer": 'A',
    },
    {
        "num": 92,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'What is prompt injection?',
        "options": {
            'A': "Malicious or unintended instructions in input that attempt to alter an AI system's behavior",
            'B': 'A type of keyboard',
            'C': 'A faster model',
            'D': 'A data backup',
        },
        "answer": 'A',
    },
    {
        "num": 93,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'A retrieved web page contains instructions telling an agent to reveal secrets. What should the agent do?',
        "options": {
            'A': 'Treat the page content as untrusted data and not follow the malicious instruction',
            'B': 'Reveal secrets',
            'C': 'Give the page administrator credentials',
            'D': 'Disable all security',
        },
        "answer": 'A',
    },
    {
        "num": 94,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'Why should external content be treated carefully in tool-using agents?',
        "options": {
            'A': 'It may contain untrusted instructions or manipulated information',
            'B': 'External content is always correct',
            'C': 'It cannot affect workflows',
            'D': 'It is automatically confidential',
        },
        "answer": 'A',
    },
    {
        "num": 95,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'What is a high-risk use case?',
        "options": {
            'A': 'A use where an AI error could cause significant harm or consequential unfair treatment',
            'B': 'A creative slogan',
            'C': 'A casual brainstorm',
            'D': 'A formatting task',
        },
        "answer": 'A',
    },
    {
        "num": 96,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'Why should organizations document acceptable AI use?',
        "options": {
            'A': 'To establish consistent boundaries, responsibilities, and controls',
            'B': 'To prevent all AI use',
            'C': 'To make models faster',
            'D': 'To remove accountability',
        },
        "answer": 'A',
    },
    {
        "num": 97,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'What is bias in an AI system?',
        "options": {
            'A': 'A systematic pattern of disadvantage or distortion that can affect outputs or decisions',
            'B': 'Any model error',
            'C': 'A prompt format',
            'D': 'A software license',
        },
        "answer": 'A',
    },
    {
        "num": 98,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'How can bias risk be investigated?',
        "options": {
            'A': 'Evaluate representative groups and relevant outcomes using appropriate metrics and context',
            'B': 'Ask the model whether it is biased',
            'C': 'Ignore demographic effects',
            'D': 'Use one example',
        },
        "answer": 'A',
    },
    {
        "num": 99,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'Why is human oversight not the same as simply having a human present?',
        "options": {
            'A': 'The person must have authority, information, and time to meaningfully review and intervene',
            'B': 'Any human automatically prevents errors',
            'C': 'Humans cannot make mistakes',
            'D': 'It means no documentation is needed',
        },
        "answer": 'A',
    },
    {
        "num": 100,
        "domain": 'Governance, Risk & Responsible Use',
        "question": "What should happen when a workflow violates an organization's AI policy?",
        "options": {
            'A': 'Stop or contain the workflow and escalate according to governance procedures',
            'B': 'Continue silently',
            'C': 'Delete evidence',
            'D': 'Blame the model',
        },
        "answer": 'A',
    },
    {
        "num": 101,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'Why should access to AI tools be role-based?',
        "options": {
            'A': 'Different roles need different permissions and data access',
            'B': 'Everyone should have identical access',
            'C': 'It increases hallucinations',
            'D': 'It removes security',
        },
        "answer": 'A',
    },
    {
        "num": 102,
        "domain": 'Governance, Risk & Responsible Use',
        "question": 'Which is an example of a consequential side effect?',
        "options": {
            'A': 'Sending a binding financial transaction based solely on an unreviewed AI output',
            'B': 'Generating a draft title',
            'C': 'Reformatting text',
            'D': 'Creating a private brainstorm',
        },
        "answer": 'A',
    },
    {
        "num": 103,
        "domain": 'Troubleshooting & Optimization',
        "question": 'An AI workflow suddenly becomes slower after adding a large document to every request. What is a likely optimization?',
        "options": {
            'A': 'Reduce unnecessary context and retrieve only relevant sections',
            'B': 'Add the document again',
            'C': 'Disable all monitoring',
            'D': 'Increase output length',
        },
        "answer": 'A',
    },
    {
        "num": 104,
        "domain": 'Troubleshooting & Optimization',
        "question": 'A prompt worked yesterday but fails after a policy update. What should be investigated first?',
        "options": {
            'A': 'Whether the inputs, instructions, source data, or workflow assumptions changed',
            'B': 'The monitor brightness',
            'C': "The user's keyboard",
            'D': 'The model logo',
        },
        "answer": 'A',
    },
    {
        "num": 105,
        "domain": 'Troubleshooting & Optimization',
        "question": 'A workflow fails intermittently when a connector times out. What is a robust design response?',
        "options": {
            'A': 'Use timeout handling, retries where safe, and a fallback path',
            'B': 'Retry forever',
            'C': 'Ignore errors',
            'D': 'Delete logs',
        },
        "answer": 'A',
    },
    {
        "num": 106,
        "domain": 'Troubleshooting & Optimization',
        "question": 'Why are logs useful in AI workflows?',
        "options": {
            'A': 'They help diagnose failures, monitor behavior, and support accountability',
            'B': 'They guarantee correctness',
            'C': 'They replace testing',
            'D': 'They prevent all outages',
        },
        "answer": 'A',
    },
    {
        "num": 107,
        "domain": 'Troubleshooting & Optimization',
        "question": "A workflow's accuracy drops after a prompt change. What is the best next step?",
        "options": {
            'A': 'Compare versions against a representative evaluation set',
            'B': 'Assume the new prompt is better',
            'C': 'Delete the test set',
            'D': 'Increase randomness',
        },
        "answer": 'A',
    },
    {
        "num": 108,
        "domain": 'Troubleshooting & Optimization',
        "question": 'What is regression testing?',
        "options": {
            'A': 'Checking that a change did not break previously working behavior',
            'B': 'Deleting old outputs',
            'C': 'Increasing model size',
            'D': 'Changing the UI',
        },
        "answer": 'A',
    },
    {
        "num": 109,
        "domain": 'Troubleshooting & Optimization',
        "question": 'A model produces inconsistent formatting. Which control can help?',
        "options": {
            'A': 'Use a clear schema or structured output requirements and validate the result',
            'B': 'Remove the format requirements',
            'C': 'Ask for more creativity',
            'D': 'Use random examples',
        },
        "answer": 'A',
    },
    {
        "num": 110,
        "domain": 'Troubleshooting & Optimization',
        "question": 'A workflow makes duplicate API calls after a retry. What should be considered?',
        "options": {
            'A': 'Idempotency or deduplication controls',
            'B': 'More retries',
            'C': 'Less logging',
            'D': 'Longer prompts',
        },
        "answer": 'A',
    },
    {
        "num": 111,
        "domain": 'Troubleshooting & Optimization',
        "question": 'Why should optimization consider cost as well as speed?',
        "options": {
            'A': 'A faster workflow can still be uneconomical if it uses excessive resources',
            'B': 'Cost never matters',
            'C': 'Speed always increases quality',
            'D': 'Cost and speed are identical',
        },
        "answer": 'A',
    },
    {
        "num": 112,
        "domain": 'Troubleshooting & Optimization',
        "question": 'A model gives poor answers because relevant documents are not being retrieved. Which layer should be examined first?',
        "options": {
            'A': 'Retrieval and knowledge/context configuration',
            'B': 'Keyboard settings',
            'C': 'Screen resolution',
            'D': 'Logo',
        },
        "answer": 'A',
    },
    {
        "num": 113,
        "domain": 'Troubleshooting & Optimization',
        "question": 'What is a useful first troubleshooting strategy?',
        "options": {
            'A': 'Reproduce the problem, isolate the failing stage, inspect evidence, and test a targeted change',
            'B': 'Change everything at once',
            'C': 'Guess randomly',
            'D': 'Delete all logs',
        },
        "answer": 'A',
    },
    {
        "num": 114,
        "domain": 'Troubleshooting & Optimization',
        "question": 'Why is changing multiple variables at once problematic during diagnosis?',
        "options": {
            'A': 'It becomes difficult to determine which change caused the outcome',
            'B': 'It always improves accuracy',
            'C': 'It reduces documentation',
            'D': 'It makes the model conscious',
        },
        "answer": 'A',
    },
    {
        "num": 115,
        "domain": 'Integrated Scenario',
        "question": 'An AI drafts a procurement recommendation using current prices but cannot verify supplier eligibility. What is the best design?',
        "options": {
            'A': 'Let it approve suppliers automatically',
            'B': 'Use AI for drafting, verify eligibility through an authoritative source, then apply approval controls',
            'C': 'Ignore eligibility',
            'D': 'Use the cheapest supplier automatically',
        },
        "answer": 'B',
    },
    {
        "num": 116,
        "domain": 'Integrated Scenario',
        "question": 'A customer-support agent retrieves a policy and then recommends a refund. The refund exceeds its authorized limit. What should happen?',
        "options": {
            'A': 'Issue it anyway',
            'B': 'Route the case to the appropriate human approval path',
            'C': 'Increase the model temperature',
            'D': 'Delete the policy',
        },
        "answer": 'B',
    },
    {
        "num": 117,
        "domain": 'Integrated Scenario',
        "question": 'A team wants an AI agent to browse the web and update a database. Which control is especially important?',
        "options": {
            'A': 'Constrain tool permissions and validate proposed changes before consequential writes',
            'B': 'Give unrestricted access',
            'C': 'Disable logs',
            'D': 'Allow every webpage instruction',
        },
        "answer": 'A',
    },
    {
        "num": 118,
        "domain": 'Integrated Scenario',
        "question": 'A model is excellent at drafting but occasionally invents numbers. What is the strongest workflow pattern?',
        "options": {
            'A': 'Use deterministic source data and validation checks before numbers reach the final action',
            'B': 'Ask it to sound confident',
            'C': 'Remove source data',
            'D': 'Publish immediately',
        },
        "answer": 'A',
    },
    {
        "num": 119,
        "domain": 'Integrated Scenario',
        "question": 'An organization wants to deploy an AI workflow for a regulated process. What should be established before deployment?',
        "options": {
            'A': 'Governance requirements, data handling, validation, accountability, monitoring, and human review',
            'B': 'Only a catchy name',
            'C': 'Only a longer prompt',
            'D': 'No documentation',
        },
        "answer": 'A',
    },
    {
        "num": 120,
        "domain": 'Integrated Scenario',
        "question": "A user says, 'The AI told me this is definitely correct.' What is the best response?",
        "options": {
            'A': 'Treat confidence as evidence',
            'B': 'Request supporting evidence and independently validate the claim when accuracy matters',
            'C': 'Publish it immediately',
            'D': 'Assume the model has checked the internet',
        },
        "answer": 'B',
    },
]

TOTAL_QUESTIONS = len(QUESTIONS)


def init_state():
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "order" not in st.session_state:
        st.session_state.order = list(range(TOTAL_QUESTIONS))
    if "current" not in st.session_state:
        st.session_state.current = 0
    if "answers" not in st.session_state:
        # answers[question_index] = chosen letter ("A"/"B"/"C"/"D") or None
        st.session_state.answers = [None] * TOTAL_QUESTIONS
    if "finished" not in st.session_state:
        st.session_state.finished = False


def start_quiz(shuffle=True):
    st.session_state.order = list(range(TOTAL_QUESTIONS))
    if shuffle:
        random.shuffle(st.session_state.order)
    st.session_state.current = 0
    st.session_state.answers = [None] * TOTAL_QUESTIONS
    st.session_state.finished = False
    st.session_state.quiz_started = True


def welcome_screen():
    st.title("PCAO-F Practice Quiz")
    st.markdown(
        f"**{TOTAL_QUESTIONS} original practice questions** covering the "
        "PCAO-F blueprint: Prompting & Task Execution, Output Evaluation & "
        "Validation, Product & Model Selection, Workflow Integration & "
        "Solution Design, Configuration & Knowledge Management, Governance "
        "Risk & Responsible Use, and Troubleshooting & Optimization."
    )
    st.write(
        "Pick your answer for each question, move to the next one, and see "
        "your full score and a question-by-question review at the end."
    )
    shuffle = st.checkbox("Shuffle question order", value=True)
    if st.button("Start Quiz", type="primary"):
        start_quiz(shuffle=shuffle)
        st.rerun()


def record_answer(question_index, letter):
    st.session_state.answers[question_index] = letter


def quiz_screen():
    idx_in_order = st.session_state.current
    question_index = st.session_state.order[idx_in_order]
    q = QUESTIONS[question_index]

    progress = (idx_in_order) / TOTAL_QUESTIONS
    st.progress(progress, text=f"Question {idx_in_order + 1} of {TOTAL_QUESTIONS}")

    st.caption(f"Domain: {q['domain']}")
    st.subheader(f"Q{idx_in_order + 1}. {q['question']}")

    letters = ["A", "B", "C", "D"]
    labels = [f"{letter}. {q['options'][letter]}" for letter in letters]

    saved = st.session_state.answers[question_index]
    saved_index = letters.index(saved) if saved in letters else None

    choice_label = st.radio(
        "Choose your answer:",
        labels,
        index=saved_index,
        key=f"radio_{question_index}",
    )
    if choice_label is not None:
        record_answer(question_index, choice_label[0])

    col1, col2, col3 = st.columns([1, 1, 1])

    if idx_in_order > 0:
        if col1.button("Previous"):
            st.session_state.current -= 1
            st.rerun()

    if idx_in_order < TOTAL_QUESTIONS - 1:
        if col2.button("Next", type="primary"):
            if st.session_state.answers[question_index] is None:
                st.warning("Please select an answer before moving on.")
            else:
                st.session_state.current += 1
                st.rerun()
    else:
        if col2.button("Submit Quiz", type="primary"):
            if st.session_state.answers[question_index] is None:
                st.warning("Please select an answer before submitting.")
            else:
                st.session_state.finished = True
                st.rerun()

    if col3.button("Quit"):
        st.session_state.quiz_started = False
        st.rerun()

    answered_count = sum(1 for a in st.session_state.answers if a is not None)
    st.caption(f"Answered so far: {answered_count} / {TOTAL_QUESTIONS}")


def results_screen():
    st.title("Quiz Complete")

    correct = 0
    review_rows = []
    for question_index, q in enumerate(QUESTIONS):
        user_letter = st.session_state.answers[question_index]
        is_correct = user_letter == q["answer"]
        if is_correct:
            correct += 1
        review_rows.append((question_index, q, user_letter, is_correct))

    score_pct = correct / TOTAL_QUESTIONS * 100
    st.subheader(f"Score: {correct} / {TOTAL_QUESTIONS}  ({score_pct:.1f}%)")

    # PCAO-F style cut score reference (720/1000 on the real exam)
    if score_pct >= 72:
        st.success("That meets the PCAO-F reference cut score of 72%. Nice work.")
    else:
        st.info("The PCAO-F reference cut score is 72%. Keep practicing the weaker domains below.")

    # Per-domain breakdown
    st.subheader("Performance by domain")
    domain_stats = {}
    for _, q, user_letter, is_correct in review_rows:
        d = q["domain"]
        stats = domain_stats.setdefault(d, [0, 0])
        stats[1] += 1
        if is_correct:
            stats[0] += 1
    for domain, (right, total) in domain_stats.items():
        st.write(f"**{domain}**: {right}/{total} ({right / total * 100:.0f}%)")

    st.subheader("Question-by-question review")
    for question_index, q, user_letter, is_correct in review_rows:
        label = "✅" if is_correct else "❌"
        with st.expander(f"{label} Q{question_index + 1}: {q['question'][:80]}"):
            st.write(q["question"])
            for letter in ["A", "B", "C", "D"]:
                prefix = ""
                if letter == q["answer"]:
                    prefix = "✓ "
                elif letter == user_letter:
                    prefix = "✗ "
                st.write(f"{prefix}{letter}. {q['options'][letter]}")
            if is_correct:
                st.success(f"Your answer: {user_letter} — Correct")
            else:
                shown = user_letter if user_letter else "No answer"
                st.error(f"Your answer: {shown} — Correct answer: {q['answer']}")

    col1, col2 = st.columns(2)
    if col1.button("Retake Quiz", type="primary"):
        start_quiz(shuffle=True)
        st.rerun()
    if col2.button("Back to Start"):
        st.session_state.quiz_started = False
        st.session_state.finished = False
        st.rerun()


def main():
    init_state()
    if not st.session_state.quiz_started:
        welcome_screen()
    elif st.session_state.finished:
        results_screen()
    else:
        quiz_screen()


if __name__ == "__main__":
    main()