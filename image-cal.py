import csv

inp = open('a.csv', 'r')
out = open('b.csv', 'wb')
r_inp = csv.DictReader(a)
w_out = csv.DictWriter(b)

# for d in ra:
# 	#print d
# 	if wb.fieldnames is None:
# 	# initialize and write b's headers
# 		dh = dict((h, h) for h in ra.fieldnames)
# 		wb.fieldnames = ra.fieldnames
# 		wb.writerow(dh)

# 	wb.writerow(d)
sort_key=["f1", "f2"]
sort_col_1=
sort_col_2=
