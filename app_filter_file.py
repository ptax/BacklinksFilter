import pandas as pd
import tkinter as tk
from tkinter import ttk, SUNKEN
from tkinter.filedialog import askopenfilename
import datafilter.input_open_file as open_file
import datafilter.choice_column as choice_column
import datafilter.filter_choice as filter_choice
import datafilter.pd_metod as pd_metod
import datafilter.choice_black_list as choice_black_list
import datetime
import io


buffer = io.StringIO()


def get_seting_filter(win_file_frame):
    MY_DATA = DATA.copy()
    colum_name = choice_column.Metod_Select_Column.get()


    duplicates_drop_name = filter_choice.check_dublicates.get()
    blacklist_1_file_name = choice_black_list.Puth_Blacklist_1.get()
    blacklist_2_file_name = choice_black_list.Puth_Blacklist_2.get()
    root_domain_drop_name = filter_choice.check_root_domain.get()
    max_char_name = filter_choice.max_char.get()

    symbol_1_name = filter_choice.symbol_1.get()
    max_char_symbol_1_name = filter_choice.max_char_symbol_1.get()
    aply_symbol_1_name = filter_choice.aply_symbol_1.get()

    symbol_2_name = filter_choice.symbol_2.get()
    max_char_symbol_2_name = filter_choice.max_char_symbol_2.get()
    aply_symbol_2_name = filter_choice.aply_symbol_2.get()

    symbol_3_name = filter_choice.symbol_3.get()
    max_char_symbol_3_name = filter_choice.max_char_symbol_3.get()
    aply_symbol_3_name = filter_choice.aply_symbol_3.get()

    max_char_affer_sybol_name = filter_choice.max_char_affer_sybol.get()
    aply_affer_sybol_name = filter_choice.aply_affer_sybol.get()

    white_list_file_name = choice_black_list.Puth_Whitelist.get()


    link_min_name = choice_column.link_min.get()
    link_max_name = choice_column.link_max.get()
    aply_links_beetwen = choice_column.aply_links_beetwen.get()
    colum_name_link = choice_column.Metod_Select_Column_to_beetwen.get()

    root_domain_white_name = filter_choice.check_root_domain_white.get()

    if int(duplicates_drop_name) == 1:
        MY_DATA = pd_metod.drop_dublicates(MY_DATA, colum_name)
        open_file.inputtxt.insert('0.0', f"Removing duplicates {datetime.datetime.now()} \n")
    if len(blacklist_1_file_name) >= 5:
        MY_DATA = pd_metod.drop_string(MY_DATA, colum_name, blacklist_1_file_name)
        open_file.inputtxt.insert('0.0', f"Removing rows from blacklist_1 {datetime.datetime.now()}  \n")
    if len(blacklist_2_file_name) >= 5:
        MY_DATA = pd_metod.drop_string(MY_DATA, colum_name, blacklist_2_file_name)
        open_file.inputtxt.insert('0.0', f"Removing rows from blacklist_2 {datetime.datetime.now()}  \n")
    if int(root_domain_drop_name) == 1:
        MY_DATA = pd_metod.drop_root_domain(MY_DATA, colum_name)
        open_file.inputtxt.insert('0.0', f"Removing root domain {datetime.datetime.now()}  \n")
    if int(max_char_name) > 0:
        MY_DATA = pd_metod.drop_line_max_char(MY_DATA, colum_name, max_char_name)
        open_file.inputtxt.insert('0.0', f"Removing rows MAX CHAR {datetime.datetime.now()}  \n")
    if int(aply_symbol_1_name) == 1:
        MY_DATA = pd_metod.drop_symbol_domain(MY_DATA, colum_name, symbol_1_name, max_char_symbol_1_name)
        open_file.inputtxt.insert('0.0', f"Removing rows SYMBOL 1 {datetime.datetime.now()}  \n")
    if int(aply_symbol_2_name) == 1:
        MY_DATA = pd_metod.drop_symbol_domain(MY_DATA, colum_name, symbol_2_name, max_char_symbol_2_name)
        open_file.inputtxt.insert('0.0', f"Removing rows SYMBOL 2 {datetime.datetime.now()}  \n")
    if int(aply_symbol_3_name) == 1:
        MY_DATA = pd_metod.drop_symbol_domain(MY_DATA, colum_name, symbol_3_name, max_char_symbol_3_name)
        open_file.inputtxt.insert('0.0', f"Removing rows SYMBOL 3 {datetime.datetime.now()}  \n")
    if int(aply_affer_sybol_name) == 1:
        MY_DATA = pd_metod.drop_sring_affer(MY_DATA, colum_name, max_char_affer_sybol_name)
        open_file.inputtxt.insert('0.0', f"Characters after a query string ?  {datetime.datetime.now()}  \n")
    if len(white_list_file_name) >= 5:
        MY_DATA = pd_metod.white_string(MY_DATA, colum_name, white_list_file_name)
        open_file.inputtxt.insert('0.0', f"White list {datetime.datetime.now()}  \n")
    if int(aply_links_beetwen) == 1:
        MY_DATA = pd_metod.link_beetwen(MY_DATA, colum_name_link, int(link_min_name), int(link_max_name))
        open_file.inputtxt.insert('0.0', f"Between links {datetime.datetime.now()}  \n")
    if int(root_domain_white_name) == 1:
        MY_DATA = pd_metod.white_root_domain(MY_DATA, colum_name)
        open_file.inputtxt.insert('0.0', f"Only root domain {datetime.datetime.now()}  \n")
    save_file_button = tk.Button(win_file_frame, text='Save file', command=lambda:save_result(MY_DATA), bg='green', fg='white')
    save_file_button.grid(column=0, row=18, padx=123, pady=15, sticky='w')





def default_filter():
    choice_column.Metod_Select_Colum_Frame.inceert(0, choice_column.Metod_Select_Column['values'][0])


def save_result(save_data):
    try:
        # with block automatically closes file
        with tk.filedialog.asksaveasfile(mode='w', defaultextension=".csv") as file:
            save_data.to_csv(file.name, index=False)
    except AttributeError:
        # if user cancels save, filedialog returns None rather than a file object, and the 'with' will raise an error
        print("The user cancelled save")
def _on_frame_configure(self, event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))
def filter_interface():
    global win_file_filter
    win_file_filter = tk.Tk()
    win_file_filter.title("Filter Backlinks")
    #win_file_filter.geometry("800x600")
    win_file_filter.configure(background="light gray")

    frame = tk.Frame(win_file_filter, borderwidth=2, relief=SUNKEN,  bg="#EBEBEB")
    frame.grid(column=0, row=0, sticky='NSEW')
    yscrollbar = tk.Scrollbar(frame)
    yscrollbar.grid(column=1, row=0, sticky='NS')
    global canvas
    canvas = tk.Canvas(frame, bd=0, yscrollcommand=yscrollbar.set, width=900, height=600)
    canvas.grid(column=0, row=0, sticky='NSEW')

    yscrollbar.config(command=canvas.yview)

    win_file_frame = tk.Frame(canvas, borderwidth=2, relief=SUNKEN,  bg="#EBEBEB")
    canvas.create_window(0, 0, window=win_file_frame, anchor='nw')


    # label text for title
    ttk.Label(win_file_frame, text="Filter Backlinks",
              background='green', foreground="white",
              font=("Times New Roman", 15)).grid(row=1, column=0)
    global DATA
    DATA = open_file.read_csv(win_file_frame, num_colum=0, num_row=2)

    choice_column.Metod_Select_Colum_Frame(win_file_frame,num_colum=0,num_row=5,data=DATA)

    filter_choice.Metod_Select_Drop_Dublicates(win_file_frame, num_colum=0, num_row=6)


    choice_black_list.Metod_Select_Blacklist_1(win_file_frame, num_colum=0, num_row=7)
    choice_black_list.Metod_Select_Blacklist_2(win_file_frame, num_colum=0, num_row=8)


    filter_choice.Metod_Select_Drop_Root_Domain(win_file_frame, num_colum=0, num_row=9)

    filter_choice.Metod_Select_Max_Char_Str(win_file_frame, num_colum=0, num_row=10)
    filter_choice.Metod_Drop_Symbol_1(win_file_frame, num_colum=0, num_row=11)
    filter_choice.Metod_Drop_Symbol_2(win_file_frame, num_colum=0, num_row=12)
    filter_choice.Metod_Drop_Symbol_3(win_file_frame, num_colum=0, num_row=13)
    filter_choice.Metod_Drop_String_Affer(win_file_frame, num_colum=0, num_row=14)
    choice_black_list.Metod_Select_White(win_file_frame, num_colum=0, num_row=15)

    choice_column.Metod_Select_Colum_Frame_to_beetwen(win_file_frame,num_colum=0,num_row=16,column_list=choice_column.Metod_Select_Column['values'])

    filter_choice.Metod_Select_White_Root_Domain(win_file_frame, num_colum=0, num_row=17)


    save_filter_button = tk.Button(win_file_frame, text='Apply the filter', command=lambda : get_seting_filter(win_file_frame), bg='orange', fg='green')
    save_filter_button.grid(column=0, row=18, padx=15, pady=20, sticky='w')


    win_file_frame.bind("<Configure>", _on_frame_configure)

    #win_file_frame.bind("<Configure>", update_scrollregion)

    win_file_frame.mainloop()

if __name__ == "__main__":
    filter_interface()
    #df = open_file()
    #drop duplicates in Name Column

    #drop contains in string (True or Falce)
    #df_new = df[df["url_from"].str.contains("vsesv") == False]

    #df_new_2 = df[df["url_from"].str.contains("vsesv") == False]

    #print ( df_new_2.head(41))
