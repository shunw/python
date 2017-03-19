# -*- coding: utf-8 -*-
import sqlite3
import csv

def create_table(table_name, col_dict):
	base = 'CREATE TABLE '
	cols = list()
	id_name = 'id'
	temp = (id_name, col_dict[id_name])
	cols.append(' '.join(temp))

	for key, value in col_dict.items():
		if key == id_name: continue
		temp = (key, value)
		cols.append(' '.join(temp))

	cols_command = ', '.join(cols)
	return base + table_name + '(' + cols_command + ')'

def add_2col_value(table_name, value_list, col_dict):
	col_id = 'id'
	for k in col_dict.keys():
		if k != 'id': col_name = k

	counter = 1
	v_to_insert = list()
	for i in value_list:
		v_to_insert.append((counter, i))
		counter += 1

	temp = (col_id, col_name)
	command = 'INSERT INTO ' + table_name + ' (' + ', '.join(temp) + ') VALUES (?, ?)'
	return command, v_to_insert

def create_table_w_fkey(table_name, col_order, col_dict, f_key_dict):
	base = 'CREATE TABLE '
	cols = list()
	for key in col_order:
		temp = (key, col_dict[key])
		cols.append(' '.join(temp))
	cols_command = ', '.join(cols)
	
	f_key = list()
	for k, v in f_key_dict.items():
		f_key.append('foreign key'+'('+k+"_id"+') '+'references '+k+'('+v+')')
	f_key_command = ', '.join(f_key)

	return base + table_name + '(' + cols_command + ',' + f_key_command + ')'	

dec='utf-8'
conn = sqlite3.connect('conan_info.db')
c = conn.cursor()

# help table --- 电视类型 <iqiyi_type>
table_name = 'iqiyi_type'
col_help_table = {'id': 'integer primary key', 'tv_type': 'text'}
c.execute(create_table(table_name, col_help_table))
value_list = ['电视版', '剧场版', '特别篇']
command, v_list = add_2col_value(table_name, value_list, col_help_table)
c.executemany(command, v_list)

# help table --- 案件类型 <event_type>
table_name = 'event_type'
col_help_table = {'id': 'integer primary key', 'event_type': 'text'}
c.execute(create_table(table_name, col_help_table))
value_list = ['密室杀人', '杀人未遂', '解谜', '杀人']
command, v_list = add_2col_value(table_name, value_list, col_help_table)
c.executemany(command, v_list)

# help table --- 事件原因 <root_cause>
table_name = 'root_cause'
col_help_table = {'id': 'integer primary key', 'root_cause': 'text'}
c.execute(create_table(table_name, col_help_table))
value_list = ['无', '复仇', '反社会', '恋情']
command, v_list = add_2col_value(table_name, value_list, col_help_table)
c.executemany(command, v_list)

# help table --- 主要人物 <key_person>	
table_name = 'key_person'
col_help_table = {'id': 'integer primary key', 'key_person': 'text'}
value_list = ['无', '服部平次', '怪盗基德', '京极真', '园子', '少年侦探团', '妃英理', '和叶', '波本']
c.execute(create_table(table_name, col_help_table))
command, v_list = add_2col_value(table_name, value_list, col_help_table)
c.executemany(command, v_list)

# help table --- 主要剧情 <key_story>	
table_name = 'key_story'
col_help_table = {'id': 'integer primary key', 'key_story': 'text'}
value_list = ['无', '黑衣人', '警视厅爱情', '怪盗基德', '园子爱情', '少年侦探团', '毛利小五郎爱情', '新一爱情', '服部平次爱情']
c.execute(create_table(table_name, col_help_table))
command, v_list = add_2col_value(table_name, value_list, col_help_table)
c.executemany(command, v_list)

col_main = {'iqiyi_num': 'integer primary key', 'name': 'text',	'qty': 'integer', 'iqiyi_type_id': 'integer', 'event_type_id': 'integer', 'root_cause_id': 'integer', 'key_person_id': 'integer', 'key_story_id': 'integer', 'comment': 'text'}
col_order = ['iqiyi_num', 'name', 'qty',
'iqiyi_type_id', 'event_type_id', 'root_cause_id', 'key_person_id', 'key_story_id', 'comment']
f_key_dict = {'iqiyi_type':'id', 'event_type':'id', 'root_cause':'id', 'key_person':'id', 'key_story': 'id'}
# main table <conan_main>
c.execute(create_table_w_fkey('conan_main', col_order, col_main, f_key_dict))



conn.commit()
conn.close()


