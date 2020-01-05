import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def exp_pdf(theta_1, x): 
    '''
    theta_1 = - 1/theta
    '''
    try: 
        m, n = x.shape
    except: 
        m = x.shape[0]
        n = 1
        x = x.reshape(m, n)
    # print (x.shape)
    y = np.zeros((m, n))
    for i in range(m): 
        for j in range(n): 
            if x[i, j] > 0: 
                y[i, j] = 1 - math.exp(x[i, j] * theta_1)
            else: 
                y[i, j] = 0
    return y

def exp_pdf_np(theta_1, x): 
    '''
    x is array
    theta_1 = - 1/theta
    '''
    try: 
        m, n = x.shape
    except: 
        m = x.shape[0]
        n = 1
        x = x.reshape(m, n)
    # print (x.shape)
    y = np.zeros((m, n))
    y[x > 0] = 1 - np.exp(x[x>0] * theta_1)
    return y

def de_exp(theta_1, x): 
    '''
    x is array
    theta_1 = - 1/ theta
    '''
    try: 
        m, n = x.shape
    except: 
        m = x.shape[0]
        n = 1
        x = x.reshape(m, n)
    # print (x.shape)
    y = np.zeros((m, n))
    
    y[x > 0] = -1 * theta_1 * np.exp(theta_1 * x[x > 0])
    return y
if __name__ == '__main__': 
    # theta_1 = -.4 
    # x_array = np.linspace(0.1, 10, 20)
    # # y_array = exp_pdf(theta_1, x_array)
    # # print (y_array)

    # y_array_np = exp_pdf_np(theta_1, x_array)
    
    # plt.scatter(x = x_array, y = y_array_np, color = 'navy')
    # plt.plot(x_array, y_array_np)
    
    
    # y_de_array_np = de_exp(theta_1, x_array)
    # plt.scatter(x = x_array, y = y_de_array_np, color = 'red')
    # plt.plot(x_array, y_de_array_np)
    # plt.show()
    res = st.chi2.ppf(.1, 14)/14
    res = st.chi2.ppf(.9, 14)/14
    print (res)