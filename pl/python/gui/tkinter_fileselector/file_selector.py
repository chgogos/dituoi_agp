# άνοιγμα αρχείου txt με επιλογή από filedialog

from tkinter import Tk
from tkinter import filedialog


Tk().withdraw()  # για να μην ανοίξει παράθυρο tkinter
fp = filedialog.askopenfile(
    initialdir=".", filetypes=(("αρχεία κειμένου", "*.txt"), ("όλα τα αρχεία", "*.*"))
)

with open(fp.name, "r") as f:
    txt = f.read()

print(txt)
