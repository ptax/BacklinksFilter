import sys
import api.parser_dialog as parser_dialog

import requests
import json
import pandas as pd
import time
import os.path




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




def get_new_backlinks(save_file,colum_comanid):
    time.sleep(3)
    api_url = f"https://api.serpstat.com/v4/?token={TOKEN['token']}".strip()
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    print(SEARCH_JSON)
    try:
        response = requests.post(api_url, data=json.dumps(SEARCH_JSON), headers=headers)
        data = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        reserv_file = save_file.replace('.csv', '_reserv.csv')
        DFInput.to_csv(reserv_file, index=False, mode='w', header=True)
        print ('Problem with connect',e)
        sys.exit(1)
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
        print(serpstat_eror)
        if data['error']['code'] == 32015:
            log_no_data = str(SEARCH_JSON['params']['query'])   + ';' +  str(colum_comanid) + ';' + str(data['error']['message']) + ';' + str(data['error']['code'])
            with open('log_no_data.txt', 'a') as log:
                log.write(log_no_data + '\n')
        else:
            reserv_file = save_file.replace('.csv', '_reserv.csv')
            DFInput.to_csv(reserv_file, index=False, mode='w', header=True)
            raise KeyError(f"{serpstat_eror}")



#get_new_backlinks(MyUrl=MyUrl,searchType='url')

def search_query_in_file(file_name):
    with open(file_name) as file:
        global SEARCH_JSON
        SEARCH_JSON = json.loads(file.read())
    return SEARCH_JSON


def read_input_file(input_file_name):
    global DFInput
    DFInput = pd.read_csv(input_file_name, sep=';')
    for data, values in DFInput.iterrows():
        my_url = values[0]
        campaign_id = values[1]
        SEARCH_JSON['params']['query'] = my_url
        print (data, my_url)
        parser_dialog.log_parser.insert('0.0', "Token: " + str(data, my_url) + "\n")
        get_new_backlinks(save_file,campaign_id)
        DFInput.drop(data, axis=0, inplace=True)




if __name__ == '__main__':

    file_name = r'C:\Users\o.trukhanskyi\Desktop\BacklinksFilter\1.json'
    save_file = 'data_8.csv'
    input_file_name = r'C:\Users\o.trukhanskyi\Desktop\BacklinksFilter\test_input.csv'

    serpastat_token()
    search_query_in_file(file_name)
    read_input_file(input_file_name)



    #my_qury_data = search_query_in_file(file_name)
    #list_url = ['https://www.samhsa.gov/find-help/national-helpline', 'https://www.chop.edu/clinical-pathway/abuse-physical-primary-care-clinical-pathway']
    #for MyUrl in list_url:
        #data_json = SEARCH_JSON['params']['query'] = MyUrl
        #print (MyUrl)
        #get_new_backlinks(save_file)