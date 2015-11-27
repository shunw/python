from ps3a import *
import time
from perm import *
import random


#
#
# Problem #6A: Computer chooses a word
#
#

def find_word(hand, word_line):
    '''
    hand is dict {alp: int}
    word_line is the word: 'abd'
    '''
    if not(set(word_line).issubset(set(hand))): 
        return False
    word_dict = dict()
    for i in list(word_line):
        word_dict[i] = word_dict.get(i, 0) + 1
    #create the word dict, after that we will compare two dict's context
    for k in word_dict.keys(): 
        if hand[k] < word_dict[k]: 
            return False
    return True

def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    word_score = 0
    word_best = str()
    temp_score = 0
    bonus_n = 7
    for i in word_list:
        if not(find_word(hand, i)): continue
        temp_score = get_word_score(i, bonus_n)
        if word_score < temp_score: 
            word_score = temp_score
            word_best = i
    return word_best

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...  
    
    temp_s = 0
    total_s  = 0
    while sum(hand.values())>0:
        word = comp_choose_word(hand, word_list)
        if word == '': break

        hand_list = list()
        for k in hand.keys():
            for i in range(hand[k]):
                hand_list.append(k)
        print 'Current Hand: %s' %(', '.join(hand_list))

        temp_s = get_word_score(word, HAND_SIZE)
        total_s += temp_s
        print '"%s" earned %d points. Total: %d points' % (word, temp_s, total_s) 
        hand = update_hand(hand, word)
    
    print 'Total score: %d points. ' % total_s

    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    hand = dict()
    hand_last = dict()
    player = str()
    while True: 
        hand_last = hand
        decision = raw_input('for a new game, pls enter -->> %s; \nto play last hand, pls enter -->> %s; \nto exit, please enter -->> %s; \nPls make your choice: ' % ('n', 'r', 'e'))
        
        if (decision != 'n') and (decision != 'r') and (decision != 'e'):
            print 'Wrong choice. Please make your choice again!'
            continue
        
        elif decision == 'r':
            #??? how to make the game renew
            if len(hand_last) == 0:
                print 'Not last hand can be used. '
                continue
            else: 
                hand = hand_last
        
        elif decision == 'e':
            print 'Game End. '
            break

        elif decision == 'n':
            hand_len = int(random.uniform(8, 12))
            hand = deal_hand(hand_len)
            
        while True:
            player = raw_input('for the computer player, pls choose -->> %s; \nfor the personal player, pls choose -->> %s; \nPls make your choice: ' %('c', 'u'))
            if (player == 'c') or (player == 'u'):
                break
            print 'Wrong choice, Please make your choice again!'
        
        

        if player == 'c': 
            comp_play_hand(hand, word_list)
        else: 
            play_hand(hand, word_list)

    

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    # play_game(word_list)
    hand_len = int(random.uniform(8, 12))
    hand = deal_hand(hand_len)
    # print comp_choose_word(hand, word_list)
    # comp_play_hand(hand, word_list)
    play_game(word_list)

    
