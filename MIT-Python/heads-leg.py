def heads_legs(head, leg):
	count=0
	for i in range(0, head+1):
		chicken=i
		pig=head-i
		if 4*pig+2*chicken==leg:
	#		print "chicken: ", chicken, "pig: ", pig
			return[chicken, pig]
	return [None, None]

def barnYard():
	head=int(raw_input("Enter number of heads:"))
	leg=int(raw_input("Enter number of legs:"))
	solve_spider_all(head, leg)
	# if pig==None:
	# 	print "There is no solution"
	# else:
	# 	print "number of pig", pig
	# 	print "number of chicken", chicken
	# 	print "number of spider", spider

def solve_spider(head, leg):
	for num_c in range(0, head+1):
		for num_p in range(0, head-num_c+1):
			num_s=head-num_c-num_p
			if 2*num_c+4*num_p+8*num_s==leg:
				return (num_c, num_p, num_s)
	return (None, None, None)


def solve_spider_all(head, leg):
	sol_found=False
	for num_c in range(0, head+1):
		for num_p in range(0, head-num_c+1):
			num_s=head-num_c-num_p
			if 2*num_c+4*num_p+8*num_s==leg:
				print "number of pig", num_p
				print "number of chicken", num_c
				print "number of spider", num_s
				sol_found=True
	if not sol_found: print "There is no solution"

barnYard()
