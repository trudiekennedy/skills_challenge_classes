from lib.todo_list import *
import pytest

"""
Given a task
#add_task stores task to task list and returns list to user
"""
def test_adding_a_task():
    your_tasks = TodoList()
    assert your_tasks.add_task("Complete coding challenge") == ["Complete coding challenge"]

"""
Given no task
#add_task raises an exception
"""
def test_adding_empty_string(): 
    your_tasks = TodoList()
    with pytest.raises(Exception) as e:
            your_tasks.add_task("")
    error_msg = str(e.value)
    assert error_msg == "List not updated: no task given."

"""
Given a task is added and another task it added
#add_task stores both tasks and return list to user
"""
def test_two_tasks_given():
    your_tasks = TodoList()
    your_tasks.add_task("Complete coding challenge")
    assert your_tasks.add_task("Take a break") == ["Complete coding challenge", "Take a break"]

"""
Given no task
#mark_complete raises an exception
"""
def test_mark_complete_no_task_given():
    your_tasks = TodoList()
    your_tasks.add_task("Complete coding challenge")
    with pytest.raises(Exception) as e:
        your_tasks.mark_complete("")
    error_msg = str(e.value)
    assert error_msg == "List not updated: no task given."

"""
Given a task
#mark_complete removes task from list and returns amended list to user
"""
def test_marking_a_task_as_completed():
    your_tasks = TodoList()
    your_tasks.add_task("Complete coding challenge") 
    your_tasks.add_task("Take a break")
    assert your_tasks.mark_complete("Take a break") == ["Complete coding challenge"]

"""
Given a task but task doesn't exist
#mark_complete returns string to user to tell them it doesn't exist
"""
def test_marking_a_task_as_completed():
    your_tasks = TodoList()
    your_tasks.add_task("Complete coding challenge")
    assert your_tasks.mark_complete("Take a break") == "That task doesn't exist!"

"""
Given a task but task list is empty
#mark_complete returns string to user to tell them it doesn't exist
"""
def test_marking_a_task_as_completed_on_empty_list():
    your_tasks = TodoList()
    assert your_tasks.mark_complete("Take a break") == "That task doesn't exist!"
    
