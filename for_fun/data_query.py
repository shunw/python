'''
python3
'''
# -*- coding: utf-8 -*-
import sqlite3
import csv

def write_output(col_name, data):
	f = open('conan_main.csv', 'w')
	data_write = list()
	for line in data: 
		data_write.append(line)
	writer = csv.writer(f)
	writer.writerow(col_name)
	writer.writerows(data_write)
	


dec='utf-8'
conn = sqlite3.connect('conan_info.db')
c = conn.cursor()
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
# output = c.execute('SELECT * from conan_main')

col_name = ['iqiyi_num', 'name', 'qty', 'iqiyi_type', 'event_type', 'root_cause', 'key_person', 'key_story', 'comment']

# for i in output:
# 	print (i)

write_output(col_name, output)

conn.close()
