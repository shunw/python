# -*- coding: utf-8 -*-
import codecs 
import random
from collections import defaultdict
import glob
import os
import word_func
import re
from jNlp.jTokenize import jTokenize

lis = ['牛奶（片假名）./data-j6.txt', '今天早上./data-j4.txt', '商店./data-j6.txt', '牛奶（片假名）./data-j12.txt']
a = '牛奶'
for i in lis:
	
	try: print re.match(a, i).group(0)
	except: print 'na'
	 