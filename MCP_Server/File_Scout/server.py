from fastmcp import FastMCP
import os
from pathlib import Path # Pathlib makes handling Windows vs Mac paths automatic.
from datetime import datetime

# Initialize the server.
mcp = FastMCP("File_Scout")

# --- TOOL 1: List Directory ---
@mcp.tool()
def list_directory(path: str = ".") -> str:
    """
    List files in a directory with their sizes. 
    Helps the agent understand the file structure.
    """
    try:
        target_path = Path(path).expanduser().resolve()
        
        if not target_path.exists():
            return f"Error: Path '{path}' does not exist."

        items = []

        for entry in target_path.iterdir():
            # Get size in Kilobytes.
            size_kb = entry.stat().st_size / 1024
            type_label = "📁" if entry.is_dir() else "📄"
            items.append(f"{type_label} {entry.name} ({size_kb:.1f} KB)")
        
        return "\n".join(items) if items else "Directory is empty."
    
    except Exception as e:
        return f"Access Denied or Error: {str(e)}"

# --- TOOL 2: Keyword Search ---
@mcp.tool()
def search_in_files(keyword: str, directory: str = ".", extension: str = ".txt") -> str:
    """
    Search for a keyword inside all files of a specific extension.
    Useful for finding specific info in logs or notes.
    """
    results = []
    target_dir = Path(directory).expanduser().resolve()
    
    # We loop through every file matching the extension.
    for file_path in target_dir.glob(f"*{extension}"):
        try:
            # We open the file in 'read' mode with UTF-8 encoding.
            content = file_path.read_text(encoding='utf-8')
            if keyword.lower() in content.lower():
                results.append(f"Found in: {file_path.name}")
        except Exception:
            continue # Skip files we can't read (e.g binaries).

    return "\n".join(results) if results else f"No matches for '{keyword}' found."

if __name__ == "__main__":
    mcp.run()