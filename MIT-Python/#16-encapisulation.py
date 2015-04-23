class Person(object):
	def __init__(self, family_name, first_name):
		self.family_name=family_name
		self.first_name=first_name
	def familyName(self):
		return self.family_name
	def firstName(self):
		return self.first_name
	def __cmp__(self, other):
		return cmp((self.family_name, self.first_name), 
					(other.family_name, other.first_name))
	def __str__(self):
		return "My name is %s %s " % (self.first_name, self.family_name)
	def say(self, toWhom, something):
		return self.first_name + " "+ self.family_name+ "says to" + toWhom.firstName() +" " + toWhom.familyName()+ " " + something
	def sing(self, toWhom, something):
		return self.say(toWhom, something+"tro la la")


per=Person("Fooba", "Frank")
# print per.say(per, "why are you not in class")
# print per.sing(per, "foo bar bas")

class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, familyName, firstName):
        Person.__init__(self, familyName, firstName)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __str__(self):
        return '<MIT Person: %s %s>'%(self.first_name, self.family_name)
    def __cmp__(self,other):
        return cmp(self.idNum, other.idNum)

# p1 = MITPerson('Smith','Fred')
# p2 = MITPerson('Foobar','Jane')
# print p1
# print p2.getIdNum()
# print p1.say(p2, "why are you not in class")


class UG(MITPerson):
    def __init__(self, familyName, firstName):
        MITPerson.__init__(self, familyName, firstName)
        self.year = None
    def setYear(self, year):
        if year > 5: raise OverflowError('Too many')
        self.year = year
    def getYear(self):
        return self.year
    def say(self,toWhom,something):
        return MITPerson.say(self,toWhom,'Excuse me, but ' + something)

me = Person("Grimson", "Eric")
ug = UG('Doe', 'Jane')
print per<ug #this can work. but ug<per cannot workL: ug.__cmp__(per)