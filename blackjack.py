# Defines the Blackjack poker game.
# Deals cards to players except there is no dealer

# IMPORTANT NOTE: First vlue of each player's deck will be the "faceup" card, so print that to everybody somewhere after the initial dealing of cards.

'''
Outline:
infoArray is the list of game data: player, deck, and river
initialDeal(infoArray) - deals 2 cards to each player; server must only display the first card
hitPlayer(infoArray, currIp) - deals one card to the specified player; if player wants to double down, then execute this function, double their bet, and do not allow a second execution
'''

import deck
import copy

# Initial dealing of cards
def initialDeal(infoArray):
	playerList = copy.copy(infoArray[0])
	dealDeck = copy.copy(infoArray[1])
	for x in playerList:
		x[3] = []
		for y in range(2):
			cardDrawn = deck.draw(middeDeck)
			x[3].append(cardDrawn)
	return infoArray

# Hit (player asks for a card)
def hitPlayer(infoArray, currIp):
	playerList = copy.copy(infoArray[0])
	dealDeck = copy.copy(infoArray[1])
	for x in playerList:
		if currIp == x[1]:
			currPlayerHand = x[3]
	cardDrawn = deck.draw(dealDeck)
	currPlayerHand.append(cardDrawn)
	return infoArray

