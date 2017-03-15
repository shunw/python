import random

'''
THIS IS THE QUIZ 5
'''

def simThrows(numFlips):
    """Simulates a sequence of numFlips coin flips, and returns True if
    the sequence contains a run of at least four consecutive
    heads and False otherwise."""
    count = 0
    for i in range(numFlips):
        if random.random() < .5: 
            if count < 4: count = 0
            else: return True
        else: count += 1
    if count >= 4: return True
    else: return False
    
def MonteCarlo_4con(trials):
    four_T = 0
    for i in range(trials):
        if simThrows(10): four_T += 1
    return float(four_T)/trials


'''
THIS IS FOR THE QUESTION 4
'''
class Shape(object):
    def __eq__(s1, s2):
        return s1.area() == s2.area()
    def __lt__(s1, s2):
        return s1.circum() < s2.circum()

class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = float(h)
        self.width = float(w)
    def circum(self):
        return 2*(self.height + self.width)
    def __str__(self):
        return 'Rectangle with area ' + str(self.height*self.width)

class Square(Rectangle):
    def __init__(self, s):
        Rectangle.__init__(self, s, s)
    def __str__(self):
        return 'Square with side ' + str(self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)
    def circum(self):
        return 3.14159*(2*self.radius)
    def __lt__(self, other):
        return self.radius < other.radius
    def __str__(self):
        return 'Circle with diameter ' + str(2.0*self.radius)

def reorder(L):
    for e in L:
        if e < L[0]:
            L[0] = e

L = [Square(6), Rectangle(2, 3), Circle(1)]
try:
    reorder(L)
    for e in L:
        print e
except:
    for e in L:
        print e
