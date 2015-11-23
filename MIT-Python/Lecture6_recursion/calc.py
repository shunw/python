def func(poly, root):
	result = 0
	for i in range(len(poly)):
		result += poly[i] * (x ** float(i))
	return result

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x = .1
print func(poly, x)