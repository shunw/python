# -*- coding: utf-8 -*-
import codecs
import sys

dec='utf-8'

def cha_compare(l, ch_type_id, dec):
	#define the col function
	ch_type_id=int(ch_type_id)
	ans=l.split()[ch_type_id].encode(dec)
	mean=l.split()[-1].encode(dec)
	if ch_type_id==1:
		ch_type='あか型'
	else:
		ch_type='文字型'

	inp=raw_input(mean+ch_type+"or enter 'stop' to stop: ")
	if inp=='stop':
		sys.exit(0)
	elif inp==ans:
		print "yes"
	else:
		print "the ans is " + ans

if __name__ == '__main__':
	f = codecs.open('data-j.txt', 'r', dec)
	counter=1
	for l in f:
		if counter!=1:
			# *********************** this is disfunction ****************
			if l.split()[2]=="*":
				cha_compare(l, 1, dec)
			else:
				ch_type_id=raw_input("want あか型 1 or 文字型 2: ")
				cha_compare(l, ch_type_id, dec)
				
				if raw_input("want to try the other type? y/n: ")=='y':
					cha_compare(l, 3-int(ch_type_id), dec)
		counter+=1

# check when the open file is csv file/ with several ones. 
# random
# 生词本 --- consider complete one/ also consider be stopped one. 
# 比较平假名 比较中文