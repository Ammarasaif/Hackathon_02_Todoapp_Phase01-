#!/usr/bin/env python3
"""
CLI-based Todo application with in-memory storage.

This application implements the Phase I specifications for the
"Hackathon II – The Evolution of Todo" project.
"""

import sys
from typing import Optional, Dict, List


class Task:
    """
    Represents a Todo task with id, title, description, and completion status.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Required title of the task
        description (Optional[str]): Optional description of the task
        completed (bool): Whether the task is completed (default False)
    """

    def __init__(self, task_id: int, title: str, description: Optional[str] = None, completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Required title of the task
            description (Optional[str]): Optional description of the task
            completed (bool): Whether the task is completed (default False)
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else None
        self.completed = completed

    def __str__(self) -> str:
        """String representation of the task."""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}: {self.title}"

    def to_detailed_str(self) -> str:
        """Detailed string representation of the task."""
        status = "Completed" if self.completed else "Pending"
        result = f"ID: {self.id}\n"
        result += f"Title: {self.title}\n"
        result += f"Status: {status}\n"
        if self.description:
            result += f"Description: {self.description}\n"
        return result


class TodoManager:
    """
    Manages the collection of tasks in memory.

    Handles all CRUD operations for tasks while maintaining
    a single source of truth for task state.
    """

    def __init__(self):
        """Initialize the TodoManager with an empty task list."""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def _generate_id(self) -> int:
        """Generate a unique ID for a new task."""
        new_id = self._next_id
        self._next_id += 1
        return new_id

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the collection.

        Args:
            title (str): Required title of the task
            description (Optional[str]): Optional description of the task

        Returns:
            Task: The newly created task

        Raises:
            ValueError: If title is empty
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task_id = self._generate_id()
        task = Task(task_id, title, description, completed=False)
        self._tasks[task_id] = task
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the collection.

        Returns:
            List[Task]: All tasks in the collection
        """
        return list(self._tasks.values())

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title or description.

        Args:
            task_id (int): ID of the task to update
            title (Optional[str]): New title if provided
            description (Optional[str]): New description if provided

        Returns:
            bool: True if task was updated, False if task not found
        """
        task = self.get_task(task_id)
        if not task:
            return False

        # Validate new title if provided
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        # Update description if provided
        if description is not None:
            task.description = description.strip() if description else None

        return True

    def toggle_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id (int): ID of the task to toggle

        Returns:
            bool: True if task status was toggled, False if task not found
        """
        task = self.get_task(task_id)
        if not task:
            return False

        task.completed = not task.completed
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the collection.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False


class TodoCLI:
    """
    Command-line interface for the Todo application.

    Handles user input, command parsing, and output formatting.
    """

    def __init__(self):
        """Initialize the CLI with a TodoManager instance."""
        self.manager = TodoManager()

    def print_help(self):
        """Print the help message showing available commands."""
        print("\n=== TODO CLI APPLICATION ===")
        print("Available commands:")
        print("  add <title> [description]   - Add a new task")
        print("  list                        - List all tasks")
        print("  update <id> [title] [desc]  - Update a task")
        print("  complete <id>               - Mark task as complete/incomplete")
        print("  delete <id>                 - Delete a task")
        print("  show <id>                   - Show details of a specific task")
        print("  help                        - Show this help message")
        print("  quit                        - Exit the application")
        print("==================================\n")

    def handle_add(self, args: List[str]) -> bool:
        """
        Handle the 'add' command to create a new task.

        Args:
            args (List[str]): Arguments passed to the add command

        Returns:
            bool: True if successful, False otherwise
        """
        if len(args) < 1:
            print("ERROR: Please provide a title for the task.")
            return False

        title = args[0]
        description = " ".join(args[1:]) if len(args) > 1 else None

        try:
            task = self.manager.add_task(title, description)
            print(f"✓ Added task: [{task.id}] {task.title}")
            return True
        except ValueError as e:
            print(f"ERROR: {e}")
            return False

    def handle_list(self, args: List[str]) -> bool:
        """
        Handle the 'list' command to display all tasks.

        Args:
            args (List[str]): Arguments passed to the list command

        Returns:
            bool: True if successful, False otherwise
        """
        tasks = self.manager.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return True

        print("\nYOUR TASKS:")
        for task in tasks:
            print(f"  {task}")
        print()
        return True

    def handle_show(self, args: List[str]) -> bool:
        """
        Handle the 'show' command to display details of a specific task.

        Args:
            args (List[str]): Arguments passed to the show command

        Returns:
            bool: True if successful, False otherwise
        """
        if len(args) != 1:
            print("ERROR: Please provide a task ID.")
            return False

        try:
            task_id = int(args[0])
        except ValueError:
            print("ERROR: Task ID must be a number.")
            return False

        task = self.manager.get_task(task_id)
        if not task:
            print(f"ERROR: Task with ID {task_id} not found.")
            return False

        print("\nTASK DETAILS:")
        print(task.to_detailed_str())
        return True

    def handle_update(self, args: List[str]) -> bool:
        """
        Handle the 'update' command to modify an existing task.

        Args:
            args (List[str]): Arguments passed to the update command

        Returns:
            bool: True if successful, False otherwise
        """
        if len(args) < 2:
            print("ERROR: Please provide task ID, and at least one field to update.")
            return False

        try:
            task_id = int(args[0])
        except ValueError:
            print("ERROR: Task ID must be a number.")
            return False

        # Extract title and description from remaining args
        title = args[1] if args[1] != '.' else None  # Use '.' to indicate no change
        description = " ".join(args[2:]) if len(args) > 2 and args[2] != '.' else None

        # If title is '.', replace with None to indicate no change
        if title == '.':
            title = None
        if description and description == '.':
            description = None

        try:
            updated = self.manager.update_task(task_id, title, description)
            if updated:
                print(f"✓ Updated task {task_id}")
                return True
            else:
                print(f"ERROR: Task with ID {task_id} not found.")
                return False
        except ValueError as e:
            print(f"ERROR: {e}")
            return False

    def handle_complete(self, args: List[str]) -> bool:
        """
        Handle the 'complete' command to toggle task completion status.

        Args:
            args (List[str]): Arguments passed to the complete command

        Returns:
            bool: True if successful, False otherwise
        """
        if len(args) != 1:
            print("ERROR: Please provide a task ID.")
            return False

        try:
            task_id = int(args[0])
        except ValueError:
            print("ERROR: Task ID must be a number.")
            return False

        task = self.manager.get_task(task_id)
        if not task:
            print(f"ERROR: Task with ID {task_id} not found.")
            return False

        was_completed = task.completed
        updated = self.manager.toggle_completion(task_id)

        if updated:
            status = "completed" if not was_completed else "marked incomplete"
            print(f"✓ Task {task_id} {status}")
            return True
        else:
            print(f"ERROR: Could not update task {task_id}.")
            return False

    def handle_delete(self, args: List[str]) -> bool:
        """
        Handle the 'delete' command to remove a task.

        Args:
            args (List[str]): Arguments passed to the delete command

        Returns:
            bool: True if successful, False otherwise
        """
        if len(args) != 1:
            print("ERROR: Please provide a task ID.")
            return False

        try:
            task_id = int(args[0])
        except ValueError:
            print("ERROR: Task ID must be a number.")
            return False

        deleted = self.manager.delete_task(task_id)
        if deleted:
            print(f"✓ Deleted task {task_id}")
            return True
        else:
            print(f"ERROR: Task with ID {task_id} not found.")
            return False

    def run(self):
        """Run the main CLI loop."""
        print("Welcome to the CLI Todo Application!")
        print("Type 'help' for available commands.")

        while True:
            try:
                # Get user input
                user_input = input("\ntodo> ").strip()

                if not user_input:
                    continue

                # Parse command
                parts = user_input.split()
                command = parts[0].lower()
                args = parts[1:]

                # Handle different commands
                if command in ['quit', 'exit']:
                    print("Goodbye!")
                    break
                elif command == 'help':
                    self.print_help()
                elif command == 'add':
                    self.handle_add(args)
                elif command == 'list':
                    self.handle_list(args)
                elif command == 'show':
                    self.handle_show(args)
                elif command == 'update':
                    self.handle_update(args)
                elif command == 'complete':
                    self.handle_complete(args)
                elif command == 'delete':
                    self.handle_delete(args)
                else:
                    print(f"Unknown command: '{command}'. Type 'help' for available commands.")

            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except EOFError:
                print("\n\nGoodbye!")
                break


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()