import numpy as np


'''
chapter 6 --- street light vs walk&stop
'''
class nn_street_light(object): 
    def __init__(self, input, target, weights, alpha, error_method = 'sqr_error'):
        self.input = input
        self.target = target
        self.weights = weights
        self.alpha = alpha
        self.error_method = error_method
    
    def forword_pp(self): 
        self.pred = np.dot(self.input, np.transpose(self.weights))
            
    def cost_cal(self): 
        if self.error_method == 'sqr_error': 
            self.error = np.power(self.target - self.pred, 2)
        
        self.delta = self.target - self.pred

    def nn_forward_back_pp(self): 
        '''
        stochastic gradient descent: 
            there are two loops: the outer is the iteration loop, the inner is the total data loop
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
            
    def final_run(self): 
        # self.forword_pp()
        # self.cost_cal()
        self.nn_forward_back_pp()

if __name__ == '__main__': 
    streetlights = np.array([[1, 0, 1], 
                            [0, 1, 1], 
                            [0, 0, 1], 
                            [1, 1, 1], 
                            [0, 1, 1], 
                            [1, 0, 1]])

    walk_vs_stop = np.array([[0], 
                            [1], 
                            [0], 
                            [1], 
                            [1], 
                            [0]])

    weights = np.array([.5, .48, -.7])
    alpha = .1
    nn_street_light = nn_street_light(input = streetlights, target = walk_vs_stop, weights = weights, alpha = alpha)
    nn_street_light.final_run()

# till page 120

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
        
        
'''
