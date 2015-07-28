import re

def get_data(fl, raw):
#this is to make the data out of the function
	for line in open(fl, 'r'):
		item=line.rstrip()
		fd=re.findall('.*=', item)[0][:len(re.findall('.*=', item)[0])-1]
		if re.findall('=.*', item)[0][1:]=="":
			data="NA"
		else:
			data=re.findall('=.*', item)[0][1:]
		try:
			raw[fd].append(data)
		except:
			raw[fd]=data

def list_name(dic):
#this is to create a full list name with len(dict)
	list_n=list()
	b_name="file"
	n=len(dic)
	while n>0:
		list_n.append(b_name+str(len(dic)-n+1))
		n-=1
	return list_n

def dic2list(dic):
#this is to count how many keys in the dic
	lt=list_name(dic) #--->>> this is a list for list names
	n=0
	for i in lt:
		lt[n]=list()
		lt[n].append(dic.keys()[n])
		lt[n].append
		n+=1

	

#module --- get all the files in the folder
#judge if this is the SAD file --- according to some key words
#make the dict file
# --->>> write the dict file to CSV format
#done
import os
from collections import defaultdict
raw=defaultdict(list)

# get all the dat file in the current folder
fl_name=list()
files=[f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if f[-3:] == 'dat':
		fl_name.append(f)

#make the dict file for all the dat data
for n in fl_name:
	get_data(n, raw)

#turn dict file to CSV format
#---create list for all the dic item
n=len(raw)
dic2list(raw)
import csv


# with open('test.csv', 'wb') as f:  # Just use 'w' mode in 3.x
#     w = csv.DictWriter(f, raw.keys())
#     #w.writeheader()
#     w.writerow(raw)
