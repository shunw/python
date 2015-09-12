# -*- coding: utf-8 -*-
import codecs 
import re


def make_vocls(fl, voc_dic, dec):
	'''transfer the file to the dict'''
	handler=codecs.open(fl, 'r', dec)
	counter=1
	for line in handler:
		if counter!=1 and len(line.split())!=0:
			ls=re.split(r'\t+', line.rstrip('\t'))
			k=ls[-2]+fl
			voc_dic[k].append(fl)
			for v in ls[:-2]: voc_dic[k].append(v)
		counter+=1
	return voc_dic