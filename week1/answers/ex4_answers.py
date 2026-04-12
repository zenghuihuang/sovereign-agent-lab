"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh "
QUERY_2_FINAL_ANSWER  = """
I searched the venue database for Edinburgh locations that can accommodate **at least 300 guests** and also offer a **vegan menu**. Unfortunately, no venues currently meet both criteria:

- When I filtered for `min_capacity = 300` and `requires_vegan = true`, the search returned zero matches.
- Even when I removed the vegan requirement (`requires_vegan = false`) and kept the 300‑person minimum, ...
"""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Changed the file mcp_venue_server.py to set The Albanach's status from "available" to "full". When I ran exercise4_mcp_client.py again, the output for Query 1 changed: The Albanach was no longer returned as a match in the search results, and the final answer only mentioned The Haymarket Vaults as the best match. I did not need to update any other files, which shows that the MCP setup correctly encapsulated the venue data and logic within the server script.
I’ve searched the available Edinburgh venue database for locations that can accommodate **at least 300 guests** and also offer a **vegan menu**. Unfortunately, no venue in the current dataset meets both of those requirements:

- When I filtered for a minimum capacity of 300 (regardless of vegan options), the search returned **zero results**.
- When I added the vegan‑menu requirement, the result ...
Before changing Albanach's status, the search results for Query 1 included both The Albanach and The Haymarket Vaults as matches. After changing The Albanach's status to "full", it was no longer included in the search results, demonstrating that the MCP server correctly reflected the updated venue availability without requiring any changes to the client code. This shows that the tools provided by the MCP server are effectively decoupled from the client, allowing for seamless updates to the underlying data and logic without impacting the agent's ability to query and retrieve information.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 283   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 217   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP allows for decoupling, scalability and code reuse.
MCP decouples tool data from agent code. Instead of hardcoding venue tools into the agent, you connect to a separate MCP server. This means: when venue data changes, you only modify mcp_venue_server.py—not the agent. Multiple clients (LangGraph + Rasa) can share the same server without code duplication. You'll prove this by changing a venue's status in the server, re-running the agent, and seeing results change instantly without touching agent code.
Both LangGraph and Rasa can use the same server without duplication
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
FILL ME IN
"""
