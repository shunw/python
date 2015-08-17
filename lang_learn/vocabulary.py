# -*- coding: utf-8 -*-
import codecs

if __name__ == '__main__':
	
	f = codecs.open('data-j.txt', 'r', 'utf-8')
	counter=1
	for l in f:
		if counter!=1:
			inp=raw_input(l.split()[3].encode('utf-8')+"あか型: ")
			if inp==l.split()[1].encode('utf-8'):
				print "yes"
			else:
				print "the ans is " + l.split()[1].encode('utf-8')
		counter+=1

# had a ending enter/ 
# random
# 生词本 --- consider complete one/ also consider be stopped one. 
# 比较平假名 比较中文