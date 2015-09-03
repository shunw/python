
pack_1 = 6
pack_2 = 9
pack_3 = 20


def get_solution(ord_qty):
	
	for a in range(ord_qty/pack_1+1):
		for b in range(ord_qty/pack_2+1):
			for c in range(ord_qty/pack_3+1):
				combination = list()
				if a * pack_1 + b * pack_2 + c * pack_3 == ord_qty:
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

if __name__ == '__main__':
	# ===========================================
	# this is to get the minimum number of the continuous 6 number 
	# ===========================================
	n = 6
	judge = True
	while (judge):
		for i in range(6):
			if get_solution(n+i) == None: 
				n = n+i+1
				break
			if i == 5: judge = False
	
	# ===========================================
	# this is to check the max number cannot be packaged
	# ===========================================
	while get_solution(n) != None:
		n -= 1
	print 'Largest number of McNuggets that cannot be bought in exact quantity: <', n, '>'
	
	# ===========================================
	# this is to test the minimum continuous 6 number
	# ===========================================
	# for i in get_list(44):
	# 	print get_solution(i), i


