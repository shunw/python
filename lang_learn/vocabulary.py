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

def operate_word(voc_dic, voc_dic_w, q_mean, type_id, inp):
	error_sign = 1
	ok =  inp==voc_dic[q_mean][type_id].encode(dec) 
	if not ok: 
		voc_dic_w[q_mean]=voc_dic[q_mean]
		error_sign = 0
		print "the ans is " + voc_dic[q_mean][type_id].encode(dec)
		
	else: 
		print 'yes'
	return error_sign
		

#========================================
# MAIN
#========================================
if __name__ == '__main__':
	voc_dic=defaultdict(list)
	voc_dic_w=defaultdict(list)

	#========================================
	#choose the txt number you want to recite, or just choose all
	#========================================
	lesson_num = raw_input('recite ALL or SEARCH word? pls enter "all": \nIf review ERROR HISTROY, enter "rev": \nOtherwise enter the lesson number (like 1 or like 1-3), you want to recite: \nMake your choice: ')

	if lesson_num != 'all':
		#========================================
		#import one lesson number: one lesson or a range of lesson
		#========================================
		if lesson_num != 'rev':
			if len(lesson_num.split('-')) != 1:
				start = lesson_num.split('-')[0]
				end = lesson_num.split('-')[1]
				files = glob.glob('.'+os.sep+'d*-j['+start+'-'+end+'].txt')
			else: 
				files = glob.glob('.'+os.sep+'d*-j'+lesson_num+'.txt')
			for f in files: 
				voc_dic=word_func.make_vocls(f, voc_dic, dec)
		
		#========================================
		#this is to find the review part.
		#========================================
		else: 
			voc_dic=word_func.make_vocls('output_word.txt', voc_dic, dec)
	else:	
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
	if lesson_num == 'all':
		dict_sign = raw_input("do you want to search word? y/n: ")
	
	if lesson_num == 'all' and dict_sign == 'y':
		need_break_search = False
		while not(need_break_search):
			search_inp = raw_input('please enter the meaning to want to do the search\nplease enter "stop" to stop: ')
			if search_inp == stop_input:
				need_break_search = True
				break
			else: 
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
		aka_id=1; ch_id=2

		key_random=voc_dic.keys()
		random.shuffle(key_random)
		
		#========================================
		#compare the key and the input, 
		#return the 生词dict
		#========================================
		need_break = False
		need_skip = False
		counter = 0
		error_count = 0
		counter_gen = 0
		for q_mean in key_random:
			if (need_break): 
				break
			error_count_sign = 1
			for i in range(1,3):
				if voc_dic[q_mean][i]=='*': 
					continue
				#此处的 tp[i-1]对应的是tp={1: 'あか型', 2: '文字型'}； 因为dict list里的位置改了，所以用i-1来对应tp的位置
				inp=raw_input(q_mean.encode(dec)+tp[i]+"\nEnter %s to stop; Enter %s to skip: " %(stop_input, 's'))

				if inp == '':
					while inp == '':
						print 'no words entered, please re-enter. '
						inp=raw_input(q_mean.encode(dec)+tp[i]+"\nEnter %s to stop; Enter %s to skip: " %(stop_input, 's'))
				
				if inp == stop_input: 
					need_break = True
					break
				
				if inp == 's':
					need_skip = True
					break

				error_count_sign = error_count_sign*operate_word(voc_dic, voc_dic_w, q_mean, i, inp)
			
			if error_count_sign == 0:
				error_count +=1
			if  inp != 's' and (inp != 'stop' or i!=1):
				counter += 1
			# ===================================================
			# here is to show the error count and the total count
			# ===================================================
			# print 'error_c is ', error_count
			# print 'counter is ', counter
			if (need_skip):
				continue
			
		
		print "Review vocabulary qty is: ", counter
		print "Review vocabulary error qty is: ", error_count

		#========================================
		#write the 生词dict
		#========================================
		output = codecs.open('output_word.txt', 'a', dec)
		now = dt.datetime.now()
		line = '\n'*2 + str(now.strftime("%Y-%m-%d %H:%M")) + '\n' + '\n' 
		output.write(line)
		for k, v in voc_dic_w.items():
			f_line='\t'.join(v)+'\t'+k+'\n'
			output.write(f_line)



# 生词本 --- consider complete one/ also consider be stopped one. 
