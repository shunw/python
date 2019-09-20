import numpy as np
import gzip
import pickle
import os.path
import os
import sys
np.random.seed(1)

'''
chapter 6 --- street light vs walk&stop
'''

def relu(x): 
    return ( x > 0 ) * x

def relu2deriv(output): 
    return output >= 0

def tanh(x): 
    return np.tanh(x)

def tanh2deriv(output): 
    return 1 - np.power(output, 2)

def softmax(x): 
    temp = np.exp(x)
    return temp / np.sum(temp, axis = 1, keepdims = True)

def get_image_section(layer, row_from, row_to, col_from, col_to): 
    sub_section = layer[:, row_from : row_to, col_from : col_to]
    # print (sub_section.shape)
    return sub_section.reshape(-1, 1, row_to - row_from, col_to - col_from)

def conv2hotlabel(labels):
    '''
    this is to convert to one-hot-label. for instance, if labels have number from 0-9, then the one-hot-label has 10 features. 
    '''
    col_feat = len(set(labels))
    one_hot_label = np.zeros((len(labels), col_feat))
    for i, j in enumerate(labels): 
        one_hot_label[i, j] = 1
    return one_hot_label
    

class book_sample(object): 
    def __init__(self, streetlights, walks_vs_stop, alpha, hidden_size, weights_0_1, weights_1_2, iterations, dropout_mask): 
        self.images = streetlights
        self.labels = walks_vs_stop
        self.alpha = alpha
        self.hidden_size = hidden_size
        self.weights_0_1 = weights_0_1
        self.weights_1_2 = weights_1_2
        self.iterations = iterations
        self.dropout_mask = dropout_mask
    
    def process_streetlight(self):

        weights_0_1 = self.weights_0_1.copy()
        weights_1_2 = self.weights_1_2.copy()

        for iteration in range(60): 
            layer_2_error = 0
            for i in range(len(self.streetlights)): 
                layer_0 = self.streetlights[i: i+1]
                
                # print ('book_weights: {}'.format(weights_0_1))
                # print ('book_layer1-mid: {}'.format(np.dot(layer_0, weights_0_1)))
                
                layer_1 = relu(np.dot(layer_0, weights_0_1))
                layer_2 = np.dot(layer_1, weights_1_2)

                layer_2_error += np.sum((layer_2 - self.walk_vs_stop[i : i+1]) ** 2)

                layer_2_delta = (layer_2 - self.walk_vs_stop[i : i+ 1])
                layer_1_delta = layer_2_delta.dot(weights_1_2.T) * relu2deriv(layer_1)
                
                
                
                weights_1_2 -= self.alpha * layer_1.T.dot(layer_2_delta)
                weights_0_1 -= self.alpha * layer_0.T.dot(layer_1_delta)
                # print ('book_layer1: {}'.format(layer_1))
                # print ('book_layer2: {}'.format(layer_2))
                print ('book_grad12: {}'.format(self.alpha * layer_1.T.dot(layer_2_delta)))
                print ('book_grad01: {}'.format(self.alpha * layer_0.T.dot(layer_1_delta)))

                break
            
            if (iteration % 10 == 9): 
                print ('Error: {}'.format(layer_2_error))

            break
    
    def process_mnist(self): 
        # iterations = 350
        for j in range(self.iterations): 
            error, correct_cnt = (0.0, 0)
            
            for i in range(len(self.images)): 
                layer_0 = self.images[i: i+1]
                layer_1 = relu(np.dot(layer_0, self.weights_0_1))
                layer_2 = np.dot(layer_1, self.weights_1_2)
                error += np.sum((self.labels[i: i+1] - layer_2) ** 2)
                correct_cnt += int(np.argmax(layer_2) == np.argmax(self.labels[i:i + 1]))

                layer_2_delta = (self.labels[i: i + 1] - layer_2)
                layer_1_delta = layer_2_delta.dot(self.weights_1_2.T) * relu2deriv(layer_1)

                self.weights_1_2 += self.alpha * layer_1.T.dot(layer_2_delta)
                self.weights_0_1 += self.alpha * layer_0.T.dot(layer_1_delta)

                # print ('book_layer1: {}'.format(layer_1))
                # print ('book_layer2: {}'.format(layer_2))
                print ('book_grad12: {}'.format(np.transpose(self.alpha * layer_1.T.dot(layer_2_delta))))

                break

            if (j == 349 or j % 10 == 9): 
                print ('I == {}'.format(j))
                print (' Error: {err:.3f} \n Correct: {corr}'.format(err = error / float(len(self.images)), corr = correct_cnt / float(len(self.images))))
            
            break

    def process_mnist_batch(self): 
        
        batch_size = 100
        alpha, iterations = (0.001, 300)
        pixels_per_image, num_labels, hidden_size = (784, 10, 100)

        weights_0_1 = self.weights_0_1.copy()
        weights_1_2 = self.weights_1_2.copy()

        for j in range(self.iterations):
            error, correct_cnt = (0.0, 0)
            for i in range(int(len(self.images) / batch_size)):
                
                batch_start, batch_end = ((i * batch_size),((i+1)*batch_size))

                layer_0 = self.images[batch_start:batch_end]
                layer_1 = relu(np.dot(layer_0,weights_0_1))
                
                # dropout_mask = np.random.randint(2,size=layer_1.shape)
                layer_1 *= self.dropout_mask * 2
                
                layer_2 = np.dot(layer_1,weights_1_2)

                error += np.sum((self.labels[batch_start:batch_end] - layer_2) ** 2)
                for k in range(batch_size):
                    correct_cnt += int(np.argmax(layer_2[k:k+1]) == np.argmax(self.labels[batch_start+k:batch_start+k+1]))

                    layer_2_delta = (self.labels[batch_start:batch_end]-layer_2)/batch_size
                    layer_1_delta = layer_2_delta.dot(weights_1_2.T)* relu2deriv(layer_1)
                    layer_1_delta *= self.dropout_mask
                    # print ('layer_2: {}'.format(np.argmax(layer_2, axis = 1)))
                    # print ('bk layer_1: {}'.format(layer_1))
                    # print ('error: {:.3f}'.format(error))
                    # print ('grad_1_2 min: {:.3f}; grad_1_2 max: {:.3f}'.format(layer_1.T.dot(layer_2_delta).min(), layer_1.T.dot(layer_2_delta).max()))
                    
                    # print ('bk grad_0_1: {}'.format(layer_0.T.dot(layer_1_delta)))
                    # print ('bk delta: {}'.format(layer_1_delta))
                    weights_1_2 += self.alpha * layer_1.T.dot(layer_2_delta)
                    weights_0_1 += self.alpha * layer_0.T.dot(layer_1_delta)
                    break
                break
                    
            if(j % 10 == 0):
                test_error = 0.0
                test_correct_cnt = 0

                # for i in range(len(test_images)):
                #     layer_0 = test_images[i:i+1]
                #     layer_1 = relu(np.dot(layer_0,weights_0_1))
                #     layer_2 = np.dot(layer_1, weights_1_2)

                #     test_error += np.sum((test_labels[i:i+1] - layer_2) ** 2)
                #     test_correct_cnt += int(np.argmax(layer_2) == np.argmax(test_labels[i:i+1]))

                sys.stdout.write("\n" + \
                                "bk I:" + str(j) + \
                                # " Test-Err:" + str(test_error/ float(len(test_images)))[0:5] +\
                                # " Test-Acc:" + str(test_correct_cnt/ float(len(test_images)))+\
                                " Train-Err:" + str(error/ float(len(self.images)))[0:5] +\
                                " Train-Acc:" + str(correct_cnt/ float(len(self.images))))

            break
            if j > 20:
                break

    
class nn_street_light(object): 
    '''
    only for one layer of hidden layer. totally three layer, the other two is one input layer, and the other is output layer. 
    '''
    def __init__(self, input, target, hidden_size, alpha, iterations, weights_0_1, weights_1_2, error_method = 'sqr_error', test_data = None, test_labels = None, batch_size = 1, dropout_mask = None, kernel_cols = None, kernel_rows = None, num_kernels = None):
        self.input = input
        self.target = target
        self.hidden_size = hidden_size
        self.alpha = alpha
        self.error_method = error_method
        self.iterations = iterations
        self.batch_size = batch_size

        self.layer1_feat = self.input.shape[1]
        self.layer2_feat = self.hidden_size
        self.layer3_feat = self.target.shape[1]

        self.weights_0_1 = weights_0_1 # 40 * 784
        self.weights_1_2 = weights_1_2 # 10 * 40

        self.weights = None # this is for the two layers nn

        self.test_data = test_data
        self.test_labels = test_labels

        self.dropout_mask = dropout_mask
        
        self.kernel_cols = kernel_cols
        self.kernel_rows = kernel_rows
        self.num_kernels = num_kernels

    def nn_forward_back_pp_3(self): 
        '''
        stochastic gradient descent: 
            there are two loops: the outer is the iteration loop, the inner is the total data loop
        
        this is for just three layers

        mini-batched stochastic gradient descent, need to assign the batch size
        '''
        
        for j in range(self.iterations): 
            layer2_error = 0.0
            correct_cnt = 0

            for r in range(int(self.input.shape[0]/ self.batch_size)):
                
                batch_start = r * self.batch_size
                batch_end = (r + 1) * self.batch_size
                
                pre_layer1 = tanh(np.dot(self.input[batch_start : batch_end, :], np.transpose(self.weights_0_1))) # [1, 784] * [784, 40] => [1, 40]
                
                
                self.dropout_mask = np.random.randint(2, size = pre_layer1.shape)

                

                if self.dropout_mask.any():
                    pre_layer1 *= self.dropout_mask * 2
                pre_layer2 = softmax(np.dot(pre_layer1, np.transpose(self.weights_1_2))) # [1, 40] * [40, 10] => [1, 10]
                
                layer2_error += np.sum(np.power(pre_layer2 - self.target[batch_start : batch_end], 2))
                
                correct_cnt += np.sum(np.argmax(pre_layer2, axis = 1) == np.argmax(self.target[batch_start : batch_end], axis = 1))

                for k in range(self.batch_size): 
                    delta = (pre_layer2 - self.target[batch_start : batch_end])/ (self.batch_size * pre_layer2.shape[0]) # [1, 10]

                    # get the grad with multiple output
                    # print (delta.shape)
                
                ##
                # DIFFERENT PLACE in chap 8 and chap 9
                ##
                grad_1_2 = np.dot(np.transpose(delta), pre_layer1.reshape(self.batch_size, self.layer2_feat)) # [10, 1] * [1, 40] => [10, 40]
                
                # print ('wendy layer_1: {}'.format(pre_layer1))
                # print ('wendy weight12: {}'.format(self.weights_1_2))

                # print ('layer2_output: {}'.format(np.argmax(pre_layer2, axis = 1)))
                # print ('error: {:.3f}'.format(layer2_error))
                # print ('grad_1_2 min: {:.3f}; grad_1_2 max: {:.3f}'.format(grad_1_2.min(), grad_1_2.max()))
                # print ('wendy grad_1_2: {}'.format(grad_1_2))
                

                layer_1_delta = np.multiply(np.dot(delta.reshape(self.batch_size, self.layer3_feat), self.weights_1_2), tanh2deriv(pre_layer1))
                
                if self.dropout_mask.any():
                    layer_1_delta *= self.dropout_mask

                # print ('wendy delta: {}'.format(layer_1_delta))
                
                grad_0_1 = np.dot(np.transpose(self.input[batch_start : batch_end, :]), layer_1_delta)
                # print ('wendy grad_0_1: {}'.format(grad_0_1))
                self.weights_1_2 -= self.alpha * grad_1_2
                self.weights_0_1 -= self.alpha * grad_0_1.T
                
                # break
                
                
                weights_ls = list([self.weights_0_1.copy(), self.weights_1_2.copy()])

                # break

            if (j % 10 == 0 and len(self.test_data)):  # <- stop here
                test_error = 0.0
                test_correct_cnt = 0

                val_part = validation_nn(self.test_data, self.test_labels, weights_ls)
                err_cnt_ls = val_part.validate_test_data()
                # print (err_cnt_ls)

                print ('wendy I == {}'.format(j))
                print (' Test-Correct: {corr:.3f}; Train-Correct: {tcorr:.3f}'.format(corr = err_cnt_ls[1],  tcorr = correct_cnt / (batch_end + 1)))

                # print (' Train-Error: {terr:.3f}; Train-Correct: {tcorr:.3f}'.format(terr = layer2_error / (len(self.input)), tcorr = correct_cnt / (len(self.input))))

                
            # # save the weights for the validation check
            # np.save('mnist_weights_0_1.npy', self.weights_0_1) 
            # np.save('mnist_weights_1_2.npy', self.weights_1_2) 
            
            # break
            # if j > 20:
            #     break

    def nn_forward_back_pp(self): 
        '''
        stochastic gradient descent: 
            there are two loops: the outer is the iteration loop, the inner is the total data loop
        
        this is for just two layers
        '''
        self.grad = np.zeros((self.weights.shape))
        if self.error_method == 'sqr_error': 
            for iteration in range(40): 
                error_for_all_lights = 0
                for r in range(self.input.shape[0]): 
                    pred = np.dot(self.input[r, :], np.transpose(self.weights))
                    error = np.power(pred - self.target[r], 2) 
                    delta = pred-self.target[r]
                    self.grad = delta * self.input[r, :] * self.alpha
                    self.weights -= self.grad
                    error_for_all_lights += error
                print ('Error: {all_lights}'.format(all_lights = error_for_all_lights))
            print (self.weights)

    def nn_w_kernel(self):      
        '''
        this is just for mnist dataset due to some shape parameter is hard coding. 
        '''     
        input_rows = self.input.shape[1] ** .5
        input_cols = self.input.shape[1] ** .5
        hidden_size = ((input_rows - self.kernel_rows) * (input_cols - self.kernel_cols)) * self.num_kernels

        kernels = .02 * np.random.random((self.kernel_rows * self.kernel_cols, self.num_kernels)) - .01
        weights_1_2 = .2 * np.random.random((hidden_size, num_labels)) - .1

        for j in range((self.iterations)): 
            correct_cnt = 0
            for i in range((int(len(self.input) / self.batch_size))):
                batch_start = i * self.batch_size
                batch_end = (i + 1) * self.batch_size
        
                self.layer_0 = self.input[batch_start: batch_end]
                
                self.layer_0 = self.layer_0.reshape(self.layer_0.shape[0], input_rows, input_cols)
        
        sects = list()
        for row_start in range(self.layer_0.shape[1] - kernel_rows + 1): 
            for col_start in range(self.layer_0.shape[2] - self.kernel_cols + 1): 
                sect = get_image_section(self.layer_0, row_start, row_start + kernel_rows, col_start, col_start + self.kernel_cols)
                # print (sect.shape)
                sects.append(sect)

            #     break
            # break
        expanded_input = np.concatenate(sects, axis = 1)
        es = expanded_input.shape
        flattened_input = expanded_input.reshape(es[0] * es[1], -1)
        print (flattened_input.shape)

        kernel_output = np.dot(flattened_input, kernels)
        print (kernel_output.shape)

    

    def final_run(self): 
        # self.forword_pp()
        # self.cost_cal()
        self.nn_w_kernel()
        
class validation_nn(): 
    '''
    this is to validate with test data and test label. 
    '''
    def __init__(self, test_data, test_label, weights, weights_num = 2): 
        self.test_data = test_data
        self.test_labels = test_label
        if weights_num == 2: 
            self.weights_0_1 = weights[0] # 40, 784
            self.weights_1_2 = weights[1] # 10, 40

    def validate_test_data(self): 
        correct_cnt = 0
        layer_1 = tanh(np.dot(self.test_data, np.transpose(self.weights_0_1))) # m * 40
        layer_2 = np.dot(layer_1, np.transpose(self.weights_1_2)) # m * 10
        test_error = np.sum(np.power(layer_2 - self.test_labels, 2))

        correct_cnt = np.sum(np.argmax(layer_2, axis = 1) == np.argmax(self.test_labels, axis = 1))
        # for i in range(len(layer_2)):
            
        #     correct_cnt += int(np.argmax(layer_2[i]) == np.argmax(self.test_labels[i]))
            
        return [test_error/self.test_labels.shape[0], correct_cnt/self.test_labels.shape[0]]

    def final_run(self): 
        self.validate_test_data()



if __name__ == '__main__': 
    streetlights = np.array([[1, 0, 1], 
                            [0, 1, 1], 
                            [0, 0, 1], 
                            [1, 1, 1] ])
                            # , 
                            # [0, 1, 1], 
                            # [1, 0, 1]])

    walk_vs_stop = np.array([[1, 1, 0, 0]]).T

    # walk_vs_stop = np.array([[0], 
    #                         [1], 
    #                         [0], 
    #                         [1], 
    #                         [1], 
    #                         [0]])

    # weights = np.array([.5, .48, -.7])

    # mnist_data_path = '/Users/zhang/github/standford_ML/pytorch/data/mnist/mnist.pkl.gz'
    mnist_data_path = './data/mnist/mnist.pkl.gz'

    with gzip.open(mnist_data_path, "rb") as f:
        ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")

    alpha = 2
    iterations = 300
    hidden_size = 100
    pixels_per_image = 784
    label_feat = 10
    pick_sample = 1000
    batch_size = 128

    kernel_rows = 3
    kernel_cols = 3
    num_kernels = 16

    images, labels = (x_train[:pick_sample], y_train[:pick_sample]) # .reshape(pick_sample, pixels_per_image)
    test_images, test_labels = (x_valid, y_valid)
    test_labels_one_hot = conv2hotlabel(test_labels).copy()
    
    labels_one_hot = conv2hotlabel(labels).copy()

    # align the random part    
    weights_0_1 = .02 * np.random.random((images.shape[1], hidden_size)) - .01
    weights_1_2 = .2 * np.random.random((hidden_size, labels_one_hot.shape[1])) - .1

    dropout_mask = np.random.randint(2,size=(batch_size, hidden_size))
    #============= WENDY PART ========================================
        
    print ()
    print ('-=' * 10)
    nn_street_light = nn_street_light(input = images, target = labels_one_hot, hidden_size = hidden_size, alpha = alpha, iterations = iterations, weights_0_1 = np.transpose(weights_0_1.copy()), weights_1_2 = np.transpose(weights_1_2.copy()), test_data = test_images, test_labels = test_labels_one_hot, batch_size = batch_size, kernel_cols = kernel_cols, kernel_rows = kernel_rows, num_kernels = num_kernels)
    nn_street_light.final_run()
    
    # #============= VALIDATION PART ========================================
    # weights_ls = list()
    # weight_name_ls = ['mnist_weights_0_1.npy', 'mnist_weights_1_2.npy']
    # for n in weight_name_ls: 
    #     weights_ls.append(np.load(n))

    # validate_test = validation_nn(test_data = test_images, test_label = test_labels_one_hot, weights = weights_ls)
    # validate_test.final_run()

    # # ============= BOOK SAMPLE PART ========================================
    # print ()
    # print ('-=' * 10)
    
    # book_sample = book_sample(images, labels_one_hot, alpha, hidden_size, weights_0_1 = weights_0_1.copy(), weights_1_2 = weights_1_2.copy(), iterations = iterations, dropout_mask = dropout_mask.copy())
    # book_sample.process_mnist_batch()

    # # ============= COMPARE THE SOME RANDOM PART ========================================
    # print (sum(sum(book_sample.dropout_mask == nn_street_light.dropout_mask)) == dropout_mask.shape[0] * dropout_mask.shape[1])

    # print (sum(sum(book_sample.weights_1_2 == nn_street_light.weights_1_2.T)) == book_sample.weights_1_2.shape[0] * book_sample.weights_1_2.shape[1])
    


    # till page 183 for the first two layer nn
        # book samples' label is to use the one_hot_labels, which has 10 column represent 10 number position. 

        # would you please try to use the neural number as the label.

'''
notice: 

1. if weight is [w1, w2, w3], w1 does not change, and w2 and w3 move according to the gradient decent. what would happen. (Page 89)
    
    1. if you converged (reached error == 0) with w2 and w3, and then tried to train w1. w1 won't move because error == 0, which means weight_delta == 0
    
        -> This reveals a potentially damaging property of neural networks: w1 maybe a powerful input with lots of predictive power, but if the network accidentally figures out how to predict a accurately on the training data without it, then it will never learn to incorporate into its prediction. 
    
    2. Also notice how w1 finds the bottom of the bowl. Instead of the black dot moving, the curve seems to move to the left. What does this mean? The black dot can move horzontally only if the weights is updated. Because the weight for w1 is frozen for this experiment, the dot must stay fixed.But error clearly goes to 0. 

    3. This tells you what the graphs really are(three graph, x-axis is weight, y-axis is error). In truth, these are 2D slices of a four-dimensional shape. Three of the dimensions are the weight values, and the fourth dimention is the error. This shape is called the error plane, and, its curvature is determined by the training data. 

    4. error is determined by the training data. Any network can have any weight value, but the value of error given any particular weight configuration is 100% determined by data, You've already seen how the steepness of the U shape is affected by the input data(on several occasions). What you are really trying to do with the neural networks is find the lowest point on this big error plance, where the lowest point refers to the lowest error. 

2. What is the relationship between input and weight? 

    1. each output node has a weight coming from every pixel. 

    2. if the weight is high, it means the model believes there is a high degree of correlation between that pixel and the output image. 

    3. Performing dot products between two identical vectors tends to result in higher scores. (if input and weights are identical/ similar, this would have a higher score. )

    4. can check the middle image for check when doing the deep learning. 

3. gradient descent: 
    
    1. stochastic gradient descent: learning one example at a time is a variant on gradient descent. 

    2. full gradient descent updates weights one dataset at a time. 

    3. batch gradient descent updates weights after n examples

4. in the process of gradient descent, each training example asserts either up pressure or down pressure on the weights. Where does the pressure come from? Why is it different for different weights? (page 111)

    1. up and down pressure comes from the data

        1. each node is individually trying to correctly predict the output given the input. For the most part, each node ignores all the other nodes when attempting to do so. The only cross communication occurs in that all three weights must share the same error measure. The weight update is nothing more than taking this shared error measure and multiplying it by each respective input. 

5. deep learning weakness/ edge case

    1. overfitting: error is shared among all  the weights. if a particular configuration of weights accidentallly creates perfect correlation between the prediction and the output dataset (such that error == 0), without giving the heavist weight to the best inputs, the neural network will stop learning. 

    2. conflicting pressure: regularization is advantageous because if a weight has equal pressure upward and donward, it isn't good for anything. 
        
6. initial weights for different activation function 
    
    1. relu: weights between -.1 and .1

    2. tanh: weights between -.01 and .01

7. error calculation for different activation function 

    1. softmax: cross entropy

??? QUESTION???

1. why the mini-batch loop is different in the page 175 and the page 159

'''
