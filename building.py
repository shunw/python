'''
https://paiza.jp/botchi/challenges/botchi_a_1001
try the re
https://www.codewars.com/kata/5a529cced8e145207e000010/train/python
'''

'''
判断门是否联通
1. 将所有的门的位置标注出来
1.5 如果是第一个建筑物，则保证门前有路
2. 将所有门前的位置标注出来
3. 门前的位置和0 x/ y坐标相邻
4. 保证所有的 0 相邻
联通的前提是 3 和 4 都为 true

放置建筑物的方法
1. 将建筑物按照面积排序
2. 按顺序/ 按门的方向将建筑物沿墙放置
    2.1 判断长宽是否足够 （南北方向）/东西方向+考虑加一排0，以防堵住南北方向上的门
    2.2 保证门前位置有一条0的走廊

4. 放置中间的，也是按照这个策略，但是上下左右要留一条0
'''

class bld_map(object): 
    def __init__(self, h_total, w_total): 
        self.h_total = h_total
        self.w_total = w_total

class bld_case(object): 
    def __init__(self, ind, h, w, r, c): 
        self.h, self.w, self.r, self.c = h, w, r, c
        self.ind = ind
    
    def area(self): 
        return self.h * self.w
    
    def dor_face(self): 
        if self.r == 1: 
            return 'up'
        elif self.c == 1: 
            return 'left'
        elif self.r == self.h: 
            return 'down'
        else: 
            return 'right'
    
    def dor_new_pos(self, left_x, left_y): 
        # top left as 0, 0
        return (left_x + self.c, left_y + self.r)
    
    def bld_shape(self, lef_x, left_y): 
        # return left up corner and right down corner
        return [left_x, left_y], [left_x + self.w, left_y + self.h]


if __name__ == '__main__': 
    input_1_1 = '5 5 2'
    input_1_2 = ['2 5 2 2', '2 5 1 3']
    input_ls = input_1_1.split(' ')
    h_total, w_total, qty = int(input_ls[0]), int(input_ls[1]), int(input_ls[2])
    L, R, U, D = 'left', 'right', 'up', 'down'
    bld_dict = {L: dict(), R: dict(), U: dict(), D:dict()} #{'left': {area1: bld_case, area2: bld_case}, 'right': {area1: bld_case, ...}}
    for i in range(qty): 
        input_line = input_1_2[i]
        temp_case = bld_case(i+1, )