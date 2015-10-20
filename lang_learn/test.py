# -*- coding: utf-8 -*-
import codecs 
import random
from collections import defaultdict
import glob
import os
import word_func
import re
from jNlp.jTokenize import jTokenize

dec = 'utf-8'

# voc_dic = defaultdict(list)
# files=glob.glob('.'+os.sep+'d*-j1.txt')
# print files
# di = word_func.make_vocls(files, voc_dic, dec)
# print di

# num = raw_input('enter the number')
# if len(num.split('-')) == 1:
# 	print num
# else:
# 	start = int(num.split('-')[0])
# 	end = int(num.split('-')[1])
# 	for i in range(start, end+1):
# 		print i

start = str(1)
end = str(2)
files=glob.glob('.'+os.sep+'d*-j['+start+'-'+end+'].txt')
print files