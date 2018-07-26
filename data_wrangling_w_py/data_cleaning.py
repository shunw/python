import pandas as pd
from csv import DictReader

df = pd.read_csv('mn.csv', index_col = 0)
df_head = pd.read_csv('mn_headers_updated.csv')

# check if these two columns could be match
# and remove some unimportant columns
not_found = list()
for i in list(df.columns):
    if i not in list(df_head['Name']):
        not_found.append(i)
df = df.drop(not_found, axis = 1)
# id_col = ['HH1', 'HH2', 'LN', 'MWM1', 'MWM2', 'MWM4', 'MWM5']
id_col = ['HH1', 'HH2']
df_nodup = df[-df.duplicated(subset = id_col, keep = 'first')]
# print (df.shape[0] - df_dup.shape[0])
print (df_nodup.shape)
# data_rdr = DictReader(open('mn.csv', 'rb'))
# header_rdr = DictReader(open('mn_headers.csv', 'rb'))

