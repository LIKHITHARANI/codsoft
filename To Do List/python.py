

import tkinter as tk

from tkinter import messagebox
from tkinter import *

def add_task():

    task = task_entry.get()

    if task:

        tasks_list.insert(tk.END, task)

        task_entry.delete(0, tk.END)

    else:

        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():

    selected_task_index = tasks_list.curselection()

    if selected_task_index:

        tasks_list.delete(selected_task_index)

    else:

        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()

root.title("To-Do List")

task_label = tk.Label(root, text="Enter a task:")

task_entry = tk.Entry(root)

add_button = tk.Button(root, text="Add Task", command=add_task)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)

tasks_list = tk.Listbox(root)
    
task_label.grid(row=0, column=0, padx=10, pady=10)

task_entry.grid(row=0, column=1, padx=10, pady=10)

add_button.grid(row=0, column=2, padx=10, pady=10)

delete_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

tasks_list.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()

 