#deck.py
import itertools
import random

rank = {1: 'A', 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:'J', 12:'Q', 13:'K'}
suit = {2:'C',1:'D',3:'H',4:'S'}

class Card(object):
    def __init__(self ,rank, suit):
        self.rank = rank #number
        self.suit = suit #character

    def __repr__(self):
        return "{suit}{rank}".format(suit = suit[self.suit], rank = rank[self.rank])
    
    def __lt__(self, other):
        return(self.suit, self.rank)<(other.suit, other.rank)
    
    def val(self):
        return rank
        
class Deck:
    def __init__(self):
        self.deck = [Card(rank,suit) for rank,suit in zip(rank,suit)]
        self.shuffle()
        
    def shuffle(self):
        self.deck = random.shuffle(deck)
        
    def draw(self):
        return deck.pop()

