import tkinter as tk
from tkinter import ttk


def CustumFileter_anhor(root,num_colum,count_anhor,type_filer):
    num_row = num_colum + count_anhor
    num_colum = 1
    ttk.Label(root, text=f"{count_anhor} Anhor from complexFilter :",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                 row=num_row, padx=1, pady=5)




    n = tk.StringVar()
    global CF_anhor_select
    CF_anhor_select = ttk.Combobox(root, width=40, textvariable=n)

    # Adding combobox drop down list
    CF_anhor_select['values'] = ('{contains} - contains (text value)',
                                  '{notContains} - does not contain (text value)',
                                  '{startsWith} - starts with (text value)',
                                  '{endsWith} - ends with (text value)'
                                  )

    CF_anhor_select.grid(column=num_colum, row=num_row, sticky='w')
    CF_anhor_select.current()


    global CF_anchor_text
    CF_anchor_text = tk.Entry(root, width=30)
    CF_anchor_text.grid(row=num_row, column=num_colum, sticky='E',  padx=150, pady=3)
    return type_filer,CF_anhor_select,CF_anchor_text
