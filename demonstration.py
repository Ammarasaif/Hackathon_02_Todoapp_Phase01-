#!/usr/bin/env python3
"""
Demonstration script for the Todo application.

This script shows how to use the Todo application with sample commands.
"""

def show_demo_commands():
    """Display sample commands for the Todo application."""
    print("CLI Todo Application - Demo Commands")
    print("="*40)
    print()
    print("1. Start the application:")
    print("   python todo_app.py")
    print()
    print("2. Once running, use these commands:")
    print()
    print("   Add tasks:")
    print("   todo> add Buy groceries Get milk, bread, and eggs")
    print("   todo> add Call mom")
    print()
    print("   List all tasks:")
    print("   todo> list")
    print()
    print("   Show details of a specific task:")
    print("   todo> show 1")
    print()
    print("   Update a task:")
    print("   todo> update 1 \"Buy shopping\" \"Get milk, bread, eggs, and cheese\"")
    print()
    print("   Mark task as complete:")
    print("   todo> complete 1")
    print()
    print("   Delete a task:")
    print("   todo> delete 2")
    print()
    print("   Get help:")
    print("   todo> help")
    print()
    print("   Quit the application:")
    print("   todo> quit")
    print()
    print("All tasks are stored in memory and will be lost when the application exits.")


if __name__ == "__main__":
    show_demo_commands()