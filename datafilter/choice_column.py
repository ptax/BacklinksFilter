
import tkinter as tk
from tkinter import ttk

def Metod_Select_Colum_Frame(root,num_colum,num_row,data):

    ttk.Label(root, text=f"Select the column with the url:",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")
    n = tk.StringVar()
    global Metod_Select_Column
    Metod_Select_Column = ttk.Combobox(root, width=35, textvariable=n)

    column_list = []
    for col in data.columns:
        column_list.append(col)
    Metod_Select_Column['values'] = tuple(column_list)

    Metod_Select_Column.grid(column=num_colum, row=num_row, sticky='w', padx=180, pady=10)
    Metod_Select_Column.current()
    #Metod_Select_Column.insert(0, Metod_Select_Column['values'][0])
    return Metod_Select_Column



def Metod_Select_Colum_Frame_to_beetwen(root,num_colum,num_row,column_list):

    ttk.Label(root, text=f"Select the column with the Outgoing_links:",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")
    n = tk.StringVar()
    global Metod_Select_Column_to_beetwen
    Metod_Select_Column_to_beetwen = ttk.Combobox(root, width=20, textvariable=n)
    #column_list = []
    #for col in data.columns:
        #column_list.append(col)
    Metod_Select_Column_to_beetwen['values'] = tuple(column_list)
    Metod_Select_Column_to_beetwen.grid(column=num_colum, row=num_row, sticky='w', padx=250, pady=10)
    Metod_Select_Column_to_beetwen.current()

    global link_min
    link_min = tk.Entry(root, width=5)
    link_min.grid(column=0, row=num_row, padx=400, pady=5, sticky='w')
    link_min.insert(0, 10)

    global link_max
    link_max = tk.Entry(root, width=5)
    link_max.grid(column=0, row=num_row, padx=450, pady=5, sticky='w')
    link_max.insert(0, 100)

    global aply_links_beetwen
    aply_links_beetwen = tk.StringVar()
    checkbutton_1 = tk.Checkbutton(root, variable=aply_links_beetwen)
    checkbutton_1.grid(row=num_row, column=num_colum, sticky="w", padx=500, pady=0)
    aply_links_beetwen.set(0)


    #Metod_Select_Column.insert(0, Metod_Select_Column['values'][0])
    return Metod_Select_Column_to_beetwen