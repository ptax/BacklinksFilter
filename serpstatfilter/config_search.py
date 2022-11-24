import tkinter as tk
import serpstatfilter.Placeholder as ph
from tkinter import ttk
from tkinter.messagebox import showinfo
def get_text():
    print (url.get())

win = tk.Tk()
win.title("Backlinks Exstractor Serpstat API")
win.geometry("500x500")

bt1 = tk.Button(win, text="Start", width=10, height=2)
bt2 = tk.Button(win, text="Stop", width=10, height=2)
bt1.grid(row=0, column=0, padx=10, pady=10)
bt2.grid(row=0, column=1, padx=10, pady=10)

tk.Label(win, text="URL:").grid(row=1, column=0, padx=10, pady=10)
url = tk.Entry(win,  width=50)
url.grid(row=1, column=1, padx=10, pady=10)

tk.Button(win, text="Search",command=get_text).grid(row=2, column=0, padx=10, pady=10)

entry = ph.EntryWithPlaceholder(win, 'Some Text')
entry.grid(row=1, column=1, padx=10, pady=10)

win.mainloop()


