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


# print('{:15}|{:^9}|{:^9}'.format('', 'lat.', 'long.')) 
# fmt = '{:15}|{:9.4f}|{:9.4f}'
# for name, cc, pop, (latitude, longitude) in metro_areas:
#     if longitude <= 0: 
#         print(fmt.format(name, latitude, longitude))


'''
Named Tuples
'''
from collections import namedtuple

City = namedtuple('city_1', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
shanghai = City('Shanghai', 'CN', 123, (135, 246))

# print (City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data) # same as City(*delhi_data)
# for k, v in delhi._asdict().items():
#     print (k, ':', v)

a = [1, 5, 3, 7, 9]
b = [2, 10, 10, 8, 10]

# a.extend(b)

a_t = (1, 3, 5, 7, 9)
b_t = (2, 4, 6, 8, 10)
# a.append(b_t)
# print (a)
# b.insert(0, 10)
# a.pop([1])
a.sort(reverse = True)

my_list =[[1, 2, 3]] 
# print (my_list * 3)

'''
Using + and * with Sequences
'''

board = [['_'] * 3 for i in range(3)]
# board = [['_'] * 3] * 3
board[1][2] = 'X'

# row = ['_'] * 3
# board = list()
# for i in range(3): 
#     board.append(row)

board = []
for i in range(3): 
    row = ['_'] * 3
    board.append(row)
    
board[1][2] = 'X'
# print (board)

a = (1, 2, 3)
# print (id(a))
b = [4, 5, 6]
a *= 2
# print (id(a))

t = (1, 2, [30, 40])

# try: 
#     t[2] += [50, 60]
    
# except:
#     print (t)

import dis

# print (dis.dis('s[a] += b'))

fruits = ['grape', 'raspberry', 'apple', 'banana']
# fruits.sort(reverse = True)
# a = sorted(fruits, key = len)
# print (a)

'''
searching w/ bisect
'''

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES): 
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print (ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    
    else: 
        bisect_fn = bisect.bisect

    print ('DEMO:', bisect_fn.__name__)
    print ('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

