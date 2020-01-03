# just to prepare the python interview, here is some trial

import numpy as np
import re

a = "not 404 50.56 found 张三 99 深圳"
p = re.compile('[^a-z0-9\W]+')
res = re.findall(p, a)
# print (res)

b = '1010000010000100'
g_res = re.findall('1.*1', b)
ng_res = re.findall('1.*?1', b)
# print (g_res)
# print (ng_res)


c = [[1, 2], [3, 4], [5, 6]]
# print (np.array(c).flatten().tolist())
# print ([a for i in c for a in i])

x = 'abc'
y = 'def'
z = ['d', 'e', 'f']
# print (x.join(y))
# print (x.join(z))

a = [1, 2, 3]
b = {'4', '5', '6'}
t = zip(a, b)
# print ([i for i in t])

a = '张明 98分'
b = re.sub('98', '100', a)
# print (b)

a = b'hello'
b = '你好'.encode()
# print (a, b.decode())
# print (len(a), len(b))
# print (type(a), type(b))

url = 'https://detail.tmall.com/item.htm?id=610008789094&ali_refid=a3_420434_1006:1105079343:N:/vIF11Kasy5TxQ01LdRplNlSe3/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1/lYD/A:6d62562c20d529db713bf8d1392da642&ali_trackid=1_6d62562c20d529db713bf8d1392da642&spm=a230r.1.1957635.6'

res = re.findall('dateRange=(.*?)%7C(.*?)&', url)
# print (res)

lis = [2, 3, 1, 10, 9, 6, 5, 4]
for k, v in enumerate(lis): 
    if k == 0: continue
    if v >= lis[k -1]: continue
    else: 
        lis[k], lis[k-1] = lis[k-1], lis[k]
    
        for j in range(k-1, 0, -1): 
            if lis[j] >= lis[j - 1]: break
            else: 
                lis[j], lis[j - 1] = lis[j - 1], lis[j]
print (lis)