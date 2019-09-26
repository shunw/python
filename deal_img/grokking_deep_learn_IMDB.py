import numpy as np
import gzip
import pickle
import os.path
import os
import sys
np.random.seed(1)


f = open('./data/IMDB/reviews.txt')
raw_reviews = f.readlines()
f.close()

f = open('./data/IMDB/labels.txt')
raw_labels = f.readlines()
f.close()

tokens = list(map(lambda x: set(x.split(' ')), raw_reviews))

vocab = set()
for sent in tokens: 
    for word in sent: 
        if word: 
        # if (len(word) > 0): 
            vocab.add(word)

word2index = {}
for i, word in enumerate(vocab): 
    word2index[word] = i

input_dataset = list()
for sent in tokens: 
    sent_indices = list()
    for word in sent: 
        try: 
            sent_indices.append(word2index[word])
        except: 
            ''
    input_dataset.append(list(set(sent_indices)))
    
