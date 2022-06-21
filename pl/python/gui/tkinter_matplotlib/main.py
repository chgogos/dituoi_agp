from tkinter import *
from turtle import color
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


def plot():
    months = ["Ιανουάριος", "Φεβρουάριος", "Μάρτιος", "Απρίλιος"]
    expenses = [200.0, 300.0, 100.0, 250.0]
    random.shuffle(expenses)
    axes.clear()
    axes.bar(months, expenses, color="red")
    canvas.draw()


window = Tk()
window.geometry("800x600")
window.title("Plot expenses of a year")
frame = Frame(window)
frame.pack()
plot_btn = Button(master=frame, command=plot, text="Plot")
plot_btn.pack()
plot_frame = Frame(window)
plot_frame.pack(side=BOTTOM)
fig = Figure(figsize=(10, 5), dpi=100)
axes = fig.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack()
plot()


if __name__ == "__main__":
    window.mainloop()
