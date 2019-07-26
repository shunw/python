import codecs 
import random
from collections import defaultdict
import glob
import os
import word_func
import re
import pandas as pd


class Prepare_web_jpwords(object): 
    def __init__(self): 
        self.word_files = []
        self.word_df_name = 'all_word.pkl'
        self.ready_2_web_name_part = 'ready_2_web'

        self.col_name_les = 'lesson_no'
        self.col_name_itemno = '番号'
        self.col_name_word = '単語'
        self.col_name_chn = '漢字'
        self.col_name_mean = '意味'
    
    def get_all_files(self): 
        for (_, _, filenames) in os.walk('.'):
            for i in filenames: 
                if re.match('data-j[0-9]+.*txt', i):
                    self.word_files.append(i)
            break

    def word_df_setup(self): 
        '''
        1. get all the words
        2. reset the index number
        3. write into one pkl dataframe
        '''
        cnt = 0
        for f in self.word_files:
            lesson_no = re.findall('[0-9]+', f)
            
            if cnt == 0: 
                self.all_word_df = pd.read_csv(f, sep="\s+", header=0)
                self.all_word_df[self.col_name_les] = lesson_no * self.all_word_df.shape[0]
                cnt += 1
            
            else: 
                # print (f)
                temp_df = pd.read_csv(f, sep="\s+", header=0)
                temp_df[self.col_name_les] = lesson_no * temp_df.shape[0]
                self.all_word_df = self.all_word_df.append(temp_df)
                cnt += 1
            # if cnt == 2: 
            #     break
        # print (self.all_word_df.tail())
        self.all_word_df = self.all_word_df.reset_index(drop = True)
        self.all_word_df.to_pickle(self.word_df_name)

    def refine_dataframe(self, word_interval = 70): 
        '''
        read pkl data
        shuffle the data
        
        future func: 
            add weight during the shuffle
        
        write to web format in txt type
        '''
        self.all_word_prepare = pd.read_pickle(self.word_df_name)
        self.all_word_prepare = self.all_word_prepare.sample(frac = 1, random_state = 1)

        total_num = self.all_word_prepare.shape[0]
        file_num = total_num // word_interval
        
        for file_ind in range(file_num): 

            output_name = '{part}_{count}.txt'.format(part = self.ready_2_web_name_part, count = file_ind)


            word_web = open(output_name,"w") 

            for i in range(word_interval): 
                # Program to show various ways to read and 
                # write data in a file. 
                w_row = i + file_ind * word_interval

                mean = self.all_word_prepare[self.col_name_mean].iloc[w_row]
                word = '{w} / {ch} ({les_no}-{wor_no})'.format(w = self.all_word_prepare[self.col_name_word].iloc[w_row], ch = self.all_word_prepare[self.col_name_chn].iloc[w_row], les_no = self.all_word_prepare[self.col_name_les].iloc[w_row], wor_no = self.all_word_prepare[self.col_name_itemno].iloc[w_row])
                L = ["- {mean}\n\n    - {word}\n\n".format(mean = mean, word = word)]  
                
                # \n is placed to indicate EOL (End of Line) 
                word_web.writelines(L) 
            
            word_web.close() #to change file access modes 
        
        w_row += 1

        if w_row < total_num - 1: 

            output_name = '{part}_{count}.txt'.format(part = self.ready_2_web_name_part, count = file_num)

            word_web = open(output_name,"w") 

            for i in range(w_row, total_num): 
                # Program to show various ways to read and 
                # write data in a file. 
                
                w_row = i 

                mean = self.all_word_prepare[self.col_name_mean].iloc[w_row]
                word = '{w} / {ch} ({les_no}-{wor_no})'.format(w = self.all_word_prepare[self.col_name_word].iloc[w_row], ch = self.all_word_prepare[self.col_name_chn].iloc[w_row], les_no = self.all_word_prepare[self.col_name_les].iloc[w_row], wor_no = self.all_word_prepare[self.col_name_itemno].iloc[w_row])
                
                L = ["- {mean}\n\n    - {word}\n\n".format(mean = mean, word = word)]  
                
                # \n is placed to indicate EOL (End of Line) 
                word_web.writelines(L) 
                
            word_web.close() #to change file access modes 


    def final_run(self): 
        self.get_all_files()
        # self.word_df_setup()
        # print (self.all_word_df.tail())
        self.refine_dataframe()
        # print (self.all_word_prepare.head())

if __name__ == '__main__': 
    jp_word = Prepare_web_jpwords()
    jp_word.final_run()
    
    # data = pd.read_csv('data-j6.txt', sep="\s+", header=0)
    # data.columns = ["item#", "word", "chinese_form", "mean", '1st_item']
    # a = 'data-j36.txt'
    # b = re.findall('[0-9]+', a)
    # print (b * 3)
    # print (data.head())

    
    
    