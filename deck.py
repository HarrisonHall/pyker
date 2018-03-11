#deck.py
import itertools
import random
rank = {1: 'A', 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:'J', 12:'Q', 13:'K'}

class card(object):
                def __init__(self ,rank, suit):
                        self.rank = rank #number
                        self.suit = suit #character

                def __repr__(self):
                        return "(suit)(rank)".format(
                                suit = suit[self.suit], rank = rank[self.rank])
                def __lt__(self, other):
                        return(self.suit, self.rank)<(other.suit, other.rank)

def makedeck():
        mdeck = [card(rank, suit) for
                 rank, suit in itertools.product(
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                         ['C', 'D', 'H', 'S'])
        ]
        return mdeck

def shuffle(deck):
        deck = random.shuffle(deck)
        return deck

def draw(deck):
        return deck.pop()
