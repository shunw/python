import csv

# -----------------------
def getAllFieldsData(issue_field_file, issue_part_file):
	''' @param {issue_field_file} file path
	    @oaram {issue_part_file}  file path
	    @return type {field_name, [a,b,c,d]} '''
	obj = {}
	field_lines = csv.reader(file(issue_field_file, 'rb'))
	for fl in field_lines:
		if (fl[1] != 'Y'): continue
		obj[fl[0]] = [] # add field as Key
	part_lines = csv.DictReader(file(issue_part_file,'rb'))
	for pl in part_lines:
		for oKey in obj.keys():
			obj[oKey].append(pl[oKey])

	return obj

if __name__ == '__main__':
	obj = getAllFieldsData('issue_field.csv', 'D-issue-part.csv')
	print obj.items()[0][0]
	#map(int, obj.items()[0][1])
	#print obj

