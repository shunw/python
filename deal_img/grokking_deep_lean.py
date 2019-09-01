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
pred = neural_network_sin(input, wgt)
win_or_lose_binary = np.array([1, 1, 0, 1])

'''
need: 
    error? 
    weight - delta weight * alpha
'''
error = np.power(pred - win_or_lose_binary, 2)

# print (wgt.shape)
print (pred - win_or_lose_binary)
# print (wgt)
# print (input.dot(pred - win_or_lose_binary))
wgt -= input.dot(pred - win_or_lose_binary)
# print (wgt)
