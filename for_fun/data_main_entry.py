# -*- coding: utf-8 -*-
import sqlite3
import csv

dec='utf-8'
conn = sqlite3.connect('conan_info.db')
c = conn.cursor()

'''
[第几集，名字，集数，类型（剧场版？），案件类型，原因，相关人物，相关情节，备注]
类型：['电视版', '剧场版', '特别篇']
案件类型：['密室杀人', '杀人未遂', '解谜', '杀人']
原因：['无', '复仇', '反社会', '恋情']
相关人物：['无', '服部平次', '怪盗基德', '京极真', '园子', '少年侦探团', '妃英理', '和叶', '波本']
相关情节：['无', '黑衣人', '警视厅爱情', '怪盗基德', '园子爱情', '少年侦探团', '毛利小五郎爱情', '新一爱情', '服部平次爱情']
'''

'''
already entried
info = [799, '怪盗基德对京极真', 2, '电视版', '解谜', '恋情', '京极真', '园子爱情', ''], [816, '柯南与平次 恋爱的暗号', 2, '电视版', '解谜', '恋情', '服部平次', '服部平次爱情', ''], [823, '气氛僵硬的茶会', 2, '电视版', '杀人', '复仇', '波本', '黑衣人', '']
'''

table_pos_dict = {3: ['iqiyi_type', 'tv_type'], 4: ['event_type', 'event_type'], 5: ['root_cause', 'root_cause'], 6: ['key_person', 'key_person'], 7: ['key_story', 'key_story']}
select_base_command = 'SELECT id FROM '
infos = []
for info in infos: 
	id_inf_trans = info[:3]
	for pos in range(3, 8):
		value = info[pos]
		colname = table_pos_dict[pos][1]
		tablename = table_pos_dict[pos][0]
		id_inf_trans.append([i[0] for i in c.execute(select_base_command + tablename + ' WHERE ' + colname + " = '" + value + "'").fetchall()][0])
	id_inf_trans.append(info[-1])

	c.execute('INSERT INTO conan_main VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', id_inf_trans)

# print ([i[0] for i in c.execute("SELECT id from iqiyi_type where tv_type == '剧场版'").fetchall()])

# c.execute("DELETE FROM conan_main")
# c.execute("INSERT INTO conan_main VALUES (816, '柯南与平次 恋爱的暗号', 2, 1, 1, 1, 2, 8, '')")
# c.execute("INSERT INTO conan_main VALUES (823, '气氛僵硬的茶会', 2, 1, 1, 1, 2, 8, '')")

conn.commit()
conn.close()
