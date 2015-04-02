def silly():
	res=[]
	done=False
	while not done:
		elem=raw_input("Enter element, return when done:")
		if elem=="":
			done =True
		else:
			res.append(elem)
	tmp=res[:]
	# print tmp, res
	tmp.reverse()
	print tmp, res
	isPal=(res==tmp)
	if isPal:
		print "is a palindrome"
	else:
		print "is NOT a palindrome"

silly()