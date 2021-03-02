# https://www.youtube.com/watch?v=8qUJ9a_3zSQ

import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("Λίστα εργασιών")


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(
            title="Σφάλμα!", message="Θα πρέπει να εισάγετε μια εργασία"
        )


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(
            title="Σφάλμα!", message="Θα πρέπει να επιλέξετε μια εργασία"
        )


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(
            title="Σφάλμα!", message="Δεν υπάρχει αρχείο αποθηκευμένων εργασιών"
        )


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


# Δημιουργία GUI

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)  # σύνδεση listbox με scrollbar
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Νέα εργασία", width=45, command=add_task)
button_add_task.pack()
button_delete_task = tkinter.Button(
    root, text="Διαγραφή εργασίας", width=45, command=delete_task
)
button_delete_task.pack()

button_load_tasks = tkinter.Button(
    root, text="Φόρτωση εργασιών", width=45, command=load_tasks
)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(
    root, text="Αποθήκευση εργασιών", width=45, command=save_tasks
)
button_save_tasks.pack()

root.mainloop()