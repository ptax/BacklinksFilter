import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import io
buffer = io.StringIO()
import datetime
import api as api

def choice_input_file():
    file_name = askopenfilename(filetypes=[("xlsx Files", "*.xlsx")])
    t = label_input_file_name['text'] = file_name

def choice_input_json():
    file_name = askopenfilename(filetypes=[("Json Files", "*.json")])
    t = label_input_json_name['text'] = file_name


def get_input(serp_file_frame,num_colum, num_row):

    b_input_file = tk.Button(serp_file_frame, text='Select the input file', command=choice_input_file, bg='black', fg='white')
    b_input_file.grid(column=0, row=2, padx=15, pady=5, sticky='w')

    #ttk.Label(serp_file_frame, text=f"separator:[, or ;]",
              #font=("Times New Roman", 10)).grid(column=0,
                                                 #row=2, padx=130, pady=5, sticky='w')
    global sep_parser
    sep_parser = 'tk.Entry(serp_file_frame, width=5)'
    #sep_parser.grid(column=0, row=2, padx=220, pady=5, sticky='w')
    #sep_parser.insert(0, ",")

    global label_input_file_name
    label_input_file_name = tk.Label(serp_file_frame)
    label_input_file_name.grid( column=0,row=2, padx=250, pady=5, sticky='w')

    #choice inpit file
    b_json_file = tk.Button(serp_file_frame, text='Select rule file', command=choice_input_json, bg='black', fg='white')
    b_json_file.grid(column=0, row=3, padx=15, pady=5, sticky='w')
    global label_input_json_name
    label_input_json_name = tk.Label(serp_file_frame)
    label_input_json_name.grid(column=0, row=3, padx=200, pady=5, sticky='w')

    ttk.Label(serp_file_frame, text=f"Status bar:",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=4, padx=5, pady=5, sticky='w')
    global log_parser
    log_parser = tk.Text(serp_file_frame, width=80, height=5)
    log_parser.grid(column=0,row=6, padx=10, pady=5, sticky='w')

    ttk.Label(serp_file_frame, text=f"Serpstat error:",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=7, padx=7, pady=5, sticky='w')

    global erro_serpstat
    erro_serpstat = tk.Text(serp_file_frame, width=80, height=5)
    erro_serpstat.grid(column=0,row=8, padx=10, pady=5, sticky='w')


def get_input_2(serp_file_frame,num_colum, num_row):

    b_input_file = tk.Button(serp_file_frame, text='Select the input file', command=choice_input_file, bg='black', fg='white')
    b_input_file.grid(column=0, row=2, padx=15, pady=5, sticky='w')

    #ttk.Label(serp_file_frame, text=f"separator:[, or ;]",
              #font=("Times New Roman", 10)).grid(column=0,
                                                 #row=2, padx=130, pady=5, sticky='w')
    global sep_parser
    sep_parser = 'tk.Entry(serp_file_frame, width=5)'
    #sep_parser.grid(column=0, row=2, padx=220, pady=5, sticky='w')
    #sep_parser.insert(0, ",")

    global label_input_file_name
    label_input_file_name = tk.Label(serp_file_frame)
    label_input_file_name.grid( column=0,row=2, padx=250, pady=5, sticky='w')

    #choice inpit file
    b_json_file = tk.Button(serp_file_frame, text='Select rule file', command=choice_input_json, bg='black', fg='white')
    b_json_file.grid(column=0, row=3, padx=15, pady=5, sticky='w')
    global label_input_json_name
    label_input_json_name = tk.Label(serp_file_frame)
    label_input_json_name.grid(column=0, row=3, padx=200, pady=5, sticky='w')

    ttk.Label(serp_file_frame, text=f"Status bar:",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=4, padx=5, pady=5, sticky='w')
    global log_parser
    log_parser = tk.Text(serp_file_frame, width=80, height=5)
    log_parser.grid(column=0,row=6, padx=10, pady=5, sticky='w')



