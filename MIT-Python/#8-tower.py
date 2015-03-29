def tower(size, froms, to, spare):
	if size==1:
		print "Move disk from, ", froms, "to ", to
	else:
		tower(size-1, froms, spare, to)
		tower(1, froms, to, spare)
		tower(size-1, spare, to, froms)

tower(5, "f", "t", "s")