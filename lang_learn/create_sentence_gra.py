# -*- coding: utf-8 -*-
import codecs 
import random
import glob
import os
import datetime as dt
from collections import defaultdict

import word_func

'''
create sentence with random grammar and words
'''

dec = 'utf-8'
stop_input = 'stop'
if __name__=='__main__':
	gram_file = 'grammar.txt'
	verb_file = 'data-v.txt'
	gram_handle = open(gram_file)
	gram_data = {}

	#========================================
	# get the gram data
	#========================================
	counter = 0
	for line in gram_handle:
		line_data = line.strip().split('\t')
		if counter == 0:
			counter += 1
			continue
		gram_data[line_data[1]] = line_data[2]

	#========================================
	# shuffle the keys
	#========================================
	key_random = gram_data.keys()
	random.shuffle(key_random)

	#========================================
	# open the verb file make a list for it
	#========================================
	file_handler = open(verb_file)
	k = 0
	verb_list = []
	for line in file_handler:
		line_list = line.strip().split('\t')
		if k == 0:
			v_ind = line_list.index('原型')
			k += 1
			continue
		if len(line_list) <= 3: continue 
		if line_list[v_ind] in verb_list: continue
		verb_list.append(line_list[v_ind])


	for item in key_random:

		#========================================
		# get the verb qty and choose the same number of the verb from the verb list
		#========================================

		v_qty = gram_data[item]
		err = int(random.uniform(0, 3))
		total_qty = int(v_qty) + err

		random.shuffle(verb_list)
		chosen_word_str = ', '.join(verb_list[:total_qty])
		# print chosen_word_str
		#========================================
		#get the n you want to create the sentence
		#========================================
		print 'pls create the sentence with' + '\n'+ str(item)
		sentence = raw_input('with words　' + chosen_word_str + '\n' + 'or enter '+ stop_input +'if you want to stop: ')
		if sentence == stop_input: break
		
		#========================================
		#write into a txt file for the future reference
		#========================================
		output = codecs.open('output_sentence.txt', 'a', dec)
		now = dt.datetime.now()
		if counter == 1: 
			line = '\n'*2 + str(now.strftime("%Y-%m-%d %H:%M")) + '\n' + item.decode(dec) + '\n' + sentence.decode(dec) + '\n'
			
			
		else: 
			line = '\n' + item.decode(dec) + '\n' + sentence.decode(dec) + '\n'
			
		counter += 1

		output.write(line)
