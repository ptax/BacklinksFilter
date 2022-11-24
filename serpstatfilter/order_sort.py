import tkinter as tk
from tkinter import ttk
def order_sort(root,num_colum,num_row):
    # label
    ttk.Label(root, text="Select to Order Parameter:",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                 row=num_row, padx=1, pady=5)
    # Combobox creation
    n = tk.StringVar()
    global orderchoosen
    orderchoosen = ttk.Combobox(root, width=100, textvariable=n)

    # Adding combobox drop down list
    orderchoosen['values'] = ('{asc} - in the ascending order',
                              '{desc} - in the descending order'
                              )

    orderchoosen.grid(column=num_colum, row=num_row)
    orderchoosen.current()

    return orderchoosen
