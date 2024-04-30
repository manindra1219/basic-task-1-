class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.description} - Priority: {task.priority}")

    def prioritize_tasks(self):
        if not self.tasks:
            print("No tasks to prioritize.")
            return

        self.tasks.sort(key=lambda x: x.priority, reverse=True)
        print("Tasks prioritized successfully.")

    def recommend_task(self, keyword):
        relevant_tasks = [task for task in self.tasks if keyword.lower() in task.description.lower()]
        if relevant_tasks:
            relevant_tasks.sort(key=lambda x: x.priority, reverse=True)
            print(f"Recommended task: {relevant_tasks[0].description}")
        else:
            print("No matching tasks found.")

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Tasks")
        print("5. Recommend Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (1-10): "))
            manager.add_task(description, priority)
        elif choice == "2":
            index = int(input("Enter task index to remove: ")) - 1
            manager.remove_task(index)
        elif choice == "3":
            manager.list_tasks()
        elif choice == "4":
            manager.prioritize_tasks()
        elif choice == "5":
            keyword = input("Enter keyword for task recommendation: ")
            manager.recommend_task(keyword)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
