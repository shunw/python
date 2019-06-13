p = (4, 5)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
data = 'Wendy'

a, b, *_ = data


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
a = line.split(':')

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_1, (*_2, year) = record

items = [1, 10, 7, 4, 5, 9]

def sum(items): 
    head, *tail = items
    return head + sum(tail) if tail else head

'''
till 1.3
'''