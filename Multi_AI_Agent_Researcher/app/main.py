# The "Orchestrator." It accepts the task, kicks off a background thread, and gives the user a task_id.

from fastapi import FastAPI, BackgroundTasks
import uuid
import os
from .agents import scout_agent, writer_agent
from .database import save_task, get_task

app = FastAPI(title="Async Multi-Agent Researcher")

# Ensure storage directory exists
os.makedirs("reports", exist_ok=True)

async def run_research_pipeline(task_id: str, topic: str):
    """The Background Worker Logic"""
    try:
        # Step 1: Scout Agent
        save_task(task_id, "Searching...")
        points = await scout_agent(topic)
        
        # Step 2: Writer Agent
        save_task(task_id, "Writing...")
        report = await writer_agent(topic, points)
        
        # Step 3: Save to local 'S3'
        file_path = f"reports/{task_id}.txt"
        with open(file_path, "w") as f:
            f.write(report)
        
        save_task(task_id, "Completed", result=file_path)
    except Exception as e:
        save_task(task_id, f"Failed: {str(e)}")

@app.post("/research")
async def start_research(topic: str, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    save_task(task_id, "Queued")
    background_tasks.add_task(run_research_pipeline, task_id, topic)
    return {"task_id": task_id, "message": "Research started in background"}

@app.get("/status/{task_id}")
async def check_status(task_id: str):
    task = get_task(task_id)
    if not task:
        return {"error": "Task not found"}
    return task