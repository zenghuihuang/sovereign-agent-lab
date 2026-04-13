"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """

AI: How many guests are you confirming for tonight's event?
My answer ->  160 guests
AI: And how many of those guests will need vegan meals?
My answer ->  about 50 need vegan
AI:What deposit amount in GBP are you proposing to secure the booking?
My answer ->  200 deposit
AI:Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?

"""

CONVERSATION_1_OUTCOME = "confirmed"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
AI: calling to confirm a booking
How many guests are you confirming for tonight's event?
My answer  ->  160 guests
AI:And how many of those guests will need vegan meals?
My answer ->  about 50 need vegan
AI:What deposit amount in GBP are you proposing to secure the booking?
My answer ->  500 deposit
AI:I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
My answer  ->  /stop
"""

CONVERSATION_2_OUTCOME = "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """

AI:How many guests are you confirming for tonight's event?
My answer  ->  160 guests
AI:And how many of those guests will need vegan meals?
My answer ->  can you arrange parking for the speakers?
AI:I'm sorry, I'm not trained to help with that.I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?

"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
CALM triggered the handle_out_of_scope flow, delivered a fixed refusal message stating it can only help
with booking confirmation, offered to redirect to the event organiser for other requests, and then asked
whether the user wanted to continue with the confirm booking flow. The current slot collection (vegan_count)
was paused but not abandoned — CALM offered to resume it.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Both agents declined the out-of-scope request without calling any tools. However, the mechanisms are
completely different:

LangGraph (Exercise 2 Scenario 3, train times): The LLM reasoned at runtime about which tools were available,
concluded none matched the question, and generated a natural, helpful refusal including a redirect suggestion
(National Rail website). The behaviour is emergent from the model's reasoning — it is flexible, and a
sufficiently persistent or cleverly-worded user might potentially steer it off-script.

Rasa CALM (Conversation 3, parking): CALM routed the out-of-scope message to the explicit handle_out_of_scope
flow defined in flows.yml and executed a fixed utter_out_of_scope response. This is deterministic and
auditable — the same message fires every time regardless of how the request is phrased. There is no path
by which the user can talk the agent into arranging parking by rephrasing the question. After the refusal,
CALM also offered to resume the interrupted confirm_booking flow, demonstrating that the structured flow
state was preserved.

The key difference is auditability and predictability: LangGraph's response depends on the model's
reasoning at inference time; CALM's response is guaranteed to match whatever was defined in flows.yml
at training time.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
Ran a conversation after 16:45 (it was 19:11 local time) with the Task B block uncommented.
After collecting all three slots (160 guests, 50 vegan, £200 deposit), the action_validate_booking
ran and immediately escalated with the message: "it is past 16:45 — insufficient time to process
the confirmation before the 5 PM deadline". The guard fired correctly before any other guard was
evaluated, demonstrating time-based pre-emption. Task B guard is now permanently uncommented in
the submitted code.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """

"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
CALM required config.yml, domain.yml, flows.yml, endpoints.yml, a train step (rasa train), two running
terminals (action server + shell), and a Rasa Pro licence. That is significant setup overhead compared
to the few dozen lines needed to spin up the LangGraph research agent.

What that setup cost bought: Rasa CALM cannot improvise a response that wasn't defined in flows.yml or
domain.yml. It cannot call a tool that wasn't declared. It cannot go off-script regardless of how the
user phrases a request. Every path through the conversation is readable and auditable before deployment.
This is not a limitation — it is the feature. For the pub-manager confirmation call, Rod does not want
an agent that might creatively agree to a £500 deposit because the manager explained it was "technically
two payments". The structured architecture makes that impossible by construction.

LangGraph could answer that call too, but it would rely on the LLM's reasoning staying within bounds
under every possible phrasing, which is not a guarantee. The Rasa CALM approach trades flexibility for
guarantee: it cannot help with anything outside its declared flows, but within those flows, every
constraint is enforced in Python and every path is traceable to a specific line of code.
"""
