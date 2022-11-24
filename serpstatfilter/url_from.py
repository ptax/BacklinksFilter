import tkinter as tk
from tkinter import ttk


def CustumFileter_url_from(root,num_colum,count_url_from,type_filer):
    num_row = num_colum + count_url_from
    num_colum = 1
    ttk.Label(root, text=f"{count_url_from} URL from complexFilter :",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                 row=num_row, padx=1, pady=5)

    n = tk.StringVar()
    global CF_url_from_select
    CF_url_from_select = ttk.Combobox(root, width=40, textvariable=n)

    # Adding combobox drop down list
    CF_url_from_select['values'] = ('{contains} - contains (text value)',
                                  '{notContains} - does not contain (text value)',
                                  '{startsWith} - starts with (text value)',
                                  '{endsWith} - ends with (text value)'
                                  )

    CF_url_from_select.grid(column=num_colum, row=num_row, sticky='w')
    CF_url_from_select.current()


    global CF_url_from_text
    CF_url_from_text = tk.Entry(root, width=30)
    CF_url_from_text.grid(row=num_row, column=num_colum, sticky='E',  padx=150, pady=3)


    #v = tk.StringVar()
    #CF_or_and = ttk.Combobox(root, width=10, textvariable=v)
    #CF_or_and['values'] = ('{AND}','{OR}',)
    #CF_or_and.grid(column=num_colum, row=num_row+1, sticky='w', padx=250, pady=0)
    #CF_or_and.insert(0, '{AND}')
    #CF_or_and.current()
    return type_filer,CF_url_from_select,CF_url_from_text
