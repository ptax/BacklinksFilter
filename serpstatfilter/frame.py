from tkinter import *
import tkinter as tk

class ScrollableFrame:
    """A scrollable tkinter frame that will fill the whole window"""

    def __init__(self, master, width, height, mousescroll=0):
        self.mousescroll = mousescroll
        self.master = master
        self.height = height
        self.width = width
        self.main_frame = Frame(self.master)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.scrollbar = Scrollbar(self.main_frame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas = Canvas(self.main_frame, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(expand=True, fill=BOTH)

        self.scrollbar.config(command=self.canvas.yview)

        self.canvas.bind(
            '<Configure>',
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.frame = Frame(self.canvas, width=self.width, height=self.height)
        self.frame.pack(expand=True, fill=BOTH)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind("<Enter>", self.entered)
        self.frame.bind("<Leave>", self.left)

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def entered(self, event):
        if self.mousescroll:
            self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

    def left(self, event):
        if self.mousescroll:
            self.canvas.unbind_all("<MouseWheel>")




#master.mainloop()
# use objframe as the main window to make widget