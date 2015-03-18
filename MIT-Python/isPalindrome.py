def isPalindrome(word):
	while len(word)>0:
		if word[0]!=word[-1]:
			return False
		else: word=word[1:-1]
	return True

def isPalindrome_1(s):
	if len(s)<=1: True
	else:
		return s[0]==s[-1] or isPalindrome_1(s[1:-1])



data=str(raw_input("Enter a string: "))
if isPalindrome_1(data):
	print "This is Palindrome"
else: 
	print "This is not Palindrome"

