def sort_base(s):
	#move the biggest to the right side
	count=0

	for j in range(0, len(s)-count):
		temp=None
		for i in range (0, len(s)-count):
			if temp is None:
				temp=s[0]
				ori_index=0
			if temp<s[i]:
				temp=s[i]
				ori_index=i
		# print s, ori_index, temp
		if ori_index!=len(s)-count-1:
			s[ori_index]=s[len(s)-count-1]
			s[len(s)-count-1]=temp
			
		# print s, count, len(s)-count
		count+=1
	print s

def bubbleSort(L):
	for j in range(len(L)):
		for i in range (len(L)-j-1):
			if L[i]>L[i+1]:
				temp=L[i]
				L[i]=L[i+1]
				L[i+1]=temp
		print L

def bubbleSort1(L):
	swapped=True
	while swapped:
		swapped=False
		for i in range(len(L)-1):
			if L[i]>L[i+1]:
				temp=L[i]
				L[i]=L[i+1]
				L[i+1]=temp
				swapped=True
		print L

def sort_test():
	s=[5, 4, 6, 2, 1]
	print bubbleSort1(s)

sort_test()