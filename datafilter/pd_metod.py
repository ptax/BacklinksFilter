import pandas as pd
from urllib.parse import urlparse
import numpy as np



def drop_dublicates(my_df,colums):
    df_new = my_df.drop_duplicates(subset=colums, keep='first')
    return df_new

import re
def drop_string(my_df,colums,black_list_file):
    with open(black_list_file, 'r') as f:
        black_list = f.read().splitlines()
    black_list = set(black_list)
    safe_matches = [re.escape(m) for m in black_list]
    df_new = my_df[my_df[colums].str.contains('|'.join(safe_matches),  regex=True)== False]
    return df_new



def drop_root_domain(my_df,colums):
    list_root_domain = []
    for date, domain in my_df[colums].iteritems():
        domain_split = domain.split('/')
        domain_split = list(filter(None, domain_split))
        if len(domain_split) == 2:
            list_root_domain.append('^'+domain+'$')
    df_new = my_df[my_df[colums].str.contains('|'.join(list_root_domain)) == False]
    return df_new


def drop_symbol_domain(my_df,colums,symbol,num):
    list_root_domain = []
    for date, domain in my_df[colums].iteritems():
        domain_split = domain.split(symbol)
        domain_split = list(filter(None, domain_split))
        if len(domain_split) >= int(num)+1:
            list_root_domain.append('^'+domain+'$')
    if len(list_root_domain) > 0:
        df_new = my_df[my_df[colums].str.contains('|'.join(list_root_domain)) == False]
        return df_new
    else:
        return my_df


def white_string(my_df,colums,black_list_file):
    with open(black_list_file, 'r') as f:
        black_list = f.read().splitlines()
    black_list = set(black_list)
    safe_matches = [re.escape(m) for m in black_list]
    df_new = my_df[my_df[colums].str.contains('|'.join(safe_matches)) == True]
    df_new = df_new.reset_index(drop=True)
    return df_new


def drop_line_max_char(my_df,colums, max_char):
    df_new = my_df[my_df[colums].str.len() <= int(max_char)]
    return df_new



def drop_sring_affer(my_df,colums,num):
    look = '\?.{' + str(num) + '}'
    df_new = my_df[my_df[colums].str.contains(look) == False]
    return df_new

def link_beetwen(my_df,colums,min_l,max_l):
    df_new = my_df[my_df[colums].between(min_l, max_l)]
    return df_new

def white_root_domain(my_df,colums):
    list_root_domain = []
    for date, domain in my_df[colums].iteritems():
        domain_split = domain.split('/')
        domain_split = list(filter(None, domain_split))
        if len(domain_split) == 2:
            list_root_domain.append('^'+domain+'$')
    df_new = my_df[my_df[colums].str.contains('|'.join(list_root_domain)) == True]
    return df_new


def look_domain_duplicates(my_df,colums):
    my_df['root_domain'] = my_df[colums].apply(lambda x: urlparse(x).hostname)
    my_df[my_df['root_domain'].value_counts()[my_df['root_domain']].values > 1]
    my_df['root_domain'].unique()
    return my_df

def white_list_duplicates(my_df,colums,white_list_file):
    with open(white_list_file, 'r') as f:
        white_list = f.read().splitlines()
    white_list = set(white_list)
    safe_matches = [re.escape(m) for m in white_list]
    my_df = my_df[my_df[colums].str.contains('|'.join(safe_matches)) == True]
    return my_df


def search_domain_duplicate(my_df,colums,duplicates_urls_white):
    with open(duplicates_urls_white, 'r') as f:
        white_list = f.read().splitlines()
    list_white_string = set(white_list)

    del_id_list = []
    white_id_list = []
    change_id_list = []
    white_domain = []
    my_df['root_domain'] = my_df[colums].apply(lambda x: urlparse(x).hostname)
    root_domain_duplicate = my_df[my_df['root_domain'].value_counts()[my_df['root_domain']].values > 1]

    safe_matches = [re.escape(m) for m in list_white_string]

    white_list_domain = root_domain_duplicate[root_domain_duplicate[f'{colums}'].str.contains('|'.join(safe_matches)) == True]

    white_only_one = white_list_domain[white_list_domain['root_domain'].value_counts()[white_list_domain['root_domain']].values == 1]
    for index, row in white_only_one.iterrows():
        white_id_list.append(index)

    white_more_than_one = white_list_domain[white_list_domain['root_domain'].value_counts()[white_list_domain['root_domain']].values > 1]

    c = 0
    if len(white_more_than_one) > 1:
        for index, row in white_more_than_one.iterrows():
            c += 1
            if c == 1:
                white_id_list.append(index)
            else:
                del_id_list.append(index)

    for id_row in white_id_list:
        white_domain.append(urlparse(root_domain_duplicate.loc[id_row, colums]).hostname)

    white_domain_df = root_domain_duplicate[root_domain_duplicate[f'{colums}'].str.contains('|'.join(white_domain)) == True]

    for index, row in white_domain_df.iterrows():
        if index not in white_id_list:
            del_id_list.append(index)


    for index, row in root_domain_duplicate.iterrows():
        if index not in white_id_list:
            change_id_list.append(index)

    for id_row in change_id_list:
        my_df.at[id_row, colums] = ' https://' + str(urlparse(my_df.loc[id_row, colums]).hostname)
    #
    my_df.drop(del_id_list, inplace=True)
    my_df.drop(columns=['root_domain'], inplace=True)

    my_df = drop_dublicates(my_df, colums)
    return my_df

if __name__ == '__main__':
    df = pd.read_csv(r'C:\Users\o.trukhanskyi\Desktop\BacklinksFilter\data_3.csv')
    black_list_file = r'C:\Users\o.trukhanskyi\Desktop\BacklinksFilter\black_list.txt'
    white_list_file = r'C:\Users\o.trukhanskyi\Desktop\BacklinksFilter\white_list.txt'
    colums = 'url_from'

    num = 3
    symbol = '&'
    min_l = 41
    max_l = 43
    list_white_string = ['?page=', 'bere-da-solo-da-giovane-er']

    df = search_domain_duplicate(df,colums,list_white_string)

    print(df.head(50))

