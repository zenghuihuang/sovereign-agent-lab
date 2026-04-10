"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
According to the U-shaped curve in model performance, the position of the answer can affect the performance of the model.
If the right answer is at the beginning or end of the prompt, the model may be more likely to select it, while if it's in the middle,
it may be less likely to be selected. In this case, the correct answer "The Haymarket Vaults" was close to the middle of the list, which may have made it less likely to be selected by the model, while "The Albanach" was at the beginning of the list, making it more likely to be selected.
However, the model still correctly identified "The Haymarket Vaults" as the correct answer in the plain condition, because meta-llama/Llama-3.3-70B-Instruct is a strong frontie-class model that can overcome positon
bias in some cases. In this case, the signal-to-noise ratio is high enough that structural help
isn't needed here, thus the model was able to select the correct answer. Weaker models rely heavily on Primacy (the beginning) and Recency (the end).
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms is the most dangerous: it satisfies capacity AND vegan,
 only failing on status. A model that skims rather than evaluating all three
 constraints will likely pick this one.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
The Part C used a smaller model, which is more likely to be affected by distractors and position bias. However, in this case, the smaller model still correctly identified "The Haymarket Vaults" as the correct answer in all conditions. This suggests that the signal-to-noise ratio was high enough for the smaller model to overcome any potential biases or distractions. 
It also indicates that the model's performance may not always follow the expected U-shaped curve, and that other factors may influence its ability to select the correct answer.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the model is faced with multiple options that satisfy the constraints, and when the model is not strong enough to overcome position bias or distractions. In such cases, the way the information is presented can significantly influence the model's ability to select the correct answer. 
Proper formatting can help highlight relevant information and reduce the likelihood of the model being misled by distractors or position bias. However, now even a smaller model can correctly identify the correct answer regardless of formatting, as seen in Part C.
"""
