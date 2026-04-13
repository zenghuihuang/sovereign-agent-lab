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

PART_A_PLAIN_CORRECT    = True
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All three conditions (plain, XML, and sandwich) returned correct answers on the baseline dataset using Llama 3.3 70B.
The plain format led the model to pick The Haymarket Vaults, while the structured XML and sandwich formats
led it to pick The Albanach. Both are valid answers since both satisfy the constraints (capacity >= 160, vegan=yes, available).
The strong frontier model handled all formats equally well on this clean, short dataset.
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
The Holyrood Arms (capacity=160, vegan=yes, status=full) is the most dangerous distractor because it satisfies
two of the three criteria — correct capacity and vegan options — and only fails on availability (status=full).
A model skimming the list or relying on partial pattern matching could easily miss the "full" status and incorrectly
recommend it, especially at lower signal-to-noise ratios.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True

PART_C_PLAIN_ANSWER    = "Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """

Interestingly, even Gemma 2 2B which is a smaller model got all three conditions correct, answering "Haymarket Vaults" for all formats.
This suggests the Edinburgh venue dataset, even with distractors, has a sufficiently high signal-to-noise ratio
that both large and small models can extract the answer regardless of presentation format.
The "lost in the middle" effect is more pronounced with much longer contexts where the
relevant information is genuinely buried — our dataset is short enough that even a 2B model handles it well.
"""


# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """ 
Context formatting matters most when the signal-to-noise ratio is low: when documents are long, when there are
many near-miss distractors designed to look almost correct, or when the model is small and has limited capacity
to reason over unstructured text. On short, clean datasets with strong frontier models, all three formats (plain,
XML, sandwich) may perform equally well — the structural scaffolding becomes a meaningful lever only when
the retrieval task is genuinely hard. In production agent systems that pass large context windows to smaller,
faster models, consistent XML or sandwich-style formatting provides a reliability buffer that is cheap to
implement and important when it matters.
"""
