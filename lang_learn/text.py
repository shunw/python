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
	txt_j = list()
	txt_c = list()
	'''
	txt = [(j1, c1), (j2, c2), (j3, c3)]
	'''
	#========================================
	#import all the files from the current dir, the result is a list
	#========================================
	files = glob.glob('.'+os.sep+'d*-t*.'+'txt')
	# files = ['data-s8.txt']  # this is for debugging
	for f in files:
		handler = codecs.open(f, 'r', dec)
		for line in handler:
			if len(line.split()) == 0: continue
			if line[0] == 'j': txt_j.append(line.split(':')[-1].strip())
			elif line[0] == 'c': txt_c.append(line.split(':')[-1].strip())
			
	for i in range(len(txt_j)):
		ans = raw_input(txt_c[i].encode(dec) + '\nOr please enter "stop" to stop: \n')
		if ans == 'stop': break
		if ans != txt_j[i].encode(dec):
			print 'the ans is: %s' % (txt_j[i].encode(dec))
		else: 
			print 'bingo!'

	
