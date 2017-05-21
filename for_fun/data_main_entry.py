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
	data = [[459, '黑色冲击！组织之手逼近的瞬间', 5, '电视版', 'N/A', 'N/A', '水无怜奈／本堂瑛海／基尔', '黑衣人', '柯南发现水无怜奈属于黑衣人组织，并企图阻止黑衣人的暗杀活动中，不小心被发现在水无怜奈的鞋底有窃听器，遂毛利小五郎被怀疑且快被做掉的时候，赤井秀一阻止并使组织怀疑是FBI安排的所有的一切，期间贝尔摩德狠帮柯南及小五郎洗清嫌疑'], [293, '情急之下的应变之道', 2, '电视版', '杀人', 'N/A', 'Judy', '无', '和Judy老师一起目击命案，Judy提到FBI，小兰用XXX逗新一，剧末贝尔摩德飞镖射中哀酱照片'], [369, '便利店的陷阱', 2, '电视版', 'N/A', 'N/A', 'Judy', '系列案件铺垫', 'Judy回忆起小时候父上被贝尔摩德杀死的场景，小兰首次自己进行推理破案，柯南为照顾哀酱住在博士家，发现自己家里被人动过，Judy辞职，小兰和园子去她家开派对帮她践行，小兰无意间发现浴室里有大量小兰，柯南和新一的照片'], [371, '与黑色组织面对面 满月之夜的两起神秘事件', 5, '电视版', 'N/A', 'N/A', '贝尔摩德／苦艾酒', '黑衣人', '贝尔摩德伪装新出医生被Judy说破，企图杀后来赶到的哀酱被兰阻止，Judy快被贝尔摩德杀掉之际，赤井秀一打伤狙击手出现，狙击手自杀，新一发现大boss邮箱键盘音，不过贝尔摩德逃脱。因为兰和新一曾经救过贝尔摩德，所以贝尔摩德一直手下留情。毛利小五郎参加某变装派对，遇杀人案，由服部平次假扮新一侦破，便装是由工藤优希子完成'], [719, '婚礼前夕', 2, '电视版', 'N/A', 'N/A', '安室透／波本威士忌', '无', '安室透首次登场'], [733, '堵上性命的恋爱转播 转播开始／穷途末路／突击现场', 3, '电视版', '绑架', '复仇', '无', '警视厅爱情', '高木被人绑架，佐藤警官去救的故事／安室透在剧前剧后有梗，可能是和过世的伊达先生是好友，剧前去警视厅可能是为了和他聚一聚，剧后在高木之前去祭奠，暗示之后安室透的好人身份。'], [786, '茱蒂的回忆与赏花的陷阱', 2, '电视版', '杀人', '复仇', 'Judy', '黑衣人', '安室透乔装接近Judy，窃取信息（关于赤井秀一），贝尔摩德也乔装帮安室透解围，并回收窃听器'], [757, '密室里的柯南/ 解谜的波本', 2, '电视版', '密室杀人', '复仇', '安室透／波本威士忌', 'N/A', '安室透发现小五郎背后的柯南，在柯南企图迷晕小五郎的时候被发现']]

	conan_op = cur_operation(cur)
	# conan_op.helpTB_insert({'key_person': ['水无怜奈／本堂瑛海／基尔']})
	conan_op.mainTB_insert(data)
	
	conn.commit()
	conn.close()
