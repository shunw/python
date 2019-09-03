import numpy as np

weights = np.array([0.1, 0.2, 0])
def neural_network_sin(input, weights):
    '''
    only have single layer of the neural network
    '''
    # pred = input.dot(weights)
    pred = weights.dot(input)
    return pred

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

weights = [[.1, .1, -.3],  # hurt? 
            [.1, .2, .0],   # wins?
            [.0, 1.3, .1]   #sad?
            ]


weights = np.array(weights)
input = np.concatenate((toes.reshape(1, 4), wlrec.reshape(1, 4), nfans.reshape(1, 4)), axis=0)
# weights = weights.reshape(1, 3)
# print (input.shape)

pred = neural_network_sin(input,weights)
# print(pred)

'''
predicting on predictions
'''

ih_wgt = [[.1, .2, -.1],  # hid[0]
            [-.1, .1, .9],  # hid[1]
            [.1, .4, .1]]   # hid [2]

hp_wgt = [[.3, 1.1, -.3],  # hurt?
            [.1, .2, .0],  # win? 
            [.0, 1.3, .1]] # sad?

ih_wgt = np.array(ih_wgt)
hp_wgt = np.array(hp_wgt)
weights = [ih_wgt, hp_wgt]

def neural_network_mult(input, weights):
    '''
    w/ 2 layers of the neural network
    '''
    hid = weights[0].dot(input)
    pred = weights[1].dot(hid)
    return pred

pred = neural_network_mult(input, weights)
# print (pred)


'''
till chapter 5
'''

wgt = ih_wgt[0]
# pred = neural_network_sin(input, wgt)
win_or_lose_binary = np.array([1, 1, 0, 1])

'''
need: 
    error? 
    weight - delta weight * alpha
'''
# for i in range(3):
#     pred = neural_network_sin(input, wgt)
#     error = np.power(pred - win_or_lose_binary, 2)

#     # print (wgt.shape)
#     grad = pred - win_or_lose_binary

#     wgt_delta = input * grad[0]

#     # print (input.dot(pred - win_or_lose_binary))
#     wgt[1:] = wgt[1:] - (wgt_delta[:, 0] *0.01)[1:]
#     print ('-' * 10)
#     print ('Iteration: ' + str(i + 1))
#     print ('Pred: ' + str(pred))
#     print ('Error: ' + str(error))
#     print ('Weight_Delta: ' + str(wgt_delta[:, 0]))
#     print ('Weights: ' + str(wgt))


# till page 90 Gradient descent learning with multiple outputs

mult_weights = np.array([.3, .2, .9])
mult_weights = mult_weights.reshape(1, 3)

wlrec = np.array([0.65, 1.0, 1.0, 0.9])
wlrec = wlrec.reshape(4, 1)

hurt = np.array([.1, .0, .0, .1])
win = np.array([1, 1, 0, 1])
sad = np.array([.1, .0, .1, .2])


true = np.concatenate((hurt.reshape(1, 4), win.reshape(1, 4), sad.reshape(1, 4)), axis=0)
true = np.transpose(true)

pred = np.dot(wlrec, mult_weights)
delta = (pred - true)
error = np.power(pred - true, 2)
grad = np.zeros((delta.shape))
# print (np.multiply(delta[:, 0], wlrec.flatten()))
for i in range(delta.shape[1]):
    grad[:, i] = np.multiply(delta[:, i], wlrec.flatten())
mult_weights -= np.transpose(grad[0, :] * .1)

# page 92 for multiple inputs and multiple outputs

weights = [[.1, .1, -.3],  # hurt? 
            [.1, .2, .0],   # wins?
            [.0, 1.3, .1]   #sad?
            ]


weights = np.array(weights)

hurt = np.array([.1, .0, .0, .1])
win = np.array([1, 1, 0, 1])
sad = np.array([.1, .0, .1, .2])

true = np.concatenate((hurt.reshape(1, 4), win.reshape(1, 4), sad.reshape(1, 4)), axis=0)
true = np.transpose(true)
input = np.transpose(input)

alpha = .01

pred = np.dot(input, np.transpose(weights))
delta = pred - true

error = np.power(delta, 2)

grad = np.zeros((delta.shape))
print (delta.shape)

for i in range(delta.shape[1]):
    grad[:, i] = np.multiply(delta.T[:, i], input[0, :].flatten())

weights -= grad

print ()
print ('----- delta -----')
print (delta)
print ()
print ('----- error -----')
print (error)
print ()
print ('----- grad -----')
print (grad)
print ()
print ('----- updated weight -----')
print (weights)
# page 92 
'''
notice: 
1. if weight is [w1, w2, w3], w1 does not change, and w2 and w3 move according to the gradient decent. what would happen. (Page 89)
    
    1. if you converged (reached error == 0) with w2 and w3, and then tried to train w1. w1 won't move because error == 0, which means weight_delta == 0
    
        -> This reveals a potentially damaging property of neural networks: w1 maybe a powerful input with lots of predictive power, but if the network accidentally figures out how to predict a accurately on the training data without it, then it will never learn to incorporate into its prediction. 
    
    2. Also notice how w1 finds the bottom of the bowl. Instead of the black dot moving, the curve seems to move to the left. What does this mean? The black dot can move horzontally only if the weights is updated. Because the weight for w1 is frozen for this experiment, the dot must stay fixed.But error clearly goes to 0. 

    3. This tells you what the graphs really are(three graph, x-axis is weight, y-axis is error). In truth, these are 2D slices of a four-dimensional shape. Three of the dimensions are the weight values, and the fourth dimention is the error. This shape is called the error plane, and, its curvature is determined by the training data. 

    4. error is determined by the training data. Any network can have any weight value, but the value of error given any particular weight configuration is 100% determined by data, You've already seen how the steepness of the U shape is affected by the input data(on several occasions). What you are really trying to do with the neural networks is find the lowest point on this big error plance, where the lowest point refers to the lowest error. 
'''
