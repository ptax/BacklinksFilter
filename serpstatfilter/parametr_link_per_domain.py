import tkinter as tk
from tkinter import ttk

def parametr_link_per_domain(root,num_colum,num_row):
    # label
    ttk.Label(root, text="Select linkPerDomain:",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                 row=num_row, padx=1, pady=5)
    # Combobox creation
    n = tk.StringVar()
    global linkperdomainchoosen
    linkperdomainchoosen = ttk.Combobox(root, width=100, textvariable=n)

    # Adding combobox drop down list
    linkperdomainchoosen['values'] = ('{0} - in the ascending order',
                              '{1} - in the descending order'
                              )

    linkperdomainchoosen.grid(column=num_colum, row=num_row)
    linkperdomainchoosen.current()

    return linkperdomainchoosen