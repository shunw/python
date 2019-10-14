import csv
import matplotlib.pyplot as plt
import scipy.stats as st
    

def mean_2_tail(h0, std, sample_n, sample_mean, alpha = 0.05): 
    # this is to check mean with two tail
    # suppose this is normal distribution and according to the given number get the lower and upper data
    alpha_2 = 1 - alpha/2
    alpha_1 = alpha/2
    z_score_upper = st.norm.ppf(alpha_2)
    z_score_lower = st.norm.ppf(alpha_1)
    
    sample_mean_norm = (sample_mean - h0) / (std / (sample_n ** .5))
    
    z_score_p = st.norm.cdf(sample_mean_norm)
    p_value = 2 * (1-z_score_p)
    
    if (sample_mean_norm < z_score_lower) or (sample_mean_norm > z_score_upper): 
        print ('reject')
    else: 
        print ('accept')
    
    print ('p_value is: {:.3f}'.format(p_value))



if __name__ == '__main__': 
    # # question 1
    # h0 = 255
    # std = 5
    # sample_n = 40
    # sample_mean = 255.8
    # alpha = .05

    # mean_2_tail(h0, std, sample_n, sample_mean)

    parts_data = [1.26, 1.19, 1.31, .97, 1.81, 1.13, .96, 1.06, 1, .94, .98, 1.1, 1.12, 1.03, 1.16, 1.12, 1.12, 0.95, 1.02, 1.13, 1.23, 0.74, 1.5, 0.5, 0.59, .99, 1.45, 1.24, 1.01, 2.03, 1.98, 1.97, 0.91, 1.22, 1.06, 1.11, 1.54, 1.08, 1.1, 1.64, 1.7, 2.37, 1.38, 1.6, 1.26, 1.17, 1.12, 1.23, .82, .86]
    print (len(parts_data))
    
