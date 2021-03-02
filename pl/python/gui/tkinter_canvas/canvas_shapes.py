from tkinter import *

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    # σημείο    
    my_canvas.create_oval(x1, y1, x2, y2, fill="black")


root = Tk()
root.title("Canvas")
root.geometry("640x480")

my_canvas = Canvas(root, width=400, height=300, bg="white")
my_canvas.pack(pady=20, expand=YES, fill=BOTH)

# ευθείες γραμμές
my_canvas.create_line(0, 0, 100, 100, fill="black")
my_canvas.create_line(100, 100, 150, 200, fill="red")
my_canvas.create_line(150, 200, 400, 300, fill="green")

# ορθογώνιο
my_canvas.create_rectangle(100, 50, 150, 100, fill="yellow")

# κύκλος
my_canvas.create_oval(150, 150, 170, 170, fill="cyan")

my_canvas.bind("<B1-Motion>", paint)

root.mainloop()