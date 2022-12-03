from tkinter.messagebox import showinfo

import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.filedialog import askopenfilename
import io
buffer = io.StringIO()

def choice_blacklist1_file():
    files = [('Text Document', '*.txt')]
    filename = filedialog.askopenfilename(
                                          title="Select a File",
                                          filetypes=files,
                                          defaultextension=files)
    filename = filename.strip()
    if (len(filename) == 0):
        messagebox.showinfo("show info", "you must select a file")
        return
    else:
        Puth_Blacklist_1.set(filename)



def Metod_Select_Blacklist_1(win_file_frame,num_colum, num_row):

    ttk.Label(win_file_frame, text=f"BLACKLISTED_STRINGS_1:",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                 row=num_row, padx=10, pady=5, sticky='w')
    button1 = tk.Button(win_file_frame, text='Select', command=choice_blacklist1_file, bg='black', fg='white')
    button1.grid(column=num_colum, row=num_row, padx=200, pady=5, sticky='w')

    global Puth_Blacklist_1
    Puth_Blacklist_1 = tk.StringVar()
    txtFileName = tk.Entry(win_file_frame, textvariable=Puth_Blacklist_1, width=50)
    txtFileName.grid(padx=300, pady=5, row=num_row, column=num_colum, sticky='w')

    return Puth_Blacklist_1

def choice_blacklist2_file():
    files = [('Text Document', '*.txt')]
    filename = filedialog.askopenfilename(
                                          title="Select a File",
                                          filetypes=files,
                                          defaultextension=files)
    filename = filename.strip()
    if (len(filename) == 0):
        messagebox.showinfo("show info", "you must select a file")
        return
    else:
        Puth_Blacklist_2.set(filename)

def choice_white_file():
    files = [('Text Document', '*.txt')]
    filename = filedialog.askopenfilename(
                                          title="Select a File",
                                          filetypes=files,
                                          defaultextension=files)
    filename = filename.strip()
    if (len(filename) == 0):
        messagebox.showinfo("show info", "you must select a file")
        return
    else:
        Puth_Whitelist.set(filename)


def choice_multiple_urls():
    files = [('Text Document', '*.txt')]
    filename = filedialog.askopenfilename(
                                          title="Select a File",
                                          filetypes=files,
                                          defaultextension=files)
    filename = filename.strip()
    if (len(filename) == 0):
        messagebox.showinfo("show info", "you must select a file")
        return
    else:
        Whitelist_multiple_urls.set(filename)

def Metod_Select_Blacklist_2(win_file_frame,num_colum, num_row):

    ttk.Label(win_file_frame, text=f"BLACKLISTED_STRINGS_2:",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                 row=num_row, padx=10, pady=5, sticky='w')
    button1 = tk.Button(win_file_frame, text='Select', command=choice_blacklist2_file, bg='black', fg='white')
    button1.grid(column=num_colum, row=num_row, padx=200, pady=5, sticky='w')

    global Puth_Blacklist_2
    Puth_Blacklist_2 = tk.StringVar()
    txtFileName = tk.Entry(win_file_frame, textvariable=Puth_Blacklist_2, width=50)
    txtFileName.grid(padx=300, pady=5, row=num_row, column=num_colum, sticky='w')

    return Puth_Blacklist_2



def Metod_Select_White(win_file_frame,num_colum, num_row):

    ttk.Label(win_file_frame, text=f"WHITELISTED_STRINGS:",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                 row=num_row, padx=10, pady=5, sticky='w')
    button1 = tk.Button(win_file_frame, text='Select', command=choice_white_file, bg='black', fg='white')
    button1.grid(column=num_colum, row=num_row, padx=200, pady=5, sticky='w')

    global Puth_Whitelist
    Puth_Whitelist = tk.StringVar()
    txtFileName = tk.Entry(win_file_frame, textvariable=Puth_Whitelist, width=50)
    txtFileName.grid(padx=300, pady=5, row=num_row, column=num_colum, sticky='w')

    return Puth_Whitelist


def Metod_Dublicates_Url(win_file_frame, num_colum, num_row):

    ttk.Label(win_file_frame, text=f"multiple URLs:",
              font=("Times New Roman", 10)).grid(column=num_colum,
                                                 row=num_row, padx=10, pady=5, sticky='w')
    button1 = tk.Button(win_file_frame, text='Select', command=choice_multiple_urls, bg='black', fg='white')
    button1.grid(column=num_colum, row=num_row, padx=200, pady=5, sticky='w')

    global Whitelist_multiple_urls
    Whitelist_multiple_urls = tk.StringVar()
    txtFileName = tk.Entry(win_file_frame, textvariable=Whitelist_multiple_urls, width=50)
    txtFileName.grid(padx=300, pady=5, row=num_row, column=num_colum, sticky='w')

    return Whitelist_multiple_urls