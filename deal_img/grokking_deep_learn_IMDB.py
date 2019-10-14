import numpy as np
import gzip
import pickle
import os.path
import os
import sys
from collections import Counter
import math
import random

np.random.seed(1)
random.seed(1)


def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

def sigmoid2dev(output): 
    return output * (1 - output)

class imdb_analysis(object): 
    def __init__(self): 
        pass

    def imdb_dataset_prepare(self): 
        f = open('./data/IMDB/reviews.txt')
        raw_reviews = f.readlines()
        f.close()

        f = open('./data/IMDB/labels.txt')
        raw_labels = f.readlines()
        f.close()

        tokens = list(map(lambda x: set(x.split(' ')), raw_reviews))

        self.vocab = set()
        for sent in tokens: 
            for word in sent: 
                if word: 
                # if (len(word) > 0): 
                    self.vocab.add(word)

        self.word2index = {}
        for i, word in enumerate(self.vocab): 
            self.word2index[word] = i

        self.input_dataset = list()
        for sent in tokens: 
            sent_indices = list()
            for word in sent: 
                try: 
                    sent_indices.append(self.word2index[word])
                except: 
                    ''
            self.input_dataset.append(list(set(sent_indices)))

        self.target_dataset = list()
        for label in raw_labels: 
            if label == 'positive\n': 
                self.target_dataset.append(1)
            else: 
                self.target_dataset.append(0)
        # return self.input_dataset, self.target_dataset
        
        # make the input into one-hot...
        self.input_feature = np.array(list(self.word2index.values())[:])
        self.input_qty = len(self.input_dataset)
        self.input_feat_qty = len(self.input_feature)
        # self.input_dataset_one_hot = np.zeros((self.input_qty, len(self.input_feature)))

        # for sent_ind in range(self.input_qty): 
        #     for word_ind in self.input_dataset[sent_ind]: 
        #         self.input_dataset_one_hot[sent_ind, word_ind] = 1

    def nn_process(self): 
        alpha, iterations = (.01, 2)
        hidden_size = 100

        self.weights_0_1 = .2 * np.random.random((len(self.vocab), hidden_size)) - .1
        self.weights_1_2 = .2 * np.random.random((hidden_size, 1)) - .1

        correct, total = (0, 0)

        for iter in range(iterations): 

            for i in range(self.input_qty - 1000): 

                x, y = (self.input_dataset[i], self.target_dataset[i])
                
                layer_1 = sigmoid(np.sum(self.weights_0_1[x], axis = 0))
                # print (layer_1.shape)
                
                layer_2 = sigmoid(np.dot(layer_1, self.weights_1_2))

                # no sigmoid2dev =========================
                layer_2_delta = layer_2 - y
                layer_1_delta = np.dot(layer_2_delta, np.transpose(self.weights_1_2))

                self.weights_0_1[x] -= layer_1_delta * alpha
                self.weights_1_2 -= np.outer(layer_1, layer_2_delta) * alpha
                # no sigmoid2dev =========================

                # # with sigmoid2dev =========================
                # layer_2_delta = (layer_2 - y) * sigmoid2dev(layer_2)
                # layer_1_delta = np.dot(layer_2_delta, np.transpose(self.weights_1_2)) 
                
                # layer_1_delta = layer_1_delta * sigmoid2dev(layer_1)
                

                # self.weights_0_1[x] -= layer_1_delta * alpha
                # self.weights_1_2 -= np.outer(layer_1, layer_2_delta) * alpha
                # # with sigmoid2dev =========================

                if (np.abs(layer_2_delta) < .5): 
                    correct += 1
                total += 1
                # break

            if i % 10 == 9: 
                progress = i/ float(self.input_qty) *100
            
        
            print ('Iter: {iter}; Progress: {progress:.3f} %; Training Accuracy: {acc:.3f} %'.format(iter = iter, progress = progress, acc = correct/ float(total) * 100))
            # break

        correct, total = (0, 0)            
        for i in range(len(self.input_dataset) - 1000, len(self.input_dataset)): 

            x = self.input_dataset[i]        
            y = self.target_dataset[i]

            layer_1 = sigmoid(np.sum(self.weights_0_1[x], axis = 0))
            layer_2 = sigmoid(np.dot(layer_1, self.weights_1_2))

            if np.abs(layer_2 - y) < .5: 
                correct += 1
            total += 1
        print ('Test Accuracy: {}'.format(correct/ float(total)))

    def similar(self, target = 'beautiful'): 
        target_index = self.word2index[target]
        scores = Counter()
        for word, index in self.word2index.items(): 
            raw_difference = self.weights_0_1[index] - self.weights_0_1[target_index]
            # print (raw_difference[0])
            squared_difference = raw_difference * raw_difference
            scores[word] = -math.sqrt(sum(squared_difference))
            # break
        print (scores.most_common(10))
        return scores.most_common(10)

    def final_run(self): 
        self.imdb_dataset_prepare()
        self.nn_process()
        self.similar()

class imdb_filling_word(object): 
    def __init__(self): 
        pass
    
    def imdb_dataset_prepare(self): 
        f = open('./data/IMDB/reviews.txt')
        raw_reviews = f.readlines()
        f.close()

        tokens = list(map(lambda x: x.split(' '), raw_reviews))
        wordcnt = Counter()
        for sent in tokens: 
            for word in sent: 
                wordcnt[word] -= 1
                # wordcnt[word] += 1
        
        # get the most/ less common word in each reviews/ 
        self.vocab = list(set(map(lambda x: x[0], wordcnt.most_common())))

        self.word2index = {}
        for i, word in enumerate(self.vocab): 
            self.word2index[word] = i

        self.concatenated = list()
        self.input_dataset = list()
        for sent in tokens: 
            sent_indices = list()

            for word in sent: 
                try: 
                    sent_indices.append(self.word2index[word])
                    self.concatenated.append(self.word2index[word])
                except: 
                    ''
            self.input_dataset.append(sent_indices)

        self.concatenated = np.array(self.concatenated)
        random.shuffle(self.input_dataset)

    def nn_process(self): 
        self.alpha, self.iterations = (.05, 2)
        self.hidden_size, self.window, self.negative = (50, 2, 5)
        
        self.weights_0_1 = (np.random.rand(len(self.vocab), self.hidden_size) - .5) * .2
        self.weights_1_2 = np.random.rand(len(self.vocab), self.hidden_size) * .2

        self.layer_2_target = np.zeros(self.negative + 1)
        self.layer_2_target[0] = 1

        # count = 0
        for rev_i, review in enumerate(self.input_dataset * self.iterations): 
            for target_i in range(len(review)): 
                
                # ? what is the target_samples for?         
                # [当前review的当前轮单词，在concatenated里任选五个单词]
                target_samples = [review[target_i]] + list(self.concatenated[(np.random.rand(self.negative) * len(self.concatenated)).astype('int').tolist()])
                
                # 以2-4个单词为范围，4个单词的话，left context就是左边两个，right context就是右边两个。有些边缘情况是，两边不相等，可能会出现一边没有单词，另外一边两个单词的情况
                left_context = review[max(0, target_i - self.window): target_i]
                right_context = review[target_i: min(len(review), target_i + self.window)]
                
                # print ()
                # print ('count = {}'.format(count))
                # print (target_samples)
                # print (left_context + right_context)

                # left_context + right_context 组成了一条 input data
                layer_1 = np.mean(self.weights_0_1[left_context + right_context], axis = 0)
                # ? weight_1_2 系数直接指向target samples，不清楚为何酱紫设计
                layer_2 = sigmoid(np.dot(layer_1, self.weights_1_2[target_samples].T))
                layer_2_delta = layer_2 - self.layer_2_target
                layer_1_delta = np.dot(layer_2_delta, self.weights_1_2[target_samples])

                self.weights_0_1[left_context + right_context] -= layer_1_delta * self.alpha
                self.weights_1_2[target_samples] -= np.outer(layer_2_delta, layer_1) * self.alpha
            #     count += 1
            #     if count == 5: break
            # break
            
            # if rev_i % 250 == 0:
            #     print ()
            #     print ('Progress: {progress} {simi_terr}'.format(progress = rev_i/float(len(self.input_dataset) * self.iterations), simi_terr = self.similar('terrible')))
        print ('*=*-' * 20)    
        print ('Progress: {progress} {simi_terr}'.format(progress = rev_i/float(len(self.input_dataset) * self.iterations), simi_terr = self.similar('terrible')))
        
    def similar(self, target = 'beautiful'): 
        target_index = self.word2index[target]
        scores = Counter()
        for word, index in self.word2index.items(): 
            raw_difference = self.weights_0_1[index] - self.weights_0_1[target_index]
            # print (raw_difference[0])
            squared_difference = raw_difference * raw_difference
            scores[word] = -math.sqrt(sum(squared_difference))
            # break
        # print (scores.most_common(10))
        return scores.most_common(10)


    def final_run(self):
        self.imdb_dataset_prepare()
        self.nn_process()

if __name__ == '__main__': 
    # imdb_analysis = imdb_analysis()
    # imdb_analysis.final_run()

    fil_word = imdb_filling_word()
    fil_word.final_run()
    
# till 202
    
