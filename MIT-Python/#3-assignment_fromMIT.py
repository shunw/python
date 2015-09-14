from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

### problem 1
def countSubStringMatch(target,key):
    fir_find = 0
    counter = 0
    while fir_find+len(key) < len(target):
        fir_find = find(target, key, fir_find)
        # raw_input('please enter anything here to continue... ')
        fir_find += 1
        counter += 1
    print counter
    
def countSubStringMatchRecursive (target, key):
    #countSubStringMatchRecursive(target, key)
    index = find(target, key)
    if index < 0: return 0
    return countSubStringMatchRecursive(target[index+len(key): ], key)+1


### problem 2
def subStringMatchExact(target,key):
    fir_index = tuple()
    fir_index = (find(target, key),)
    while find(target, key, fir_index[-1]+1) >= 0:
        # print fir_index, find(target, key, fir_index[-1]+1)
        fir_index = fir_index+(find(target, key, fir_index[-1]+1), )
    return fir_index




### the following procedure you will use in Problem 3

def constrainedMatchPair(firstMatch,secondMatch,length):
    ans = ()
    for i in firstMatch:
        for j in secondMatch:
            if i+length+1 == j: 
                ans=ans+(i,)
    return ans

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        # print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        # print 'match1',match1
        # print 'match2',match2
        # print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

### problem 4
def subStringMatchExactlyOneSub(target,key):
    only_sub = ()
    no_sub = subStringMatchExact(target,key)
    w_sub = subStringMatchOneSub(key, target)
    for i in w_sub:
        if i not in no_sub:
            only_sub = only_sub+(i,)
    print 'no_sub is: ', no_sub
    print 'w_sub is: ', w_sub
    print 'only_sub is: ', only_sub

if __name__ == '__main__':
    subStringMatchExactlyOneSub(target2, key13)
