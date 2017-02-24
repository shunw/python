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
		distance.append(float(m))
		weight.append(float(n))
	return (distance, weight)

def plot_spring(x_data_list, y_data_list):
	x_data_a = np.array(x_data_list)
	y_data_a = np.array(y_data_list)
	plt.plot(y_data_a, x_data_a, 'bo')
	plt.show()

def plot_spr_n_fit(x_data_list, y_data_list, slope, inter):
	fit_data = [i*slope+inter for i in x_data_list]
	x_data_a = np.array(x_data_list)
	y_data_a = np.array(y_data_list)
	fit_data_a = np.array(fit_data)
	plt.plot(y_data_a, x_data_a, 'bo')
	plt.plot(fit_data_a, x_data_a)
	plt.show()



if __name__ == '__main__':
	dis, weight= get_data("springData.txt")
	# print type(np.array(weight))
	m, b = np.polyfit(np.array(dis), np.array(weight), 1)
	plot_spr_n_fit(dis, weight, m, b)

	# stuck in the polyfit thing