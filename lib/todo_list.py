class TodoList: 
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        if task == "":
            raise Exception("List not updated: no task given.")
        else:
            self.task_list.append(task)
            return self.task_list
    
    def mark_complete(self, task):
        if task == "":
            raise Exception("List not updated: no task given.")
        else:
            try: 
                self.task_list.remove(task)
                return self.task_list
            except ValueError:
                return "That task doesn't exist"