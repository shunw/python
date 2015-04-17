import csv
import itertools

a = open('a.csv', 'r')
b = open('b.csv', 'wb')
ra = csv.DictReader(a)
wb = csv.DictWriter(b, None)

for d in ra:

  if wb.fieldnames is None:
    # initialize and write b's headers
    dh = dict((h, h) for h in ra.fieldnames)
    print ra.fieldnames
    wb.fieldnames = ra.fieldnames
    wb.writerow(dh)

  wb.writerow(d)

b.close()
a.close()
