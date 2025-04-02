# Task-Tracker

A simple CLI application to track your tasks.

## Commands

- `task-cli add <description>` - Add a new task.
- `task-cli update <id> <new description>` - Update an existing task.
- `task-cli delete <id>` - Delete a task.
- `task-cli mark-in-progress <id>` - Mark a task as in progress.
- `task-cli mark-done <id>` - Mark a task as done.
- `task-cli list` - List all tasks.
- `task-cli list <status>` - List tasks by status (`todo`, `in-progress`, `done`).

## Example

```bash
task-cli add "Buy groceries"
task-cli update 1 "Buy groceries and cook dinner"
task-cli mark-in-progress 1
task-cli mark-done 1
task-cli list
task-cli list done
