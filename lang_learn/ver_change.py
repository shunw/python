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
		from_form_0 = int(raw_input('please choose which type is the from_form: '))
		for item in data_row:
			if data_row.index(item) == from_form_0 or data_row.index(item) == 0: continue
			print item, data_row.index(item)
		to_form_0 = int(raw_input('please choose which type is the to_form: '))
	
	#-- make dict, and prepare the test. 
	#-- if the 文字型is *, need to replace with the かた型
	else: 
		from_form = from_form_0
		to_form = to_form_0
		
		if data_row[from_form_0] == '*':
			from_form = 1

		elif data_row[to_form_0] == '*':
			to_form = 1
		
		data_dict[data_row[from_form]] = data_row[to_form]

	line_counter += 1

key_random = data_dict.keys()
random.shuffle(key_random)

#-- provide questions
correct_qty = 0
error_qty = 0
for q in key_random:
	ans_opt = raw_input('print "stop" to stop the test\n'+q.encode(dec)+'"'+Field[from_form].encode(dec)+'"'+', please give form '+'"'+Field[to_form].encode(dec)+'": ')
	if ans_opt == 'stop': break
	elif ans_opt.decode(dec) == data_dict[q]:
		correct_qty += 1
		print 'yes'
	else: 
		error_qty +=1
		print 'ans is: ', data_dict[q]
print 'Total test words are: ', correct_qty+error_qty
print 'Error words are: ', error_qty