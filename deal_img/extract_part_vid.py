'''
https://gist.github.com/keithweaver/70df4922fec74ea87405b83840b45d57

https://www.programcreek.com/python/example/85663/cv2.VideoCapture
'''
import cv2
import numpy as np
import os
import time
import pandas as pd

from PIL import Image, ImageChops, ImageDraw
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from scipy.misc import toimage
from skimage import data, io, filters, color
from skimage.filters import threshold_local
from skimage.feature import peak_local_max
from skimage.feature import canny
import skimage.color as skcolor
import skimage
from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label

from functools import partial 
import time

class Vid_deal(object):
    def __init__(self, fl_name, cp_p_inf = [(81, 152), (132, 193)], start_print_frm = 0):
        '''
        cp_p_inf: (start_r, end_r, start_c, end_c) --- this is to get the control panel position within the image
        '''
        self.fl_name = fl_name

        # Playing video from file:
        self.cap = cv2.VideoCapture(self.fl_name)

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.fcount = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.v_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.v_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.cp_frm = cp_p_inf
        self.cp_start_r = self.cp_frm[0][1]
        self.cp_end_r = self.cp_frm[1][1]
        self.cp_start_c = self.cp_frm[0][0]
        self.cp_end_c = self.cp_frm[1][0]

        self.start_print_frm = start_print_frm
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print ('Error: Creating directory of data')
    
    def extract_part_video(self):
        start_mm = 0
        start_ss = 10
        end_mm = 0
        end_ss = 15

        start_frame = (start_mm * 60 + start_ss) * self.fps 
        end_frame = (end_mm * 60 + end_ss) * self.fps 
        
        cap = cv2.VideoCapture(self.fl_name)

        fourcc = cv2.VideoWriter_fourcc(*'MJPG') # MPG4
        out = cv2.VideoWriter('output.avi', fourcc, int(self.fps), (int(self.v_width), int(self.v_height)))
        
        currentFrame = 0

        while (True):
            ret, frame = cap.read()
            
            if cap.get(cv2.CAP_PROP_POS_FRAMES) > start_frame:
            # if currentFrame > start_frame:
                

                # frame = cv2.flip(frame,0)
                out.write(frame)

                # cv2.imshow('frame',frame)
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     break
                # print ('after the start point')
            if (not ret) or (cap.get(cv2.CAP_PROP_POS_FRAMES) > end_frame):  
            # if (not ret) or (currentFrame > end_frame):  
                print ('after the end point')
                break
            
            currentFrame += 1
        
        cap.release()
        out.release()
        cv2.destroyAllWindows()    

    def final_run(self):
        # get part of the video for study    --- seemed failed
        self.extract_part_video()
        
if __name__ == '__main__':
    start_time = time.time()
    
    fl_name = '119.mp4'
    
    # # this is to get the cooling down time. 
    vid_1 = Vid_deal(fl_name)
    vid_1.final_run()

    print("--- %s seconds ---" % (time.time() - start_time))