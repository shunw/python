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

import numpy as np

L, R, U, D = 'left', 'right', 'up', 'down'

class bld_map(object): 
    def __init__(self, h_total, w_total): 
        self.h_total = h_total
        self.w_total = w_total
        self.map = np.zeros((self.h_total, self.w_total))
        self.left_top_org, self.right_bottom_org = tuple((0, 0)), tuple((self.h_total, self.w_total))
        self.dor_pos = list() # load tuple in the list [(xp1, yp1), (xp2, yp2)]
    
    def dor_position_collect(self, d_x, d_y): 
        pass
    

    def _boundary_check(self): 
        if self.map.sum() == 0:
            self.left_top = self.left_top_org
            self.right_bottom = self.right_bottom_org
            
        self.tl_r_cur, self.tl_c_cur = self.left_top[0], self.left_top[1]
        self.br_r_cur, self.br_c_cur = self.right_bottom[0], self.right_bottom[1]

    def _map_update(self, bld_left_top_r, bld_left_top_c, bld_right_bot_r, bld_right_bot_c, ind):        
        self.map[bld_left_top_r:bld_right_bot_r, bld_left_top_c:bld_right_bot_c] = ind

    def _update_4_corner(self, p, max_h, max_w):
        # check 4 corner, make sure the square/ 矩形 are all 0; 
        # p is the door direction
        if p == L: 
            self.right_bottom = tuple((self.right_bottom[0], self.right_bottom[1] - (max_w + 1)))
        elif p == R: 
            self.left_top = tuple((self.left_top[0], self.left_top[1] - (max_w + 1)))
        elif p == U: 
            self.right_bottom = tuple((self.right_bottom[0] - (max_h + 1), self.right_bottom[1]))
        elif p == D: 
            self.right_bottom = tuple((self.left_top[0] - (max_h + 1), self.left_top[1]))

    def bld_load(self, p, bld_case_dict, area_des_list): 
        # bld_case is the building class case, p is the dor_direction
        # to load the pos in the map
        # strategy will be applied here
        
        self._boundary_check()
        h_cur = self.br_r_cur - self.tl_r_cur + 1
        w_cur = self.br_c_cur - self.tl_c_cur + 1

        print (self.left_top, self.right_bottom)
        
        max_h, max_w = 0, 0
        for a in area_des_list: # the list listed all the key
            bld_case = bld_case_dict[a]
            
            
            if bld_case.h > h_cur or bld_case.w > w_cur: 
                break

            if p == U: 
                
                bld_left_top_r = self.br_r_cur - bld_case.h
                bld_left_top_c = self.tl_c_cur
                bld_right_bot_r = self.br_r_cur
                bld_right_bot_c = self.tl_c_cur + bld_case.w
                
                w_cur -= bld_case.w

                if bld_case.h > max_h: 
                    max_h = bld_case.h
            
            elif p == D or p == R:
                bld_left_top_r = self.tl_r_cur
                bld_left_top_c = self.tl_c_cur
                bld_right_bot_r = self.tl_r_cur + bld_case.h
                bld_right_bot_c = self.tl_c_cur + bld_case.w
                
                if p == D: 
                    w_cur -= bld_case.w

                    if bld_case.h > max_h: 
                        max_h = bld_case.h

                elif p == R: 
                    h_cur -= bld_case.h

                    if bld_case.w > max_w: 
                        max_w = bld_case.w

            elif p == L:
                bld_left_top_r = self.tl_r_cur
                bld_left_top_c = self.br_c_cur - bld_case.w
                bld_right_bot_r = self.tl_r_cur + bld_case.h
                bld_right_bot_c = self.br_c_cur
                
                h_cur -= bld_case.h

                if bld_case.w > max_w: 
                    max_w = bld_case.w
            
            self._map_update(bld_left_top_r, bld_left_top_c, bld_right_bot_r, bld_right_bot_c, bld_case.ind)
        
        self._update_4_corner(p, max_h, max_w)
    def to_str_dis(self): 
        str_stream = self.map.flatten()
        res_total = str_stream[:self.w_total]
        print (' '.join([str(i).split('.')[0] for i in res_total]))
        for w in range(1, self.w_total): 
            res_cur = str_stream[self.w_total * w: self.w_total * (w + 1)]
            print (' '.join([str(i).split('.')[0] for i in res_cur]))
            

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
    
    def bld_shape(self, left_x, left_y): 
        # return left up corner and right down corner
        return [left_x, left_y], [left_x + self.w, left_y + self.h]


if __name__ == '__main__': 
    input_1_1 = '5 5 2'
    input_1_2 = ['2 5 2 2', '2 5 1 3']
    # input_1_2 = ['2 5 2 2', '2 3 2 2', '2 5 1 3']
    
    input_ls = input_1_1.split(' ')
    h_total, w_total, qty = int(input_ls[0]), int(input_ls[1]), int(input_ls[2])
    map_status = bld_map(h_total, w_total)
    

    L, R, U, D = 'left', 'right', 'up', 'down'
    bld_dict = {L: dict(), R: dict(), U: dict(), D:dict()} #{'left': {area1: bld_case, area2: bld_case}, 'right': {area1: bld_case, ...}}
    for i in range(qty): 
        input_line = input_1_2[i].split(' ')
        temp_case = bld_case(i+1, int(input_line[0]), int(input_line[1]), int(input_line[2]), int(input_line[3]))
        bld_dict[temp_case.dor_face()][temp_case.area()] = temp_case
    
    pos_order = [D, U, L, R]
    for p in pos_order: 
        area_des_list = sorted(list(bld_dict[p].keys()), reverse = True)
                
        # 在这里标注门的位置， 将map的可以放置的位置去掉
        map_status.bld_load(p, bld_dict[p], area_des_list) # 将一个方向上的，一次性全部load到map里去
    map_status.to_str_dis()
    
    
            
    
    
    