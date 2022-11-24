import tkinter as tk
from tkinter import ttk


def params_searchtype(root,num_colum,num_row):
    # label
    ttk.Label(root, text="Select to searchType :",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                 row=num_row, padx=1, pady=5)
    # Combobox creation
    n = tk.StringVar()
    global searchTypechoosen
    searchTypechoosen = ttk.Combobox(root, width=100, textvariable=n)

    # Adding combobox drop down list
    searchTypechoosen['values'] = ('{url} - the specific URL (site.com/path/)',
                              '{part_url} - URL starts with (site.com/path/*)',
                              '{domain} - only domain (site.com)',
                              '{domain_with_subdomains} - domain with subdomains (subdomain.site.com)'
                              )

    searchTypechoosen.grid(column=num_colum, row=num_row)
    searchTypechoosen.current()
    return searchTypechoosen
