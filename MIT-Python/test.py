import time

# start_time = time.time()
# name = raw_input('what is your name: ')
# end_time = time.time()
# total_time = end_time-start_time

# print total_time
# print 'It took %0.2f to enter your name' % total_time

class Vec: 
	def __init__(self, labels, function):
		self.D = labels
		self.f = function
	def func(self):
		function_set = []
		for i in self.D:
			if i in self.f: 
				function_set.append (self.f[i])
		return function_set

def setitem(v, d, val): 
	v.f[d] = val

def list_dot(u, v): return sum([u[i] * v[i] for i in range(len(u))])

def zero_vec(D): return Vec(D, {})

def triangular_solve(rowlist, b):
	x = zero_vec(rowlist[0].D)
	for i in reversed(range(len(rowlist))):
		x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
	return x

def triangular_solve_1(rowlist, label_list, b):
	x = zero_vec(set(label_list))
	for r in reversed(range(len(rowlist))):
		c = label_list[r]
		x[c] = (b[r] - x*rowlist[r])/rowlist[r][c]
	return x

if __name__ == '__main__': 
	u = [1, 2]
	v = [3, 4]
	print list_dot(u, v)