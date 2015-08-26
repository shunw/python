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
	voc_aka=dict()
	#========================================
	#import all the files from the current dir, the result is a list
	#========================================
	files = glob.glob('.'+os.sep+'d*.'+'txt')
	for f in files:
		handler = codecs.open(f, 'r', dec)
		for lines in handler:
			if len(lines.split())>1:
				word = lines.split()[1]
				if word not in voc_aka.keys():
					if word.split()[0] == '〜'.decode(dec):
						voc_aka[word] = word.split()[1]
					else:
						voc_aka[word] = word.split()[0]

	first_cha = raw_input("please enter the first character you want to seach: ")
	

	for key, value in voc_aka.iteritems():
		print key, value
		if first_cha.decode(dec) == value:
			print key
	
