# -*- coding: utf-8 -*-
import sqlite3
import csv

def insert_helptb(cur, tb, insert_ls): 
	# insert_dic = {}
	# to insert/ change the help tables. 
	cur.execute('''
		SELECT id FROM {tablename} ORDER BY id DESC LIMIT 1
		'''.format(tablename = tb))
	new_key = (cur.fetchone()[0]+1)

	insert_ls_wind = list()
	for i in range(new_key, len(insert_ls)+new_key):
		insert_ls_wind.append([i, insert_ls[i - new_key]])
	# print (insert_ls_wind)
	cur.executemany('INSERT INTO {tablename} values (?, ?)'.format(tablename = tb), insert_ls_wind)

	return cur

class cur_operation:
	def __init__(self, cur): 
		self.cur = cur

	def mainTB_insert(self, datalists):
		table_pos_dict = {3: ['iqiyi_type', 'tv_type'], 4: ['event_type', 'event_type'], 5: ['root_cause', 'root_cause'], 6: ['key_person', 'key_person'], 7: ['key_story', 'key_story']}
		
		for info in datalists: 
			id_inf_trans = info[:3]
			
			if (info[0] in [i[0] for i in self.cur.execute('SELECT iqiyi_num from conan_main').fetchall()]): 
				duplicate = self.cur.execute('SELECT iqiyi_num, name from conan_main where iqiyi_num = {id_num}'.format(id_num = info[0])).fetchall()
				print ('\n******************\n"{id_num}, {tv_name}" is already duplicated as {duplicate}, please check\n******************\n'.format(id_num = info[0], tv_name = info[1], duplicate = duplicate))
			for pos in range(3, 8):
				value = info[pos]
				colname = table_pos_dict[pos][1]
				tablename = table_pos_dict[pos][0]
				if not (value in [i[0] for i in self.cur.execute('SELECT {colname} from {tablename}'.format(colname = colname, tablename = tablename)).fetchall()]): 
					print ('\n******************\n"{value}" in not in table: {tablename}\n******************\n'.format(value = value, tablename = tablename))

				id_inf_trans.append(self.cur.execute('''
						SELECT id FROM {tablename}
						WHERE {colname} = '{value}'
						'''.format(tablename = tablename, colname = colname, value = value)).fetchall()[0][0])
			id_inf_trans.append(info[-1])
			self.cur.execute('INSERT INTO conan_main VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', id_inf_trans)
		return self.cur

	def helpTB_insert(self, data_dict): 
		# datalists = {tablename: [value1, value2, ...]}
		insert_helptb(self.cur, list(data_dict.keys())[0], list(data_dict.values())[0])
		return self.cur

	def output_helpTB(self, tablename):
		pass

	def output_mainTB(self):
		pass

	def query_helpTB(self, tablename): 
		self.cur.execute('SELECT * FROM {tablename}'.format(tablename = tablename))
		return self.cur.fetchall()

	def helpTB_update(self, tablename, change_dict):
		# change_dict = {fd: [value_beforechange, value_afterchange]}
		self.cur.execute('UPDATE {tablename} set {fd} = "{update_value}" where {fd} = "{original_value}"'.format(tablename = tablename, fd = list(change_dict.keys())[0], original_value = list(change_dict.values())[0][0], update_value = list(change_dict.values())[0][1]))
		return self.cur


if __name__ == '__main__': 
	dec='utf-8'
	conn = sqlite3.connect('conan_info.db')
	cur = conn.cursor()

	# UPDATE value
	# c.execute('update key_person set key_person = "安室透／波本威士忌" where key_person = "波本"')

	
	infos = [[311, '光彦森林迷失记', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [318, '屋形船海钓记', 1, '电视版', '？？', '？？', '？？', '？？', '？？' ], [321, '关门海峡的友情与杀机', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [326, '震撼警视厅 1200万人质', 4, '电视版', '？？', '？？', '？？', '？？', '？？' ], [330, '看不见的嫌犯', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [332, '残留下来的无声证言', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [334, '接触黑色组织', 3, '电视版', '？？', '？？', '？？', '？？', '？？' ], [339, '扶手损毁的瞭望台', 1, '电视版', '？？', '？？', '？？', '？？', '？？' ], [341, '被沾污的蒙面英雄', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [343, '幸运的香烟盒', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [354, '用钱买不到的友情', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [552, '妃英理证言']]

	# sample = [No_of_iqiyi, name_of_story, qty_of_story, iqiyi_type = '电视篇', event_type = '杀人', root_cause = '复仇', key_person = '本堂瑛佑', key_story = '黑衣人', comment = xxx]
	data = []

	conan_op = cur_operation(cur)
	# conan_op.helpTB_insert({'key_person': ['水无怜奈／本堂瑛海／基尔']})
	conan_op.mainTB_insert(data)
	
	conn.commit()
	conn.close()
