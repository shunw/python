def test(n): 
	if n == 0:
		return 0
	for i in range(10):
		print i
		if i > 5:
			return 5

if __name__ == '__main__':
	print test(1)