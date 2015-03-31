def b_sort_w(s):
	#just failed
	mid=len(s)/2
	half_bf=s[0:mid]
	half_aft=s[mid:len(s)]
	if len(half_bf)<2 or len(half_aft)<2:
		if half_aft<half_bf:
			merged=half_aft+half_bf

def merge_w(left, right):
	merged=[]
	while len(left)>0 and len(right)>0:
		if left[0]<right[0]:
			merged.append(left[0])
			left=left[1:]
		else:
			merged.append(right[0])
			right=right[1:]
	if len(left)>0:
		for i in left:
			merged.append(i)
	else:
		for n in right:
			merged.append(n)
	return merged

def merge(left, right):
	#SAMPLE
	#this is the sample shown in the MIT
	result=[]
	i, j=0, 0
	while i < len(left) and j<len(right):
		if left[i]<=right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	while (i<len(left)):
		result.append(left[i])
		i+=1
	while (j<len(right)):
		result.append(right[j])
		j+=1
	return result



def mergesort(L):
	#SAMPLE
	#still not good at the iteration. So mine is still failure example. 
	print L
	if len(L)<2:
		return L[:]
	else: 
		middle=len(L)/2
		left=mergesort(L[:middle])
		right=mergesort(L[middle:])
		together=merge_w(left, right)
		print "merged", together
		return together

def mergesort_test():
	L=[12]
	mergesort(L)

def merge_test():
	left=[1, 3, 4, 7, 18, 19]
	right=[2, 9, 11, 14]
	print merge(left, right)

#next are for the hashing ...
def create(smallest, largest):
	#SAMPLE
	intSet=[]
	for i in range(smallest, largest+1): intSet.append(None)
	return intSet

def insert(intSet, e):
	#SAMPLE
	intSet[e]=1

def member(intSet, e):
	#SAMPLE
	return intSet[e]==1

def hashChar(c):
	#SAMPLE
	# c is a char
	#function returns a different integar in the range 0-255
	#for each possible vlue of c
	return ord(c)

def cSetCreate():
	cSet=[]
	for i in range (0, 255): cSet.append(None)
	return cSet

def cSetInsert(cSet, e):
	cSet[hashChar(e)]=1

def cSetMember(cSet, e):
	return cSet[hashChar(e)]==1

print ord("4")

