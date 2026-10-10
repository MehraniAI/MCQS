import random
import time
import streamlit as st

DOMAINS = {
    "D1": ("Prompting and Task Execution", "14%"),
    "D2": ("Output Evaluation and Validation", "21%"),
    "D3": ("Product and Model Selection", "12%"),
    "D4": ("Workflow Integration and Solution Design", "16%"),
    "D5": ("Configuration and Knowledge Management", "12%"),
    "D6": ("Governance, Risk and Responsible Use", "15%"),
    "D7": ("Troubleshooting and Optimization", "10%"),
}
EXAM_SECONDS = 12 * 6
PASS_SCORE = 720
LETTERS = "ABCDEF"

EXAM_SECONDS = 120 * 60
PASS_SCORE = 720
LETTERS = "ABCDEF"
 
QUESTIONS = [{'domain': 'D1',
  'q': 'Priya works in the HR department of a regulated bank, and the head of HR has asked her to produce a '
       'one-page onboarding guide for new hires before the next intake starts on Monday. She types "Write an '
       'onboarding guide" into Claude and receives a generic five-page document written in a chatty tone '
       "that does not suit the bank's culture. She does have the real onboarding checklist, the list of "
       "compliance rules every new employee must know in their first week, and last year's guide, which "
       'staff praised for being short and clear. Her manager wants a usable first draft by the end of the '
       'day so it can go to legal for review. What should Priya do to get the best draft?',
  'options': ['Re-send the same request several times until one version happens to come out close enough',
              "Supply the checklist, the compliance rules and last year's guide, and state the audience, "
              'length, tone and format she wants',
              'Ask for a much longer guide and trim it down by hand afterwards',
              'Open a new chat with the identical one-line request in case the model behaves differently'],
  'answer': ['B'],
  'multi': False,
  'why': 'Specific source material plus audience, length, tone and format turns a vague task into a '
         'checkable one. Repeating the same vague request only reshuffles the same weak result.'},
 {'domain': 'D1',
  'q': 'A consultant has been hired to deliver a 30-page market analysis for a client in just three days. '
       'His first attempt was a single request asking Claude to write the whole report in one go. The result '
       'was shallow, repeated itself across sections, and contained several figures he cannot trace to any '
       'source, which makes him nervous about putting his name on it. He still has his raw research notes, '
       "interview summaries and the client's original brief, and he knows the client will challenge any "
       'number that cannot be defended. With the deadline approaching, which approach is most likely to '
       'produce a reliable report in the time he has?',
  'options': ['Ask for the full 30 pages again in one request and edit whatever comes back',
              'Tell Claude to skip explaining its reasoning so the output arrives faster',
              'Wait until all research is finished, then request the final text with no outline',
              'Agree an outline first, draft section by section using the supplied notes, and review each '
              'stage before moving on'],
  'answer': ['D'],
  'multi': False,
  'why': 'Staged delegation with supplied sources lets a human catch problems early. One giant request hides '
         'errors until the end.'},
 {'domain': 'D1',
  'q': 'A team lead manages eight people who each use Claude to turn their meeting notes into summaries for '
       'senior managers. She has noticed that the quality varies widely: some summaries come back crisp and '
       'useful, while others ramble and bury the decisions in the middle of long paragraphs. The senior '
       'managers have said they only want the decisions made, the actions assigned and the deadlines, and '
       'they read these on their phones between meetings. She has one summary from last month that she '
       'considers ideal and would like every team member to produce something similar. What is the best way '
       'to improve consistency across the team?',
  'options': ['Share the ideal summary and a short template, and state the audience, the length limit and '
              'what to leave out',
              'Ask team members to try harder when writing their requests',
              'Tell Claude only to be good and professional in every summary',
              'Stop using AI for summaries because quality varies'],
  'answer': ['A'],
  'multi': False,
  'why': 'A concrete example, a template and stated constraints make the output predictable and reusable '
         'across people.'},
 {'domain': 'D1',
  'q': 'A customer support manager has been experimenting with Claude to draft replies to complaints. Her '
       'prompt is simply "Reply to this angry customer," followed by the customer\'s message. The replies '
       'swing between two extremes: some are so soft that they offer no resolution, while others sound '
       "legalistic and cold, quoting terms and conditions at upset people. The company's refund policy is "
       'clear and written down, and the manager can easily describe the tone she wants the team to use, as '
       'well as point to a past reply she considers excellent. She wants consistent, useful drafts that '
       'agents can send with light editing. Which TWO additions would most improve the replies?',
  'options': ['State the refund policy and the outcome the reply should reach',
              'Add a line saying the reply must be perfect',
              'Describe the tone wanted (empathetic, concise, no legal language) and include one good '
              'example reply',
              'Mention that the customer is very important to the business'],
  'answer': ['A', 'C'],
  'multi': True,
  'why': 'Policy and desired outcome plus tone and an example give Claude what it needs. Pressure and '
         'flattery add nothing it can use.'},
 {'domain': 'D1',
  'q': 'An analyst at a research firm is about to ask Claude to analyze 300 open-ended survey responses for '
       'a board paper. The board will use the findings to decide whether to expand a product line, so the '
       'analysis needs to be both useful and defensible. She has the raw responses in a spreadsheet and has '
       'not yet written her request. Colleagues have told her stories of AI output that looked impressive '
       'but could not be checked afterwards, and she does not want to repeat that. Before she writes '
       'anything to Claude, there is one thing she should settle so that the result will be usable and '
       'checkable. What should she define first?',
  'options': ['Which colours the charts should use',
              'How many times to rerun the analysis to see which answer appears most',
              'What the finished analysis must contain, its format, and how she will check key figures '
              'against the raw responses',
              'Nothing yet, since she can judge the output once she sees it'],
  'answer': ['C'],
  'multi': False,
  'why': 'Defining what good looks like, and how it will be checked, comes before delegating. Otherwise '
         'there is no standard to judge against.'},
 {'domain': 'D1',
  'q': 'An associate at a consultancy asks Claude to draft a policy memo for a client about data retention. '
       'The draft reads well, but it includes several confident statements about a specific regulation that '
       'the associate never mentioned in his request, and when he tries to find where those statements came '
       'from he cannot. The memo is intended for a partner who will send it on to the client, so any wrong '
       "claim about the regulation could damage the firm's credibility. Looking back, he realises the "
       'request was very short and gave Claude nothing to rely on. Which TWO prompt practices would have '
       'made this risk easier to manage?',
  'options': ['Ask Claude to list its assumptions and flag anything it is unsure of',
              'Tell Claude never to express uncertainty so the memo reads with authority',
              'Supply the actual regulation text and instruct Claude to rely only on it',
              'Ask for the memo in a more formal tone'],
  'answer': ['A', 'C'],
  'multi': True,
  'why': 'Visible assumptions and supplied source text make unsupported claims easier to spot or prevent. '
         'Suppressing uncertainty makes the problem worse.'},
 {'domain': 'D1',
  'q': 'A marketing coordinator pastes a promotional email into Claude and asks it to "make this email '
       'better." The new version reads smoothly and sounds more energetic, but on closer reading she notices '
       'that it has changed the meaning of one paragraph about eligibility and has dropped the line that '
       'said the discount ends on Friday. The email is scheduled to go to 40,000 customers the next morning, '
       'and the legal team has already approved the original wording. She is unsure whether the problem lies '
       'with the tool or with how she asked. What is the most likely cause, and what is the best fix?',
  'options': ['The model is unreliable, so the coordinator should stop using it for email',
              'The request did not say what better means or what must stay unchanged, so she should state '
              'the goal and list the details that must be kept, including the deadline',
              'Emails should always be rewritten by hand',
              'The coordinator should repeat the same request in capital letters'],
  'answer': ['B'],
  'multi': False,
  'why': 'Vague goals invite changes. Stating the objective and the must-keep details is the fix.'},
 {'domain': 'D1',
  'q': 'A project manager oversees five projects and wants Claude to produce a weekly status report for each '
       'one. In the first week, the reports looked exactly as she wanted, with the same sections in the same '
       'order. In the second week, the format was different and some sections were missing entirely, even '
       'though she described the task in similar words. Each project lead also tends to paste in their '
       'updates in a different layout. She plans to hand the process over to a junior colleague next month '
       'and wants it to work reliably without her constant attention. Which setup most reduces this drift?',
  'options': ['Ask Claude each week to "do the same as last time"',
              'Remind Claude verbally in each chat to keep the format',
              'Let each project lead write their own prompt',
              "Use reusable instructions with a fixed template and a sample report, and provide each week's "
              'data in the same structure'],
  'answer': ['D'],
  'multi': False,
  'why': 'Reusable instructions, a template and consistent inputs give repeatable output. Relying on memory '
         'of earlier chats does not.'},
 {'domain': 'D2',
  'q': 'An analyst at a consulting firm asked Claude to summarize a 40-page vendor report on customer '
       'retention. The summary says customer churn "fell to 4.1 percent per the vendor\'s Q2 data," which '
       "fits nicely with the story her client's deck is trying to tell. The deck goes to the client's "
       'leadership tomorrow morning, and the analyst has the original report open in another window but is '
       'short on time after a long day. She knows that vendor reports often present figures for different '
       'periods or customer groups, and she has no idea whether Claude pulled this number from the right '
       'table. What should she do before using the figure?',
  'options': ['Use it, since Claude summarized a document she supplied',
              'Ask Claude to rate its own confidence in the figure and use it if the answer is high',
              'Find the figure and its context in the original report and correct the summary if it differs',
              'Round the figure to 4 percent so a small error will not matter'],
  'answer': ['C'],
  'multi': False,
  'why': 'Figures that go to a client must be checked against the source. Self-rated confidence is not '
         'validation.'},
 {'domain': 'D2',
  'q': 'A researcher is writing the background section of a paper and asks Claude for supporting references. '
       'Claude returns eight, each with authors, year, journal title and a short description of the finding. '
       'She searches for each one in the university library database and finds six easily, but two cannot be '
       'located anywhere, even when she searches by author and keyword. The descriptions of those two papers '
       'are so well matched to her argument that she is tempted to keep them, because replacing them would '
       'take another day of searching. The paper is due to a supervisor on Friday. How should she treat the '
       'two references she cannot find?',
  'options': ['As possibly fabricated: do not use them until the sources are located, and check the other '
              'six as well',
              'As too new to be indexed, so they are safe to cite',
              'As correct, since Claude would not invent a reference',
              'As acceptable if she cites them with the word "reportedly"'],
  'answer': ['A'],
  'multi': False,
  'why': 'Plausible but nonexistent citations are a known failure. Unverifiable sources should not be used, '
         'and the rest deserve a check too.'},
 {'domain': 'D2',
  'q': 'A finance associate asked Claude to compute sales commissions from a spreadsheet of 800 rows, using '
       'a tiered rate table. Claude returned a clean table with totals per salesperson, and the numbers look '
       'plausible at a glance. Payroll runs in two days, and any overpayment would be awkward to recover '
       'while an underpayment would cause complaints. The associate does not have time to redo everything by '
       'hand, but she wants to be sure of the result before sending it to payroll. Which TWO actions are the '
       'most reliable ways to validate the result?',
  'options': ['Recompute a sample of rows independently with a separate formula or by hand',
              'Accept the totals because Claude calculates quickly',
              'Compare the overall total against the payroll or sales system report',
              'Ask Claude whether it is sure about the totals'],
  'answer': ['A', 'C'],
  'multi': True,
  'why': 'Independent recalculation and reconciliation against another system catch errors. Speed and '
         'self-confirmation do not.'},
 {'domain': 'D2',
  'q': 'An associate in a procurement team asked Claude to summarize a 40-page supplier contract and, with a '
       'busy week ahead, read only the summary before telling his manager the terms were acceptable. Three '
       'weeks later, the team discovers that the contract contains a substantial early termination penalty '
       'that the summary never mentioned. The summary itself was fluent, well organised and accurate in '
       'everything it did say. His manager asks him what went wrong and how the team should avoid the same '
       'problem with other contracts. What kind of error is this, and what should the process include?',
  'options': ['A formatting error that needs a better template',
              'A typing error that spell-check would catch',
              'A one-off error that needs no change to the process',
              'An omission that changes meaning; key clauses should be checked against the source document '
              'before decisions are made'],
  'answer': ['D'],
  'multi': False,
  'why': 'Omissions are hard to see without comparing to the source. For contracts, key clauses must be '
         'checked directly.'},
 {'domain': 'D2',
  'q': 'A compliance colleague needed to know the filing deadline for a regulatory report. To be careful, '
       'she asked two different AI tools the same question, and both returned the same date in the same '
       'month. She now tells the team the date is "verified by two independent tools" and wants to put it in '
       'the project plan, which will drive several other deadlines and the staffing of an entire team for a '
       'month. A more cautious colleague is not sure that two matching answers are enough for something that '
       'has legal consequences if it is wrong. What is the best response to her claim?',
  'options': ['She is right, since agreement between two tools proves it',
              'She is right if both tools are paid versions',
              'Agreement is not independent verification, because both can share the same error; she should '
              "check the regulator's published rule",
              'She is wrong only if the dates differ by a day or more'],
  'answer': ['B'],
  'multi': False,
  'why': 'Models can make the same mistake. For a legal deadline, the primary source is the authority.'},
 {'domain': 'D2',
  'q': "A customer service agent is using Claude to draft replies. For one customer, Claude's draft says "
       "refunds are available for 60 days after purchase. The company's published policy page says 30 days. "
       "The agent is in a hurry, has twelve other tickets waiting, and notes that Claude's answer sounds "
       'more detailed and more certain than the short policy page. A teammate suggests simply sending the '
       'draft because the customer will be happy to hear 60 days, and the difference is not worth the '
       'trouble. What should happen?',
  'options': ["Use Claude's version because it is more detailed",
              'Average the two and say 45 days',
              "Treat the published policy as the authority, correct the answer, and find out why Claude's "
              'answer differed, including whether outdated documents were supplied',
              'Ask Claude to vote again until it agrees with the policy'],
  'answer': ['C'],
  'multi': False,
  'why': 'Authoritative sources outrank fluent output. The mismatch also signals a possible stale-source '
         'problem to fix.'},
 {'domain': 'D2',
  'q': "A company's leadership team is deciding where human review must be built into its use of AI, because "
       'they cannot afford to review everything and do not want to review nothing. They have listed a number '
       'of situations in which staff are already using AI-generated output, ranging from casual to '
       'consequential. The head of risk wants to focus review effort on the cases where an unnoticed mistake '
       'would do real harm to customers or employees. Which TWO situations most clearly need a named person '
       'to review the output first?',
  'options': ["A customer-facing email stating the customer's refund rights",
              'A brainstorm list of ideas for the team offsite',
              'A shortlist of job candidates to interview',
              "A casual rewrite of the user's own private note"],
  'answer': ['A', 'C'],
  'multi': True,
  'why': 'Statements of customer rights and decisions about people carry real consequences. Low-stakes '
         'brainstorming and personal notes do not.'},
 {'domain': 'D2',
  'q': 'A product team receives a report stating that "47.3 percent of customers prefer option B." The '
       'number came from Claude analyzing about 2,000 open comments from a survey. There is no description '
       'of how comments were classified, what counted as a preference, or how unclear comments were handled. '
       'Leadership intends to use the number to choose between two product directions that would each cost '
       'months of engineering time. The analyst who ran the request is proud of how quickly it was done and '
       'would rather not redo it. What should she do first?',
  'options': ['Present it, since the precision suggests careful work',
              'Round it to 50 percent for readability',
              'Delete the figure and avoid numbers altogether',
              'Ask Claude to explain its method, reproduce the count from the raw comments, and spot-check a '
              'sample by hand'],
  'answer': ['D'],
  'multi': False,
  'why': 'Precise-looking numbers are not necessarily accurate. A figure must be reproducible and '
         'spot-checked before it drives a decision.'},
 {'domain': 'D2',
  'q': 'A non-engineer on a finance team asked Claude to write an Excel formula that updates a budget '
       'forecast as new monthly figures are entered. Claude produced a long formula, she pasted it into the '
       'sheet, and it ran without any error message. The numbers it produced look reasonable. The forecast '
       'will guide a decision about how many people to hire in the next quarter, and the formula uses nested '
       'conditions that she does not fully understand. A colleague suggests she simply uses it and watches '
       'for problems. What is the most appropriate step before relying on it?',
  'options': ['Test it with inputs where the correct answer is already known, and have someone competent '
              'review it because the stakes are high',
              'Trust it because no error message appeared',
              'Ask Claude to confirm that the formula is correct',
              'Use it for one month and see whether anyone complains'],
  'answer': ['A'],
  'multi': False,
  'why': 'Running without error is not the same as being correct. Test against known answers and escalate '
         'review when stakes are high.'},
 {'domain': 'D2',
  'q': 'A department manager wants her team to review AI-generated drafts more reliably, because she has '
       'noticed that people tend to approve drafts that look polished and sound confident. Last month, a '
       'draft with an incorrect date and a misspelled client name nearly went out, and was caught only by '
       'chance. She wants to give the team a few concrete habits that will make review dependable even when '
       'people are busy and the draft looks good. Which TWO practices make review more dependable?',
  'options': ['Check claims against primary sources',
              'Treat a confident tone as a sign of accuracy',
              'Use a checklist of must-verify items such as numbers, names, dates and legal claims',
              'Approve anything with professional formatting'],
  'answer': ['A', 'C'],
  'multi': True,
  'why': 'Source checks and a standard checklist make review consistent. Tone and formatting are not '
         'evidence of accuracy.'},
 {'domain': 'D2',
  'q': 'A regional sales manager asked Claude to analyze a spreadsheet of regional sales and report the '
       "quarter's total. Claude's total is about 3 percent lower than the figure shown in the finance "
       'system. Two members of the team argue about which one is right: one says the finance system is '
       'always correct, while the other says Claude processed every row directly and so must be more '
       'accurate. The quarterly review meeting is in two days, and the manager does not want to present a '
       'number that she cannot explain. What is the best next step?',
  'options': ["Use Claude's figure because it was calculated automatically",
              'Reconcile the two: compare row counts, filters, date ranges and definitions to trace the '
              'cause before using either number',
              'Use the finance figure without investigating',
              'Average the two figures'],
  'answer': ['B'],
  'multi': False,
  'why': 'Discrepancies usually have a traceable cause. Finding it prevents repeating the error and shows '
         'which figure is correct.'},
 {'domain': 'D2',
  'q': 'A communications team asked Claude to draft a press statement responding to a news story about a '
       'competitor. The draft says the competitor "was fined by a regulator last year for data misuse." The '
       'draft gives no source for this claim, and the person who ran the request does not remember it from '
       'any other source. The statement is scheduled to go out this afternoon, and the communications '
       'director is travelling and hard to reach. The junior team member who wrote the prompt thinks the '
       'claim sounds right and is inclined to send it. Who should decide whether the statement is released, '
       'and on what basis?',
  'options': ['The AI, since it produced the statement',
              'The junior who wrote the prompt, based on how plausible it sounds',
              'A named human with authority, after the claim is verified against a primary source and '
              'reviewed by legal',
              'No one, since draft statements are never binding'],
  'answer': ['C'],
  'multi': False,
  'why': 'A factual claim about a named company carries legal and reputational risk. A responsible person '
         'must verify it and approve release.'},
 {'domain': 'D2',
  'q': 'An associate asks Claude a question about a tax rule and receives a detailed answer. Unsure, he '
       'types "Are you sure about that?" and Claude replies "Yes, I am confident," adding two further '
       'paragraphs of supporting detail and an example. Relieved, he treats the matter as checked and copies '
       'the answer into a client email. Later, a colleague points out that the associate has not looked at '
       'any tax authority guidance or tested the example against real figures. The associate protests that '
       'he did check, because he asked Claude directly and it said yes. Why is his check insufficient?',
  'options': ['Claude can repeat and elaborate an error confidently, so an independent check against a '
              'source or calculation is still needed',
              'Claude never answers honestly about its own answers',
              'The extra detail proves the answer is wrong',
              'The question should have been asked three times'],
  'answer': ['A'],
  'multi': False,
  'why': 'Asking a model to confirm itself is not independent validation. An external source or calculation '
         'is required.'},
 {'domain': 'D3',
  'q': 'An operations team at a mid-sized online retailer receives about 10,000 short support tickets a day '
       'and must sort them into five fixed categories such as delivery, refunds and account access, so that '
       'each ticket reaches the right team. Cost and speed matter because the volume is high, and the '
       'categories are clearly defined in a short document. The team has also labelled a sample of 500 '
       'tickets by hand over the past month. The head of operations wants a setup that is cheap enough to '
       'run every day but reliable enough that customers with urgent problems are not lost. Which choice '
       'best fits?',
  'options': ['Use the largest, slowest model for every ticket regardless of cost',
              'Use a faster, cheaper model with clear category definitions, test it on the labelled sample, '
              'and have humans review low-confidence tickets',
              'Avoid AI entirely',
              'Choose whichever model is most talked about online'],
  'answer': ['B'],
  'multi': False,
  'why': 'Simple high-volume tasks suit a smaller model, but it should be validated on a labelled sample '
         'with human review for uncertain cases.'},
 {'domain': 'D3',
  'q': 'A consultant has been asked to advise a law firm on which AI tool to adopt for working with '
       'confidential client contracts. Three tools have been shortlisted, and in demonstrations all of them '
       'summarized contracts equally well and answered questions fluently. The partners are impressed by all '
       'three and have asked the consultant to give a clear recommendation framework by the end of the week. '
       'She knows that an error in this decision could put client confidentiality at risk and expose the '
       'firm to professional liability. Which factor should come first in the comparison?',
  'options': ["Data handling terms, retention, access controls and the firm's own confidentiality "
              'obligations',
              'The attractiveness of the interface',
              'The number of features advertised',
              "The tool's popularity in the press"],
  'answer': ['A'],
  'multi': False,
  'why': 'For confidential material, data governance decides whether a tool is even eligible. Capability is '
         'compared afterwards.'},
 {'domain': 'D3',
  'q': 'An associate has spent three hours in one long Claude session on a complex report with many '
       'sections. Early on, he set out a formatting rule and a list of terms to avoid. Now Claude has begun '
       'ignoring the formatting rule and is repeating mistakes that were corrected an hour ago, which is '
       'wasting his time. He is reluctant to start again, because he has made many decisions during the '
       'session and fears losing the thread of the work. The report is due this evening, and he is worried '
       'that a restart will cost him an hour. What is the best action?',
  'options': ['Repeat the rule in capital letters and continue in the same chat',
              'Delete earlier messages and carry on',
              'Ask Claude to summarize the agreed decisions and rules, then start a fresh session with that '
              'summary',
              'Conclude the tool has permanently stopped working'],
  'answer': ['C'],
  'multi': False,
  'why': 'Long sessions drift. A concise summary carried into a new session restores clarity without losing '
         'the work.'},
 {'domain': 'D3',
  'q': 'A department head asks how her team should choose between different model sizes and tiers. Her team '
       'does two kinds of work. The first is quick drafting of routine replies and short messages, where '
       'speed matters and mistakes are easy to spot. The second is a monthly analysis that combines messy '
       'data from several sources, requires multi-step reasoning, and feeds into decisions about budgets. A '
       'colleague suggests using the same model for everything to keep life simple, while another says the '
       'largest model should always be used. What is the sensible approach?',
  'options': ['Use the smallest model for everything to save money',
              'Use the largest model for everything to be safe',
              'Pick a model at random per task',
              'Match the model to the task: a faster, cheaper tier for routine drafting and a more capable '
              'tier for ambiguous multi-step analysis, tested on real examples'],
  'answer': ['D'],
  'multi': False,
  'why': 'Model choice is a trade-off between speed, cost and depth. Matching tier to task, and testing, is '
         'the right approach.'},
 {'domain': 'D3',
  'q': "A client's chief information officer has heard that models now offer very long context windows and "
       'concludes that the company can simply paste in all of its documents at once, a few hundred pages of '
       'policies, contracts and reports, and ask questions across them. He asks the consultant whether this '
       'removes the need for careful preparation of materials and for review of answers. The consultant '
       'wants to give an accurate and balanced view without either overselling or dismissing the technology. '
       'Which TWO statements about this are accurate?',
  'options': ['More text can be provided in one go, but cost and the chance of missed details can still rise',
              'It guarantees that nothing in the pasted material will be missed',
              'Selecting and structuring the relevant material still improves results',
              'Review of the output is no longer necessary'],
  'answer': ['A', 'C'],
  'multi': True,
  'why': 'A larger window helps but does not remove costs, limits or the need to organize input and check '
         'output.'},
 {'domain': 'D3',
  'q': "A mid-sized company uses Claude for some tasks and another vendor's AI for others, because different "
       'teams adopted different tools over time. The finance director wants to rationalize and asks the '
       'consultant how to judge the tools fairly. Team leads have strong opinions, mostly based on early '
       'impressions and brand loyalty, and some have suggested simply asking each tool which one is better. '
       'The consultant needs a method that is fair, repeatable and defensible in front of the board. What is '
       'the best approach?',
  'options': ['Choose the one with the better-known brand',
              'Test both on the same real tasks using the same criteria, such as accuracy, cost and data '
              'terms, and compare the results',
              'Ask each tool which one is better',
              'Choose whichever the most senior person prefers'],
  'answer': ['B'],
  'multi': False,
  'why': 'A vendor-neutral comparison uses identical tasks and criteria, not brand or self-assessment.'},
 {'domain': 'D3',
  'q': 'A customer service team wants very fast replies for live chat triage, where customers wait in real '
       'time and each response is short, and also wants deep, careful work for a quarterly analysis that '
       'goes to the board and may take an hour to run. A manager suggests using a single model setting for '
       'both jobs to keep configuration simple and avoid confusing staff. An engineer on the team is worried '
       'that one setting will be either too slow for chat or too shallow for the analysis. What is the '
       'better design?',
  'options': ['Use different model tiers for the two jobs, matching speed and cost to triage and depth to '
              'the analysis, and test each',
              'Use one setting for both, since simplicity matters most',
              'Use the slowest model for both',
              'Use the fastest model for both'],
  'answer': ['A'],
  'multi': False,
  'why': 'Different jobs have different needs. Tiering by task is a standard trade-off, validated by '
         'testing.'},
 {'domain': 'D4',
  'q': 'In a customer service process at an insurance company, Claude drafts replies and a human agent '
       'reviews and sends them. After a month, agents complain that they rewrite almost every draft from '
       'scratch, so no time is saved and some feel the tool is slowing them down. A manager, frustrated by '
       'the lack of results, proposes removing the human review step and letting drafts go out directly, on '
       'the theory that the agents are just being fussy. Before any decision is made, the team lead wants to '
       'understand why the drafts are so poor. What should be diagnosed first?',
  'options': ['Whether to replace the agents with a second AI',
              'Whether the prompt, templates, examples and source information given to Claude are good '
              'enough to draft well',
              'Whether to add another AI step after the first',
              'Whether to stop drafting altogether'],
  'answer': ['B'],
  'multi': False,
  'why': 'Poor drafts usually point to weak inputs or instructions. Fix those before removing a safeguard.'},
 {'domain': 'D4',
  'q': 'A company is automating several steps in its operations with AI and has to decide where human '
       'approval is needed. The operations director does not want to slow things down unnecessarily, but she '
       'also remembers an earlier incident in which an automated action caused real damage. She asks the '
       'team to propose clear criteria for when a human must approve an action before it is carried out. '
       'Which TWO reasons most clearly justify putting a human approval step before an AI-triggered action?',
  'options': ['The action cannot be undone',
              'The action is trivial and easy to reverse',
              "The action affects a customer's money or legal rights",
              'The AI wrote its answer in a hesitant tone'],
  'answer': ['A', 'C'],
  'multi': True,
  'why': 'Irreversible actions and actions affecting money or rights warrant human approval. Tone is not a '
         'risk signal.'},
 {'domain': 'D4',
  'q': 'A company wants to roll out an AI-assisted drafting process to 200 staff across three departments '
       'next week. So far, the process has only been tried by the person who designed it, who is an '
       'enthusiast and knows the tool well. Some managers are keen to launch everywhere at once so that the '
       'benefits arrive sooner, while others are nervous about unforeseen problems with customer '
       'communications. The project sponsor asks for the approach that best balances speed and safety. What '
       'is the best approach?',
  'options': ['Launch to all 200 at once to save time',
              'Let each staff member invent their own rules',
              'Skip testing because the designer is experienced',
              'Pilot with a small group, measure quality and errors, fix the problems found, then expand'],
  'answer': ['D'],
  'multi': False,
  'why': 'Pilots reveal real-world problems at low cost. Measure, adjust, then scale.'},
 {'domain': 'D4',
  'q': 'A five-step AI workflow at a logistics company reads a shipping document, extracts key fields, '
       'checks them against an order system, drafts a customer notification and then formats it for sending. '
       'The final notification contains errors, such as the wrong delivery date for some customers. The team '
       'is unsure which step is responsible, and several people have already started rewriting prompts in '
       'different steps, which is making it even harder to understand what is happening. Management wants '
       'the problem fixed within a few days. What is the most efficient way to find the cause?',
  'options': ['Inspect the output of each step in order to find where the error first appears',
              'Rewrite all five steps from scratch',
              'Ask the AI to say who is to blame',
              'Remove the last step and hope it helps'],
  'answer': ['A'],
  'multi': False,
  'why': 'Tracing step by step isolates the failing stage so only that part needs fixing.'},
 {'domain': 'D4',
  'q': "A consultant has redesigned a team's monthly reporting process using AI to draft the first version "
       'of each report. After a month, the team lead sends a message saying the team loves it, and the '
       "consultant is preparing a summary for the client's director. The director has asked for evidence "
       'that the redesign worked, and will compare it with the manual process the team ran before. The '
       'consultant had the foresight to record how long reports took and how many corrections were needed '
       'before the change. Which result is the strongest evidence that the redesign worked?',
  'options': ['Staff say they enjoy the new tools',
              'The number of prompts written has increased',
              'Time per report fell while the error rate stayed the same or improved, compared with the '
              'baseline measured before',
              'The tool has more features than the old one'],
  'answer': ['C'],
  'multi': False,
  'why': 'Evidence of improvement is measured against a baseline on time and quality, not opinion or '
         'activity.'},
 {'domain': 'D4',
  'q': 'A manager at a manufacturing company has been told by the CEO to "add AI" to the procurement '
       'process, and wants to move quickly to show results. He has not yet spent time observing how the '
       'process runs today: purchase requests come in by email, are checked by a buyer, approved by a budget '
       'holder, and then ordered. Some requests wait for days, and some contain errors, but he does not know '
       'how often or why. A vendor has offered to demonstrate a tool that promises to automate procurement. '
       'What should happen first?',
  'options': ['Buy the most capable tool available',
              'Map the current process, find where time is lost or errors occur, and decide where AI could '
              'actually help',
              'Announce the AI project to the whole company',
              'Remove existing approval steps to make room for AI'],
  'answer': ['B'],
  'multi': False,
  'why': 'Understanding the current process shows where AI helps, and where it should not be used.'},
 {'domain': 'D4',
  'q': 'A finance team uses Claude in a workflow to categorize expense claims into accounting codes. Results '
       'vary from run to run: similar claims sometimes get different codes, and the finance staff have '
       'started to double-check everything, which defeats the purpose of the tool. The workflow currently '
       'consists of a short instruction and a free-text claim pasted in, with no defined list of codes and '
       'no check on the output. The finance controller wants the results to be consistent and trusted, and '
       'is willing to invest a little effort in the design. Which change most improves consistency?',
  'options': ['Ask for more creative wording',
              'Switch to a different font in the report',
              'Accept the variation as normal',
              'Use a clear template, defined inputs and categories, and a validation step with stated '
              'criteria'],
  'answer': ['D'],
  'multi': False,
  'why': 'Structure and validation reduce variation and make output trustworthy.'},
 {'domain': 'D4',
  'q': "A company's leadership is reviewing a list of tasks that could be handed to AI, because the board "
       'has asked for a clear policy on what is acceptable. The list contains drafts, summaries, decisions '
       'and filings of many kinds. The head of legal wants the policy to encourage useful uses while '
       'ensuring that anything with serious consequences for people keeps a human accountable. Which TWO of '
       'the following are sensible candidates for AI assistance with appropriate controls?',
  'options': ['First drafts of routine internal communications reviewed by the sender',
              'Final decisions on employee dismissals with no human review',
              'Summaries of long documents that a person will read and check before acting',
              'Autonomous legal filings submitted with no oversight'],
  'answer': ['A', 'C'],
  'multi': True,
  'why': 'AI works well for drafts and summaries that a human reviews. Consequential decisions and filings '
         'need human accountability.'},
 {'domain': 'D4',
  'q': 'A company uses a script to pay supplier invoices automatically from totals that Claude extracts from '
       'scanned invoices. Last month, one total was misread as ten times its true value, and the invoice was '
       'paid before anyone noticed. The finance director is annoyed but does not want to abandon the '
       'automation, because it saves the team about twenty hours a week. She asks the consultant to redesign '
       'the process so that this kind of error is caught while most of the time savings are kept. Which '
       'redesign is best?',
  'options': ['Tell Claude in the prompt to be extra careful with numbers',
              'Add validation against the purchase order, require human approval for amounts over a '
              'threshold or failing validation, and audit a sample regularly',
              'Remove validation to speed things up since errors are rare',
              'Ask Claude to double-check its own extraction in the same step'],
  'answer': ['B'],
  'multi': False,
  'why': 'Independent validation, targeted approval and audit keep the speed without relying on the same '
         'system to check itself.'},
 {'domain': 'D4',
  'q': 'A retailer wants to send AI-written refund decisions directly to customers with no review, in order '
       'to respond within minutes. Most refunds are routine, for example a damaged item with a clear photo, '
       'but a few involve very large amounts, signs of possible fraud, or unusual situations that the '
       'written policy does not cover. The head of customer experience is excited about the speed, while the '
       'head of risk is concerned about wrongful denials that could trigger complaints to regulators. What '
       'is the most appropriate design?',
  'options': ['Send all decisions automatically since most are routine',
              'Send decisions only at night',
              'Add a human checkpoint for edge cases and high-value refunds, pilot the process, and monitor '
              'results',
              'Let the AI approve and then audit its own decisions'],
  'answer': ['C'],
  'multi': False,
  'why': 'Automation can cover routine cases, but unusual and high-value ones need human review, and the '
         'process should be tested and monitored.'},
 {'domain': 'D5',
  'q': 'A company wants all staff to get a consistent brand voice from Claude in emails, proposals and '
       'social posts. At present, each person writes their own tone instructions at the start of every chat, '
       'so the results vary: some drafts sound formal and stiff, others sound casual and jokey, and some '
       'include slogans that the brand team retired two years ago. The marketing director wants a solution '
       'that does not depend on every employee remembering the rules, and that new staff can pick up '
       'immediately. What is the best configuration approach?',
  'options': ['Ask each user to remember the tone',
              'Put the tone and style rules in shared standing instructions, with a short example',
              'Hope the model learns the tone over time',
              'Prohibit using Claude for drafting'],
  'answer': ['B'],
  'multi': False,
  'why': 'Shared instructions with a clear example apply the same rules to everyone.'},
 {'domain': 'D5',
  'q': 'A team keeps a shared knowledge base of policies, procedures and product information that Claude '
       'draws on when staff ask questions. Over the years the base has grown messy: some documents have no '
       'dates, several exist in multiple versions, and a few contain personal notes that were saved in the '
       'wrong folder. Staff have started to complain that answers are sometimes outdated or contradict one '
       'another. The knowledge manager wants to make the base reliable without spending months on it. Which '
       'TWO practices most improve its quality?',
  'options': ['Give documents clear titles, dates and named owners',
              'Keep several duplicate versions of each file',
              'Remove or archive superseded policies',
              'Mix personal notes into official policy folders'],
  'answer': ['A', 'C'],
  'multi': True,
  'why': 'Clear metadata and removal of outdated material keep the knowledge reliable.'},
 {'domain': 'D5',
  'q': 'The IT department proposes connecting Claude to the company shared drive so that staff can ask '
       'questions about documents without searching for them manually. The drive holds thousands of files, '
       'including finance records, HR files, client contracts and public marketing material, and over the '
       'years permissions have been set inconsistently, with some folders open to everyone. The proposal is '
       'popular with staff, who would love the convenience, and the vendor says setup takes an afternoon. '
       'The security lead asks what should be checked before the connector is switched on. What should be '
       'checked first?',
  'options': ["How attractive the connector's icon is",
              'How many files exist on the drive',
              'How long the connector has existed',
              'What data it can reach, who can use it, and whether access follows least privilege'],
  'answer': ['D'],
  'multi': False,
  'why': 'Connectors extend what the AI can see. Scope and permissions come before convenience.'},
 {'domain': 'D5',
  'q': 'A team has agreed that every answer produced in a certain project must cite the source document it '
       'relied on and must say when the documents do not contain the answer. The rule is important because '
       'the answers are used by customer-facing staff, who may repeat them to customers. At present, team '
       'members include the rule in their chat messages only some of the time, and when they forget, answers '
       'arrive without citations. The team lead wants the rule to apply to every task in the project, '
       'regardless of who asks. Where should the rule be placed?',
  'options': ["In the project's standing instructions",
              'In each individual chat message',
              'In the title of the project',
              'Nowhere; the model will infer it'],
  'answer': ['A'],
  'multi': False,
  'why': 'Standing instructions apply across all tasks, so the rule does not depend on memory.'},
 {'domain': 'D5',
  'q': 'A customer was recently told by an AI assistant that refunds could be requested within 90 days, '
       "which was the policy last year but not now. The company's knowledge base holds the current refund "
       'policy but also old drafts, a superseded version, and several emails pasted in as reference. '
       'Customer service leaders are embarrassed and want a durable fix, not just an apology to this '
       'customer. An engineer suggests several ideas, including adding more documents. Which fix addresses '
       'the cause?',
  'options': ['Add more documents so the right one is likelier to appear',
              'Tell customers the assistant may be wrong',
              'Archive outdated and draft documents, assign an owner to keep content current, and instruct '
              'the assistant to cite its source and flag conflicts',
              'Rely on the assistant to work out which version is newest'],
  'answer': ['C'],
  'multi': False,
  'why': 'Stale and conflicting content causes stale answers. Clean, owned content plus source citation '
         'addresses the root.'},
 {'domain': 'D5',
  'q': 'A team\'s project instructions for Claude include the line "Keep replies under 100 words" and, '
       'further down, "Provide a detailed, thorough explanation with examples for every question." Users '
       'report that replies are inconsistent: sometimes very short and sometimes long and detailed, with no '
       'obvious pattern. Some users suspect the tool has been changed by the vendor and are asking for a '
       'switch to another product. The team lead believes the problem may lie closer to home, and she wants '
       'to find the real cause before spending money on a new tool. What is the most likely cause and the '
       'best fix?',
  'options': ['The model is defective, so switch vendors',
              'The two instructions conflict, so the team should resolve the conflict and state one clear '
              'rule',
              'Users should write longer questions',
              'Instructions never affect output, so remove them'],
  'answer': ['B'],
  'multi': False,
  'why': 'Conflicting instructions produce inconsistent output. Fix the instructions first.'},
 {'domain': 'D5',
  'q': "An associate attaches the company's policy documents to a task before asking Claude to answer staff "
       'questions about leave and expenses. A colleague who is excited about the approach tells the team '
       "that grounding Claude in the company's own documents means hallucinations can no longer happen, so "
       'there is no need to review the answers. The team lead is not sure that is right, particularly since '
       'staff will rely on the answers to make decisions about their own leave and reimbursements. What is '
       'the accurate view?',
  'options': ['Attaching documents grounds answers in the supplied material and reduces guessing, but '
              'answers still need checking',
              'Attaching documents removes all errors',
              "Attaching documents trains the vendor's model for the company",
              'Attaching documents is only useful for long questions'],
  'answer': ['A'],
  'multi': False,
  'why': 'Grounding helps but does not guarantee accuracy. Review is still needed.'},
 {'domain': 'D6',
  'q': "A support team at a telecom company records customer calls, with the customers' consent, for quality "
       'assurance, and the transcripts already sit in an approved Claude workspace. The product team asks an '
       'associate to mine the same transcripts for upsell opportunities to pass to sales. The associate '
       'notes that the data is already in the workspace, the tool is approved, and no new upload would be '
       'needed, so the job would take only an afternoon. The notice customers heard on the call mentioned '
       'quality assurance and training only. What is the most appropriate action?',
  'options': ['Proceed as asked, since the transcripts are already inside an approved workspace and the '
              'analysis needs no new upload',
              'Strip customer names from the transcripts first, then run the upsell analysis inside the '
              'approved workspace',
              'Run the analysis in incognito chats so that the upsell work leaves no trace in the workspace '
              'history',
              'Take it to the data owner, since the transcripts were collected for one purpose and a new use '
              'needs fresh permission'],
  'answer': ['D'],
  'multi': False,
  'why': 'Purpose limitation: consent covered quality assurance, not sales. An approved tool does not make '
         'every use approved, and removing names or hiding the work does not fix the change of purpose.'},
 {'domain': 'D6',
  'q': 'A hospital administrator wants Claude to summarize several hundred patient feedback emails to find '
       'common complaints. Many of the emails contain names, diagnoses and phone numbers. The hospital has '
       "an approved Claude workspace with a data agreement, but the hospital's policy says that any new AI "
       'use involving clinical details requires privacy officer sign-off first. The administrator is under '
       'pressure from the board to report on patient experience next week and suggests that the approved '
       'workspace is good enough. Which TWO actions are most appropriate?',
  'options': ['Start the summaries now, since the workspace is approved',
              'Raise the request with the privacy officer before starting',
              'Paste the emails into a free personal account to avoid delay',
              'Define what data the task actually needs and remove or minimize identifiers where possible'],
  'answer': ['B', 'D'],
  'multi': True,
  'why': 'An approved workspace is not an approved use. Get sign-off and apply data minimization. A personal '
         'account bypasses controls entirely.'},
 {'domain': 'D6',
  'q': 'At a mid-sized company, a staff member is about to paste customer complaint letters, including names '
       'and account details, into an AI tool. When a colleague raises a concern, the staff member replies, '
       '"This AI tool has been approved by IT, so we can put any data into it." In fact, the approval notice '
       'states that the tool was approved for drafting internal documents and marketing content only, and '
       'says nothing about customer personal data. The colleague wants to respond in a way that is accurate '
       'and helpful. What is the best correction?',
  'options': ['Approved tools can take any data',
              'Only names and phone numbers need protecting',
              'Approval is for stated uses and data types, so check whether this data and purpose are '
              'covered before using it',
              'Approval is a formality and can be ignored'],
  'answer': ['C'],
  'multi': False,
  'why': 'Approval is scoped to specific uses and data. Anything outside the scope needs a new decision from '
         'the right owner.'},
 {'domain': 'D6',
  'q': 'A manager at a retail company asks an associate to use Claude to rank 200 job applicants against the '
       'job description and send the top ten straight to interview, with no person looking at the remainder. '
       'The manager says this will save two days and make the process more consistent. The associate notices '
       'that the job description includes requirements that might favour certain backgrounds, and that the '
       'company has no process to check ranking results for fairness. The manager is senior and expects a '
       'quick yes. What is the most appropriate response?',
  'options': ['Proceed, since ranking by AI is more consistent than people',
              'Use Claude to assist the screening, but keep a human reviewing the criteria and the '
              'decisions, and check the results for bias',
              'Remove names and photos and let Claude decide fully',
              'Refuse to use AI anywhere in hiring'],
  'answer': ['B'],
  'multi': False,
  'why': 'Hiring affects people, so humans must stay accountable and bias must be checked. AI can assist, '
         'but not decide alone.'},
 {'domain': 'D6',
  'q': "A company's HR team plans to have Claude evaluate performance reviews written by many different "
       'managers, some of whom rate everyone highly while others are very strict, and to recommend which '
       'employees should be placed on an improvement plan. The head of HR says this will remove human '
       'inconsistency and make decisions fairer. The associate asked to run the analysis has doubts about '
       'how the recommendations will be used, because the plans can affect pay and employment. Which TWO '
       'concerns should the associate raise?',
  'options': ['Inconsistent manager standards could be amplified into biased recommendations',
              'Decisions affecting employment need human judgment and accountability',
              'The recommendations should be applied automatically for consistency',
              'AI is always more objective than managers'],
  'answer': ['A', 'B'],
  'multi': True,
  'why': 'Bias can be carried and amplified by the data, and people affected by a decision need a human who '
         'is accountable for it.'},
 {'domain': 'D6',
  'q': 'A financial services firm asks a consultant whether Claude can draft customer-facing investment '
       "suitability letters, which explain why a particular product suits a particular client. The firm's "
       'compliance officer notes that regulators require documented human accountability for advice, and the '
       "sales director argues that a reputable vendor's tool should be exempt from that burden since it is "
       'so well tested. The consultant needs to give a clear and accurate view on how the firm can use AI '
       'here while meeting its duties. What should the consultant advise?',
  'options': ['AI-generated letters are exempt from regulation if the vendor is reputable',
              'AI can draft, but a qualified human must review and own each letter, with the review process '
              'documented and the limits of AI use defined in advance',
              "The vendor's acceptable-use policy covers the client's regulatory duties",
              'Regulation applies only if a customer complains'],
  'answer': ['B'],
  'multi': False,
  'why': "The client's regulatory duties remain with the client. A documented human review process is "
         'required.'},
 {'domain': 'D6',
  'q': 'A teacher uses Claude to grade 80 student essays against a clear rubric and plans to release the '
       'grades without reading any of them, because the scores look reasonable and she is short of time '
       'before report deadlines. Some students have previously complained about unfair marking, and parents '
       'have asked how grades are decided. A colleague warns her that she may be taking on risk, but she '
       'says the rubric makes the grading objective. What is the most appropriate approach?',
  'options': ['Release the grades because they match the rubric',
              'Tell Claude to grade more strictly to reduce disputes',
              'Spot-check a sample, especially borderline and unusual essays, tell students how AI was used, '
              'and give them a route to request human review',
              'Release the grades without mentioning AI to avoid questions'],
  'answer': ['C'],
  'multi': False,
  'why': 'Spot-checking, transparency and a route to human review give students fair treatment and '
         'accountability.'},
 {'domain': 'D6',
  'q': 'A bank uses an AI tool to help decide loan applications. A routine review finds that the tool '
       'approves a noticeably lower share of applicants from one group than from others with similar '
       'financial profiles, and there is no clear business reason for the difference. The head of lending '
       'points out that the model is accurate overall and the loan volume is high, and suggests waiting '
       'until the annual model review to look into it. The risk officer is uneasy about leaving this for '
       'months. What is the most appropriate response?',
  'options': ['Ignore it, since the model is only statistical',
              'Hide the findings until the next annual review',
              'Keep running it, since overall accuracy is high',
              'Pause or add human review, investigate the cause, and document the corrective action'],
  'answer': ['D'],
  'multi': False,
  'why': 'Evidence of disparate impact requires investigation, human oversight and documentation, not delay '
         'or concealment.'},
 {'domain': 'D6',
  'q': 'After an AI-assisted process wrongly denies a customer a service, a complaint reaches the operations '
       'manager. During the review meeting, a colleague says, "It was the AI\'s fault, not ours," and '
       'suggests replying that the system made the decision, so the company cannot be held responsible. The '
       'customer has been affected financially, and the regulator may ask who was accountable for the '
       'decision. The manager wants to respond in a way that is honest and protects the customer. What is '
       'the best response?',
  'options': ['The organization and the responsible people remain accountable for decisions made with AI, so '
              'the issue must be reviewed and corrected',
              'The AI vendor is solely responsible',
              'No one is accountable when software decides',
              'Only the customer is responsible for checking'],
  'answer': ['A'],
  'multi': False,
  'why': 'AI does not carry accountability. The organization and its people do.'},
 {'domain': 'D7',
  'q': "A team's Claude results were good for several weeks. Then the team added many new instructions to "
       'the project, covering tone, length, formatting, topics to avoid and special cases, one after another '
       'as problems arose. Since then, answers have become inconsistent and sometimes ignore key rules that '
       'previously worked. The team lead is considering switching vendors, while an engineer thinks the '
       "problem may have been introduced by the team's own changes. Before making any big decision, what "
       'should the team check first?',
  'options': ['Whether the new instructions conflict with or overload the existing ones, and simplify them',
              "The speed of the team's computers",
              'The time of day when the requests are made',
              'Nothing; more instructions always improve results'],
  'answer': ['A'],
  'multi': False,
  'why': 'Instruction conflict or overload is a common cause of worse output. Simplify and test.'},
 {'domain': 'D7',
  'q': 'A team uses an agent that browses the web and fills in several forms for them, for example '
       'submitting supplier registration requests. One run fails halfway through, leaving two forms '
       "completed and a third half-filled. The team's first reaction is to run the whole task again ten "
       'times and see whether it eventually works. A more careful colleague suggests that repeating the same '
       'run blindly might create duplicate submissions or make problems harder to see. What is the better '
       'approach?',
  'options': ['Delete the task and avoid agents',
              'Add random delays between steps',
              'Review where it stopped, check access and inputs, and rerun in smaller steps',
              'Run the same task unchanged at a different time'],
  'answer': ['C'],
  'multi': False,
  'why': 'Diagnose where and why it failed, then rerun in smaller steps. Blind repetition does not address '
         'the cause.'},
 {'domain': 'D7',
  'q': "A manager asks Claude several questions about her department's performance. The answers are correct "
       'but generic: they could apply to any company, and use phrases like "consider improving '
       'communication" that she finds unhelpful. She has been giving only short, one-line questions, and she '
       'wants answers specific to her business, her team structure and her goals. Colleagues have suggested '
       'various tricks, including asking in capital letters and requesting much longer answers. What is the '
       'best first fix?',
  'options': ['Ask for longer answers',
              'Add specific context, the audience, constraints and an example of a good answer',
              'Ask the same question in capital letters',
              'Accept generic answers as the best AI can do'],
  'answer': ['B'],
  'multi': False,
  'why': 'Generic input produces generic output. Specific context and an example are the quickest '
         'improvement.'},
 {'domain': 'D7',
  'q': "A team's project instructions include several formatting rules, such as using short paragraphs, "
       'putting key numbers in a summary table, and ending with a list of next steps. Claude follows all of '
       'them except one: it keeps ignoring the rule that dates must be written in day-month-year format. The '
       'rule appears clearly in the instructions, and other rules are followed. The team is tempted to add '
       'many more rules about dates in the hope that one of them will work. Which approach is most likely to '
       'solve it?',
  'options': ['Add ten more rules about formatting',
              'Delete all instructions and start again',
              'Blame the model and stop',
              'State the rule once, clearly and positively, check it does not conflict with other '
              'instructions, and test again'],
  'answer': ['D'],
  'multi': False,
  'why': 'Clear, non-conflicting instructions and testing are the right approach. More rules often cause '
         'more conflict.'},
 {'domain': 'D7',
  'q': 'A workflow at a services firm reads data from a connected tool, such as a project management system, '
       'to prepare weekly updates. Partway through a run, the step that reads from the tool returns an '
       'error, and the rest of the workflow fails. The team has no clear idea whether the problem is with '
       'permissions, the connection, the tool itself or the instructions given to Claude. An impatient '
       'colleague suggests rebuilding the whole workflow from scratch. What is a sensible order of checks?',
  'options': ['Confirm the connection and permissions, test the tool on its own, then rerun the workflow',
              'Rewrite the whole workflow immediately',
              'Ignore the error and continue',
              'Delete the connection permanently'],
  'answer': ['A'],
  'multi': False,
  'why': 'Check the connection, test the tool alone and only then rerun the workflow. Isolating the fault '
         'first saves effort.'},
 {'domain': 'D7',
  'q': 'A company has set up an assistant that is supposed to answer staff questions only from attached '
       'policy documents. Lately, it has begun giving answers that come from general knowledge and do not '
       'match company policy, for example describing a standard industry leave entitlement instead of the '
       "company's own. Staff trust the assistant and have started to repeat these answers to colleagues. The "
       'knowledge manager needs to restore reliable behaviour quickly. What should be checked and done?',
  'options': ['Nothing, since general knowledge is usually fine',
              'Confirm the documents are attached, readable and current, and instruct it to answer only from '
              'them and say when something is not found',
              'Add more general-knowledge questions to the prompt',
              'Remove the documents so the model is less confused'],
  'answer': ['B'],
  'multi': False,
  'why': 'Check the source setup first, then constrain the assistant to the documents and require it to flag '
         'gaps.'}]
 
 
def build_paper(seed=None):
    """Shuffle answer options for each question so the key is not predictable."""
    rng = random.Random(seed)
    paper = []
    for q in QUESTIONS:
        order = list(range(len(q["options"])))
        rng.shuffle(order)
        opts = [q["options"][k] for k in order]
        ans = [LETTERS[order.index(LETTERS.index(a))] for a in q["answer"]]
        paper.append({**q, "options": opts, "answer": sorted(ans)})
    return paper
 
 
def grade(answers, paper):
    """Return (correct_count, per-domain dict, per-question results)."""
    per = {d: [0, 0] for d in DOMAINS}
    results = []
    correct = 0
    for i, q in enumerate(paper):
        chosen = sorted(answers.get(i, []))
        ok = chosen == sorted(q["answer"])
        per[q["domain"]][1] += 1
        if ok:
            per[q["domain"]][0] += 1
            correct += 1
        results.append((ok, chosen))
    return correct, per, results
 
 
def scaled(correct, total=60):
    # Approximation only: 72 percent correct maps to 720 on a 100-1000 scale.
    return max(100, round(correct / total * 1000))
 
 
def reset():
    for k in list(st.session_state.keys()):
        del st.session_state[k]
 
 
def show_timer():
    left = max(0, EXAM_SECONDS - int(time.time() - st.session_state.start))
    st.sidebar.metric("Time left", f"{left // 60:02d}:{left % 60:02d}")
    return left
 
 
def render_start():
    st.title("GCAO-F / PCAO-F Practice Exam")
    st.write("60 scenario questions | 120 minutes | pass mark 720 / 1000 (about 72 percent).")
    st.caption("Practice questions based on the published blueprint. Not real exam items.")
    st.subheader("Blueprint weights")
    st.table({"Domain": [f"{k}: {v[0]}" for k, v in DOMAINS.items()],
              "Weight": [v[1] for v in DOMAINS.values()]})
    st.info("Questions marked SELECT 2 need both correct answers to score.")
    if st.button("Start exam", type="primary"):
        st.session_state.start = time.time()
        st.session_state.paper = build_paper()
        st.session_state.phase = "exam"
        st.rerun()
 
 
def render_exam():
    left = show_timer()
    paper = st.session_state.paper
    st.sidebar.write("Answered:")
    answered = sum(1 for i in range(len(paper)) if st.session_state.get(f"q{i}"))
    st.sidebar.progress(answered / len(paper), text=f"{answered} / {len(paper)}")
    st.title("Exam in progress")
    cur = None
    for i, q in enumerate(paper):
        if q["domain"] != cur:
            cur = q["domain"]
            name, wt = DOMAINS[cur]
            st.header(f"{cur}: {name} ({wt})")
        st.markdown(f"**Q{i + 1}.** {q['q']}")
        labels = [f"{LETTERS[j]}. {o}" for j, o in enumerate(q["options"])]
        if q["multi"]:
            st.caption("SELECT 2")
            picked = st.multiselect("Choose two", labels, key=f"q{i}", label_visibility="collapsed")
        else:
            choice = st.radio("Choose one", labels, index=None, key=f"q{i}", label_visibility="collapsed")
            picked = [choice] if choice else []
        st.session_state[f"ans{i}"] = [p[0] for p in picked]
        st.divider()
    if st.button("Submit exam", type="primary") or left == 0:
        st.session_state.answers = {i: st.session_state.get(f"ans{i}", []) for i in range(len(paper))}
        st.session_state.phase = "result"
        st.rerun()
 
 
def render_result():
    answers = st.session_state.answers
    paper = st.session_state.paper
    correct, per, results = grade(answers, paper)
    score = scaled(correct, len(paper))
    st.title("Results")
    c1, c2, c3 = st.columns(3)
    c1.metric("Correct", f"{correct} / {len(paper)}")
    c2.metric("Approx. scaled score", score)
    c3.metric("Result", "PASS" if score >= PASS_SCORE else "NOT YET")
    st.caption("The scaled score is an approximation for practice. The real exam uses its own scaling.")
    st.subheader("By domain")
    st.table({"Domain": [f"{k}: {DOMAINS[k][0]}" for k in DOMAINS],
              "Correct": [f"{v[0]} / {v[1]}" for v in per.values()],
              "Percent": [f"{round(100 * v[0] / v[1])}%" for v in per.values()]})
    weak = [k for k, v in per.items() if v[0] / v[1] < 0.72]
    if weak:
        st.warning("Review first: " + ", ".join(f"{k} {DOMAINS[k][0]}" for k in weak))
    st.subheader("Review")
    for i, q in enumerate(paper):
        ok, chosen = results[i]
        icon = "OK" if ok else "WRONG"
        with st.expander(f"Q{i + 1} [{icon}] {q['q'][:80]}"):
            st.write(q["q"])
            for j, o in enumerate(q["options"]):
                tag = ""
                if LETTERS[j] in q["answer"]:
                    tag = "  (correct)"
                if LETTERS[j] in chosen:
                    tag += "  (your answer)"
                st.write(f"{LETTERS[j]}. {o}{tag}")
            if q["why"]:
                st.info(q["why"])
    if st.button("Try again"):
        reset()
        st.rerun()
 
 
def main():
    st.set_page_config(page_title="GCAO-F Practice Exam", page_icon="🧠", layout="centered")
    phase = st.session_state.get("phase", "start")
    if phase == "start":
        render_start()
    elif phase == "exam":
        render_exam()
    else:
        render_result()
 
 
if __name__ == "__main__":
    main()