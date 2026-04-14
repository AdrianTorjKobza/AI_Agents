# Data Summarizer
**Data Summarizer** is an MCP server designed to help AI Agents analyze large CSV datasets without exceeding their context limits. It performs local data processing using Pandas and returns concise summaries to the AI Agent.

## Features
- **Schema Insight**: Instantly see row counts and column data types.
- **Local Analytics**: Calculates mean, median, and distribution for numerical data on your machine.
- **Memory Efficient**: Prevents AI "Context Overload" by summarizing data before transmission.

## Setup
1. `pip install -r requirements.txt`
2. Add to your MCP host (Claude/Cursor) using the path to `server.py`.

## Agentic Workflow
**User:** *"How are the sales figures looking in the 2025_report.csv?"*
1. **Explore**: AI calls `get_csv_info` to find the correct column.
2. **Analyze**: AI calls `get_column_stats(column_name="Sales")`.
3. **Report**: AI says: *"The average sale was $450, with a peak of $2,300."*