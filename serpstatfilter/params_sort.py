import tkinter as tk
from tkinter import ttk


def params_sort(root,num_colum,num_row):
    # label
    ttk.Label(root, text="Select to Sort Parameter:",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                 row=num_row, padx=1, pady=5)
    # Combobox creation
    n = tk.StringVar()
    global sortchoosen
    sortchoosen = ttk.Combobox(root, width=100, textvariable=n)

    # Adding combobox drop down list
    sortchoosen['values'] = ('{check} - date of the first detection',
                              '{url_from} - the referring page',
                              '{anchor} - the anchor of the backlink',
                              '{link_nofollow} - link attributes',
                              '{links_external} - a number of outgoing links from the referring page',
                              '{link_type} - the type of incoming link',
                               '{url_to} - a landing page'
                              )

    sortchoosen.grid(column=num_colum, row=num_row)
    sortchoosen.current()

    return sortchoosen