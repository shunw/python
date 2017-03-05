import random

class Shape(object):
    def __eq__(s1, s2):
        return s1.area() == s2.area()
    def __ge__(s1, s2):
        return s1.area() >= s2.area()

class Square(Shape):
    def __init__(self, h):
        self.side = float(h)
    def area(self):
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)

def f(L):
	if len(L) == 0: return None
	x = L[0]
	for s in L:
		if s >= x: x = s
	return x

# s = Square(4)
# print s.area()
# L = []
# shapes = {0:Circle, 1: Square}
# for i in range(10):
#     L.append(shapes[i%2](i))
# print L[4]
# print f(L)

def cmpGuess(guess, maxVal):
    """Assumes that guess is an integer in range(maxVal).  returns
-1 if guess is < than the magic number, 0 if it is equal to the
magic number and 1 if it is greater than the magic number.  The
magic number is in range(maxVal)."""
	magic = random.randint(0, maxVal-1)
	if guess < magic: return -1
	elif guess > magic: return 1
	else: return 0

def findNumber(maxVal):
    """Assumes that maxVal is a positive integer.  Returns a
number, num, such that cmpGuess(num, maxVal) == 0."""
	
