# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program

def show_alps(alp, bef_list, guess):
    for n, i in enumerate(guess): 
        if i == alp:
            bef_list[n] = alp
    return bef_list

wordlist = load_words()

# your code begins here!
guess = choose_word(wordlist)
guess_list = list(guess)
show_list = list('_' * len(guess_list))

cycle = 8
alphs = list(string.ascii_lowercase)

print 'Welcome to the game, Hangman!'
print 'I am thinking of a word what is %d letters long. ' % len(guess)

while cycle >= 0:
    print '------------------------------'    
    print 'You have %d guesses left. ' % cycle
    print 'Available letters: %s' % ''.join(alphs)
    alp_inp = raw_input('Please guess a letter: ')
    if (alp_inp in guess_list) and (alp_inp in alphs): 
        show_list = show_alps(alp_inp, show_list, guess_list)
        print 'Good guess: %s' %''.join(show_list)
        alphs.remove(alp_inp)
        if '_' not in show_list: 
            print '------------------------------'    
            print 'Congratulations, you won!'
            break
    elif alp_inp not in guess_list:
        print 'Oops! That letter is not in my word: %s' %''.join(show_list)
        cycle -= 1
    elif alp_inp not in alphs:
        print 'Oops! That letter is not in available letters: %s' %''.join(alphs)
        cycle -= 1

if (cycle < 0) and ('_' in show_list):
    print '------------------------------'    
    print 'Oops, you lose!'
            
