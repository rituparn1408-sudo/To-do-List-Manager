import db

def start():
  name = input("Enter your name: ")
  print("  Diaplay the tasks")
  task = db.get()
  if not task:
        print("No tasks available.")
        return
  score = 0
  for number, t in enumerate(task, start=1):
        print(f"\nTask {number}: {t}")

def report():
 while True:
   print("\n1. Diaplay the tasks  2. Logout")
   choice = input("Enter code from 1-2: ")
   if choice == "1":
            start()
   elif choice == "2":
            print("Logged out.")
            return
   else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    report()