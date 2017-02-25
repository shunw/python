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
		weight.append(float(n)*9.81)
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
	plt.plot(x_data_a, y_data_a, 'bo', label = 'Measured Displacements')
	plt.plot(x_data_a, fit_data_a, label = 'Linear Fit k = ' + str(1/slope))
	plt.title('Measured Distance of Spring')
	plt.xlabel('|Force (Newtons)|')
	plt.ylabel('Distance (Meters)')
	plt.legend(loc = 'best')
	plt.show()

def plot_spr_fit_poly(filename):
	y_val, x_val = get_data(filename)
	z = np.polyfit(x_val, y_val, 3)
	p = np.poly1d(z)
	fit_val = p(x_val)

	plt.plot(x_val, y_val, 'bo', label = 'Measured Displacements')
	plt.plot(x_val, fit_val, label = 'Poly Fit')
	plt.title('Measured Distance of Spring')
	plt.xlabel('|Force (Newtons)|')
	plt.ylabel('Distance (Meters')
	plt.legend(loc = 'best')
	plt.show()

def get_Trajectory_data(filename):
	handle = open(filename, 'r')
	distance = []
	height1, height2, height3, height4 = [], [], [], []
	discardheader = handle.readline()
	for line in handle:
		d, h1, h2, h3, h4 = line.split()
		distance.append(float(d)*36.0)
		height1.append(float(h1))
		height2.append(float(h2))
		height3.append(float(h3))
		height4.append(float(h4))
	handle.close()
	return distance, [height1, height2, height3, height4]

def tryFits(filename):
	distance, heights = get_Trajectory_data(filename)
	heights = np.matrix(heights)
	yval = np.mean(heights, axis = 0)
	yval = yval.tolist()[0]

	plt.title('Trajectory and Its Fit')
	plt.xlabel('Distance (Inches)')
	plt.ylabel('Height (Inches)')

	fit_linear = np.poly1d(np.polyfit(distance, yval, 1))
	y_linear_val = fit_linear(distance)

	fit_poly = np.poly1d(np.polyfit(distance, yval, 3))
	y_poly_val = fit_poly(distance)
	
	plt.plot(distance, yval, 'bo', label = 'Distance and Height')
	plt.plot(distance, y_linear_val, label = 'Linear Fit')
	plt.plot(distance, y_poly_val, color = 'r', label = 'Poly Fit w 3')

	plt.legend(loc = 'best')

	plt.show()


if __name__ == '__main__':
	# dis, weight= get_data("springData.txt")

	# slope, inter = np.polyfit(np.array(weight), np.array(dis), 1)
	# plot_spr_n_fit(weight, dis, slope, inter)
	# plot_spr_fit_poly('springData.txt')
	
	tryFits('launcherData.txt')