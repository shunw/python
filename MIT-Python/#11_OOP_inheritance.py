class intSet(object):
    #An intSet is a set of integers
    def __init__(self):
        """Create an empty set of integers"""
        self.numBuckets = 47
        self.vals = []
        for i in range(self.numBuckets):
            self.vals.append([])

    def hashE(self, e):
        #Private function, should not be used outside of class
        return abs(e)%len(self.vals)

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        for i in self.vals[self.hashE(e)]:
            if i == e: return
        self.vals[self.hashE(e)].append(e)


def test1():
    s = intSet()
    for i in range(40):
        s.insert(i)
    print s.member(14)
    print s.member(41)
    print self
    print s.vals  #Evil


import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        try: 
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank + 1]
        except:
            self.lastName = name
        self.birthday = None
    
    def getLastName(self):
        #return self's last name
        return self.lastName

    def setBirthday(self, birthDate):
        #assumes birthDate is of type datetime.date
        #sets self's birthday to birthDate
        assert type(birthDate) == datetime.date
        self.birthday = birthDate

    def getAge(self):
        #assumes that self's birthday has been set
        #returns self's current age in days
        assert self.birthday != None
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        #return True if self's name is lexicographically greater
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __eq__(self, other):
        return self.lastName < other.lastName

    def __str__(self):
        #return self's name
        return self.name

class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def isStudent(self):
        return type(self) == UG or type(self) == G

class UG(MITPerson):
    def __init__(self, name):
        MITPerson.__init__(self, name)
        self.year = None

    def setYear(self, year):
        if year > 5:
            raise OverflowError ('Too many')
        self.year = year

    def getYear(self):
        return self.year


if __name__ == '__main__':
    # me = Person('John Guttag')
    # him = Person('Barack Hussein Obama')
    # her = Person('Madonna')
    # him.setBirthday(datetime.date(1961, 8, 4))
    # her.setBirthday(datetime.date(1958, 8, 16))
    # pList = [me, him, her]
    # print 'The people in pList are:'
    # for p in pList:
    #     print p
    # pList.sort()
    # print 'The people in pList are:'
    # for p in pList:
    #     print p
    p1 = MITPerson('Barbara Beaver')
    # print p1, p1.getIdNum()

    p2 = MITPerson('Sue Yuan')
    # print p2, p2.getIdNum()

    # print 'p1 < p2 =', p1 < p2

    p3 = MITPerson('Sue Yuan')
    p4 = Person('Sue Yuan')

    # print p2 == p3
    # print Person.__lt__(p2, p3)
    # print p4, p3
    # print p4 == p3
    # # print p3 < p4

    # print '_lt__(p1, p2) =', Person.__lt__(p1, p2)
    # print 'p1 == p4 =', p1 == p4
    # print 'p4 < p3 =', p4 < p3
    # print 'p3 < p4 =', p3 < p4

    ug1 = UG('Jane Doe')
    ug2 = UG('Jane Doe')
    p3 = MITPerson('Sue Yuan')
    ug1.setYear(5)
    print ug1.getIdNum()

    '''
    question 1: why there is p1==p4 here, it should use the __lt__. If so, it should always be false. 
    question 2: p4 < p3 is correct, but p3 < p4 prompt error message. does this mean p4 < p3 uses the Person.__lt__ / and p3 < p4 uses the MIT.Person.__lt__???
    question 3: which one is class variable
    status: till 43 min
    '''