# Simple dictionary to act as the local "DynamoDB.

import json
import os

DB_FILE = "tasks.json"

def save_task(task_id, status, result=None):
    db = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            db = json.load(f)
    
    db[task_id] = {"status": status, "result": result}
    with open(DB_FILE, "w") as f:
        json.dump(db, f)

def get_task(task_id):
    if not os.path.exists(DB_FILE): return None
    with open(DB_FILE, "r") as f:
        db = json.load(f)
    return db.get(task_id)