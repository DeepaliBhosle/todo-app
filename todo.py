import os
import json

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()
    while True:
        show_tasks(tasks)
        print("Options: [1] Add Task  [2] Delete Task  [3] Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            idx = int(input("Enter task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
            else:
                print("Invalid task number!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()
