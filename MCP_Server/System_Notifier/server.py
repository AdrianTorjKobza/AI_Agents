from fastmcp import FastMCP
from plyer import notification
import platform

# Initialize the server
mcp = FastMCP("System_Notifier")

# --- TOOL 1: Desktop Notification ---
@mcp.tool()
def send_notification(title: str, message: str) -> str:
    """
    Send a native desktop notification to the user.
    Use this to alert the user when a task is finished or if an error occurs.
    """
    try:
        notification.notify(
            title = title,
            message = message,
            app_name = "AI Agent",
            timeout = 5  # Notification stays for 5 seconds
        )
        
        return f"Notification sent: [{title}] {message}"
    
    except Exception as e:
        return f"Failed to send notification: {str(e)}"

# --- TOOL 2: OS Check ---
@mcp.tool()
def get_os_status() -> str:
    """Check the OS and platform for compatibility."""
    return f"Running on {platform.system()} {platform.release()}"

if __name__ == "__main__":
    mcp.run()