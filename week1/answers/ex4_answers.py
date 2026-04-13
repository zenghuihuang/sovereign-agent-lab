"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No venues were found that can accommodate 300 guests with vegan options. The search returned zero matches."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
When The Albanach's status was changed from 'available' to 'full' in mcp_venue_server.py, the search_venues
tool automatically excluded it from results — the filter (info["status"] == "available") meant it was not
returned. Query 1 now returned only The Haymarket Vaults (1 match instead of 2), and the agent correctly
picked that as the best match and fetched its details with get_venue_details.

Critically: only mcp_venue_server.py needed to change. The exercise4_mcp_client.py file — and the LangGraph
agent code — did not need ANY modification. The tools are discovered dynamically at runtime, so the agent
immediately got the updated view of the world. This demonstrates the core MCP value: tool implementations
and client code are decoupled. Update the server, all clients see the change automatically.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 6   # 4 explicit imports + 4 names passed to create_react_agent
LINES_OF_TOOL_CODE_EX4 = 1   # tools, tool_names = await discover_tools(SERVER_SCRIPT)

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides dynamic tool discovery and language-agnostic interoperability. In exercise2, the agent
must explicitly import and name every tool at code-write time — if a new tool is added, the client
must be updated. In exercise4, the agent calls discover_tools() at runtime and gets whatever tools
the server currently exposes, with no client changes needed.

Beyond that: MCP is a protocol, not a Python import. The server could be written in any language,
deployed remotely, or shared by completely different clients (e.g., the LangGraph research loop AND
the Rasa CALM structured agent could both connect to the same server — which is exactly what the
final assignment does with PyNanoClaw). A Python import can only be shared within the same Python
process. An MCP server can be shared across processes, machines, and programming languages.
The experiment proved it: changing the server changed both halves' world view simultaneously,
without touching any client code.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """

"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """

"""