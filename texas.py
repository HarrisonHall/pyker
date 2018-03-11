# Defines the Texas Hold'em poker game.
# Creates the river and allows player to combine river and hand.

'''
Outline:
infoArray is the list of game data: player, deck, and river
initialDeal(infoArray) - deals 3 cards to each player
initRiver(infoArray) - creates and deals the flop
plusRiver(infoArray) - deals 1 card to the community (called river here)
replaceHand(infoArray, playerChoice) - replaces the player's hand to their choice of 5 cards from the river and original hand
'''

import deck
import copy

# Initial dealing of cards
def initialDeal(infoArray):
    playerList = copy.copy(infoArray[0])
    middleDeck = copy.copy(infoArray[1])
    for x in playerList:
        x[3] = []
        for y in range(2):
            cardDrawn = deck.draw(middleDeck)
            x[3].append(cardDrawn)
    return infoArray

# Creates the river
def initRiver(infoArray):
    infoArray[2] = []
    for x in range(3):
        cardDrawn = deck.draw(infoArray[1])
        infoArray[2].append(cardDrawn)
    return infoArray
'''
# Deals one card to each player
def dealCard(infoArray) 
        playerList = copy.copy(infoArray[0])
        middleDeck = copy.copy(infoArray[1])
        for x in playerList:
                cardDrawn = deck.draw(middleDeck)
                playerList[x][3].append(cardDrawn)
        return infoArray
'''
# Places one card to river
def plusRiver(infoArray):
    cardDrawn = deck.draw(infoArray[1])
    infoArray[2].append(cardDrawn)
    return infoArray

# Replaces player's "hand" with their choices from river and hand
def replaceHand(infoArray, playerChoice):
    river = copy.copy(infoArray[2])
    playerList = copy.copy(infoArray[0])
    for x in playerList:
        x[3] = []
        for y in playerChoice:
            playerList[x][3].append(playerChoice[y])
    return infoArray
