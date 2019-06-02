symbols = '$¢£¥€¤'
# print ([ord(x) for x in symbols if ord(x) > 127])
# for k in map(ord, symbols):
#     print (k)


'''
generator expressions could be used in: 
list/ tuple/ arrays, etc
'''
tuple_gen = tuple(ord(s) for s in symbols)
# print (tuple_gen)

import array
array_gen = array.array('I', (ord(s) for s in symbols))

'''
Tuples's position/ order is always vital.
'''

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

a_test = sorted(traveler_ids, key = lambda x: x[1], reverse = True)
# for p in a_test:
#     print ('{c}/{id}'.format(c = p[0], id = p[1]))

'''
use * to grab items / set multiple items
prefix can be applied to exactly one variable, but it can appear in any position.
'''
t = (20, 8)
# print (divmod(*t))

a, b, *rest = range(5)
# print (rest)

*head, a, b = range(2)
# print (head)

'''
nested tuple unpacking
'''

metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)), 
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.')) 
print('{:15}|{:^9}|{:^9}'.format('', 'lat.', 'long.')) 
fmt = '{:15}|{:9.4f}|{:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0: 
        print(fmt.format(name, latitude, longitude))
