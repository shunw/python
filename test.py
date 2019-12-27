import csv
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import pandas as pd

from doepy import build, read_write
    
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


def trial_exp_inter(n, sum_xi, alpha = .05): 
    # to check how to get the exponential interval
    chi_sqrt_low = st.chi2.ppf(q = alpha/2, df = 2 * n )
    chi_sqrt_high = st.chi2.ppf(q = 1 - alpha/2, df = 2 * n )
    print (chi_sqrt_low / (2 * sum_xi), chi_sqrt_high / (2 * sum_xi))
    print ( (2 * sum_xi) / chi_sqrt_low, (2 * sum_xi) / chi_sqrt_high)

# def _move_nan_in_list(data_list):
    
def trial_doe(): 
    df = pd.read_csv('ranges.csv')
    dict_ready = df.to_dict('list')
    for k, v in dict_ready.items():
        dict_ready[k] = [x for x in v if str(x) != 'nan'].copy()
    # print (dict_ready)
    read_write.write_csv(
    build.frac_fact_res(dict_ready),
    filename='DOE_table.csv'
    )    

if __name__ == '__main__':
    # print (wilson(0,10))
    # print (wilson(2,10))
    # print (wilson(20,100))
    # print (wilson(200,1000))
    # z_value = -.7 * (2**.5) / .4
    # print (z_value)
    # z_value_p = st.norm.cdf(z_value)
    # print (z_value_p/2)

    # p1 = .27
    # p2 = .35
    # p = .31
    # z_value = (p1 - p2)/ ((p *(1-p) * 2/200) ** .5)
    # z_value_p = st.norm.cdf(z_value)
    
    # p1 = 33/300
    # p2 = 84/300
    # d = .10
    # divid = ((p1 * (1-p1) / 300 + p2 * (1-p2) / 300 )**.5)
    # z_value = (p2 - p1 - d)/ divid
    
    # z_value_p = st.norm.cdf(z_value)
    # z_interval = st.norm.ppf(.95)
    # z_interval_lower = st.norm.ppf(.05)
    
    # upper = z_interval * divid
    # lower = z_interval * -1 *divid
    # d_upper = p2 - p1 - upper
    # d_lower = p2 - p1 - lower
    # # print (d_lower, d_upper)

    # a = (1.1 - 0)**2 * .05
    # b = (1.1 - 1)**2 * .8 
    # c = (1.1 - 2)**2 * .15
    # print (a + b + c)

    # n = 7689
    # sum_xi = 6151
    # trial_exp_inter(n, sum_xi)
    # https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_the_Exponential_Lifetime_Mean.pdf

    # https://people.missouristate.edu/songfengzheng/Teaching/MTH541/Lecture%20notes/CI.pdf

    
    trial_doe()
    # a = build.frac_fact_res(
    # {'Pressure':[40,55,70],
    # 'Temperature':[290, 320, 350],
    # 'Flow rate':[0.2,0.4],
    # 'Time':[5,8]}
    # )
    # print (a)
    
    

"""    
--------------------
results:
(0.07048879557839793, 0.4518041980521754)
(0.14384999046998084, 0.27112660859398174)
(0.1805388068716823, 0.22099327100894336)
"""
