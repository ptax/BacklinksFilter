#  **** SCROLL BAR TEST *****
from tkinter import *
from tkinter import ttk

def _on_frame_configure(self, event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()
root.title("Scrollbar Test")
root.geometry("800x400")
root.configure(background="light gray")

frame = Frame(root, borderwidth=2, relief=SUNKEN, background="light gray")
frame.grid(column=0, row=0, sticky=N+S+E+W)


yscrollbar = Scrollbar(frame)
yscrollbar.grid(column=1, row=0, sticky=N+S)

canvas = Canvas(frame, bd=0, yscrollcommand=yscrollbar.set)
canvas.grid(column=0, row=0, sticky=N+S+E+W)

yscrollbar.config(command=canvas.yview)

frame = Frame(canvas, borderwidth=2, relief=SUNKEN, background="light gray")
canvas.create_window(4, 4, window=frame, anchor='nw')
frame.bind("<Configure>", _on_frame_configure)

for i in range(30):
    label = ttk.Label(frame, text="This is a label "+str(i))
    label.grid(column=1, row=i, sticky=W)

    text = ttk.Entry(frame, textvariable="text")
    text.grid(column=2, row=i, sticky=W)

root.mainloop()