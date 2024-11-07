import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(tasks, task_description, priority="Low"):
    tasks.append({"description": task_description, "priority": priority})
    save_tasks(tasks)

def delete_task(tasks, task_index):
    tasks.pop(task_index)
    save_tasks(tasks)

if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks):
            print(f"{idx + 1}. {task['description']} (Priority: {task['priority']})")
        
        print("\nOptions: add, delete, quit")
        option = input("Choose an option: ").strip().lower()
        
        if option == "add":
            description = input("Task description: ")
            priority = input("Priority (High, Medium, Low): ").capitalize()
            add_task(tasks, description, priority)
        elif option == "delete":
            index = int(input("Task number to delete: ")) - 1
            delete_task(tasks, index)
        elif option == "quit":
            break
        else:
            print("Invalid option.")
