# -*- coding: utf-8 -*-
import random
import codecs 

'''
Purpose:
this is to check the data-v_lesson's verb is same as the data-v's verb, based on the 原型
if different, JUST add the missing verb into the data-v_lesson
if same, do nothing
'''

dec = 'utf-8'


#--- transfer the "data-v_lesson"'s verb into one list, prepare for the comparison
v_les = list()
f_lesson = codecs.open('data-v_lesson.txt', 'r', dec)
for line in f_lesson:
	line = line.strip()
	if len(line) == 0: continue
	if line.isnumeric(): continue
	elif line in v_les: continue
	else: v_les.append(line)

#--- get the verb from "data-v" into one list, prepare for the comparison
# 原型 is in the 5th col. 
v = list()
col = 1
row_n = 0
f = codecs.open('data-v.txt', 'r', dec)
for line in f:
	line = line.split()
	if len(line) == 0: continue
	if not(line[0].isnumeric): continue
	row_n += 1
	if line[col] in v: continue
	else: v.append(line[col])


#--- begin the comparison
v_miss = list()
for i in v_les:
	if i in v: continue
	elif i in v_miss: continue
	else: v_miss.append(i)

#--- add the v_miss list in to the data-v. complete the combination
output = codecs.open('data-v.txt', 'a', dec)
for i in v_miss:
	output.write('\n' + str(row_n) + '\t' + i)
	row_n += 1
