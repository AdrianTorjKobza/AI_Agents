from fastmcp import FastMCP
import psutil
import platform

# Initialize the server. The name "System_Scout" is what the AI will see.
mcp = FastMCP("System_Scout")

# --- TOOL 1: System Stats ---
@mcp.tool()
def get_system_stats() -> str:
    """Get real-time CPU, Memory, and Disk usage."""
    cpu = psutil.cpu_percent(interval=1) # Waits 1 second to calculate the average usage.
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    os_name = platform.system()

    return f"OS: {os_name} | CPU: {cpu}% | RAM: {memory}% | Disk: {disk}%"

# --- TOOL 2: Process Usage Monitor ---
@mcp.tool()
def get_top_processes(count: int = 5) -> str:
    """
    List the top 5 most memory-intensive processes currently running.
    Use this if the system stats show high RAM usage to find the culprit.
    """
    processes = [] # Define empty dictionar.
    
    # Iterate through all running processes.
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            # Fetch process info as a dictionary.
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Skip processes that are closed or we don't have permission to see.
            continue

    # Sort the list by memory usage in descending order.
    top_procs = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:count]
    
    # Format the results into a clean string for the AI Agent.
    results = [f"PID: {p['pid']} | Name: {p['name']} | RAM: {p['memory_percent']:.2f}%" for p in top_procs]
    
    return "\n".join(results) if results else "No process data available."

# --- ENVIRONMENT: Hardware Info ---
@mcp.resource("system://hardware-info")
def get_hardware_info() -> str:
    """"Provides static hardware specifications including processor and machine type."""
    return f"Processor: {platform.processor()} | Machine: {platform.machine()}"

if __name__ == "__main__":
    mcp.run() # Run the server using Standard Input/Output. This is how AI Desktop apps communicate with your script.