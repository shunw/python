# -*- coding: utf-8 -*-
import codecs 
import random
from collections import defaultdict
import glob
import os

dec='utf-8'
tp={1: 'あか型', 2: '文字型'}
stop_input = 'stop'

def operate_word(voc_dic, voc_dic_w, q_mean, type_id, inp):
	ok =  inp==voc_dic[q_mean][type_id].encode(dec) 
	if not ok: 
		voc_dic_w[q_mean]=voc_dic[q_mean]
		print "the ans is " + voc_dic[q_mean][type_id].encode(dec)
	else: print 'yes'
		

def make_vocls(fl, voc_dic, dec):
	'''transfer the file to the dict'''
	handler=codecs.open(fl, 'r', dec)
	counter=1
	for line in handler:
		if counter!=1:
			k=line.split()[-1]
			for v in line.split()[:-1]: voc_dic[k].append(v)
		counter+=1
	return voc_dic


#========================================
# MAIN
#========================================
if __name__ == '__main__':
	voc_dic=defaultdict(list)
	voc_dic_w=defaultdict(list)

	#========================================
	#import all the files from the current dir
	#========================================
	files=glob.glob('.'+os.sep+'*.'+'txt')
	for f in files: 
		voc_dic=make_vocls(f, voc_dic, dec)
	
	#========================================
	#get the random key
	#========================================
	aka_id=1; ch_id=2

	key_random=voc_dic.keys()
	random.shuffle(key_random)
	
	#========================================
	#compare the key and the input, 
	#return the 生词dict
	#========================================
	need_break = False
	for q_mean in key_random:
		if (need_break): break
		for i in range(1,3):
			if voc_dic[q_mean][i]=='*': continue
			inp=raw_input(q_mean.encode(dec)+tp[i]+"or enter '"+stop_input+"' to stop: ")
			if inp == stop_input: need_break = True; break
			operate_word(voc_dic, voc_dic_w, q_mean, i, inp)

	#========================================
	#write the 生词dict
	#========================================
	output=codecs.open('output.txt', 'w', dec)
	for k, v in voc_dic_w.items():
		f_line='\t'.join(v)+'\t'+k+'\n'
		output.write(f_line)



# 生词本 --- consider complete one/ also consider be stopped one. 
