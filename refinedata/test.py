import csv

with open('names.csv', 'wb') as csvfile:
    # fieldnames = ['first_name', 'last_name']
    a='/***/Dorado-MT-2012/***/Dorado/***/75g-Xerox Business Multipurpose 4200/***/'
    b=a.split('/***/')
    print b
    writer = csv.writer(csvfile)
        # writer.writeheader()
    writer.writerow(b)
    # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})