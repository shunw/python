def search_num(search_body,num):
	count=0
	# print search_body
	for i in search_body:
		if num>i: 
			count+=1
			continue
		elif num!=i: 
			print "cannot fine the num, and the count is ", count
			break
		else: print "find the num ", i, "count ", (count)
		
def search_sample(s, e):
	answer=None
	i=0
	numCompares=0
	while i<len(s) and answer==None:
		numCompares+=1
		if e==s[i]:
			answer=True
		elif e<s[i]:
			answer=False
		i+=1
	print answer, numCompares

def search_opt(s, e):
	
	answer=None
	high=len(s)-1
	low=0
	mid=(low+high)/2
	if len(s)==1 or len(s)==2: 
		if e==s[low] or e==s[high]: answer=True
		else: answer=False
		print answer
	else:
		if e==s[mid]:
			answer==True
		elif e<s[mid]:
			s=s[low:mid-1]
		else:
			s=s[mid+1: high]
		print s[0], s[-1]
		search_opt(s,e)

def bsearch(s, e, first, last):
	print first, last
	if (last-first) <2: return s[first] ==e or s[last]==e
	mid=first + (last-first)/2
	if s[mid]==e: return True
	if s[mid]>e: return bsearch(s, e, first, mid-1)
	return bsearch(s, e, mid+1, last)
def search1(s, e):
	print bsearch(s, e, 0, len(s)-1)
	print "search complete" 

def testSearch():
	s=range(0, 1000000)
	# raw_input("basic, -1")
	# print search_sample(s, -1)
	# raw_input("w-basic, -1")
	# print search_num(s, -1)
	# raw_input("bisearch, -1")
	# print search1(s, -1)
	raw_input("w-bisearch, -1")
	print search_opt(s, -1)



# search_sample()
# search_num()
testSearch()