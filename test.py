import csv
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
    
# sample_1 = np.array([16.869, 25.050, 22.429, 8.456, 20.589, 12.207])
# compare_2 = np.array([11.074, 9.686, 12.064, 9.351, 8.182, 6.642])
# # h0: mean_1 <= mean_2; h1: mean_1 > mean_2
# mean_sp = np.mean(sample_1)
# mean_cp = np.mean(compare_2)

# n = len(sample_1)
# std_sp = np.std(sample_1, ddof = 1)
# std_cp = np.std(compare_2, ddof = 1)

# t_value = abs(mean_sp - mean_cp)/ (((std_cp ** 2 + std_sp ** 2)/ n) ** .5)
# t_p = st.t.cdf(t_value, 5.94)
# # print (mean_cp, mean_sp)
# print (t_value)
# print (t_p)

# # check if two sample sets std same
# sample = np.array([7, -2, 15, 17, 0, -3, 1, 8, 9, -2])
# compare = np.array([-1, 12, -1, -3, 3, -5, 5, 2, -11, -1, -3])

# sample_n = len(sample)
# compare_n = len(compare)
# mean_s = np.mean(sample)
# mean_c = np.mean(compare)
# std_s = np.std(sample, ddof = 1)
# std_c = np.std(compare, ddof = 1)

# F_value = (std_c/ std_s) ** 2
# F_p = st.f.cdf(F_value, compare_n - 1, sample_n - 1)
# print (1 - F_p)

from math import sqrt
 
def confidence(clicks, impressions):
    n = impressions
    if n == 0: return 0
    z = 1.96 #1.96 -> 95% confidence
    phat = float(clicks) / n
    denorm = 1. + (z*z/n)
    enum1 = phat + z*z/(2*n)
    enum2 = z * sqrt(phat*(1-phat)/n + z*z/(4*n*n))
    
    return (enum1-enum2)/denorm, (enum1+enum2)/denorm
 
def wilson(clicks, impressions):
    if impressions == 0:
        return 0
    else:
        return confidence(clicks, impressions)
 
if __name__ == '__main__':
    print (wilson(0,10))
    # print (wilson(2,10))
    # print (wilson(20,100))
    # print (wilson(200,1000))
 
"""    
--------------------
results:
(0.07048879557839793, 0.4518041980521754)
(0.14384999046998084, 0.27112660859398174)
(0.1805388068716823, 0.22099327100894336)
"""
