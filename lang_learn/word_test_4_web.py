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
    
    def get_all_files(self): 
        for (_, _, filenames) in os.walk('.'):
            for i in filenames: 
                if re.match('data-j[0-9]*.*txt', i):
                    self.word_files.append(i)
            break

    def word_df_setup(self): 
        for f in self.word_files:
            pass

    def final_run(self): 
        self.get_all_files()
        self.word_df_setup()

if __name__ == '__main__': 
    # jp_word = Prepare_web_jpwords()
    # jp_word.final_run()
    data = pd.read_csv('data-j6.txt', sep="\s+", header=None)
    data.columns = ["a", "b", "c", "etc.", 'aga']
    print (data['etc.'])
    
    
    