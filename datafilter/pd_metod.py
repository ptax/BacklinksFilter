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
    list_black_list = []
    black_list = set(black_list)

    for word in black_list:
        if '?' in word:
            word = word.replace('?', '\?')
            list_black_list.append(word)
        else:
            list_black_list.append(word)


    df_new = my_df[my_df[colums].str.contains('|'.join(list_black_list),  regex=True)== False]
    #df_new = my_df([my_df[colums].str.contains('|'.join(black_list)) == False], regex=False)
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

    white_list = []
    for word in black_list:
        if '?' in word:
            word = word.replace('?', '\?')
            white_list.append(word)
        else:
            white_list.append(word)
    df_new = my_df[my_df[colums].str.contains('|'.join(white_list)) == True]
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

def search_domain_duplicate(my_df,colums):
    my_df['root_domain'] = my_df[colums].apply(lambda x: urlparse(x).hostname)
    my_df = my_df[my_df['root_domain'].value_counts()[my_df['root_domain']].values > 1]
    #print (my_df)

    list_white_string = ['page']
    df_new = my_df[my_df[colums].str.contains('|'.join(list_white_string)) == True]
    df_new = df_new.drop(axis=0, index=16, inplace=False)
    #print (df_new)
    print (df_new.head())

    #with open(black_list_file, 'r') as f:
        #black_list = f.read().splitlines()
    #black_list = set(black_list)
    #df_new = my_df[my_df[colums].str.contains('|'.join(black_list)) == True]
    #print (my_df.head(40))
    #my_df['url_from'] =
    #my_df['root_domain'].value_counts()
    #df_new = my_df[my_df[colums].str.contains('|'.join(list_root_domain)) == True]
    #row = len(df_new)
    #print ('row',row)

    #return df_new

if __name__ == '__main__':
    df = pd.read_csv(r'C:\Users\o.trukhanskyi\Desktop\BacklinksFilter\data_3.csv')
    black_list_file = r'C:\Users\o.trukhanskyi\Desktop\BacklinksFilter\black_list.txt'
    colums = 'url_from'

    num = 3
    symbol = '&'
    min_l = 41
    max_l = 43

    df = search_domain_duplicate(df,colums)
    print(df)

