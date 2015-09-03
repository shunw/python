
###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

def get_solution(ord_qty):
	
	for a in range(ord_qty/packages[0]+1):
		for b in range(ord_qty/packages[1]+1):
			for c in range(ord_qty/packages[2]+1):
				combination = list()
				if a * packages[0] + b * packages[1] + c * packages[2] == ord_qty:
					combination.append(a)
					combination.append(b)
					combination.append(c)
					#com_total.append(combination)
					return combination				

def get_list(n):
	ls = list()
	for i in range(6):
		ls.append(n+i)
	return ls


bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,16)   # variable that contains package sizes


for n in range(1, 200):   # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    if get_solution(n) == None:
    	bestSoFar = n
    ## when done, your answer should be bound to bestSoFar
print 'Given package sizes <', packages[0], '>, <', packages[1], '>, and <', packages[2], '>, the largest number of McNuggets that cannot be bought in exact quantity is: <', bestSoFar, '>'

