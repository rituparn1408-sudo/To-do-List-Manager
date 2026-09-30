import db

def display_tasks():
    tasks = db.get()
    print("\n--- Current Tasks ---")
    if not tasks:
        print("No tasks available.")
        return False
    for number, t in enumerate(tasks, start=1):
        task_title = t.get("task", t) if isinstance(t, dict) else t
        print(f"Task {number}: {task_title}")
    return True

def add_task_menu():
    while True:
        task_text = input("\nEnter the task: ").strip()
        if task_text:
            db.add(task_text)
            print("Task added successfully.")
        else:
            print("Task cannot be empty.")
            
        more = input("Do you want to add another task? (y/n): ").strip().lower()
        if more != 'y':
            break

def remove_task_menu():
    if not display_tasks():
        return
    number = input("\nEnter Task number to remove: ").strip()
    if number.isdigit():
        removed = db.remove(int(number) - 1)
        if removed:
            print("Task removed successfully.")
        else:
            print("Task number not found.")
    else:
        print("Invalid number.")

def main():
    name = input("Enter your name: ").strip()
    print(f"\nWelcome, {name}!")

    while True:
        print("\n1. Display Tasks  2. Add Task  3. Remove Task  4. Logout")
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task_menu()
        elif choice == "3":
            remove_task_menu()
        elif choice == "4":
            print(f"Goodbye, {name}! Logged out.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()