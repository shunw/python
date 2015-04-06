def fib(x):
	global numCalls
	numCalls+=1
	print "fib called with ", x
	if x==0 or x==1: 
		return 1
	else: 
		return fib(x-1)+fib(x-2)


def fib_op_w(x):
#failed
	global numCalls
	numCalls+=1
	# global DT
	# if not x in DT:
	# 	DT[x]=
	print "fib called with ", x
	if x==0 or x==1: 
		return 1
	else: 
		return fib(x-1)+fib(x-2)

def fastFib(n, memo):
	#SAMPLE
	global numCalls
	numCalls+=1
	print "fib called with ", n
	if not n in memo:
		memo[n]=fastFib(n-1, memo)+fastFib(n-2, memo)
	return memo[n]
def fib1(n):
	#SAMPLE
	memo={0:1, 1:1}
	return fastFib(n, memo)

# def node(rest_w, w, v, i):
# 	#by wendy try

def decision_tree(w, v, limit):
	#by Wendy try
	#failed
	i=len(w)-1
	value=0
	best_w=[i, limit, value]
	while i>=0:
		if w[i]<=limit: 
			limit_1-=w[i]
			value_1+=v[i]
		if value<value_1:
			betst_w=[i, limit_1, va_1]
		i-=1

def maxVal(w, v, i, aW):
	#mit samples
	#aW for the available weight
	#implement with the decision tree
	print "maxVal called with: ", i, aW
	global numCalls
	numCalls+=1
	if i==0:
		if w[i]<=aW: return v[i]
		else: return 0
	without_i=maxVal(w, v, i-1, aW)
	if w[i]>aW:
		return without_i
	else:
		with_i=v[i]+maxVal(w, v, i-1, aW-w[i])
	# print "without_i = ", without_i, "with_i = ", with_i, "i = ", i
	return max(with_i, without_i)

def maxVal_1(w, v, i, aW, memo):
	#mit samples
	#aW for the available weight
	#implement with the decision tree
	# print "maxVal called with: ", i, aW
	# The following is the not optimal, because it did not store everyone into the dict, 
	#it only store the max data into the memo
	global numCalls
	numCalls+=1
	if not (i, aW) in memo:
		if i==0:
			if w[i]<=aW: return v[i]
			else: return 0
		without_i=maxVal_1(w, v, i-1, aW, memo)
		if w[i]>aW:
			return without_i
		else:
			with_i=v[i]+maxVal_1(w, v, i-1, aW-w[i], memo)

	# print "without_i = ", without_i, "with_i = ", with_i, "i = ", i
		memo[(i, aW)]= max(with_i, without_i)
	print "i = ", i, "aW = ", aW, "res = ", memo[(i, aW)]
	return memo[(i, aW)]

def decision(w, v, i, aW):
	#wendy try
	memo={}
	return maxVal_1(w, v, i, aW, memo)

def fastMaxVal(w, v, i, aW, m):
	#MIT sample
	global numCalls
	numCalls+=1
	try: return m[(i, aW)]
	except KeyError:
		if i==0:
			if w[i]<=aW:
				m[(i,aW)]=v[i]
				return v[i]
			else:
				m[(i, aW)]=0
				return 0
		without_i=fastMaxVal(w, v, i-1, aW, m)
		if w[i]>aW:
			m[(i, aW)]=without_i
			return without_i
		else: 
			with_i=v[i]+fastMaxVal(w, v, i-1, aW-w[i], m)
		res=max(with_i, without_i)
		m[(i, aW)]=res
		return res
def maxVal0(w, v, i, aW):
	m=dict()
	return fastMaxVal(w, v, i, aW, m)


weights=[1, 1, 5, 5, 3, 3, 4, 4]
vals=[15, 15, 10, 10, 9,9, 5,  5]
# weights=[1, 5, 3, 4]
# vals=[15, 10, 9, 5]
numCalls=0
# res=maxVal0(weights, vals, len(vals)-1, 8)
res=decision(weights, vals, len(vals)-1, 8)
print "max Val= ", res, "number of calls ", numCalls







# numCalls=0
# n=6
# res=fib1(n)
# print "fib of", n, "=", res, "numCalls", numCalls