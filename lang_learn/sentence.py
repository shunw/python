# -*- coding: utf-8 -*-
import codecs 
import random
import glob
import os
import datetime as dt
from collections import defaultdict
import re

import word_func

'''
this function is to check the sentence in the text book
'''

dec = 'utf-8'
stop_input = 'stop'
if __name__=='__main__':
	sentence = list()
	'''
	sentence = [[file1，item＃1, 日1, 中1，日2，中2，日3，中3]，[file1，item＃2, 日1, 中1，日2，中2，日3，中3]]
	'''
	#========================================
	#import all the files from the current dir, the result is a list
	#========================================
	# files = glob.glob('.'+os.sep+'d*-s1.'+'txt')
	files = glob.glob('.'+os.sep+'d*-s*.'+'txt')

	# following is to create the sentence
	for f in files:
		handler = codecs.open(f, 'r', dec)

		for line in handler:
			sen = line.strip()
			if len(sen) == 0: continue 
			
			if sen == '1':
				temp = list()
				temp.append(f)
				temp.append(sen)

			elif len(sen) < 3 and sen != '1':
				sentence.append(temp)
				temp = list()
				temp.append(f)
				temp.append(sen)
			
			else: 
				temp.append(sen)
			
	
	
	random.shuffle(sentence)
	# print sentence

	# for i in sentence:
	# 	for n in i:
	# 		print n.encode(dec)
	stop_sign = False
	for s in sentence:
		if stop_sign: break
		for k in range(1, len(s)/2):
			ans = raw_input(s[0][s[0].find('-') +1 : ] + s[k*2+1].encode(dec) + '\nOr please enter "skip" to skip:' + '\nOr please enter "stop" to stop: \n')
			if ans == 'skip': break
			if ans == 'stop': 
				stop_sign = True
				break
			if ans != s[k*2].encode(dec):
				print 'the ans is: %s' % (s[k*2].encode(dec))
			else: 
				print 'bingo!'

	
