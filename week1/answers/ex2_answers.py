"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = ""

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "placeholder"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Albanach+%7C+160+guests&id=4e065f03dfb0"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for AI Meetup, Edinburgh, professional at The Albanach, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
The agent interacts with a tool abstraction (generate_event_flyer) that encapsulates the image provider behind a
stable interface — when Nebius removed FLUX, only the tool's internal implementation changed to use a graceful
fallback, while the agent's loop, tool name, input schema, and success contract remained identical.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
After the tool returned {"pub_name": "The Bow Bar", "capacity": 80, "status": "full", "meets_all_constraints": false},
the agent immediately called check_pub_availability for The Albanach without waiting for further instructions,
autonomously deciding to try the next known venue that might satisfy the 160-person vegan requirement.
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
Okay, let's see. The user is looking for a venue in Edinburgh that can accommodate 300 people with vegan options. They provided four known venues: The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. I checked each one using the check_pub_availability function.

First, The Albanach had a capacity of 180 and vegan options, but that's too small. Then The Haymarket Vaults with 160 capacity, also too small. The Guilford Arms had 200 capacity but no vegan options. Finally, ...
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False

SCENARIO_3_RESPONSE = """Okay, the user is asking about the last train time from Edinburgh Waverley to London tonight. Let me check the tools provided.
Looking at the available functions: check_pub_availability, get_edinburgh_weather, calculate_catering_cost, generate_event_flyer. None of these are related to train schedules. The functions are for checking pub availability, weather, catering costs, and generating flyers. 
Since there's no tool for train times, I can't use any of the provided functions to answe..."""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, this behaviour is acceptable and appropriate for a real booking assistant. The agent correctly identified that the user's request about train times was out of scope for its capabilities and the tools it has access to. 
Instead of attempting to hallucinate an answer or call an irrelevant tool, it transparently communicated its limitations and politely declined to provide information it cannot reliably access. This maintains user trust and sets clear expectations about what the assistant can and cannot do.
Perhaps in a more advanced system, the agent could suggest alternative resources (like a link to a train schedule website) or offer to help with other aspects of the event planning that it can assist with.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
	__start__([<p>__start__</p>]):::first
	agent(agent)
	tools(tools)
	__end__([<p>__end__</p>]):::last
	__start__ --> agent;
	agent -.-> __end__;
	agent -.-> tools;
	tools --> agent;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph graph is minimal — just three nodes (start → agent ↔ tools → end) forming a tight loop where
the model decides at runtime what to do next and whether to call a tool or stop. There is no declared
sequence of steps in the graph itself; all routing is implicit in the model's reasoning.

Rasa CALM's flows.yml is the opposite: every flow is explicitly described with an ordered list of collect
and action steps. The LLM only decides which flow to trigger; once inside a flow, Rasa executes the steps
deterministically. The confirm_booking flow collects guest_count, then vegan_count, then deposit_amount_gbp,
then runs action_validate_booking — that sequence is fixed and auditable. There is no equivalent of "the
model decides the order" in the CALM agent.

The trade-off is autonomy vs. auditability. LangGraph is better for open-ended research (the agent can
chain tools in any order based on what it discovers). Rasa CALM is better for high-stakes structured
conversations (every constraint is guaranteed, every path is readable).
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most unexpected behaviour was in Scenario 2 (impossible constraint, 300 guests): rather than stopping
after the first venue failed, the agent systematically and autonomously checked all four known venues
(The Albanach, The Haymarket Vaults, The Guilford Arms, The Bow Bar) before concluding that no venue could
satisfy the constraint. It was never told to check all four — it inferred from context that it should
exhaust the known options before reporting failure. Even more notably, it did NOT hallucinate a fictitious
venue with 300-person capacity, which is the failure mode one might expect from a generative model under
pressure to give a positive answer. The agent stayed grounded in actual tool data throughout.
"""