# -*- coding: utf-8 -*-
import codecs 
import random
import glob
import os
import datetime as dt
from collections import defaultdict
import re

import word_func

dec = 'utf-8'
stop_input = 'stop'
if __name__=='__main__':
	sentence = defaultdict(list)
	'''
	sentence = {'中文意思': [file name, 日文句子]}
	'''
	#========================================
	#import all the files from the current dir, the result is a list
	#========================================
	# files = glob.glob('.'+os.sep+'d*-s*.'+'txt')
	files = ['data-s13.txt']  # this is for debugging
	for f in files:
		handler = codecs.open(f, 'r', dec)
		counter = 0
		for line in handler:
			if counter == 0: 
				counter += 1
				continue
			if len(line.split()) == 0: continue
			row = line.split('\t')
			sentence[row[-1].strip()].append(f)
			sentence[row[-1].strip()].append(row[1].strip())
	
	keys = sentence.keys()
	random.shuffle(keys)

	for k in keys:
		ans = raw_input(k.encode(dec) + '\nOr please enter "stop" to stop: \n')
		if ans == 'stop': break
		if ans != sentence[k][1].encode(dec):
			print 'the ans is: %s' % (sentence[k][1].encode(dec))
		else: 
			print 'bingo!'

	
