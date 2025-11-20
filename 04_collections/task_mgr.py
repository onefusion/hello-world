def show_menu():
    print("\nTask Manager")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List all tasks")
    print("4. Quit")

def list_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter a new task:")
    tasks.append(task)
    print(f"Task added: {task}")

def remove_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter the number of the task to remove: "))
        removed = tasks.pop(task_number - 1)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
        