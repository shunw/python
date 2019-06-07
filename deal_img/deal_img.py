import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.misc
import os
import cv2

class photo_deal(object): 
    def __init__(self, fl_name, face_top = None, face_bottom = None): 
        self.fl_name = fl_name
        self.face_top = face_top
        self.face_bottom = face_bottom
        
        
    def crop_2_tw(self, dpi = 300):
        '''
        according to the taiwan visa photo's request. cut the photo. only tried on US visa photo which is 602, 602 px. 
        '''
        self.img = mpimg.imread(self.fl_name)
        
        self.actual_len, self.actual_width, self.actual_channels = self.img.shape

        if self.face_top is not None and self.face_bottom is not None: 
            # self.face_top edge y actual photo
            # self.face_bottom edge y in actual photo
            self.f_len = self.face_bottom - self.face_top # actual face length
            self.non_face_ratio = self.face_top / (self.actual_len - self.face_bottom)

        # requirement according to tw
        limit_bottom = 3.2/4.5 # face in the photo's ratial bottom limit @ sample photo
        limit_top = 3.6/4.5 # face in the photo's ratial top limit @ sample photo
        p_ratial = 4.5/3.5 # photo length/ width @ sample photo

        # calculate length and width on the photo we want to crop
        t_len_1 = self.f_len / limit_bottom
        t_len_2 = self.f_len / limit_top
        t_len = max((t_len_1, t_len_2)) 
        t_width = t_len / p_ratial
        if t_width > self.actual_width: 
            t_width = self.actual_width
        if t_len > self.actual_len:
            t_len = self.actual_len
        
        # calculate new left/ right/ top/ bottom edge
        w_cut_distance = (self.actual_width - t_width)/2
        p_left_new = w_cut_distance
        p_right_new = self.actual_width - p_left_new
        # print (p_left_new, p_right_new)
        l_cut_distance = self.actual_len - t_len
        p_top_new = self.non_face_ratio * l_cut_distance
        p_bottom_new = self.actual_len - (l_cut_distance - p_top_new)
        # print (t_len, p_top_new, p_bottom_new)

        # print (p_left_new, p_right_new, p_top_new, p_bottom_new)
        # print (round(p_left_new), round(p_right_new), round(p_top_new), round(p_bottom_new))
        
        img_new = self.img[round(p_top_new):round(p_bottom_new), round(p_left_new):round(p_right_new)]
        f_new = self.fl_name.split('.')[0]+'_{dpi}dpi'.format(dpi = dpi)
        ext = self.fl_name.split('.')[1]
        mpimg.imsave(('.').join((f_new, ext)), img_new, dpi = dpi)

    def change_bg_id_photo(self):
        '''
        reference to link: 
        https://blog.csdn.net/haofan_/article/details/76618362
        https://blog.csdn.net/taily_duan/article/details/51506776
        '''
        self.img = cv2.imread(self.fl_name)
        self.actual_len, self.actual_width, self.actual_channels = self.img.shape

        hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([0, 0, 221])
        upper_blue = np.array([180, 20, 255])
        
        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        erode = cv2.erode(mask, None, iterations = 1)

        dilate = cv2.dilate(erode, None, iterations = 1)

        for i in range(self.actual_len): 
            for j in range(self.actual_width): 
                if dilate[i, j] == 255:
                    self.img[i, j] = (178, 178, 178)
        cv2.imshow('res', self.img)
        cv2.waitKey(0)
        

if __name__ == '__main__':
    f_name = 'vivian.JPG'
    
    # f_top = 50
    # f_bottom = 479
    # photo_crop = photo_deal(f_name, f_top, f_bottom)
    # photo_crop.crop_2_tw(300)

    change_bg = photo_deal(f_name)
    change_bg.change_bg_id_photo()


        
    