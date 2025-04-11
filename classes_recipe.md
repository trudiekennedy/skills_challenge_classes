Recipe template - class design

# {{PROBLEM}} TO-DO Tasks Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TodoList:
    # User-facing properties:
    #   task: string

    def __init__(self):
        # Parameters:
        #   task_list: list of strings
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   task_list with task appended
        # Side-effects
        #   Saves the task to the self task_list object
        #   Throws exception if empty string added
        pass # No code here yet

    def mark_complete(self, task):
        # Parameters:
        #  task: string representing the task the person wants to mark as complete
        # Returns:
        #   task_list without completed task
        # Side-effects:
        #   Removes task from task_list object
        #   Throws an exception if no task is passed
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
#add_task stores task to task list and returns list to user
"""
your_tasks = TodoList()
your_tasks.add_task("Complete coding challenge") # => ["Complete coding challenge"]

"""
Given no task
#add_task raises an exception
"""
your_tasks = TodoList()
your_tasks.add_task("") # => ["List not updated: no task given."]

"""
Given a task is added and another task it added
#add_task stores both tasks and return list to user
"""
your_tasks = TodoList()
your_tasks.add_task("Complete coding challenge")
your_tasks.add_task("Take a break")  
# => ["Complete coding challenge", "Take a break]

"""
Given no task
#mark_complete raises an exception
"""
your_tasks = TodoList()
your_tasks.mark_complete("") # => ["List not updated: no task given."]

"""
Given a task
#mark_complete removes task from list and returns amended list to user
"""
your_tasks = TodoList()
your_tasks.add_task("Complete coding challenge") 
your_tasks.add_task("Take a break")
your_tasks.mark_complete("Take a break") # => ["Complete coding challenge"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
