'''
python3
'''
# -*- coding: utf-8 -*-
import sqlite3
import csv

def write_output(col_name, data, fl_name):
	f = open(fl_name, 'w')
	data_write = list()
	for line in data: 
		data_write.append(line)
	writer = csv.writer(f)
	writer.writerow(col_name)
	writer.writerows(data_write)
	
class conan_db:
	def __init__(self):
		self.conn = None

	def conan_main_query(self):
		self.conn = sqlite3.connect('conan_info.db')
		c = self.conn.cursor()
		output = c.execute('''
			select conan_main.iqiyi_num, conan_main.name, conan_main.qty
				, iqiyi_type.tv_type, event_type.event_type, root_cause.root_cause
				, key_person.key_person, key_story.key_story
				, conan_main.comment


			from conan_main
			left join iqiyi_type on conan_main.iqiyi_type_id = iqiyi_type.id
			left join event_type on conan_main.event_type_id = event_type.id
			left join root_cause on conan_main.root_cause_id = root_cause.id
			left join key_person on conan_main.key_person_id = key_person.id
			left join key_story on conan_main.key_story_id = key_story.id


			''')
		col_name = ['iqiyi_num', 'name', 'qty', 'iqiyi_type', 'event_type', 'root_cause', 'key_person', 'key_story', 'comment']
		
		write_output(col_name, output, 'conan_main.csv')
		# c.execute('select * from conan_main where iqiyi_num = 226 or iqiyi_num = 110')
		# print (c.fetchall())
		self.conn.close()
	
	def help_db_query(self, tb_name):
		self.conn = sqlite3.connect('conan_info.db')
		c = self.conn.cursor()
		output = c.execute('select * from {tb_name}'.format(tb_name = tb_name))
		col_name = [desp[0] for desp in c.description]
		write_output(col_name, output, '{tb_name}.csv'.format(tb_name = tb_name))
		self.conn.close()


if __name__ == '__main__':
	q = conan_db()
	q.conan_main_query()

	'''
	help_table_name: 
	iqiyi_type; event_type; root_cause; key_person; key_story
	'''
	# q.help_db_query('event_type')
	# q.help_db_query('root_cause')
	# q.help_db_query('key_person')
	# q.help_db_query('key_story')
