import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MinuteLocator, SecondLocator
import numpy as np
from StringIO import StringIO
import datetime as dt
import csv



#Plot function
def interlines(y, xstart, xstop, color='b'):
    """Plot timelines at y from xstart to xstop with given color."""   
    plt.hlines(y, xstart, xstop, color, lw=4)
    plt.vlines(xstart, y+0.03, y-0.03, color, lw=2)
    plt.vlines(xstop, y+0.03, y-0.03, color, lw=2)



if __name__ == '__main__':
	### get from csv
	f_name = 'test.csv'
	raw = csv.reader(open(f_name, 'r'))
	
	cat_1 = 'xxx'
	start_75 = 'yyy'
	end_75 = 'zzz'
	data = np.genfromtxt(f_name, delimiter=',', dtype=None, names=True)
	cat_1, start_75_data, end_75_data = data[cat_1], data[start_75], data[end_75]
	
	for i in data[end_75]:
		if i =='N/A':
			i = -1

	print type(data[end_75])
	# #Get unique captions and there indices and the inverse mapping
	# pro_cap, unique_idx, pro_inv = np.unique(cat_1, 1, 1)

	# #Build y values from the number of unique captions.
	# y = (pro_inv + 1) / float(len(cat_1) + 1)

	# interlines(y, start_75_data, end_75_data, 'r')

	# #To adjust the xlimits a timedelta is needed.
	# delta = (end_75_data.max() - start_75_data.min())/10
	# plt.ylim(0,1)
	# plt.xlim(start_75_data.min()-delta, end_75_data.max()+delta)
	# # plt.xlim(start.min()-delta, stop.max()+delta)
	# plt.xlabel('Page Number')
	# plt.show()