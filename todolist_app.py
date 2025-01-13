class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("\nNo tasks to show.\n")
        else:
            print("\nCurrent Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def show_completed_tasks(self):
        if not self.completed_tasks:
            print("\nNo completed tasks to show.\n")
        else:
            print("\nCompleted Tasks:")
            for idx, task in enumerate(self.completed_tasks, start=1):
                print(f"{idx}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            completed_task = self.tasks.pop(task_number - 1)
            self.completed_tasks.append(completed_task)
            print(f"Task completed: {completed_task}")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\n------------- To-Do List Application -------------")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Complete Task")
            print("4. View Completed Tasks")
            print("5. Delete Task")
            print("6. Exit")

            try:
                choice = int(input("Choose an option: "))

                if choice == 1:
                    self.show_tasks()
                elif choice == 2:
                    task = input("Enter the task: ")
                    self.add_task(task)
                elif choice == 3:
                    self.show_tasks()
                    try:
                        task_number = int(input("Enter the task number to complete: "))
                        self.complete_task(task_number)
                    except ValueError:
                        print("Please enter a valid number.")
                elif choice == 4:
                    self.show_completed_tasks()
                elif choice == 5:
                    self.show_tasks()
                    try:
                        task_number = int(input("Enter the task number to delete: "))
                        self.delete_task(task_number)
                    except ValueError:
                        print("Please enter a valid number.")
                elif choice == 6:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    app = ToDoList()
    app.run()
