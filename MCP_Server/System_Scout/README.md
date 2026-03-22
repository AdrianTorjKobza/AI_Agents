# System Scout
A lightweight MCP Server that gives AI Agents the ability to monitor local system performance.

## Features
- **Real-Time Health Check**: Get instant CPU, RAM, and Disk usage percentages.
- **Process Inspector**: Identify the top memory-hungry processes currently running on your machine.
- **Hardware Profile**: Access static hardware specifications (Processor, Architecture).
- **Safe Execution**: Handles system permissions gracefully without crashing on restricted processes.

## Setup
1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. To use with Claude Desktop, add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "system-scout": {
      "command": "python",
      "args": ["/path/to/your/system-scout/server.py"]
    }
  }
}


## How the AI can use this (The "Agentic" Workflow):
If you ask an AI "Why is my computer slow?", it will perform a multi-step logic chain:
1. Call get_system_stats: It sees RAM is at 95%.
2. Logic: "I should see what is using that RAM."
3. Call get_top_processes: It sees chrome.exe is using 40%.
4. Response: "Your RAM is at 95%, and it looks like Chrome is the main culprit using 40% of your memory."