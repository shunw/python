import random

fl = open("verb.txt")
line_counter = 0
data_dict = dict()
for line in fl:
	
	data_row = line.split()
	#-- this is to filter the empty line
	if len(data_row) < 1: continue
	
	#-- get the from_form and to_form index ID.
	if line_counter == 0:
		for item in name_field:
			print item, name_field.index(item)
		from_form = raw_input('please choose which type is the from_form: ')
		for item in name_field:
			if name_field.index(item) == int(from_form): continue
			print item, name_field.index(item)
		to_form = raw_input('please choose which type is the to_form: ')
	
	#-- make dict, and prepare the test. 
	else: 
		data_dict[data_row[from_form]] = data_row[to_form]

	line_counter += 1

key_random = data_dict.keys()
random.shuffle(key_random)

#-- questions
