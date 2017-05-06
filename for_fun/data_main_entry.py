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

	
	infos = [[311, '光彦森林迷失记', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [318, '屋形船海钓记', 1, '电视版', '？？', '？？', '？？', '？？', '？？' ], [321, '关门海峡的友情与杀机', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [326, '震撼警视厅 1200万人质', 4, '电视版', '？？', '？？', '？？', '？？', '？？' ], [330, '看不见的嫌犯', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [332, '残留下来的无声证言', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [334, '接触黑色组织', 3, '电视版', '？？', '？？', '？？', '？？', '？？' ], [339, '扶手损毁的瞭望台', 1, '电视版', '？？', '？？', '？？', '？？', '？？' ], [341, '被沾污的蒙面英雄', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [343, '幸运的香烟盒', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ], [354, '用钱买不到的友情', 2, '电视版', '？？', '？？', '？？', '？？', '？？' ]]

	data = [[226, '五彩传说的水中豪宅', 2, '电视版', '密室杀人', 'N/A', '无', '无', '' ], [249, '神秘乘客', 2, '电视版', '绑架', 'N/A', '赤井秀一', '黑衣人', '开场有黑衣人桥段，及贝尔摩德' ], [306, '中华街的雨中幻影', 2, '电视版', '杀人', '复仇', '无', '系列案件铺垫', '兰高烧，回忆起以前的一些片段，其中有赤井秀一，莎朗，和工藤新一' ], [308, '工藤新一的纽约事件 事件篇／推理篇', 2, '电视版', '杀人', '复仇', '无', '系列案件铺垫', '兰高烧，回忆起以前的一些片段，其中有赤井秀一，莎朗，和工藤新一' ], [313, '孤岛之花与海龙宫', 3, '电视版', '杀人', '复仇', '服部平次', '无', '' ], [316, '爱与决断的冲击', 2, '电视版', '杀人未遂', '复仇', '无', '无', '兰被绑架' ], [319, '法庭对决II 妃英理大战九条', 2, '电视版', '杀人', 'N/A', '妃英理', '毛利小五郎爱情', '' ], [323, '恶意与圣者的游行', 2, '电视版', '抢劫', '无', '无', '警视厅爱情', '佐藤和高木的约会被泄漏／佐藤觉得自己被诅咒，觉得重要的人都会离她而去' ], [337, '沾染夕阳的女儿节娃娃', 2, '电视版', '解谜', 'N/A', '无', '无', '步美想和柯南拍娃娃真人版失败' ], [345, '忍法制造不在场证明之术', 1, '电视版', '杀人', 'N/A', '无', '无', '' ], [346, '消失的绑架脱逃车', 2, '电视版', '绑架', 'N/A', '无', '无', '柯南遭绑架／有佐藤警官和高木警官的暧昧桥段' ], [356, '疑惑的辣味咖喱', 2, '电视版', '杀人', '复仇', '无', '无', '' ], [702, '柯南vs平次 东西侦探推理对决', 2, '电视版', '杀人', 'N/A', '服部平次', '系列案件铺垫', '世良真纯坐看服部平次和新一推理对决，有FBI Judy和James的戏份' ], [704, '毒和恨的设计 EYE / S / Poison / Illusion', 4, '电视版', '杀人', '复仇', '服部平次', '服部平次爱情', '得知工藤新一在伦敦向小兰表白后，和叶企图表白失败' ], [830, '少年侦探团VS老人侦探团', 1, '电视版', '杀人', '复仇', '少年侦探团', '无', '' ], [832, '绯色的序章／绯色的追求／绯色的交错／绯色的归还／绯色的真相', 5, '电视版', 'N/A', 'N/A', '安室透／波本威士忌', 'FBI', '接823茶话会的梗，安室透想确认赤井秀一是否真的挂了，柯南察觉安排他爹和他妈解围，并安排赤井秀一去解Judy他们的围；另外发现安室透是代号 降谷零，非敌人' ], [910, '消失的黑带之谜', 1, '电视版', 'N/A', 'N/A', '京极真', '园子爱情', '园子带柯南去某道场看京极真' ], [911, '名流夫妇的秘密', 1, '电视版', '杀人', 'N/A', '无', '无', '' ]]

	conan_op = cur_operation(cur)
	conan_op.helpTB_insert({'event_type': ['抢劫']})
	conan_op.helpTB_insert({'key_person': ['世良真纯']})
	conan_op.mainTB_insert(data)
, [502, '黑暗组织之影 小小目击者／奇妙的照明／神秘高额报酬／珍珠流星', 4, '电视版', '杀人', '复仇', '本堂瑛佑', '黑衣人', '水无怜奈／本堂瑛海／基尔' ]
 
	# cur.execute('SELECT * from conan_main where iqiyi_num = 350')
	# print (cur.fetchall())
		
	
	conn.commit()
	conn.close()
