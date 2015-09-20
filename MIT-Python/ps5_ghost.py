# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string
import re

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()
print type(wordlist)

# TO DO: your code begins here!
def win_judge(word_cur, wordlist):
    valid = -2
    #failure mode = {complete: -1; cannot_find: -2; valid: 1}
    #need to judge if this word is 
        # 1//complete one, len()>3; 2//cannot find that one; 3//the beginning of the other word 
    for i in wordlist:
        if word_cur == i[ :len(word_cur)]: 
            
            valid = 1
            if len(word_cur) <= 3: 
                break
            else: 
                if word_cur == i: 
                    valid = -1
                    break
    return valid


welcome = 'Welcome to Ghost! '
go_first = 'Player 1 goes first. '
current_frag = 'Current word fragment: '
P1 = 'Player 1'
P2 = 'Player 2'
R1 = ' is a word!' #valid_judge == -1
R2 = 'no word begin with ' #valid_judge == -2



if __name__ == '__main__':
    word_cur = ''
    print welcome
    print go_first
    print current_frag+"'"+word_cur+"'"
    word_raw = raw_input(P1+'says letter: ')
    while not (word_raw in string.ascii_letters):
        word_raw = raw_input(word_raw+'is not a letter. Please re-enter'+'\n'+P1+'says letter: ')
    word_cur = word_raw.lower()
    print word_cur
    counter = 0
    valid_judge = win_judge(word_cur, wordlist)
    while valid_judge == 1: 
        print current_frag+"'"+word_cur.upper()+"'"
        if counter%2 == 0: 
            P_cur = P2
            P_oth = P1
        else: 
            P_cur = P1
            P_oth = P2
        print P_cur+"'s turn. "
        word_raw = raw_input(P_cur+' says letter: ')
        while not (word_raw in string.ascii_letters):
            word_raw = raw_input(word_raw+'is not a letter. Please re-enter'+'\n'+P_cur+' says letter: ')
        word_cur = (word_cur+word_raw).lower()
        print word_cur
        counter += 1
        valid_judge = win_judge(word_cur, wordlist)
    print current_frag+"'"+word_cur.upper()+"'"
    if valid_judge == -1:
        print P_cur+' loses because '+"'"+word_cur.upper()+"'"+R1+'!'
        print P_oth+' wins!'
    if valid_judge == -2:
        print P_cur+' loses because '+R2+"'"+word_cur.upper()+"'"+'!'
        print P_oth+' wins!'