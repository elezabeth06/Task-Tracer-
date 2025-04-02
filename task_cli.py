import json
import os
import sys
from datetime import datetime

TASKS_FILE = 'tasks.json'


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")


def update_task(task_id, description):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['description'] = description
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task {task_id} updated successfully.")
    else:
        print(f"Task with ID {task_id} not found.")


def delete_task(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Task with ID {task_id} not found.")


def mark_in_progress(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['status'] = 'in-progress'
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task {task_id} marked as in progress.")
    else:
        print(f"Task with ID {task_id} not found.")


def mark_done(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['status'] = 'done'
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task {task_id} marked as done.")
    else:
        print(f"Task with ID {task_id} not found.")


def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']} - {task['description']} - Status: {task['status']} "
              f"- Created At: {task['createdAt']} - Updated At: {task['updatedAt']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli [command] [arguments]")
        return

    command = sys.argv[1]

    if command == 'add' and len(sys.argv) > 2:
        add_task(' '.join(sys.argv[2:]))
    elif command == 'update' and len(sys.argv) > 3:
        task_id = int(sys.argv[2])
        update_task(task_id, ' '.join(sys.argv[3:]))
    elif command == 'delete' and len(sys.argv) > 2:
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == 'mark-in-progress' and len(sys.argv) > 2:
        task_id = int(sys.argv[2])
        mark_in_progress(task_id)
    elif command == 'mark-done' and len(sys.argv) > 2:
        task_id = int(sys.argv[2])
        mark_done(task_id)
    elif command == 'list':
        if len(sys.argv) > 2:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print("Invalid command or arguments.")
        print("Commands: add, update, delete, mark-in-progress, mark-done, list")

if __name__ == '__main__':
    main()
