import tkinter as tk
from tkinter import ttk


def CustumFileter_links_external(root,num_colum,count_links_external,type_filer):
    num_row = num_colum + count_links_external
    num_colum = 1
    ttk.Label(root, text=f"{count_links_external} Links_external:",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                 row=num_row, padx=1, pady=5)

    n = tk.StringVar()
    global CF_links_external_select
    CF_links_external_select = ttk.Combobox(root, width=40, textvariable=n)

    # Adding combobox drop down list
    CF_links_external_select['values'] = ('{gt} - greater than (number value)',
                                  '{lt} - less than (number value)',
                                  '{gte} - greater than or equal (number value)',
                                  '{lte} - less than or equal (number value)'
                                  '{eq} - exact match (number or text value)',
                                  )
    '{between} - between (number value)'

    CF_links_external_select.grid(column=num_colum, row=num_row, sticky='w')

    CF_links_external_select.current()


    print (CF_links_external_select.get())

    global CF_links_external_text
    CF_links_external_text = tk.Entry(root, width=30)
    CF_links_external_text.grid(row=num_row, column=num_colum, sticky='E',  padx=150, pady=3)

    #CF_links_external_text.insert(0, 'For example If {between} 10:20 another 10 ')

    return type_filer,CF_links_external_select,CF_links_external_text
