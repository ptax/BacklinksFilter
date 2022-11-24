import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import io
buffer = io.StringIO()
import datetime



def name_file(filename):
    return filename

list_colums = []
def read_data_frame(filename, separator):
    if filename is not None:
        my_df = pd.read_csv(filename, sep=separator.get())
        file_info = my_df.info(verbose = True, buf=buffer)
        inputtxt.insert(tk.END, str(buffer.getvalue().replace("<class 'pandas.core.frame.DataFrame'>",f'{datetime.datetime.now()} FILE STATS:')))
        for col in my_df.columns:
            list_colums.append(col)
            global my_data
            my_data = my_df.copy()
        return file_info



def choice_input_file():
    file_name = askopenfilename(filetypes=[("CSV Files", "*.csv")])
    t = label_input_file_name['text'] = file_name

def choice_input_json():
    file_name = askopenfilename(filetypes=[("CSV Files", "*.csv")])
    t = label_input_file_name['text'] = file_name

def read_csv(win_file_frame,num_colum, num_row):
    button1 = tk.Button(win_file_frame, text='Select the input file', command=choice_input_file, bg='brown', fg='white')
    button1.grid(column=0, row=num_row, padx=15, pady=5, sticky='w')


    ttk.Label(win_file_frame, text=f"separator:[, or ;]",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=num_row, padx=130, pady=5, sticky='w')
    global separator
    separator = tk.Entry(win_file_frame, width=5)
    separator.grid(column=0, row=num_row, padx=220, pady=5, sticky='w')
    separator.insert(0, ",")

    global label_input_file_name
    label_input_file_name = tk.Label(win_file_frame)
    label_input_file_name.grid( column=0,row=num_row, padx=250, pady=5, sticky='w')


    #global label_input_json_name
    #label_input_json_name = tk.Label(win_file_frame)
    #label_input_json_name.grid( column=0,row=num_row+1, padx=10, pady=5, sticky='w')

    #button2 = tk.Button(win_file_frame, text='Select the JSON', command=choice_input_json, bg='brown', fg='white')
    #button2.grid(column=0, row=num_row+1, padx=10, pady=5, sticky='w')

    global inputtxt
    inputtxt = tk.Text(win_file_frame, width=100, height=5)
    inputtxt.grid(column=0,row=num_row+2, padx=10, pady=5, sticky='w')

    var = tk.IntVar()
    button2 = tk.Button(win_file_frame, text='Check file', command=lambda: var.set(1), bg='brown', fg='white')
    button2.grid(column=0, row=num_row+3, padx=15, pady=5, sticky='w')
    button2.wait_variable(var)




    data = read_data_frame(label_input_file_name['text'], separator)


    list_colums = []
    if label_input_file_name['text'] is not None:
        my_df = pd.read_csv(label_input_file_name['text'], sep=separator.get())
        file_info = my_df.info(verbose = True, buf=buffer)
        inputtxt.insert(tk.END, str(buffer.getvalue().replace("<class 'pandas.core.frame.DataFrame'>",'FILE STATS:')))

    return my_df