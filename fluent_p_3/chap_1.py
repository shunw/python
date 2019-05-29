import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


'''
SORTING
--- ranking cards is by rank (with aces being highest)
--- then by suit in the order of spades (highest), then hearts, diamonds, and clubs (lowest). 
'''

suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    # return rank_value * len(suit_values) + suit_values[card.suit]
    return rank_value + suit_values[card.suit] * (len(FrenchDeck.ranks) + 1)

if __name__ == '__main__':
    deck = FrenchDeck()
    for card in sorted(deck, key = spades_high, reverse = True):
        print (card)
    # for i in deck:
    #     print (i)
    
