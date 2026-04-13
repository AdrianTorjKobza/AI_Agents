from fastmcp import FastMCP
import pandas as pd
from pathlib import Path

# Initialize the server
mcp = FastMCP("DataSummarizer")

# --- TOOL 1: Schema & Overview ---
@mcp.tool()
def get_csv_info(file_path: str) -> str:
    """
    Get the structure of a CSV file: column names, types, and total rows.
    Use this first to understand what data is available.
    """
    try:
        path = Path(file_path).expanduser().resolve()
        df = pd.read_csv(path)
        
        info = [
            f"Total Rows: {len(df)}",
            f"Columns: {', '.join(df.columns)}",
            "\nData Types:",
            str(df.dtypes)
        ]
        
        return "\n".join(info)
    
    except Exception as e:
        return f"Error reading file: {str(e)}"

# --- TOOL 2: Numerical Statistics ---
@mcp.tool()
def get_column_stats(file_path: str, column_name: str) -> str:
    """
    Get statistical summary (mean, max, min, etc.) for a specific numerical column.
    """
    try:
        path = Path(file_path).expanduser().resolve()
        df = pd.read_csv(path)
        
        if column_name not in df.columns:
            return f"Error: Column '{column_name}' not found."
            
        # .describe() calculates count, mean, std, min, 25%, 50%, 75%, max
        stats = df[column_name].describe()
        
        return f"Statistics for {column_name}:\n{str(stats)}"
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()