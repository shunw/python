from requests_html import HTMLSession
from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd
import joblib
import os
import re

'''
dev tool -> Elements -> search "zion-data-table_wrapper"
用下面一层 table id="zion-data-table"
select the table content and choose copy outHTML

purpose: 
    1. for fun
    2. check every sheets and combine to one dataframe
        2.1 save each html file
        2.2 read through each html file by python
        2.3 combine to one dataframe
    3. export to csv file 
'''
def refine(text):
    '''
    to remove space, comma, or others within the line, to avoid future error
    ''' 
    
    # for line in text: 
    #     print (line)
    # print (text)
    text = re.sub(r'\n中国.+(\s).+级\n', '_', text)
        # break
    # if '\n' in text: 
    #     print (1)
    print (text)
    return text

def read_each_html_df(fl_name): 
    '''
    read through each html file
    return as df
    '''
    f = open(fl_name, 'r')
    a = ''
    for line in f: 
        if '<td></td>' in line: 
            a += line.replace('<td></td>', '<td>0</td>')
        else: 
            a += line
    f.close()
    soup = BeautifulSoup(a, features="lxml")

    for s in soup(['script', 'style']): 
        s.extact()

    text = soup.get_text()
    
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    # text = refine(text)
    # print (text)
    # print (text[:40])
    text_ls = text.split('\n')[7:]
    # print (text_ls[:10])
    id_ls = [v for i, v in enumerate(text_ls) if i % 9 == 0]
    name_ls = [v for i, v in enumerate(text_ls) if i % 9 == 1]
    try: 
        df = pd.DataFrame({'id': id_ls, 'name': name_ls})
    except: 
        print (id_ls)
        print (name_ls)
    #     # print (text_ls)
    #     pass
    return df

def combine_data():
    '''
    process: 
        1. list all the html files
        2. combine the returned df into a complete one
        3. export to csv file
    '''
    for _, _, files in os.walk('./'):
        pass
    
    data_fls = [re.findall('wait_.*html$', f) for f in files]
    
    df = pd.DataFrame()
    for fl in data_fls: 
        if fl:
            print (fl[0])
            temp_df = read_each_html_df(fl[0])
            if len(df) == 0: 
                df = temp_df.copy()
            else: 
                df = df.append(temp_df)
    print (df.shape)
    df.to_csv('wait_list_name.csv', index= False)


if __name__ == '__main__': 
    # =====================
    # step 1: get the update table 
    combine_data()
    # print ()
    # print ('current applicant qty: {}'.format(updated_df.shape[0]))
    # read_each_html_df('wait_chart_data_3.html')

    
    