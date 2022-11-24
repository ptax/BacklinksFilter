import tkinter as tk
from tkinter import ttk, SUNKEN
from tkinter.filedialog import askopenfilename
import api.parser_dialog as parser_dialog
#import api.get_data as get_data
import requests
import json
import pandas as pd
import time
import sys
import threading


Serp_Error = {
    '400': 'Query required: The query parameter (domain, URL) was not specified;',
    '400': 'SE database parameter not set! Add {required_se} to your get query: The SEparameter was not specified.',
    '400': 'Wrong search engine! Invalid search engine;',
    '400': 'Missing token! Query token missing;',
    '400': 'Json schema validation error: not a valid json query schema;',
    '402': 'Plan credit exceeded! The pricing plan has run out of credits;',
    '402': 'Pricing plan credits exceeded;',
    '402': 'To get more than {max_sort_size} results use export report methods: The maximum allowable credit for sorting has been exceeded. You can use export to get the data;',
    '403': 'Problems with authorization (invalid token, forbidden method or user blocked);',
    '403': 'Selected SE is limited for your account: The selected search engine is not available for your account;',
    '403': 'Forbidden query! Query access denied;',
    '403': 'Invalid token! Invalid query token;',
    '403': 'Invalid user! Not a valid user;',
    '403': 'Not enough credits for this query: Not enough credits for this query;',
    '403': 'API not allowed for your plan! API access is not available for your plan;',
    '403': 'Method forbidden: access to the procedure is prohibited;',
    '403': 'Not access to functional: no access to functionality;403 Wrong method or access denied! Invalid request method or access denied for this procedure;',
    '404': 'Empty result! Empty query result;',
    '404': 'Wrong API query! Use API domain subdomain: Invalid API query;',
    '429': 'Query frequency exceeded, we recommend increasing the interval between queries;',
    '429': 'Too many queriesy: too many queries;',
    '500': 'Server error: Undefined server error;',
    '32012': 'Credits exceeded: credits are over;',
    '32018': 'Wrong search engine provided: Invalid search engine specified;',
    '32016': 'Large query domains not supported: large domains are not available for query;',
    '32116': 'Procedure name not allowed exact count: used when getting the exact number of available rows;',
    '32116': 'Method not supported by this provider: the query or procedure is not supported by the specified provider (for example, some methods are not available if the serpstat provider);',
    '32015': 'No data found for requested domain: no information found for the specified domain;',
    '32017': 'No data found for requested domain: no information found for the specified domain;',
    '32117': 'Not allowed field: {field}: The field for the filter is incorrect or not used in this procedure;',
    '32010': 'Invalid crawl date: the date in the filter is incorrect;',
    '32117': 'Not allowed method {method} for field {field}: the method for filtering is specified incorrectly (for the compareType parameter) or the field does not support the specified filtering method;',
    '32117': 'Not allowed values ​​for between method: Invalid values ​​for the between method;',
    '32117': 'Field compareType is required: compareType filtering method not specified;',
    '32117': 'Field value is required: the field for filtering is not set;',
    '32117': 'Not allowed params for filter: invalid params for filtering.'}

def _on_frame_configure(self, event=None):
    serp_canvas.configure(scrollregion=serp_canvas.bbox("all"))


def look_file(save_file):
    try:
        with open(save_file) as check_file:
            check_file = check_file.readline()
        if check_file:
            return False
        else:
            return True
    except FileNotFoundError:
        return True


def serpastat_token():
    with open('token.json') as token:
        global TOKEN
        TOKEN = json.loads(token.read())
    return TOKEN




def get_new_backlinks(save_file,colum_comanid,input_file_name):
    time.sleep(3)
    api_url = f"https://api.serpstat.com/v4/?token={TOKEN['token']}".strip()
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    try:
        response = requests.post(api_url, data=json.dumps(SEARCH_JSON), headers=headers)
        data = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        reserv_file = input_file_name.replace('.csv', '_reserv.csv')
        DFInput.to_csv(reserv_file, index=False, mode='w', header=True)
        print ('Problem with connect',e)
    try:
        DFserpstat = pd.DataFrame(data['result']['data'])
        DFserpstat['Urls'] = SEARCH_JSON['params']['query']
        DFserpstat['Campaign ID'] = colum_comanid
        if look_file(save_file):
            DFserpstat.to_csv(save_file, index=False, mode='a', header=True)
        else:
            DFserpstat.to_csv(save_file, index=False, mode='a', header=False)
    except KeyError as key_error:
        serpstat_eror = str(data['error']['message']) + 'Num Mistake ' + str(data['error']['code'])
        #parser_dialog.log_parser.insert('0.0', "Err: " + str(serpstat_eror) + "\n")
        try:
            num_code = str(data['error']['code'])
            answer = Serp_Error[num_code]
        except KeyError:
            num_code = None
            answer = None
        if answer:
            log_no_data = str(SEARCH_JSON['params']['query'])   + ';' +  str(colum_comanid) + ';' + str(data['error']['message']) + ';' + str(data['error']['code'])
            log_no_data = f"Err; {num_code};{answer}; {str(SEARCH_JSON['params']['query'])}; {str(colum_comanid)} \n"
            parser_dialog.erro_serpstat.insert('end', log_no_data + "\n")
            parser_dialog.erro_serpstat.see('end')
            parser_dialog.erro_serpstat.update_idletasks()

            with open('log_no_data.txt', 'a') as log:
                log.write(log_no_data + '\n')
        else:
            reserv_file = input_file_name.replace('.csv', '_reserv.csv')
            DFInput.to_csv(reserv_file, index=False, mode='w', header=True)
            raise KeyError(f"{serpstat_eror}")



#get_new_backlinks(MyUrl=MyUrl,searchType='url')

def search_query_in_file(file_name):
    with open(file_name) as file:
        global SEARCH_JSON
        SEARCH_JSON = json.loads(file.read())
    return SEARCH_JSON


def read_input_file(input_file_name,save_file,sep_p):
    global DFInput

    DFInput = pd.read_csv(input_file_name, sep=sep_p)

    for data, values in DFInput.iterrows():
        my_url = values[0]
        campaign_id = values[1]
        SEARCH_JSON['params']['query'] = my_url
        log_print =  str(data) + ' ' + str(my_url)
        print (log_print)

        parser_dialog.log_parser.insert('end', "URL: " + str(log_print) + "\n")
        parser_dialog.log_parser.see('end')
        parser_dialog.log_parser.update_idletasks()

        get_new_backlinks(save_file,campaign_id,input_file_name)
        DFInput.drop(data, axis=0, inplace=True)
        #sep_win.update_idletasks()
        sep_win.update()
        sep_win.after(1000)



def run():

    serpastat_token()
    #parser_dialog.log_parser.insert('0.0', "Token: " + str(TOKEN["token"]) + "\n" )
    input_file_name = parser_dialog.label_input_file_name['text']
    json_file_name = parser_dialog.label_input_json_name['text']
    sep_p = parser_dialog.sep_parser.get()
    save_file = input_file_name.replace('.csv', '_result.csv')
    search_query_in_file(json_file_name)
    t = read_input_file(input_file_name,save_file,sep_p)




from threading import Thread
def serpstat_parser_interfeice():
    global sep_win
    sep_win = tk.Tk()
    sep_win.title("Parser Backlinks")
    sep_win.configure(background="light gray")
    frame_serpstat = tk.Frame(sep_win, borderwidth=2, relief=SUNKEN,  bg="#EBEBEB")
    frame_serpstat.grid(column=0, row=0, sticky='NSEW')
    serp_scrollbar = tk.Scrollbar(frame_serpstat)
    serp_scrollbar.grid(column=1, row=0, sticky='NS')
    global serp_canvas
    serp_canvas = tk.Canvas(frame_serpstat, bd=0, yscrollcommand=serp_scrollbar.set, width=800, height=500)
    serp_canvas.grid(column=0, row=0, sticky='NSEW')
    serp_scrollbar.config(command=serp_canvas.yview)
    serp_file_frame = tk.Frame(serp_canvas, borderwidth=2, relief=SUNKEN,  bg="#EBEBEB")
    serp_canvas.create_window(0, 0, window=serp_file_frame, anchor='nw')

    ttk.Label(serp_file_frame, text="Parser Backlinks",
              background='green', foreground="white",
              font=("Times New Roman", 15)).grid(row=0, column=0)

    parser_dialog.get_input(serp_file_frame, num_colum=0, num_row=4)

    #button2 = tk.Button(serp_file_frame, text='Run', command=run, bg='brown', fg='white')

    button2 = tk.Button(serp_file_frame, text='Run', command=lambda:Thread(target=run).start(), bg='brown', fg='white')
    button2.grid(column=0, row=9, padx=15, pady=5, sticky='w')




    serp_file_frame.bind("<Configure>", _on_frame_configure)
    serp_file_frame.mainloop()


if __name__ == "__main__":
    serpstat_parser_interfeice()
    #t = '32015'
    #print (Serp_Error[t])