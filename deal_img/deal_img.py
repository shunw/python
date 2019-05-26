import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.misc
import os

class photo_crop(object): 
    def __init__(self, fl_name, face_top, face_bottom): 
        self.img = mpimg.imread(fl_name)
        self.actual_len, self.actual_width, _ = self.img.shape

        self.face_top = face_top # face top edge y actual photo
        self.face_bottom = face_bottom # face bottom edge y in actual photo
        self.f_len = self.face_bottom - self.face_top # actual face length
        self.non_face_ratio = self.face_top / (self.actual_len - self.face_bottom)
        self.fl_name = fl_name
        

    def crop_2_tw(self, dpi):
        '''
        according to the taiwan visa photo's request. cut the photo. only tried on US visa photo which is 602, 602 px. 
        '''

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

if __name__ == '__main__':
    f_name = 'zjf.JPG'
    f_top = 50
    f_bottom = 479
    # f_top = 30
    # f_bottom = 407
    photo_crop = photo_crop(f_name, f_top, f_bottom)
    photo_crop.crop_2_tw(300)
    # print (photo_crop.non_face_ratio)
    # print (photo_crop.actual_len, photo_crop.actual_width)
        
    