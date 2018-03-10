# Defines the Texas Hold'em poker game.
# Creates the river and allows player to combine river and hand.

import deck
import copy

# Initial dealing of cards
def initialDeal(infoarray)
	playerlist = copy.shallowcopy(infoarray[0])
	middledeck = copy.shallowcopy(infoarray[1])
	for x in playerlist:
		playerlist[x][3] = []
		for x in range(2)
			carddrawn = deck.draw(middledeck)
			playerlist[x][3].append(carddrawn)
	return infoarray

# Creates the river
def initRiver(infoarray)
	river = copy.shallowcopy(infoarray[2])
	river = []
	middledeck = copy.shallowcopy(infoarray[1])
	for x in range(3)
		carddrawn = deck.draw(middledeck)
		river.append(carddrawn)
	return infoarray

# Deals one card to each player
def dealCard(infoarray)	
	playerlist = copy.shallowcopy(infoarray[0])
	middledeck = copy.shallowcopy(infoarray[1])
	for x in playerlist:
		carddrawn = deck.draw(middledeck)
		playerlist[x][3].append(carddrawn)
	return infoarray

# Places one card to river
def plusRiver(infoarray)
	river = copy.shallowcopy(infoarray[2])
	middledeck = copy.shallowcopy(infoarray[1])
	carddrawn = deck.draw(middledeck)
	river.append(carddrawn)
	return infoarray
