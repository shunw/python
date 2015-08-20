# -*- coding: utf-8 -*-
import codecs
import sys
import random
from collections import defaultdict

dec='utf-8'

def cha_compare(q_mean, type_id, voc_dic, dec):
	#define the col function
	tp={1: 'あか型', 2: '文字型'}
	inp=raw_input(q_mean.encode(dec)+tp[type_id]+"or enter 'stop' to stop: ")
	if inp=='stop':
		sys.exit(0)	
	elif inp==voc_dic[q_mean][type_id].encode(dec):
		print "yes"
	else:
		print "the ans is " + voc_dic[q_mean][type_id].encode(dec)	

def make_vocls(fl, voc_dic, dec):
	#transfer the file to the dict
	handler=codecs.open(fl, 'r', dec)
	counter=1
	for line in handler:
		if counter!=1:
			k=line.split()[-1]
			for v in line.split()[:-1]:
				voc_dic[k].append(v)
		counter+=1
	return voc_dic

def ran(key_list):
	#make the random key
	key_random=key_list
	random.shuffle(key_random)
	return key_random

if __name__ == '__main__':
	voc_dic=defaultdict(list)
	voc_dic=make_vocls('data-j.txt', voc_dic, dec)
			
	#get the random key
	#************ ING *****************
	aka_id=1
	ch_id=2

	key_random=list()
	key_random=voc_dic.keys()
	random.shuffle(key_random)
	
	for q_mean in key_random:	
		q_aka=voc_dic[q_mean][aka_id]
		q_ch=voc_dic[q_mean][ch_id]

		#compare the key and the input, parameter should include: q, dict
		cha_compare(q_mean, aka_id, voc_dic,dec)
		if voc_dic[q_mean][ch_id]!='*':
			cha_compare(q_mean, ch_id, voc_dic, dec)
		


# ---- for the txt file, maybe could only store in the dict and store the keys in a list. shuffle the list. 
# ---- check when the open file is csv file/ with several ones. 
# ---- random
# 生词本 --- consider complete one/ also consider be stopped one. 
# 比较平假名 比较中文