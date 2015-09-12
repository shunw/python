# -*- coding: utf-8 -*-
import codecs 
import random
from collections import defaultdict
import glob
import os
import word_func
import datetime as dt
import re

dec='utf-8'
tp={1: 'あか型', 2: '文字型'}
stop_input = 'stop'

def operate_word(voc_dic, voc_dic_w, q_mean, type_id, inp, error_count):
	ok =  inp==voc_dic[q_mean][type_id].encode(dec) 
	if not ok: 
		voc_dic_w[q_mean]=voc_dic[q_mean]
		error_count += 1
		print "the ans is " + voc_dic[q_mean][type_id].encode(dec)
		
	else: 
		print 'yes'
	return error_count
		

#========================================
# MAIN
#========================================
if __name__ == '__main__':
	voc_dic=defaultdict(list)
	voc_dic_w=defaultdict(list)

	#========================================
	#import all the files from the current dir
	#========================================
	files=glob.glob('.'+os.sep+'d*-j*'+'txt')
	for f in files: 
		voc_dic=word_func.make_vocls(f, voc_dic, dec)
	#========================================
	#========================================
	#this is the search module
	#========================================
	#========================================
	if raw_input("do you want to search word? y/n: ") == 'y':
		search_inp = raw_input('please enter the meaning to want to do the search: ')
		for key in voc_dic.keys():
			if re.search(search_inp.decode(dec), key) != None:
				for item in voc_dic[key]:
					print item
	
	#========================================
	#========================================
	#this is the recite vocabulary module
	#========================================
	#========================================
	else:
		#========================================
		#get the random key
		#========================================
		aka_id=2; ch_id=3

		key_random=voc_dic.keys()
		random.shuffle(key_random)
		
		#========================================
		#compare the key and the input, 
		#return the 生词dict
		#========================================
		need_break = False
		counter = 0
		error_count = 0
		for q_mean in key_random:
			if (need_break): 
				break
			for i in range(2,4):
				if voc_dic[q_mean][i]=='*': 
					continue
				#此处的 tp[i-1]对应的是tp={1: 'あか型', 2: '文字型'}； 因为dict list里的位置改了，所以用i-1来对应tp的位置
				inp=raw_input(q_mean.encode(dec)+tp[i-1]+"or enter '"+stop_input+"' to stop: ")

				if inp == stop_input: 
					need_break = True
					print "Review vocabulary qty is: ", counter
					print "Review vocabulary error qty is: ", error_count
					break
				
				error_count = operate_word(voc_dic, voc_dic_w, q_mean, i, inp, error_count)
			counter += 1
				

		#========================================
		#write the 生词dict
		#========================================
		output = codecs.open('output.txt', 'a', dec)
		now = dt.datetime.now()
		line = '\n'*2 + str(now.strftime("%Y-%m-%d %H:%M")) + '\n' + '\n' 
		output.write(line)
		for k, v in voc_dic_w.items():
			f_line='\t'.join(v)+'\t'+k+'\n'
			output.write(f_line)



# 生词本 --- consider complete one/ also consider be stopped one. 
