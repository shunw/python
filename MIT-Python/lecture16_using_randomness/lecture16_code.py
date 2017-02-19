import random

def needle_once():
	x = random.uniform(-1.0, 1.0)
	y = random.uniform(-1.0, 1.0)
	if (x**2 + y**2)**.5 <= 1: return 1
	else: return 0

def cal_pi(needle_q):
	n = needle_q
	base = 0
	circle = 0
	while n >= 0:
		result = needle_once()
		if result == 1:
			circle += 1
			base += 1
		else: base += 1
		n -= 1
	return (circle*1.0/base*1.0)*4.0

def cal_std(pi_q, once_needle_q):
	n = pi_q
	pi_list = []
	while n >= 0:
		pi_list.append(cal_pi(once_needle_q))
		n -= 1
	avg = sum(pi_list)/float(len(pi_list))
	s2n = 0
	for i in pi_list:
		s2n += (i - avg)**2 
	return (avg, (s2n/float(len(pi_list)))**.5)

if __name__ == '__main__':
	pi_q = 20
	once_needle_q = 1000
	avg, std = cal_std(pi_q, once_needle_q)
	while std >= (.01/4):
		once_needle_q = once_needle_q * 2
		avg, std = cal_std(pi_q, once_needle_q)
	print (avg, std)
		
