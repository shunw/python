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


numCalls=0
n=6
# fib_op_w(n)
res=fib1(n)
print "fib of", n, "=", res, "numCalls", numCalls