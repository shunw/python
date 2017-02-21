import random

def rol_once():
	first = random.randint(1, 6)
	second = random.randint(1, 6)
	if first != second: return False
	third = random.randint(1, 6)
	if second != third: return False
	fourth = random.randint(1, 6)
	if fourth != third: return False
	fifth = random.randint(1, 6)
	if fourth != fifth: return False
	return True

if __name__ == '__main__':
	trial = 20000
	trial_q = 20
	starts = list()

	for j in range(trial_q):
		start = 0
		for i in range(trial):
			if rol_once():
				start += 1
		starts.append(start*1.0)
	mean_s = sum(starts)/ trial_q
	print (mean_s) / trial
