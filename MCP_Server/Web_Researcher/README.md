# Web Researcher

**Web Researcher** is an MCP server that grants AI Agents real-time access to the internet. It allows LLMs to look up current events, documentation, and facts that occurred after their training cutoff.

## Features
- **Live Search**: Fetches the top 5-10 most relevant web pages for any query.
- **Citations**: Returns URLs for every result so the AI can verify its claims.
- **Instant Answers**: Accesses DuckDuckGo's instant answer API for quick definitions.
- **Privacy-Focused**: Uses DuckDuckGo to ensure searches are anonymous.

## Setup
1. `pip install -r requirements.txt`
2. Add to your MCP host (Claude/Cursor) using the path to `server.py`.


## Agentic Workflow Example
**User:** *"What is the current version of the FastMCP library?"*
1. **Action**: AI recognizes its training data might be old.
2. **Tool Call**: Calls `search_web(query="latest FastMCP version python")`.
3. **Reasoning**: AI reads the snippets, finds "Version 0.1.2 released yesterday," and answers the user accurately.