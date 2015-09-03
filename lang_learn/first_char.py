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
	voc_aka=defaultdict(list)
	#========================================
	#import all the files from the current dir, the result is a list
	#========================================
	files = glob.glob('.'+os.sep+'d*-j*.'+'txt')
	for f in files:
		handler = codecs.open(f, 'r', dec)
		for line in handler:
			if len(line.split()) == 0: continue
			row = line.split()
			voc_aka[row[-1]].append(row[1])
	
	first_cha = raw_input("please enter the first character you want to seach: ")
	qty = int(raw_input("please enter how many words you want to show: "))
	
	if len(voc_aka[first_cha.decode(dec)]) == 0:
		print 'There is no word begin with that character. '
	else:
		words = voc_aka[first_cha.decode(dec)]
		random.shuffle(words)
		if len(words) < qty: 
			qty = len(words)

		for i in range(qty):
			print words[i]
	
	
