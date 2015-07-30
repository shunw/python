import re
import csv
import sys
import os
import datetime as dt
import shutil

def get_data(fl, raw):
#this is to make the data out of the function
	for line in open(fl, 'r'):
		item=line.rstrip()
		fd=re.findall('.*=', item)[0][:len(re.findall('.*=', item)[0])-1]
		print fd
		if re.findall('=.*', item)[0][1:]=="":
			data="NA"
		else:
			data=re.findall('=.*', item)[0][1:]
		#the following 4 lines is for the 1st entry of the dict
		try:
			raw[fd].append(data)
		except:
			raw[fd]=data

def get_data_1(fl, raw, fd_list):
#this is to make the data out of the function
	temp=list() #===>>> this is the name list in the dat/ txt file
	#this is to get all the field name in the dat file
	print fl
	for line in open(fl, 'r'):
		item=line.rstrip()
		dat_=re.findall('.*=', item)[0][:len(re.findall('.*=', item)[0])-1]
		
		if re.findall('=.*', item)[0][1:]=="":
			data="NA"
		else:
			data=re.findall('=.*', item)[0][1:]
		#the following 4 lines is for the 1st entry of the dict
		try:
			raw[dat_].append(data)
		except:
			raw[dat_]=[]
			raw[dat_].append(data)
		temp.append(dat_)

	#this is to compare the temp list and the base one
	if sorted(temp)!=sorted(fd_list):
		diff=list(set(fd_list) -set(temp))
		#print temp, len(temp)
		#print diff, len(diff)
		for dat_ in diff:
			raw[dat_].append("NA")


def collect_field(fl_names):
#this is to collect all the field name in all the files: 
	fd_list=list()
	for f in fl_names:
		for line in open(f, 'r'):
			item=line.rstrip()
			fd=re.findall('.*=', item)[0][:len(re.findall('.*=', item)[0])-1]

			if fd in fd_list:
				continue
			else:
				fd_list.append(fd)
	#print fd_list, len(fd_list)
	return fd_list
	
def get_M_ID(filename):
#this is to judge the what measurement the file contain. 
	for lines in open(filename, 'r'): 
		item=lines.rstrip()
		
		if re.search(".*TestPageID=.*", item):
			m_number=re.findall('=.*', item)[0][1:]
	#print m_number
	return m_number
	
		
def folder_name(ID, extention):
	today=dt.datetime.today().strftime("%Y-%m-%d")
	name=today+"-"+extention+"-"+ID
	
	return name


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

def copytree_bkp(src, dst, names, symlinks=False):
#++++++++++++ NOT VERY USEFUL HERE ++++++++++++
#++++++++++++ COPIED FROM PYTHON WEB ++++++++++++
    os.makedirs(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks)
            else:
                copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
    try:
        copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)

def movetree(src_dir, dst_dir, names):
    for file_ in names:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.move(src_file, dst_dir)


#READ ME
#PURPOSE: get all TXT files in the folder and make the csv data


#STEP 1: make the empty dict file first
from collections import defaultdict
raw=defaultdict(list)

#STEP 2: get all the TXT file names in the current folder
#======= one function add/ 20150730======== judge what PQ measurement it is
fl_name=list()
files=[f for f in os.listdir('.') if os.path.isfile(f)]
extention=raw_input("please enter files extention: ")

#=================if not, judge if the file is same as the first one

for f in files:
	counter=1 #===>>> this is for the judgement. If this is the first file, get the measurement ID/ 
	if f[-3:] == extention:
		#print counter
		if counter==1:
			m_id=get_M_ID(f)
			fl_name.append(f)
			print m_id
		elif get_M_ID(f) != m_id: 
			continue
		else:
			fl_name.append(f)
		counter+=1

#STEP 3: collect the data from files one by one 
#========and make the dict file for all the dat data
#========IF THIS IS DAT FILE, NEED TO COLLECT THE FIELD FIRST
fd_list=collect_field(fl_name)
print fd_list, len(fd_list)
for n in fl_name:
	get_data_1(n, raw, fd_list)


#STEP 4: make the dict to list
#========exchange the col and row
print raw
data_0=sorted(dic2list(raw))
dataflow=listT(data_0)
print dataflow

#STEP 5: write into the csv files
output_name=extention+m_id+".csv"
writeListData(output_name, dataflow)

#STEP 6: move all the files to the backupfolder. 
#====>>> create a new folder/ w date/ w test page ID/ w txt or dat
fd_name=folder_name(m_id, extention)

if not os.path.exists(fd_name):
    os.mkdir(fd_name)
	
#====>>> move all the files to the backupone
scr= "/Users/zhang" #"C:\Users\lishunw\My Work\program\Python\data_imp"
dest=scr+os.sep+fd_name

movetree(scr, dest, fl_name)
#========================END========================


