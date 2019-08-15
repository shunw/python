'''
https://gist.github.com/keithweaver/70df4922fec74ea87405b83840b45d57

https://www.programcreek.com/python/example/85663/cv2.VideoCapture
'''
import cv2
import numpy as np
import os
from os import walk
import shutil
import time
import pandas as pd
import math 
from imutils import contours
import imutils

from PIL import Image, ImageChops, ImageDraw, ImageStat
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from scipy.misc import toimage
from skimage import data, io, filters, color, measure
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
import operator
import re
import glob

from sklearn.cluster import MiniBatchKMeans, KMeans
import math
import torch
import torch.nn.functional as F
from torch import nn
from torch.nn import Linear
from torch import optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models
from torch.autograd import Variable

def get_img_under_folder(mypath): 
    '''
    this is to get all the jpg files under one folder
    '''
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break
    return f

class Training_set_setup(object): 
    '''
    purpose: to setup the training image sets

    '''
    def __init__(self, img_dir):         
        self.img_dir = img_dir
        self.img_name_ls = get_img_under_folder(self.img_dir)
        self.cp_frm = [(86, 153), (126, 193)]

        self.cp_start_r = self.cp_frm[0][1]
        self.cp_end_r = self.cp_frm[1][1]
        self.cp_start_c = self.cp_frm[0][0]
        self.cp_end_c = self.cp_frm[1][0]

    def setup_training_set(self): 
        x_train = list()
        y_train = list()
        
        for p in self.img_name_ls:
            if 'txt' in p: 
                continue
            
            pic = cv2.imread(os.path.join(self.img_dir, p))[self.cp_start_r:self.cp_end_r, self.cp_start_c:self.cp_end_c]
            x_train.append(pic.flatten())
            y_train.append(int(p.split('.')[-2].split('_')[1]))
            
            # plt.imshow(cv2.cvtColor(pic_data.reshape((40, 40, 3)), cv2.COLOR_BGR2RGB))
            # plt.show()
        x_train = np.array(x_train)
        y_train = np.array(y_train)
        x_train, y_train = map(torch.tensor, (x_train, y_train))    
        
        return x_train, y_train
        

    
    def final_run(self):
        pass
class Mnist_Logistic(nn.Module): 
    def __init__(self, input_size, hidden_size, output_size):
        super(Mnist_Logistic, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer1_2 = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, output_size)
        self.layer2_2 = nn.ReLU()
    
    def forward(self, input):
        out = self.layer1(input)
        out = self.layer1_2(out)
        out = self.layer2(out)
        out = self.layer2_2(out)
        return out


class Image_torch_train(object): 
    def __init__(self, img_dir): 
        '''
        x_train and y_train are tensor data
        '''
        # self.x_train = x_train
        # self.y_train = y_train  

        # # self.x_train_normal = (self.x_train - self.x_train.min()) *1.0 / (self.x_train.max() - self.x_train.min())    
        simple_transform = transforms.Compose([transforms.RandomHorizontalFlip(), transforms.RandomRotation(.2), transforms.ToTensor(), transforms.Normalize([.485, .456, .406], [.229, .224, .225])]) 
        # self.x_train_normal = self.x_train(transform = simple_transfer)
        # # self.x_train_normal = self.x_train_normal.float()
        # self.y_train = self.y_train.type(torch.LongTensor)  
        
        self.img_dir = img_dir
        self.train = datasets.ImageFolder(os.path.join(self.img_dir, 'train'), simple_transform)
        self.valid = datasets.ImageFolder(os.path.join(self.img_dir, 'valid'), simple_transform)

        self.train_data_gen = torch.utils.data.DataLoader(self.train, batch_size = 1, num_workers = 3)
        self.valid_data_gen = torch.utils.data.DataLoader(self.valid, batch_size = 1, num_workers = 3)
        
        self.loss_func = F.cross_entropy
        # self.n, self.c = self.x_train.shape
        # self.weights = torch.randn(self.c, 10)/ math.sqrt(self.c)
        # self.weights.requires_grad_()
        self.bias = torch.zeros(10, requires_grad = True)
        
        self.epochs = 50 # how many epochs to train for
        self.lr = .5 # learning rate
        self.bs = 64

        # self.model = Mnist_Logistic()
    def get_model(self): 
        self.model = Mnist_Logistic(self.c, 10, 3)
        self.opt = optim.SGD(self.model.parameters(), lr = self.lr)
        return self.model, self.opt

    def img_train(self): 
        print (self.x_train_normal)
        print ('loss func',self.loss_func(self.model(self.x_train_normal), self.y_train))

    def fit(self): 

        for ep in range(self.epochs): 
            for i in range((self.n - 1)//self.bs + 1):
                start_i = i * self.bs
                end_i = start_i + self.bs
                self.xb = self.x_train_normal[start_i : end_i]
                self.yb = self.y_train[start_i: end_i]
                pred = self.model(self.xb)
                loss = self.loss_func(pred, self.yb)

                loss.backward()

                # with torch.no_grad():
                #     for p in self.model.parameters():
                #         p -= p.grad * self.lr
                #     self.model.zero_grad()

                self.opt.step()
                self.opt.zero_grad()

    def train_model(self): 
        model = models.resnet18(pretrained = False)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 3)

        learning_rate = .001
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(model.parameters(), lr = learning_rate, momentum = .9)
        scheduler = optim.lr_scheduler.StepLR(optimizer, step_size = 7, gamma = .1)
        num_epochs = 25

        dataset_sizes = {'train': len(self.train_data_gen), 'valid':len(self.valid_data_gen)}
        dataloaders = {'train': self.train_data_gen, 'valid': self.valid_data_gen}
        since = time.time()

        best_model_wts = model.state_dict()
        best_acc = 0.0

        for epoch in range(num_epochs): 
        # for epoch in range(1): 
        
            print ('Epoch{}/{}'.format(epoch, num_epochs - 1))
            print ('-' * 10)

            # Each epoch has a training and validation phase
            for phase in ['train', 'valid']: 
                if phase == 'train': 
                    scheduler.step()
                    model.train(True) # set model to training mode
            
                else: 
                    model.train(False) # set model to evaluate mode

                running_loss = 0.0
                running_corrects = 0

                # Iterate over data
                
                for data in dataloaders[phase]: 
                # for data in self.valid_data_gen:

                    # get the inputs
                    inputs, labels = data

                    # wrap them in Variable
                    inputs, labels = Variable(inputs), Variable(labels)
                    
                    # zero the parameter gradients
                    optimizer.zero_grad()

                    # forward
                    outputs = model(inputs)
                    # print ('output.size: ', outputs.size())
                    # print ('label.size: ', labels.size())
                    _, preds = torch.max(outputs.data, 1)
                    # print ('preds')
                    # print ('-' * 10)
                    # print (preds.size())
                    # print ('labels')
                    # print ('-' * 10)
                    # print (labels)
                    loss = criterion(outputs, labels)

                    # backward + optimize only if in training phase
                    if phase == 'train': 
                        loss.backward()
                        optimizer.step()
                    
                    # statistics 
                    # running_loss += loss.data[0]
                    # print ('inner loss: ', loss.data)
                    # print ('inner correct: ', torch.sum(preds == labels.data))
                    running_loss += loss.item()
                    running_corrects += torch.sum(preds == labels.data)
                
                # print ('corrects: ', running_corrects)
                # print ('loss: ', running_loss)
                # print ('datasize: ', dataset_sizes[phase])
                epoch_loss = running_loss/ dataset_sizes[phase]
                epoch_acc = running_corrects.float()/ dataset_sizes[phase]

                print ('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))

                # deep copy the model
                if phase == 'valid' and epoch_acc > best_acc: 
                    best_acc = epoch_acc
                    best_model_wts = model.state_dict()
            print()
        
        time_elapsed = time.time() - since

        print ('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed// 60, time_elapsed% 60))
        print ('Best val Acc: {:4f}'.format(best_acc))

        # load best model weights 
        model.load_state_dict(best_model_wts)
        return model
class Setup_dataset_folder(object): 
    def __init__(self, to_path): 
        '''
        three purpose in the class
        1. copy image from other folder to datasets, and category the image by label
        2. move the image to the train/ valid folder
        3. move back the image to the original folder in the datasets
        '''
        self.to_path = to_path

    def copy_img_2_datasets(self, from_path, cp_pos = None, unit_name = None): 
        '''
        copy image from from_path to to_path and put the image in different label folder
        and only save the control panel position
        '''
        self.from_path = from_path
        self.unit_name = unit_name
        self.cp_pos = cp_pos
        if self.cp_pos: 
            self.row_s = self.cp_pos[0][1]
            self.row_e = self.cp_pos[1][1]
            self.col_s = self.cp_pos[0][0]
            self.col_e = self.cp_pos[1][0]

        for (dirpath, dirnames, files) in walk(self.from_path): 
            # cnt = 0
            for f in files: 
                if f.split('.')[-1].lower() != 'jpg': continue

                # check the label and create the folder
                label = f.split('.')[-2].split('_')[-1]
                newpath = os.path.join(self.to_path, label)
                if not os.path.exists(newpath):
                    os.makedirs(newpath)

                f_new = f
                # add the unitname
                if self.unit_name: 
                    f_new = '{unit}_{f}'.format(unit = self.unit_name, f = f)
                
                to_be_copied = os.path.join(dirpath, f)
                f_new = os.path.join(newpath, f_new)
                shutil.copy(to_be_copied, f_new)
                
                temp = io.imread(f_new)[self.row_s:self.row_e, self.col_s: self.col_e]
                io.imsave(f_new, temp)

    def create_train_valid(self, trn_vs_valid = 0.7):
        '''
        this is to create the train/ valid folder from the datasets
        '''

        # get the label lvl list
        for (dirpath, dirnames, files) in walk(self.to_path): 
            if not files:
                label_lvl_ls = dirnames.copy()

        files = glob.glob(os.path.join(self.to_path, '*/*.jpg'))
        print (f'Total no of images {len(files)}')

        no_of_images = len(files)

        # Create a shuffled index which can be used to crate a validation data set
        shuffle = np.random.permutation(no_of_images)

        # Create a validation directory for holding validation images. 
        first_lvl_name_ls = ['train', 'valid']

        for fd in first_lvl_name_ls: 
            if not os.path.isdir(os.path.join(self.to_path, fd)): 
                os.mkdir(os.path.join(self.to_path, fd))
        
        # Create directories with label names
        for t in first_lvl_name_ls:
            for folder in label_lvl_ls: 
                if not os.path.isdir(os.path.join(self.to_path, t, folder)): 
                    os.mkdir(os.path.join(self.to_path, t, folder))

        # Copy a small subset of images into the validation folder. 
        sample_last_ind = int(no_of_images * trn_vs_valid)
        for i in shuffle[:sample_last_ind]: 
            f_path = os.path.normpath(files[i])
            folder = f_path.split('\\')[-1].split('.')[-2].split('_')[-1]
            image = os.path.basename(files[i])
            os.rename(files[i], os.path.join(self.to_path, 'valid', folder, image))

        # Copy a small subset of images into the training folder
        for i in shuffle[sample_last_ind: ]:
            f_path = os.path.normpath(files[i])
            folder = f_path.split('\\')[-1].split('.')[-2].split('_')[-1]
            image = os.path.basename(files[i])
            os.rename(files[i], os.path.join(self.to_path, 'train', folder, image))

    def move_trn_valid_back(self): 
        '''
        to move back the training image to original folder
        '''
            
        files = glob.glob(os.path.join(self.to_path, '*/*/*.jpg'))
        print (f'Total no of images {len(files)}')

        com_folder = os.path.commonpath(files)

        for f in files: 
            f_path = os.path.normpath(f)
            folder = f_path.split('\\')[-1].split('.')[-2].split('_')[-1]
            image = os.path.basename(f)
            os.rename(f, os.path.join(com_folder, folder, image))

        

if __name__ == '__main__':
    start_time = time.time()
    
    
    # img_dir = './data/datasets'
    # # training_data = Training_set_setup(img_dir)
    # # x_train, y_train = training_data.setup_training_set()
    
    # img_cost = Image_torch_train(img_dir)
    # # img_cost.get_model()
    # img_cost.train_model()
    
    # img_cost.img_train()
    # img_cost.fit()
    # img_cost.img_train()

    # ------------------------------- TRAIN / VALID FOLDER --------------------------
    from_path = './data/G2079_to_be_copied'
    to_path = './data/datasets'
    unit_name = 'G2079'
    cp_pos = [(86, 153), (126, 193)]
    setup_folder = Setup_dataset_folder(to_path)

    # this is to copy the images to the dataset folder
    setup_folder.copy_img_2_datasets(from_path, cp_pos, unit_name)

    # # this is to create train/ valid folder
    # setup_folder.create_train_valid()

    # # this is to move the images back to original folder from train/ valid
    # setup_folder.move_trn_valid_back()

    # -------------------------------  --------------------------