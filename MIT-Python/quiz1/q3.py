def f(s):
	if len(s) <= 1:
		return s
	return f(f(s[1:])) + s[0]

print f('mat')
print f('math')