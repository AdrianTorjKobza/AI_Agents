# System Scout
A lightweight MCP Server that gives AI Agents the ability to navigate, search, and inspect your local file system safely.

## Features
- **Directory Mapping**: Lists all files and folders in a given path, including their sizes in KB.
- **Deep Keyword Search**: Recursively searches for specific text strings inside files (supports `.txt`, `.md`, `.log`, and more).
- **Intelligent Path Resolution**: Automatically handles home directory expansion (`~`) and absolute paths for cross-platform compatibility.
- **Safety First**: Implements robust error handling to skip system-locked or restricted files without crashing the server.

## Setup
1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. To use with Claude Desktop, add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "file-scout": {
      "command": "python",
      "args": ["/absolute/path/to/AI Agents/MCP Servers/File_Scout/server.py"]
    }
  }
}


## How the AI can use this (The "Agentic" Workflow):
**User Query:** *"Find the error message in my logs folder and tell me when it happened."*

1.  **Step 1 (Exploration)**: The AI calls `list_directory(path="./logs")` to see what files exist.
2.  **Step 2 (Targeting)**: The AI identifies `error.log` and calls `search_in_files(keyword="CRITICAL", directory="./logs", extension=".log")`.
3.  **Step 3 (Extraction)**: After finding the line, the AI uses its internal logic to summarize the timestamp and the cause for the user.
