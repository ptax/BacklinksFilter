import tkinter as tk
from tkinter import ttk


def CustumFileter_link_nofollow(root,num_colum,count_links_external,type_filter):

    num_row = num_colum + count_links_external
    num_colum = 1
    ttk.Label(root, text=f"{count_links_external} link_nofollow:",
              font=("Times New Roman", 10)).grid(column=num_colum-1,
                                                  row=num_row, padx=1, pady=5)



    n = tk.StringVar()
    global CF_link_nofollow_select
    CF_link_nofollow_select = ttk.Combobox(root, width=45, textvariable=n)

    # Adding combobox drop down list
    CF_link_nofollow_select['values'] = ('{contains} - contains (text value)',
                                  '{notContains} - does not contain (text value)'
                                  )


    CF_link_nofollow_select.grid(column=num_colum, row=num_row, sticky='w', padx=0, pady=10)
    CF_link_nofollow_select.current()

    follow = tk.StringVar()
    checkbutton_1 = tk.Checkbutton(root, text="follow", variable=follow)
    checkbutton_1.grid(row=num_row+1, column=num_colum, sticky="w", padx=0, pady=0,)
    nofollow = tk.StringVar()
    checkbutton_2 = tk.Checkbutton(root, text="nofollow", variable=nofollow)
    checkbutton_2.grid(row=num_row+1, column=num_colum, sticky="w", padx=70, pady=0)
    ugc = tk.StringVar()
    checkbutton_3 = tk.Checkbutton(root, text="ugc", variable=ugc)
    checkbutton_3.grid(row=num_row+1, column=num_colum, sticky="w", padx=150, pady=0)
    sponsored = tk.StringVar()
    checkbutton_4 = tk.Checkbutton(root, text="sponsored", variable=sponsored)
    checkbutton_4.grid(row=num_row+1, column=num_colum, sticky="w", padx=220, pady=0)



    dict_checkbutton = {'follow': follow, 'nofollow': nofollow, 'ugc': ugc, 'sponsored': sponsored}

    return type_filter,CF_link_nofollow_select,dict_checkbutton
