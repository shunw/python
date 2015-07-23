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


from collections import defaultdict
raw=defaultdict(list)

get_data("file1.dat", raw)
get_data("file2.dat", raw)

print raw
