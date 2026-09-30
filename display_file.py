import db
def start():
 name = input("Enter your name: ")
 tasks = db.get()
 print(f"\nWelcome, {name}!")
 print("--- Current Tasks ---")
 if not tasks:
        print("No tasks available.")
        return
 for number, t in enumerate(tasks, start=1):
        task_title = t.get("task", t) if isinstance(t, dict) else t
        print(f"Task {number}: {task_title}")

def report():
    while True:
        print("\n1. Display the tasks  2. Logout")
        choice = input("Enter choice (1-2): ").strip()
        if choice == "1":
            start()
        elif choice == "2":
            print("Logged out.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    report()