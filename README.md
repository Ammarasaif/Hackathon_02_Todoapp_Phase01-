# CLI Todo Application

This is a command-line interface (CLI) based Todo application implemented in Python. It stores tasks in memory and supports basic task management operations.

## Features

- Add new tasks with titles and optional descriptions
- List all tasks with their completion status
- Update existing tasks
- Mark tasks as complete/incomplete
- Delete tasks
- View detailed information about specific tasks

## Requirements

- Python 3.6 or higher

## Usage

To run the application, simply execute the Python script:

```bash
python todo_app.py
```

Once the application is running, you can use the following commands:

### Available Commands

- `add <title> [description]` - Add a new task
- `list` - List all tasks
- `show <id>` - Show details of a specific task
- `update <id> [title] [description]` - Update a task (use '.' to skip updating a field)
- `complete <id>` - Toggle completion status of a task
- `delete <id>` - Delete a task
- `help` - Show help message
- `quit` or `exit` - Exit the application

### Examples

```
todo> add Buy groceries Get milk, bread, and eggs
✓ Added task: [1] Buy groceries

todo> add Call mom
✓ Added task: [2] Call mom

todo> list

YOUR TASKS:
  [○] 1: Buy groceries
  [○] 2: Call mom

todo> complete 1
✓ Task 1 completed

todo> list

YOUR TASKS:
  [✓] 1: Buy groceries
  [○] 2: Call mom

todo> show 1

TASK DETAILS:
ID: 1
Title: Buy groceries
Status: Completed
Description: Get milk, bread, and eggs

todo> update 2 "Call mom tomorrow"
✓ Updated task 2

todo> delete 2
✓ Deleted task 2
```

## Architecture

The application consists of three main components:

1. **Task Class**: Represents a single task with id, title, description, and completion status
2. **TodoManager Class**: Handles all business logic for managing tasks in memory
3. **TodoCLI Class**: Handles user input, command parsing, and output formatting

## Limitations

- Tasks are stored only in memory and will be lost when the application exits
- No persistent storage mechanism
- Single-user application