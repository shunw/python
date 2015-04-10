import csv
#set the same condition
#define different items
#find the common condition for different items ---> with a funtion to do this. 

def diff_item(fl, diff):
	#find how many different items in the fields of "diff_condition"
	diff_ls=list()
	handle=csv.DictReader(open(fl, 'rU'))
	for line in handle:
		if line[diff] not in diff_ls:
			diff_ls.append(line[diff])
	return diff_ls

def get_condition(fl, Field, item, same_condition_ls):
	#get the condittion for each item, create the list for each item
	item_condition=list()
	handle=csv.DictReader(open(fl, 'rU'))
	for line in handle:
		if line[Field]!=item: continue
		temp_ls=list()
		for i in same_condition_ls:
			temp_ls.append(line[i])
		if temp_ls not in item_condition:
			item_condition.append(temp_ls)
	return item_condition



main_data="INPUTFILE.csv"
field1_lines = csv.reader(open(main_data, 'rU'))
same_condition=["SAME FIELD1", "SAME FIELD2", "SAME FIELD3", "SAME FIELD4"]
diff_condition="DIFF FIELD 1"

diff_list=diff_item(main_data, diff_condition) #get all different items under the diff_condition field
dict_all=dict() 
#this is to get all the conditions for all the items. 
for item in diff_list:
	dict_all[item]=get_condition(main_data, diff_condition, item, same_condition)

common_ls=list()
count=0


#this is to build a common list
if len(diff_list)<2:
	print "there is no different item under the field"

if count==0:
	#this is to build common_list
	for cond in dict_all[diff_list[0]]:
		if cond not in dict_all[diff_list[1]]: 
			continue
		if (cond in dict_all[diff_list[1]]) and (cond not in common_ls):
			common_ls.append(cond)
	count+=1

if count>=1:
	#compare with the common_list
	for key in range(2, len(diff_list)):
		for cond in common_ls:
			if cond not in dict_all[diff_list[key]]: 
				common_ls.remove(cond)
#this is to build a common list --- END

out_file="test.csv"
f = open(out_file, "wb")
f.truncate()
with open(main_data, 'rU') as infile, open(out_file, 'ab') as outfile:
		reader = csv.reader(infile)
		writer=csv.writer(outfile)
		line_count=0
		for row in reader:
			if line_count==0:
				temp_id=[]
				for item in same_condition: 
					temp_id.append(row.index(item))
				writer.writerow(row)
				line_count+=1
				
			if line_count>0:
				temp=[]
				for i in temp_id: 
					temp.append(row[i])
				if temp in common_ls: 
					writer.writerow(row)


