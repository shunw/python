def squareRootBi(x, epsilon):
	"""assume x>=0 and epsilon >0
	Return y if abs(y**2-x) < epsilon"""
	assert x>=0, "must be non-negative, not" +str(x)
	assert epsilon>0, "must be positive, not" +str(epsilon)
	low=0
	high=x
	guess=(low+high)/2.0
	ctr=1
	while abs(guess**2-x)>epsilon and ctr<=100:
		# print "low:", low, "high:", high, "guess:", guess
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2.0
		ctr+=1
	assert ctr<=100, "count exceeded"
	print  "calculation cycle", ctr, "candidate", guess
	return guess

x=float(raw_input("Enter x: "))
epsilon=float(raw_input("Enter epsilon: "))
squareRootBi(x, epsilon)

