import tkinter as tk
from todo import load_tasks, save_tasks, add_task, delete_task

def refresh_tasks():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END, f"{task['description']} (Priority: {task['priority']})")

def add_task_gui():
    description = description_entry.get()
    priority = priority_entry.get()
    add_task(tasks, description, priority)
    refresh_tasks()

def delete_task_gui():
    selected_task_index = tasks_listbox.curselection()[0]
    delete_task(tasks, selected_task_index)
    refresh_tasks()

tasks = load_tasks()
root = tk.Tk()
root.title("To-Do List")

description_entry = tk.Entry(root)
description_entry.grid(row=0, column=1)
priority_entry = tk.Entry(root)
priority_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add Task", command=add_task_gui)
add_button.grid(row=2, column=0)
delete_button = tk.Button(root, text="Delete Task", command=delete_task_gui)
delete_button.grid(row=2, column=1)

tasks_listbox = tk.Listbox(root)
tasks_listbox.grid(row=3, columnspan=2)
refresh_tasks()

root.mainloop()
