# Παράδειγμα με Button, (Entry + StringVar), Labels 

import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test")

        self.btn1 = ttk.Button(self, text="Push Me!", command=self.open_child_window)
        self.btn1.place(x=10, y=0)

        self.string_var = tk.StringVar()
        self.string_var.set("test")
        self.ent1 = ttk.Entry(self, textvariable=self.string_var)
        self.ent1.place(x=10, y=30)

        self.lbl1 = ttk.Label(self, text="dummy")
        self.lbl1.place(x=10, y=60)

        self.lbl2 = ttk.Label(self, text="dummy")
        self.lbl2.place(x=10, y=90)

    def open_child_window(self):
        self.lbl1["text"] = "!!!"

        # εναλλακτικά με
        # self.lbl1.config(text="!!!")

        self.lbl2["text"] = self.string_var.get()


if __name__ == "__main__":
    app = App()
    app.mainloop()
