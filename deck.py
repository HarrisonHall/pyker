#deck.py
import itertools
import random

'''
class Player(object):
	name = "" #string
	money = 0 #int
	phand = [] #array

	def __init__(name):
		name.name = name
		name.money = 100
'''

class card(object):
		def __init__(self ,rank, suit):
			self.rank = rank #number
			self.suit = suit #character

def makedeck():
        mdeck = [card(rank, suit) for
		 rank, suit in itertools.product(
			 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
			 ['C', 'D', 'H', 'S'])
        ]
        return mdeck

def shuffle(deck):
	random.shuffle(deck)
        return deck

def draw(deck):
	deck.pop()
        return deck
