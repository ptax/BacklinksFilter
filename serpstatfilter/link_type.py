import tkinter as tk
from tkinter import ttk

def CustumFileter_link_type(root,num_colum,count_link_type,type_filer):

    num_row = num_colum + count_link_type
    num_colum = 1
    ttk.Label(root, text=f"{count_link_type} Link Type:",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                  row=num_row, padx=1, pady=5)
    n = tk.StringVar()
    global CF_link_type_select
    CF_link_type_select = ttk.Combobox(root, width=35, textvariable=n)

    # Adding combobox drop down list
    CF_link_type_select['values'] = ('{eq} - exact match (number or text value)',
                                  '{neq} - does not meet the requirement (number or text value)',
                                  )

    CF_link_type_select.grid(column=num_colum, row=num_row, sticky='w', padx=0, pady=3)
    CF_link_type_select.current()

    v = tk.StringVar()
    CF_link_type_select_2 = ttk.Combobox(root, width=20, textvariable=v)

    # Adding combobox drop down list
    CF_link_type_select_2['values'] = ('href',
                                       'redirect',
                                       'frame',
                                       'from the form',
                                       'canonical',
                                       'from rss',
                                       'from alternate tag',
                                       'image',
                                  )

    CF_link_type_select_2.grid(column=num_colum, row=num_row, sticky='w', padx=240, pady=3)
    CF_link_type_select_2.current()
    return type_filer,CF_link_type_select,CF_link_type_select_2



