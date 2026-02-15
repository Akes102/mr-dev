# todo_list.py

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

tasks = load_tasks()

while True:
    print("\n1) Add  2) View  3) Remove  4) Save  5) Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        task = input("Task name: ").strip()
        if task:
            tasks.append(task)
            print("Added.")
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        show_tasks(tasks)
        num = input("Task number to remove: ").strip()
        if num.isdigit():
            idx = int(num) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        else:
            print("Enter a valid number.")
    elif choice == "4":
        save_tasks(tasks)
        print("Saved to tasks.txt")
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid option.")
