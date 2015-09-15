# -*- coding: utf-8 -*-
import random
import codecs 

dec = 'utf-8'

handler = codecs.open('data-v.txt', 'r', dec)
line_counter = 0
data_dict = dict()
for line in handler:
	
	data_row = line.split()

	#-- this is to filter the empty line
	if len(data_row) < 1: continue
	
	#-- get the from_form and to_form index ID.
	if line_counter == 0:
		Field = data_row
		for item in data_row:
			if data_row.index(item) == 0: continue
			print item, data_row.index(item)
		from_form = int(raw_input('please choose which type is the from_form: '))
		for item in data_row:
			if data_row.index(item) == from_form or data_row.index(item) == 0: continue
			print item, data_row.index(item)
		to_form = int(raw_input('please choose which type is the to_form: '))
	
	#-- make dict, and prepare the test. 
	else: 
		data_dict[data_row[from_form]] = data_row[to_form]

	line_counter += 1

key_random = data_dict.keys()
random.shuffle(key_random)

#-- provide questions
for q in key_random:
	ans_opt = raw_input('print "stop" to stop the test\n'+q.encode(dec)+'"'+Field[from_form].encode(dec)+'"'+', please give form '+'"'+Field[to_form].encode(dec)+'": ')
	if ans_opt == 'stop': break
	elif ans_opt == data_dict[q]:
		print 'yes'
	else: 
		print 'ans is: ', data_dict[q]
