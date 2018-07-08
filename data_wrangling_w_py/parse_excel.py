import xlrd
import pandas as pd

fl_name = 'SOWC 2014 Stat Tables_Table 9.xlsx'
sht_name = 'Table 9 '


'''
**** list all the sheet name ****
'''
book = xlrd.open_workbook(fl_name)
sheet = book.sheet_by_name(sht_name)

xls = pd.ExcelFile(fl_name)
df = pd.read_excel(xls, sht_name, parse_cols = 'B, E, G, I, K, M', skiprows = 13)
col_name = ['countries_n_areas', 'child_labor_total', 'child_labor_male', 'child_labor_female', 'child_marriage_by_15', 'child_marriage_by_18']

'''
**** deal w/ merged items **** PANDAS / EXCEL :
 https://stackoverflow.com/questions/22937650/pandas-reading-excel-with-merged-cells
'''
df.index = pd.Series(df.index).fillna(method='ffill')
df.columns = col_name


end_row = df.loc[df['countries_n_areas'] == 'Zimbabwe'].index.values
end_2 = df.shape[0]
df = df.iloc[:end_row[0]+1]
print (df.tail())