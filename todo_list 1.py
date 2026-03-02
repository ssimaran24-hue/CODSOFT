# Simple To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour To-Do List:")
        for i in range(len(tasks)):
            status = "Done" if tasks[i]["done"] else "Pending"
            print(f"{i+1}. {tasks[i]['task']} - {status}")
        print()

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!\n")

def delete_task():
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted successfully!\n")
            else:
                print("Invalid task number!\n")
        except:
            print("Please enter a valid number!\n")

def mark_completed():
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark as completed: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print("Task marked as completed!\n")
            else:
                print("Invalid task number!\n")
        except:
            print("Please enter a valid number!\n")

# Main Program Loop
while True:
    print("===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")