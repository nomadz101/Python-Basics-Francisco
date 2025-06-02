# Interactive Task Manager

tasks = []

def add_task():
    description = input("Enter task description: ")
    task = {"description": description, "completed": False}
    tasks.append(task)
    print(f'Task added: "{description}"')

def list_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['description']}")

def remove_task():
    list_tasks()
    try:
        index = int(input("Enter task number to remove: "))
        if 0 < index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f'Task removed: "{removed["description"]}"')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def complete_task():
    list_tasks()
    try:
        index = int(input("Enter task number to mark as complete: "))
        if 0 < index <= len(tasks):
            tasks[index - 1]["completed"] = True
            print(f'Task marked as complete: "{tasks[index - 1]["description"]}"')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()