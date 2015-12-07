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

    def __str__(self):
        """Returns a string representation of self"""
        elems = []
        for bucket in self.vals:
            for e in bucket: elems.append(e)
        elems.sort()
        result = ''
        for e in elems: result = result + str(e) + ','
        return '{' + result[:-1] + '}'

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals[self.hashE(e)]


def test1():
    s = intSet()
    for i in range(40):
        s.insert(i)
    print s.member(14)
    print s.member(50)
    # print s
    # print s.vals  #Evil


import datetime

class Person(object):

    def __init__(self, name):
        # create a person with name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1: ]
        except:
            self.lastName = name

    def __lt__(self, other):
        # return True if self's name is lexicographically greater than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        # return self's name
        return self.name

    def getLastName(self):
        # return self's last name
        return self.lastName

    def setBirthday(self, birthDate):
        # assumes birthDate is of type datetime.date
        # sets self's birthday to birthDate
        assert type(birthDate) == datetime.date
        self.birthday = birthDate

    def getAge(self):
        # assumes that self's birthday has been set
        # returns self's current age in days
        assert self.birthday != None
        return (datetime.date.today()-self.birthday).days

if __name__ == '__main__':
    me = Person('John Guttag')
    him = Person('Barack Hussein Obama')
    her = Person('Madonna')
    him.setBirthday(datetime.date(1961, 8, 4))
    print him.getAge()
