import random, pylab

principal = 10000.0
interestRate = .05
years = 20
values = []

for i in range(years + 1):
	values.append(principal)
	principal += interestRate * principal
pylab.plot(values)
pylab.show()