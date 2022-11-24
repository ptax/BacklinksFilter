
import tkinter as tk
from tkinter import ttk


def params_num_link(root,num_colum,num_row):
    # Select to Search Type
    ttk.Label(root, text="How many backlinks can you get?:",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                 row=num_row, padx=1, pady=5)
    global Num_link
    Num_link = tk.Entry(root, width=10)
    Num_link.grid(row=num_row, column=1,sticky='w')

    return Num_link

def get_link_per_domain(num):
    num = int(num)
    max_size = 100
    if num <= 100:
        page = 1
        size = num
    elif num >= 101:
        size = 100
        page = num // max_size
    return {'page':page, 'size':size}