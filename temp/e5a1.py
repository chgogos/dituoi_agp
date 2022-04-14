from email import message
import tkinter as tk
from turtle import title

root = tk.Tk()
root.title("Λίστα εργασιών")


def add_task():
    task = entry_task.get()
    if task == "":
        tk.messagebox.showwarning(title="Σφάλμα", message="Πρέπει να εισάγετε κείμενο")
    elif task in tasks.get():
        tk.messagebox.showwarning(title="Σφάλμα", message="Υπάρχει ήδη η τιμή")
    else:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)


def del_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tk.messagebox.showwarning(
            title="Σφάλμα", message="Δεν έχετε επιλέξει εργασία προς διαγραφή"
        )


frame_tasks = tk.Frame(root)
frame_tasks.pack()

tasks = tk.Variable(value=[])
listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, listvariable=tasks)
listbox_tasks.pack()

entry_task = tk.Entry(root, width=50)
entry_task.pack()

btn_add_task = tk.Button(root, text="Νέα εργασία", width=50, command=add_task)
btn_add_task.pack()

btn_del_task = tk.Button(root, text="Διαγραφή", width=50, command=del_task)
btn_del_task.pack()


root.mainloop()
