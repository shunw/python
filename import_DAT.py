import re
import csv
import sys
import os

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
#++++++++++++ NOT VERY USEFUL HERE ++++++++++++
	list_n=list()
	b_name="file"
	n=len(dic)
	while n>0:
		list_n.append(b_name+str(len(dic)-n+1))
		n-=1
	return list_n

def dic2list(dic):
#this is to make the dict into lists
	lt=list() 
	for key, value in dic.iteritems():
		temp=list()
		temp.append(key)
		for i in value:
			temp.append(i)
		lt.append(temp)
		# print lt
		# debug_1()

	return lt

def listT(dataflow):
#this is to exchange the col and row data
	x=zip(*dataflow)
	return x



def writeListData(csvFile, listData):
	fileStream = open(csvFile, 'wb')
	csvWriter = csv.writer(fileStream)
	csvWriter.writerows(listData)


def debug_1():
	#debug code begin
	judge=raw_input("press 1 here: ")
	if judge=="1":
		print " "
	else:
		print "break"
		sys.exit()
	#debug code end


#READ ME
#PURPOSE: get all TXT files in the folder and make the csv data


#STEP 1: make the empty dict file first
from collections import defaultdict
raw=defaultdict(list)

#STEP 2: get all the TXT file names in the current folder
fl_name=list()
files=[f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if f[-3:] == 'txt':
		fl_name.append(f)

#STEP 3: collect the data from files one by one 
#========and make the dict file for all the dat data
for n in fl_name:
	get_data(n, raw)

#STEP 4: make the dict to list
#========exchange the col and row
data_0=sorted(dic2list(raw))
dataflow=listT(data_0)

#STEP 5: write into the csv files
writeListData("test.csv", dataflow)

#========================END========================


