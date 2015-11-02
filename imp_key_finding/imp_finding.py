import operator
import csv
from os import listdir
from numpy import *
from collections import defaultdict

from kNN import *

handler = csv.reader(open('test.csv', 'rU'))


keys = list()
raw = defaultdict(list)

### this is to build the raw data in defaultdict way
counter = 0
for line in handler:
	#first line, which is also the defaultdict key
	if counter == 0:
		index = len(line)
		for fd in line:
			keys.append(fd)
		counter += 1
	#the rest of the lines is to make the list part for the defaultdict. 
	else:
		for i in range(index):
			raw[keys[i]].append(line[i])
###get the total item number.
counter = 0
for v in raw.values():
	if counter >=1: break
	value_list_qty = len(v)
	counter +=1

### this is to buil a dict: the key is the field; and the value is the [highest percent, element value]
### ignore the fields if all elements value are the same
def cal_dictelement(key, value_list, value_list_qty):
	class_k = key
	temp = dict()
	for i in value_list:
		temp[i] = temp.get(i, 0)+1
	sortedTemp = sorted(temp.iteritems(), key=operator.itemgetter(1), reverse=True)
	class_v_fd = sortedTemp[0][0]
	class_v_val = sortedTemp[0][1]/float(value_list_qty)
	return class_k, class_v_fd, class_v_val

class_count = defaultdict(list)
for k, v in raw.items():
	class_k, class_v_fd, class_v_val = cal_dictelement(k, v, value_list_qty)
	class_count[class_k].append(class_v_fd)
	class_count[class_k].append(class_v_val)

counter = 0
class_count_comb = dict()
for k, v in raw.items():
	class_k, class_v_fd, class_v_val = cal_dictelement(k, v, value_list_qty)
	if class_v_val == 1.0: continue
	class_count_comb[class_k+' && '+class_v_fd] = class_v_val
	
### find the first n element
fir_n = 3
sortedClass_Comb = sorted(class_count_comb.iteritems(), key=operator.itemgetter(1), reverse=True)

print sortedClass_Comb