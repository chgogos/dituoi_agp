from PIL import Image, ImageTk
import tkinter as tk


def transform_to_bw():
    img = Image.open("arta.jpg")
    img = img.convert("1")  # ασπρόμαυρο
    imgtk = ImageTk.PhotoImage(img)
    l1.configure(image=imgtk)
    l1.image = imgtk


def transform_to_grey():
    img = Image.open("arta.jpg")
    img = img.convert("L")  # αποχρώσεις του γκρι
    imgtk = ImageTk.PhotoImage(img)
    l1.configure(image=imgtk)
    l1.image = imgtk


root = tk.Tk()
root.geometry("750x600")
root.title("Εικόνες")
img = Image.open("arta.jpg")
imgtk = ImageTk.PhotoImage(img)
l1 = tk.Label(root, image=imgtk)
b1 = tk.Button(root, text="Ασπρόμαυρη εικόνα", command=transform_to_bw)
b2 = tk.Button(root, text="Κλίμακα του γκρι", command=transform_to_grey)
b3 = tk.Button(root, text="Έξοδος", command=root.destroy)


l1.pack()
b1.pack()
b2.pack()
b3.pack()

root.mainloop()
