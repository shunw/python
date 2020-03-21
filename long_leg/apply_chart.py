from requests_html import HTMLSession
from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd
import joblib

'''
dev tool -> Elements -> search "DataTables_Table_0_wrapper"
select the table content and choose copy outHTML
'''
def update_df(): 
    f = open('chart_data.html', 'r')
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
    
    # print (text[:20])
    text_ls = text.split('\n')[6:]
    # print (text_ls[:10])
    id_ls = [v for i, v in enumerate(text_ls) if i % 8 == 0]
    name_ls = [v for i, v in enumerate(text_ls) if i % 8 == 1]
    df = pd.DataFrame({'id': id_ls, 'name': name_ls})
    return df

def first_time_data(): 
    f = open('original', 'r')
    id_ls = list()
    name_ls = list()
    for line in f: 
        [id_item, name_item]= line.strip().split(' ')
        id_ls.append(id_item)
        name_ls.append(name_item)
    f.close()
    df = pd.DataFrame({'id': id_ls, 'name': name_ls})
    
    df['checked'] = 1
    df['comment'] = ''

    # df.set_index('id', inplace = True)
    return df

def update_one_cell(df, col, idx_ls, value): 
    df.set_index('id', inplace = True)
    for idx in idx_ls: 
        df.at[idx, col] = value
    df.reset_index(inplace = True)

if __name__ == '__main__': 
    # =====================
    # step 1: get the update table 
    updated_df = update_df()
    # print (updated_df.head())
    print ()
    print ('current applicant qty: {}'.format(updated_df.shape[0]))

    
    # =====================
    # step 2: 
    # load the old one; 
    # update the new one with checked/ comment inf by left join old one
    last_df = joblib.load('last_checked.pkl')
    print ()
    print ('checked applicant qty: {}'.format(last_df.shape[0]))
    # print (last_df.shape)

    # # =====================
    # # step 2.5: show the good one
    # # good_one = updated_df.loc[updated_df['checked'] == 1]
    # print (last_df.loc[last_df['comment'] == 'very good', ['id', 'name']])

    # =====================
    # step 3: 
    # find and print the unchecked one
    result = pd.merge(updated_df, last_df, how = 'left', on=['name'], suffixes=('', '_old'))
    print (result.loc[result['checked'] != 1])
    
    unchecked_ind = list(result.loc[result['checked'] != 1, 'id'])
    print (unchecked_ind)
    print ()
    print ('to be check applicant qty: {}'.format(len(unchecked_ind)))
    
    # # =====================
    # # step 4: 
    # # update check and comment info with the latests
    # update_one_cell(result, 'checked', unchecked_ind, 1)
    # # print (unchecked_ind)
    # update_one_cell(result, 'comment', [], 'good')
    # update_one_cell(result, 'comment', [], 'very good')

    # result['comment'].fillna('', inplace = True)
    # result.drop(['id_old'], axis = 1, inplace = True)
    
    # # =====================
    # # step 5 save as the pkl
    # joblib.dump(result, 'last_checked.pkl')
    # print ()
    # print ('latest info updated!')