def exp1(base, exp):
	value=1
	while exp>0:
		value*=base
		exp-=1
	return value

def exp2(a, b):
	if b==0: return 1
	if b==1: return a
	else: 
		return a*exp2(a, b-1)

def exp3(a, b):
	if b==0: return 1
	if b==1: return a
	if b%2==0:
		return exp3(a*a, b/2)
	else:
		return a*exp3(a, b-1)



base=input("Enter Base: ")
exp=input("Enter exp: ")

print exp3(base, exp)