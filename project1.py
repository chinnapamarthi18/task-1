class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = "Pending"

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task] = "Completed"
        else:
            print("Task not found.")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            self.tasks[new_task] = self.tasks.pop(old_task)
        else:
            print("Task not found.")

    def get_status(self, task):
        return self.tasks.get(task, "Task not found.")

    def show_tasks(self):
        for task, status in self.tasks.items():
            print(f"{task}: {status}")

    def run(self):
        while True:
            print("\nCommands: add, complete, update, status, show, exit")
            command = input("Enter command: ").strip().lower()
            if command == 'add':
                task = input("Enter task to add: ")
                self.add_task(task)
            elif command == 'complete':
                task = input("Enter task to complete: ")
                self.complete_task(task)
            elif command == 'update':
                old_task = input("Enter old task name: ")
                new_task = input("Enter new task name: ")
                self.update_task(old_task, new_task)
            elif command == 'status':
                task = input("Enter task to get status: ")
                print(self.get_status(task))
            elif command == 'show':
                self.show_tasks()
            elif command == 'exit':
                break
            else:
                print("Invalid command.")

# Example usage:
todo_list = ToDoList()
todo_list.run()
