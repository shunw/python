# -*- coding: utf-8 -*-
import sqlite3
import csv
# import codecs
dec='utf-8'
conn = sqlite3.connect('test.db')
c = conn.cursor()

# c.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', '我', '哎哟', 100, 35.14)")
# conn.commit()
# conn.close()

''' 
check how to search with Chinese
'''
c.execute("SELECT * from stocks WHERE trans == '我'")
for i in c:
	for t in i:
		try: print t.encode(dec)
		except: print t

# # encode Chinese
# data_raw = c.execute("SELECT * from stocks")
# data = list()
# for i in data_raw:
# 	temp = list()
# 	for t in i:
# 		if type(t) == float: temp.append(t)
# 		else: temp.append(t.encode(dec))
# 	data.append(temp)

# # to write the output
# with open('output.csv', 'wb') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(['Date', 'Trans', 'Symbol', 'qty', 'Price'])
# 	writer.writerows(data)
# conn.close()

