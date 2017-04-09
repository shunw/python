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

dec='utf-8'
conn = sqlite3.connect('conan_info.db')
c = conn.cursor()


'''
already entried
info = [799, '怪盗基德对京极真', 2, '电视版', '解谜', '恋情', '京极真', '园子爱情', ''], 
		[816, '柯南与平次 恋爱的暗号', 2, '电视版', '解谜', '恋情', '服部平次', '服部平次爱情', ''], 
		[823, '气氛僵硬的茶会', 2, '电视版', '杀人', '复仇', '波本', '黑衣人', '']
		[110, '窃盗集团别墅事件', 2, '电视版', '解谜', '无', '无', '无', '' ], 
		[158, '地上电车紧急刹车事件', 1, '电视版', '杀人', '恋情', '无', '无', '' ], 
		[172, '飞天密室 工藤新一最初的事件', 2, '电视版', '杀人', '复仇', '工藤新一', '无', '工藤新一第一次破获杀人事件' ], 
		[203, '生死一瞬间', 6, '电视版', 'N/A', '无', '多人', '哀酱新药测试', '兰坐等柯南坦白； 哀酱饭柯南； 哀酱警告柯南不可透露身份；服部平次假扮工藤新一被识破；柯南在游园会上恢复高中生；在爹妈定情的高档餐厅破案后回复柯南' ], 
		[277, '来自芝加哥的男人', 2, '电视版', '绑架', 'N/A', 'James', 'FBI', '赤井秀一找James；James首秀' ], 
		[360, '东都现象所得秘密', 2, '电视版', '杀人', '复仇', '工藤有希子', '黑衣人', '新一妈妈发现哀酱饭新一；赤井秀一搜索哀酱' ], 
		[362, '坠落事件的内幕', 2, '电视版', '杀人', '复仇', '无', '无', '' ], 
		[365, '隐藏在厕所中的秘密', 2, '电视版', '杀人', '复仇', '贝尔摩德／苦艾酒', '黑衣人', '' ], 
		[554, '卡拉ok包厢的死角', 2, '电视版', '杀人', '复仇', '本堂瑛祐', '黑衣人', '本堂瑛祐设套让柯南坦白' ], 
		[661, '被害者是工藤新一', 1, '电视版', '密室杀人', '无', '服部平次', '系列案件铺垫', '' ], 
		[662, '犬伏城 炎之魔犬', 3, '电视版', '杀人', '财产继承', '服部平次', '无', '' ], 
		[676, '手术室惊魂', 2, '电视版', '杀人', '复仇', '园子', '园子破案', '' ], 
		[753, '漆黑的神秘列车', 4, '电视版', '密室杀人', '复仇', '多人', '黑衣人', '黑衣人狙杀雪莉失败'], 
		[776, '怪盗基德与赤面人鱼', 2, '电视版', '解谜', '无', '怪盗基德', '怪盗基德', '' ], 
		[908, '樱花班的回忆', 2, '电视版', '绑架', 'N/A', '工藤优作', '新一爱情', '幼年新一和小兰的第一次见面和初次相互印象；新一的首次推理；企图绑架小兰，被幼年新一识破']

already inserted help table
事件原因/ root_cause: '财产继承', 'N/A'
案件类型/ event_type: '探险', 'N/A', '绑架'
主要人物/ key_person 添加：'工藤新一', '本堂瑛祐', '工藤有希子', '工藤优作', '多人', 'James', '赤井秀一／黑麦威士忌', '贝尔摩德／苦艾酒'
主要剧情/ key_story：'系列案件铺垫', '园子破案', '哀酱新药测试', 'FBI'

already changed
主要人物/ key_person 更改：'波本' to '安室透／波本威士忌'
'''

# UPDATE value
# c.execute('update key_person set key_person = "安室透／波本威士忌" where key_person = "波本"')

# INSERT HELP TB
# insert_helptb(c, 'root_cause', ['财产继承', 'N/A'])
# insert_helptb(c, 'event_type', ['探险', 'N/A', '绑架'])
# insert_helptb(c, 'key_person', ['工藤新一', '本堂瑛祐', '工藤有希子', '工藤优作', '多人', 'James', '赤井秀一／黑麦威士忌', '贝尔摩德／苦艾酒'])
# insert_helptb(c, 'key_story', ['系列案件铺垫', '园子破案', '哀酱新药测试', 'FBI'])
# c.execute('select * from key_story')
# print (c.fetchall())

table_pos_dict = {3: ['iqiyi_type', 'tv_type'], 4: ['event_type', 'event_type'], 5: ['root_cause', 'root_cause'], 6: ['key_person', 'key_person'], 7: ['key_story', 'key_story']}

infos = [[363, '四台保时捷', 2, '电视版', '杀人', '复仇', 'Judy', '黑衣人', '苦艾酒找到哀酱／Judy怀疑哀酱身份' ]]

for info in infos: 
	id_inf_trans = info[:3]
	for pos in range(3, 8):
		value = info[pos]
		colname = table_pos_dict[pos][1]
		tablename = table_pos_dict[pos][0]
		id_inf_trans.append(c.execute('''
			SELECT id FROM {tablename}
			WHERE {colname} = '{value}'
			'''.format(tablename = tablename, colname = colname, value = value)).fetchall()[0][0])
	id_inf_trans.append(info[-1])


	c.execute('INSERT INTO conan_main VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', id_inf_trans)

conn.commit()
conn.close()
