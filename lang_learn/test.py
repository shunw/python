# -*- coding: utf-8 -*-
import codecs 
import random
from collections import defaultdict
import glob
import os
import word_func


dec = 'utf-8'
#========================================
# MAIN
#========================================
if __name__ == '__main__':
	voc_dic=defaultdict(list)
	voc_dic_w=defaultdict(list)
	
	voc_dic=word_func.make_vocls('data-j1.txt', voc_dic, dec)
	
	for i in voc_dic.keys():
		if i.strip() == '请多关照'.decode(dec):
			print voc_dic[i][1]
	