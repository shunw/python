# -*- coding: utf-8 -*-
import codecs 
import random
from collections import defaultdict
from random import shuffle
import glob
import os
import word_func
import datetime as dt
import re

dec='utf-8'
tp={1: 'あか型', 2: '文字型'}
stop_input = 'stop'

class words_check:
	def __init__(self, fl_name): 
		self.fl_name = fl_name

		self.data_ls = list() # [{'No': 1, '他动词': xxx, '自动词': xxx, '意思': zzz}, {'No': xxx... }]
		self.head = list()

		self.jdshi = '自動詞'
		self.jdtest = list()

		self.tdshi = '他動詞'
		self.tdtest = list()
		
		self.yimi = '意味'
		
	def get_data_ls(self):
		handle = open(self.fl_name, 'r')
		count = 0
		for line in handle: 
			if count == 0: 
				self.head = (line.strip()).split('\t')
				count += 1
			else: 
				temp_dict = dict()
				temp_content = (line.strip()).split('\t')[:]
				for fd in self.head:
					temp_dict[fd] = temp_content[self.head.index(fd)]
				self.data_ls.append(temp_dict)
		
	def shuffle_words(self):
		# return value be shuffled
		self.get_data_ls()
		shuffle(self.data_ls)
		
	def test_jdshi_output(self):
		self.shuffle_words()
		for data in self.data_ls: 
			self.jdtest.append({data[self.jdshi]: data[self.yimi]})
		return self.jdtest

	def test_tdshi_output(self):
		self.shuffle_words()
		for data in self.data_ls: 
			self.tdtest.append({data[self.tdshi]: data[self.yimi]})
		return self.tdtest

def judge_ans(ans, ans_input):
	if ans == ans_input: 
		print ('bingo~~~')
	if ans != ans_input: 
		print ('the correct ans is: {ans}'.format(ans = ans))


if __name__=='__main__': 
	words = words_check('jidoushi_tadoushi.txt')
	test_type = input('What is the word type you want: jidoshi? tadoshi? \n')
	if test_type == 'jidoshi': 
		test_cont = words.test_jdshi_output()[:]
	else: 
		test_cont = words.test_tdshi_output()[:]
	for d in test_cont: 
		yimi = list(d.values())[0]
		ans_input = input('What is the {test_type} of {yimi}\nOr enter "stop" to quit. \n'.format(test_type = test_type, yimi = yimi))
		if ans_input == 'stop': break
		judge_ans(list(d.keys())[0], ans_input)