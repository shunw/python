# -*- coding: utf-8 -*-
import codecs 
import random
import glob
import os
import datetime as dt
from collections import defaultdict

import word_func

'''
create sentence with random words
but seems there are some bugs
'''

dec = 'utf-8'
stop_input = 'stop'
if __name__=='__main__':
	voc_lib=defaultdict(list)
	#========================================
	#import all the files from the current dir
	#========================================
	files = glob.glob('.'+os.sep+'d*j*.'+'txt')
	for f in files:
		voc_lib = word_func.make_vocls(f, voc_lib, dec)
	word_qty = len(voc_lib)

	#========================================
	#this is to make the time stample in the file
	#========================================
	counter = 1
	while True:
		
		#========================================
		#get the n you want to create the sentence
		#========================================
		inp=raw_input('how many words <=' + str(word_qty) + ' you want to create the sentence, '+'\n'+'or enter '+ stop_input +'if you want to stop: ')
		if inp == stop_input: break
		else:
			try:
				n = int(inp)
				if n > word_qty: 
					print 'the number is larger than the max words, please re-enter a valid number'
					continue
			except:
				print "it's not a number"
				continue

		#========================================
		#create a list, for the key words. 
		#random the key and get the meaning list
		#rule: if it has the chinese type (type2), use that one, otherwise, use type1
		#========================================
		chosen_mean = random.sample(voc_lib.keys(), n)
		chosen_word = list()
		for i in chosen_mean:
			if voc_lib[i][2]=='*':
				chosen_word.append (voc_lib[i][1])
			else: 
				chosen_word.append (voc_lib[i][2])
		chosen_word_str = ', '.join(chosen_word)
		sentence=raw_input('key words are' + chosen_word_str.encode(dec) + 'please create a sentence w them: ')

		#========================================
		#write into a txt file for the future reference
		#========================================
		# print sentence.decode(dec)
		# continue
		output = codecs.open('output_sentence.txt', 'a', dec)
		now = dt.datetime.now()
		if counter == 1: 
			line = '\n'*2 + str(now.strftime("%Y-%m-%d %H:%M")) + '\n' + chosen_word_str + '\n' + sentence.decode(dec) + '\n'
			
			
		else: 
			line = '\n' + chosen_word_str + '\n' + sentence.decode(dec) + '\n'
			
		counter += 1

		output.write(line)

		
		
# read all the txt files, and get the 中文型 / if they don't have this type, use the 'あか型', 
# enter how many words you want to create the sentence
# get the random n words for the sentence