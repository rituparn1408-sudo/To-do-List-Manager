from datetime import datetime
import json
import os
FILE_NAME = "tasks_data.json"
def load():
 if not os.path.exists(FILE_NAME):
    return {"tasks": []}
 try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
 except (json.JSONDecodeError, FileNotFoundError):
        return {"tasks": []}

def save(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def get():
    data = load()
    return data.get("tasks", [])

def add(task_text):
    data = load()
    data["tasks"].append({
        "task": task_text,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save(data)

def remove(index):
    data = load()
    tasks = data.get("tasks", [])
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save(data)
        return removed
    return None