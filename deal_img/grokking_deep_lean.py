import numpy as np

weights = np.array([0.1, 0.2, 0])
def neural_network(input, weights):
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

pred = neural_network(input,weights)
print(pred)

'''
till predicting on predictions
'''