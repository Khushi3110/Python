class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.task_id = 1

    def add_task(self, task):
        self.tasks[self.task_id] = task
        self.task_id += 1
        print("Task added successfully!")

    def update_task(self, task_id, new_task):
        if task_id in self.tasks:
            self.tasks[task_id] = new_task
            print("Task updated successfully!")
        else:
            print("Task not found.")

    def show_tasks(self):
        if self.tasks:
            print("ToDo List:")
            for task_id, task in self.tasks.items():
                print(f"{task_id}. {task}")
        else:
            print("No tasks in the list.")

    def run(self):
        while True:
            print("\nSelect an option:")
            print("1. Add task")
            print("2. Update task")
            print("3. Show tasks")
            print("4. Quit")

            choice = input("Enter choice (1/2/3/4): ")

            if choice == '1':
                task = input("Enter task: ")
                self.add_task(task)
            elif choice == '2':
                task_id = int(input("Enter task ID to update: "))
                new_task = input("Enter new task: ")
                self.update_task(task_id, new_task)
            elif choice == '3':
                self.show_tasks()
            elif choice == '4':
                print("Exiting ToDo List.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    todo = ToDoList()
    todo.run()
