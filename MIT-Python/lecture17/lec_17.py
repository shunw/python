import numpy as np
import matplotlib.pyplot as plt

def get_data(filename):
	handle = open(filename)
	count = 0
	distance = list()
	weight = list()
	for line in handle:
		if count == 0: 
			count += 1
			continue
			
		m, n = (line.strip()).split(' ')
		distance.append(m)
		weight.append(n)
	return (distance, weight)

def plot_spring(x_data_list, y_data_list):
	x_data_a = np.array(x_data_list)
	y_data_a = np.array(y_data_list)
	plt.plot(y_data_a, x_data_a, 'bo')
	plt.show()




if __name__ == '__main__':
	dis, weight= get_data("springData.txt")
	# plot_spring(dis, weight)
	m, b = np.polyfit(np.arange(dis), np.arange(weight), 1)
	print m + ', ' + b

	# pause in the polyfit thing