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
			# print (info[0])
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
	data = [[723, '侦探们的夜想曲 案件／诱拐／推理／波本', 4, '电视版', '杀人', '复仇', '安室透／波本威士忌', '无', '安室透跟着毛利小五郎查某个案件，柯南疑似被嫌疑人诱拐，冲矢昴开车带阿笠博士定位柯南，安室透和适量真纯合力强拦绑架柯南的车，最后有一个贝尔摩德给波本电话的梗'], [868, '悄悄靠近安室的黑影', 1, '电视版', '解谜', 'N/A', '安室透／波本威士忌', '无', '最后有个梗，贝尔摩德警告安室透最近他被琴酒盯上了'], [891, '关系恶劣的女子乐队', 2, '电视版', '杀人', '复仇', '安室透／波本威士忌', '无', '世良真纯回忆起之前在日本看到过赤井秀一，并且赤井秀一边上的男子曾教过她几个音阶的贝斯，在赤井秀一帮世良真纯去买票的时候，安室透曾经出现，并叫那个教她贝斯的男子为苏格兰酒。安室透剧中承认这个是被赤井秀一杀掉的日本公安卧底'], [697, '幽灵饭店的推理对决', 2, '电视版', '杀人', '复仇', '世良真纯', '无', '世良真纯首秀，且貌似很了解柯南'], [699, '侦探事务所挟持事件 突发／狙击／解放', 3, '电视版', '密室杀人', 'N/A', '世良真纯', '无', '一开始有些世良真纯的信息，柯南觉得哪里好像见过她，世良真纯表示小兰是个强劲的对手，可能是在和小兰抢新一方面？'], [708, '博士的影音网站', 2, '电视版', '绑架', 'N/A', '世良真纯', '无', '有世良真纯发现博士家哀酱的梗，还有冲矢昴监视+保护哀酱的梗'], [798, '京极真是嫌犯', 2, '电视版', '杀人', '复仇', '世良真纯', '园子爱情', '片头一开始有世良真纯对京极真的梗，另外有世良真纯二哥的梗，及对柯南的评价'], [807, '红衣女的惨剧 水蒸气／恶灵／报仇', 3, '电视版', '杀人', '复仇', '世良真纯', '无', '一开始有一些世良真纯消息的梗，最后有世良真纯和某少女的合影，且故意让柯南看到'], [779, '装满水果的宝箱', 2, '电视版', '杀人', 'N/A', '世良真纯', '无', '柯南询问是否在哪里见过世良真纯，世良真纯假装不知道，内心想的是，那件事还不到时候让柯南知道。小兰也觉得有种哪里见过世良的感觉，和海岸有关'],[812, '意外结果的爱情小说', 2, '电视版', '杀人', 'N/A', '世良真纯', '无', '去世良住的旅馆，虽然号称是一个人住，不过还是发现有个小孩样貌的人，最后的梗中发现了柯南的窃听器，并让世良称她为领域外的妹妹／ 柯南被问到喜欢哀酱还是喜欢步美'], [838, '太阁之恋的名人战', 2, '电视版', '绑架', 'N/A', '羽田秀吉', '警视厅爱情', '巡警由美的爱情，其中有世良真纯 和 冲矢昴的梗，怀疑这个是世良真纯的二哥'], [465, '超机密的上学路', 2, '电视版', '解谜', 'N/A', '无', '无', '有由美提到她男友的梗，长相帅气，但是性格幼稚的男生，在大学时代认识'], [783, '现场的邻人是前男友', 2, '电视版', '杀人', 'N/A', '羽田秀吉', '警视厅爱情', '有千叶和三池苗子的梗， 认出了帮佣是比他小一届的同学，不过没认出三池苗子就是边上那个／由美和羽田秀吉的梗，如何演变成前男友且如何演变成羽田秀吉为了由美去争夺七冠王的缘由／突出了羽田秀吉的记忆和推理能力'], [904, '结婚登记表的密码', 2, '电视版', '解谜', 'N/A', '羽田秀吉', '警视厅爱情', '由美和前男友的梗，还有哀酱发现见过羽田秀吉的义兄的名字'], [840, '盛夏里沉入泳池的谜', 2, '电视版', '杀人', '复仇', '世良真纯', '无', '前后有世良真纯那个领域外的妹妹的梗，还有小兰想起好像在哪里见过世良和她领域外的妹妹的记忆'], [882, '美味得要死的拉面2', 2, '电视版', '杀人', 'N/A', '世良真纯', '警视厅爱情', '有由美和羽田秀吉的梗，有佐藤和高木的打情骂俏梗，还有世良真纯的手帕让柯南觉得在哪里见过她们'], [624, '令人害羞的护身符的下落', 2, '电视版', 'N/A', 'N/A', '服部平次', '服部平次爱情', '情敌梗：某男生也稀饭和叶／和叶的护身符里是手铐碎片，还有服部平次的照片，不过被那个男生看到，小恶作剧了一把。。。'], [762, '大家都看见了', 2, '电视版', '密室杀人', '复仇', '服部平次', '系列案件铺垫', '正好大泷警官和服部平次一行人在东京'], [863, '镰鼬旅馆', 2, '电视版', '杀人', '复仇', '服部平次', '服部平次爱情', '腹部平和表白的录音被柯南录下了下来，为了让他把录音删掉，服部平次给柯南介绍了某个案件。柯南最后如约删掉录音，不过告知服部平次少年侦探团人手一份这个录音，且哀酱的来电铃声已经设置成这个录音'], [399, '巫婆蛋糕之家', 1, '电视版', '杀人', '复仇', '无', '无', ''], [885, '被僵尸包围的别墅', 3, '电视版', '杀人', 'N/A', '服部平次', '服部平次爱情', '有服部平次希望表白，后失败的梗'], [605, '鹳的探索之旅 小兰搜索篇／追踪阳菜篇', 3, '电视版', '绑架', 'N/A', '服部平次', '无', ''], [282, '大阪双重疑案 浪花剑客与太阁城 之一／之二／之三／之四', 4, '电视版', '杀人', '复仇', '服部平次', '服部平次爱情', '前两集服部平次放弃比赛去破案；后两集服部平次他爹放儿子出去当诱饵，也说明老爹道高一尺'], [257, '大阪3k事件', 2, '电视版', '杀人', '复仇', '服部平次', '无', '碰到喜欢的明星，柯南也没有办法冷静进行判断'], [622, '妖怪仓库的寻宝战争', 2, '电视版', 'N/A', 'N/A', '服部平次', '无', '服部平次有一张ms柯南拜师的照片，其实是平次骗柯南低头，然后自拍'], [473, '侦探团特别专访', 2, '电视版', '杀人', '复仇', '小林澄子', '无', '小林澄子第一次看到柯南的强势推理，然后希望可以加入少年侦探团当顾问老师'], [512, '工藤新一少年冒险', 2, '电视版', '解谜', 'N/A', '多人', '无', '有毛利小五郎，夫妇／工藤优作夫妇／怪盗基德父子出场'], [619, '白鸟警官 樱花的回忆', 2, '电视版', '杀人', '复仇', '小林澄子', '警视厅爱情', '白鸟警官小时候偶遇小林老师的梗；还有因此而开始当警察的梗；在这集里和小林老师重逢的梗'], [634, '小林老师的恋情/ 白鸟警官的失恋／跨越时空的樱花之恋', 3, '电视版', '杀人', '复仇', '小林澄子', '警视厅爱情', '最后一集的下半部分有怪盗基德的开场；小林老师终于和白鸟警官相认，且小林老师有做爱心便当给白鸟警官'], [657, '法庭的对决IV  陪审员 小林澄子', 2, '电视版', '杀人', '复仇', '妃英理', '法庭对决', '妃英理和九条女神的第四版对决，小林老师提出关键性问题'], [239, '满口谎言的委托人', 2, '电视版', '杀人', 'N/A', '服部平次', '系列案件铺垫', '有服部平次母上大人出场的梗；母上大人各种试探小五郎；最后有服部平次出来的梗为之后的案件铺垫'], [330, '看不见的嫌疑犯', 2, '电视版', '杀人', '复仇', '无', '毛利小五郎爱情', '有雨城琉璃暗恋小五郎的梗，还有说起小五郎和英理以前的梗'], [214, '毛利小五郎涉嫌记', 2, '电视版', '杀人', 'N/A', '妃英理', '毛利小五郎爱情', '真凶爱慕妃英理律师；有妃英理买领带做结婚纪念日礼物的梗；有毛利小五郎求妃英理回家的梗，只是妃律师还没玩够']]

	

	conan_op = cur_operation(cur)
	# conan_op.helpTB_update('key_person', {'key_person': ['赤井秀一／黑麦威士忌', '赤井秀一／黑麦威士忌／冲矢昴']})
	conan_op.helpTB_insert({'key_person': ['羽田秀吉', '小林澄子']})
	conan_op.helpTB_insert({'key_story': ['法庭对决']})
	conan_op.mainTB_insert(data)
	
	conn.commit()
	conn.close()
