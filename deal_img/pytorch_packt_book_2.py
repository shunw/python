import pickle
import gzip
from pathlib import Path

import torch
import torch.nn as nn
from torch.nn import Linear
from torch.autograd import Variable
import torch.optim as optim
from torchvision import models
from torch.optim import lr_scheduler
import time

import glob
import os
import numpy as np

class MyFirstNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size): 
        super(MyFirstNetwork, self).__init__()
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

class Mnist_data_train(object): 
    def __init__(self):
        DATA_PATH = Path("data")
        PATH = DATA_PATH / "mnist"

        FILENAME = "mnist.pkl.gz"

        with gzip.open((PATH / FILENAME).as_posix(), "rb") as f:
            ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")

        self.x_train, self.y_train, self.x_valid, self.y_valid = map(torch.tensor, (x_train, y_train, x_valid, y_valid))

        self.epochs = 2
        self.bs = 64
        self.n, self.c = self.x_train.shape
        self.loss_func = nn.CrossEntropyLoss()
        self.lr = .001 # learning rate

    def data_fit(self):
        
        model = MyFirstNetwork(self.c, 10, 10)
        optimizer = optim.SGD(model.parameters(), lr = self.lr)
        
        print (self.loss_func(model(self.x_train), self.y_train))

        for self.epoch in range(self.epochs):
            for i in range((self.n - 1) // self.bs + 1):
                start_i = i * self.bs
                end_i = start_i + self.bs

                xb = self.x_train[start_i: end_i]
                yb = self.y_train[start_i: end_i]

                pred = model(xb)
                loss = self.loss_func(pred, yb)

                loss.backward()
                # with torch.no_grad(): 
                #     for p in model.parameters(): 
                #         p -= p.grad * self.lr
                    
                #     model.zero_grad()
                optimizer.step()
                optimizer.zero_grad()

        print (self.loss_func(model(self.x_train), self.y_train))

    def train_model(self): 
        model_ft = models.resnet18(pretrained = True)
        num_ftrs = model_ft.fc.in_features
        model_ft.fc = nn.Linear(num_ftrs, 10)
        
        num_epochs = 25

        criterion = nn.CrossEntropyLoss()
        optimizer_ft = optim.SGD(model_ft.parameters(), lr = self.lr, momentum= .9)
        exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size = 7, gamma = .1)

        train_data_gen = torch.utils.data.DataLoader(self.x_train, batch_size= 64, num_workers=3)
        valid_data_gen = torch.utils.data.DataLoader(self.x_valid, batch_size= 64, num_workers= 3)
        dataloaders = {'train': train_data_gen, 'valid': valid_data_gen}
        
        cnt = 0
        for i in dataloaders['train']: 
            print (i)
            inputs, labels = i
            print (inputs)
            print (labels)
            if cnt == 0: break
        # since = time.time()

        # best_model_wts = model_ft.state_dict()
        # best_acc = 0.0

        # for ep in range(num_epochs): 
        #     print ('Epoch {}/ {}'.format(ep, num_epochs - 1))
        #     print ('-' * 10)

        #     # each ep has a trianing and validation phase
        #     for phase in ['train', 'valid']: 
        #         if phase == 'train': 
        #             exp_lr_scheduler.step()
        #             model_ft.train(True) # set model to training mode
        #         else: 
        #             model_ft.train(False)

        #         running_loss = 0.0
        #         running_corrects = 0

        #         # iterate over data
        #         for data in dataloaders[phase]: 
        #             # get the inputs
        #             inputs, labels = data

        #             # wrap them in Variable
                    
        #             inputs, labels = Variable(inputs), Variable(labels)

        #             # zero the parameter gradients
        #             optimizer_ft.zero_grad()

        #             # forward
        #             outputs = model_ft(inputs)
        #             _, preds = torch.max(outputs.data, 1)

        #             loss = criterion(outputs, labels)

        #             # backward + optimize only if in training phase
        #             if phase == 'train': 
        #                 loss.backward()
        #                 optimizer_ft.step()
                    
        #             # statistics
        #             running_loss += loss.data[0]
        #             running_corrects += torch.sum(preds == labels.data)
                
        #         ep_loss = running_loss/ dataset_sizes[phase]
        #         ep_acc = running_corrects/ dataset_size[phase]

        #         print ('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, ep_loss, ep_acc))

        #         # deep copy the model
        #         if phase == 'valid' and ep_acc > best_acc: 
        #             best_acc = ep_acc
        #             best_model_wts = model_ft.state_dict()

        #     print ()
        # time_elapsed = time.time() - since
        # print ('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))

        # print ('Best val Acc: {:4f}'.format(best_acc))

        # # load best model weights
        # model_ft.load_state_dict(best_model_wts)
        # return model_ft

class Manage_img_n_folder(object):
    def __init__(self, from_path, to_path = None): 
        self.from_path = from_path
        self.to_path = to_path
    
    def set_train_valid(self):
        '''
        shuffle and choose images move to train/ valid folder
        '''
        files = glob.glob(os.path.join(self.from_path, '*/*.jpg'))
        print (f'Total no of images {len(files)}')

        no_of_images = len(files)

        # Create a shuffled index which can be used to crate a validation data set
        shuffle = np.random.permutation(no_of_images)

        # Create a validation directory for holding validation images. 
        if not os.path.isdir(os.path.join(self.from_path, 'train')): 
            os.mkdir(os.path.join(self.from_path, 'train'))
        if not os.path.isdir(os.path.join(self.from_path, 'valid')): 
            os.mkdir(os.path.join(self.from_path, 'valid'))

        # Create directories with label names
        for t in ['train', 'valid']:
            for folder in ['dog/', 'cat/']: 
                if not os.path.isdir(os.path.join(self.from_path, t, folder)): 
                    os.mkdir(os.path.join(self.from_path, t, folder))

        # Copy a small subset of images into the validation folder. 
        for i in shuffle[:20]: 
            folder = files[i].split('/')[-1].split('.')[0]
            image = files[i].split('/')[-1]
            os.rename(files[i], os.path.join(self.from_path, 'valid', folder, image))

        # Copy a small subset of images into the training folder
        for i in shuffle[20:40]:
            folder = files[i].split('/')[-1].split('.')[0]
            image = files[i].split('/')[-1]
            os.rename(files[i], os.path.join(self.from_path, 'train', folder, image))

    def return_back_original(self):
        '''
        move the images in the train/ valid folder back to original folders
        '''
        pass
def add_label_before_img(from_path):
    '''
    to rename all the files in the image
    '''
    files = glob.glob(os.path.join(from_path, '*/*.jpg'))
    
    for f in files: 
        img_name = f.split('/')[-1]
        label = f.split('/')[-2]
        new_img_name = '{lab}.{img_name}'.format(lab = label.lower(), img_name = img_name)
        os.rename(f, os.path.join(from_path, label, new_img_name))
    


if __name__ == '__main__':
    # mnist_train = Mnist_data_train()
    # mnist_train.train_model()
    from_path = './data/kagglecatsanddogs_3367a/PetImages/'
    img_folder = Manage_img_n_folder(from_path)
    img_folder.manage_img_folder()
    

    # # to rename the files with label
    # add_label_before_img(from_path)

    