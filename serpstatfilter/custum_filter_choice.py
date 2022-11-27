import tkinter as tk
from tkinter import ttk

def custum_filter_choice(root,num_colum,num_row):
    # label
    ttk.Label(root, text="Select to Order Parameter:",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                 row=num_row, padx=1, pady=5)
    # Combobox creation
    n = tk.StringVar()
    global CF_Filter_Chosen_Select
    CF_Filter_Chosen_Select = ttk.Combobox(root, width=100, textvariable=n)

    # Adding combobox drop down list
    CF_Filter_Chosen_Select['values'] = ('{url_from} - the referring page',
                             '{anchor} - the anchor of the backlink',
                             '{links_external} - the number of external links from the referring page',
                             '{link_type} - the type of the backlink. Possible values: text, redirect, iframe, form, canonical, rss, alternate, image'
                              )
    '{link_nofollow} - link attributes. Possible values: follow, nofollow, ugc, sponsored',

    CF_Filter_Chosen_Select.grid(column=num_colum, row=num_row)
    CF_Filter_Chosen_Select.current()
    CF_Filter_Chosen_Select.current()


    return CF_Filter_Chosen_Select