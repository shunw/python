#problem 1 for the 1000th prime data
from math import *

def prime_n(len_n):
	n = 3
	prime = list()
	prime.append(2)
	prime.append(3)

	while len(prime) <= len_n-1:
		n += 2
		b_divide = False
		for i in prime:
			if n % i == 0: 
				b_divide = True
				break
		if not b_divide: prime.append(n)
	return prime
	

if __name__ == '__main__':	
	num = int(raw_input('please enter a number for prime qty: '))
	prime = prime_n(num)
	product_sum = 1
	for i in prime: 
		product_sum *= i
	log_sum = log(product_sum)
	e_n = e**num

	print 'log_sum = ', log_sum
	print 'num = ', prime[-1]
	print 'ratio = ', log_sum/prime[-1]




	