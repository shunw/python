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

'''
Vector basic 
--- need function between vectors: add/ abs
'''

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Vector({x}, {y})'.format(x = self.x, y = self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** .5
    
    def __bool__(self):
        pass
    
    def __add__(self, other):
        pass
    
    def __mul__(self, other):
        # return 'Vector({x}, {y})'.format(x = self.x * other, y = self.y * other)
        self.x = self.x * other
        self.y = self.y * other
        return self.x, self.y

if __name__ == '__main__':
    # # for the Frech Deck
    # deck = FrenchDeck()
    # for card in sorted(deck, key = spades_high, reverse = True):
    #     print (card)
    
    # for Vector
    v1 = Vector(3, 4)
    v2 = Vector(2, 1)
    # print (v1 + v2)
    print (abs(v1 * 3))
