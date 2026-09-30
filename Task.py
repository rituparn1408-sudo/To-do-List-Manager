import db

def add_task():
    print("Add Tasks To The list:")
    Task = input("Enter the Task : ")
    db.add(Task)
    print("Task added successfully.")
    while True:
        more = input("Do you want to add more Task? (y/n): ")
        if more.lower() != 'y':
            break
        Task = input("Enter the Task : ")
        db.add(Task)
        print("Task added successfully.")

def remove_task():
    print("Remove_Task:")
    number = input("Enter Task number: ")
    if number.isdigit():
        removed = db.remove(int(number) - 1)
        if removed:
            print("Task removed successfully.")
        else:
            print("Task not found.")
    else:
        print("Invalid number.")

def to():
    while True:
        print("\n1. Add Task  2. Remove Task  3. Logout")
        choice = input("Enter code from 1-3: ") 
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            print("Logged out.")
            return
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    to()