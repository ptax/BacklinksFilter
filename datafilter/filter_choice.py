import tkinter as tk
from tkinter import ttk


def Metod_Select_Drop_Dublicates(root, num_colum, num_row):
    ttk.Label(root, text=f"Remove duplicates",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")

    global check_dublicates
    check_dublicates = tk.StringVar()
    checkbutton_1 = tk.Checkbutton(root, variable=check_dublicates)
    checkbutton_1.grid(row=num_row, column=num_colum, sticky="w", padx=130, pady=0)
    check_dublicates.set(1)



    return check_dublicates



def Metod_Select_Drop_Root_Domain(root, num_colum, num_row):
    ttk.Label(root, text=f"Remove root domain",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")
    global check_root_domain
    check_root_domain = tk.StringVar()
    checkbutton_1 = tk.Checkbutton(root, variable=check_root_domain)
    checkbutton_1.grid(row=num_row, column=num_colum, sticky="w", padx=130, pady=0)
    check_root_domain.set(1)
    return check_root_domain



def Metod_Select_White_Root_Domain(root, num_colum, num_row):
    ttk.Label(root, text=f"Only root domain",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")
    global check_root_domain_white
    check_root_domain_white = tk.StringVar()
    checkbutton_1 = tk.Checkbutton(root, variable=check_root_domain_white)
    checkbutton_1.grid(row=num_row, column=num_colum, sticky="w", padx=130, pady=0)
    check_root_domain_white.set(0)
    return check_root_domain_white





def Metod_Select_Max_Char_Str(root, num_colum, num_row):
    ttk.Label(root, text=f"Remove URL MAX_NUMBER_OF_CHARACTERS",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")
    global max_char
    max_char = tk.Entry(root, width=5)
    max_char.grid(column=0, row=num_row, padx=300, pady=5, sticky='w')
    max_char.insert(0, "150")
    return max_char


def Metod_Drop_Symbol_1(root, num_colum, num_row):
    ttk.Label(root, text=f"MAX_NUMBER_OF_SYMBOL_1 ",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")
    global symbol_1
    symbol_1 = tk.Entry(root, width=5)
    symbol_1.grid(column=0, row=num_row, padx=200, pady=5, sticky='w')
    symbol_1.insert(0, "-")

    global max_char_symbol_1
    max_char_symbol_1 = tk.Entry(root, width=5)
    max_char_symbol_1.grid(column=0, row=num_row, padx=300, pady=5, sticky='w')
    max_char_symbol_1.insert(0, "5")

    global aply_symbol_1
    aply_symbol_1 = tk.StringVar()
    checkbutton_1 = tk.Checkbutton(root, variable=aply_symbol_1)
    checkbutton_1.grid(row=num_row, column=num_colum, sticky="w", padx=350, pady=0)
    aply_symbol_1.set(1)
    return symbol_1, max_char_symbol_1,aply_symbol_1


def Metod_Drop_Symbol_2(root, num_colum, num_row):
    ttk.Label(root, text=f"MAX_NUMBER_OF_SYMBOL_2 ",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")
    global symbol_2
    symbol_2 = tk.Entry(root, width=5)
    symbol_2.grid(column=0, row=num_row, padx=200, pady=5, sticky='w')
    symbol_2.insert(0, "=")

    global max_char_symbol_2
    max_char_symbol_2 = tk.Entry(root, width=5)
    max_char_symbol_2.grid(column=0, row=num_row, padx=300, pady=5, sticky='w')
    max_char_symbol_2.insert(0, "5")

    global aply_symbol_2
    aply_symbol_2 = tk.StringVar()
    checkbutton_1 = tk.Checkbutton(root, variable=aply_symbol_2)
    checkbutton_1.grid(row=num_row, column=num_colum, sticky="w", padx=350, pady=0)
    aply_symbol_2.set(1)
    return symbol_2, max_char_symbol_2,aply_symbol_2


def Metod_Drop_Symbol_3(root, num_colum, num_row):
    ttk.Label(root, text=f"MAX_NUMBER_OF_SYMBOL_3",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")
    global symbol_3
    symbol_3 = tk.Entry(root, width=5)
    symbol_3.grid(column=0, row=num_row, padx=200, pady=5, sticky='w')
    symbol_3.insert(0, "&")

    global max_char_symbol_3
    max_char_symbol_3 = tk.Entry(root, width=5)
    max_char_symbol_3.grid(column=0, row=num_row, padx=300, pady=5, sticky='w')
    max_char_symbol_3.insert(0, "5")

    global aply_symbol_3
    aply_symbol_3 = tk.StringVar()
    checkbutton_1 = tk.Checkbutton(root, variable=aply_symbol_3)
    checkbutton_1.grid(row=num_row, column=num_colum, sticky="w", padx=350, pady=0)
    aply_symbol_3.set(1)
    return symbol_3, max_char_symbol_3,aply_symbol_3


def Metod_Drop_String_Affer(root, num_colum, num_row):
    ttk.Label(root, text=f"Characters after a query string ? ",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                  row=num_row, padx=10, pady=5, sticky="w")


    global max_char_affer_sybol
    max_char_affer_sybol = tk.Entry(root, width=5)
    max_char_affer_sybol.grid(column=0, row=num_row, padx=300, pady=5, sticky='w')
    max_char_affer_sybol.insert(0, "20")

    global aply_affer_sybol
    aply_affer_sybol = tk.StringVar()
    checkbutton_1 = tk.Checkbutton(root, variable=aply_affer_sybol)
    checkbutton_1.grid(row=num_row, column=num_colum, sticky="w", padx=350, pady=0)
    aply_affer_sybol.set(1)
    return max_char_affer_sybol,aply_affer_sybol