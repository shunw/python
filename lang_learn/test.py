# -*- coding: utf-8 -*-
import codecs 
import random
from collections import defaultdict
import glob
import os
import word_func
from jNlp.jTokenize import jTokenize

dec = 'utf-8'
#========================================
# MAIN
#========================================
if __name__ == '__main__':
	# voc_dic=defaultdict(list)
	# voc_dic_w=defaultdict(list)
	
	# voc_dic=word_func.make_vocls('data-j1.txt', voc_dic, dec)
	
	# for i in voc_dic.keys():
	# 	if i.strip() == '请多关照'.decode(dec):
	# 		print voc_dic[i][1]

	
	input_sentence = u'私は彼を５日前、つまりこの前の金曜日に駅で見かけた'
	list_of_tokens = jTokenize(input_sentence)
	print list_of_tokens
	print '--'.join(list_of_tokens).encode('utf-8')