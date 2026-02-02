#!/usr/bin/env python3
"""
Test script for the Todo application.

This script demonstrates the functionality of the Todo application
by performing various operations and verifying the expected outcomes.
"""

from todo_app import TodoManager, Task


def test_task_creation():
    """Test basic task creation."""
    print("Testing task creation...")

    # Test valid task creation
    manager = TodoManager()
    task = manager.add_task("Test task", "This is a test description")

    assert task.title == "Test task"
    assert task.description == "This is a test description"
    assert task.completed == False
    assert task.id == 1

    print("PASS: Task creation works correctly")


def test_task_validation():
    """Test task validation."""
    print("\nTesting task validation...")

    manager = TodoManager()

    # Test empty title validation
    try:
        manager.add_task("")
        assert False, "Should have raised ValueError for empty title"
    except ValueError:
        print("PASS: Empty title validation works correctly")

    # Test whitespace-only title validation
    try:
        manager.add_task("   ")
        assert False, "Should have raised ValueError for whitespace-only title"
    except ValueError:
        print("PASS: Whitespace-only title validation works correctly")


def test_task_operations():
    """Test basic task operations."""
    print("\nTesting task operations...")

    manager = TodoManager()

    # Add a task
    task1 = manager.add_task("First task", "Description 1")
    task2 = manager.add_task("Second task", "Description 2")

    # Test listing tasks
    all_tasks = manager.get_all_tasks()
    assert len(all_tasks) == 2
    assert all_tasks[0].id == 1
    assert all_tasks[1].id == 2
    print("PASS: Task listing works correctly")

    # Test getting specific task
    retrieved_task = manager.get_task(1)
    assert retrieved_task is not None
    assert retrieved_task.title == "First task"
    print("PASS: Task retrieval works correctly")

    # Test updating task
    updated = manager.update_task(1, "Updated task", "Updated description")
    assert updated == True
    updated_task = manager.get_task(1)
    assert updated_task.title == "Updated task"
    assert updated_task.description == "Updated description"
    print("PASS: Task update works correctly")

    # Test toggling completion
    initial_status = updated_task.completed
    toggled = manager.toggle_completion(1)
    assert toggled == True
    task_after_toggle = manager.get_task(1)
    assert task_after_toggle.completed != initial_status
    print("PASS: Task completion toggle works correctly")

    # Test deleting task
    deleted = manager.delete_task(2)
    assert deleted == True
    assert manager.get_task(2) is None
    print("PASS: Task deletion works correctly")


def test_task_not_found():
    """Test operations on non-existent tasks."""
    print("\nTesting operations on non-existent tasks...")

    manager = TodoManager()

    # Try to get non-existent task
    assert manager.get_task(999) is None
    print("PASS: Non-existent task retrieval handled correctly")

    # Try to update non-existent task
    updated = manager.update_task(999, "New title")
    assert updated == False
    print("PASS: Non-existent task update handled correctly")

    # Try to toggle completion of non-existent task
    toggled = manager.toggle_completion(999)
    assert toggled == False
    print("PASS: Non-existent task toggle handled correctly")

    # Try to delete non-existent task
    deleted = manager.delete_task(999)
    assert deleted == False
    print("PASS: Non-existent task deletion handled correctly")


def test_task_update_partial():
    """Test partial task updates."""
    print("\nTesting partial task updates...")

    manager = TodoManager()
    task = manager.add_task("Original title", "Original description")

    # Update only title
    manager.update_task(task.id, "New title")
    updated_task = manager.get_task(task.id)
    assert updated_task.title == "New title"
    assert updated_task.description == "Original description"  # Should remain unchanged
    print("PASS: Partial title update works correctly")

    # Update only description
    manager.update_task(task.id, description="New description")
    updated_task = manager.get_task(task.id)
    assert updated_task.title == "New title"  # Should remain unchanged
    assert updated_task.description == "New description"
    print("PASS: Partial description update works correctly")


def run_tests():
    """Run all tests."""
    print("Running tests for Todo application...\n")

    try:
        test_task_creation()
        test_task_validation()
        test_task_operations()
        test_task_not_found()
        test_task_update_partial()

        print("\nSUCCESS: All tests passed successfully!")
        return True
    except Exception as e:
        print(f"\nERROR: Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    run_tests()