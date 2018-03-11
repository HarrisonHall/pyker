#server.py
import os
import sys
from socket import *
import deck
import hands
import texas
import blackjack

def sendDataToPlayer(player,data,port):
    try:
        ip = player[1]
        addr = (ip, port+1)
        newSock = socket(AF_INET, SOCK_DGRAM)
        newSock.sendto(data.encode('utf8'), addr)
    except:
        print("Error: Did not send correctly.")
    newSock.close()

def call(infoArray, presentPlayers,  maxBet, currPlayerIp):
        i = 0
        for x in infoArray[0]:
                if x[1] == currPlayerIp:
                        betDiff = maxBet - infoArray[0][i][4]
                        infoArray[0][i][2] -= betDiff
                        infoArray[0][i][4] += betDiff
                i += 1
        for x in presentPlayers:
                if x[1] == currPlayerIp:
                        betDiff = maxBet - presentPlayers[i][4]
                        presentPlayers[i][2] -= betDiff
                        presentPlayers[i][4] += betDiff
                i += 1
        infoArray[3] += betDiff

def reassign(infoArray, presentPlayers):
        i = 0
        for x in infoArray[0]:
                for y in presentPlayers:
                        if x[1] == y[1]:
                                infoArray[0][i] = presentPlayers[i]
                i += 1

def bet (infoArray, playersAvailable, port):
        playerList = copy.copy(infoArray[0])
        presentPlayers = copy.copy(playersAvailable)
        highestBet = 0
        i = 0
        countCall = 0
        validInput = False
        while countCall != len(presentPlayers):
                for x in presentPlayers:
                        if countCall != len(presentPlayers):
                                while validInput == False:
                                        # Ask for input
                                        cmdOut = "9Would you like to fold (f), call (c), or raise (r)?"
                                        sendDataToPlayer(x, cmdOut, port)
                                        # Recieve input
                                        (usrIn, x[1]) = UDPSock.recvfrom(buf)
                                        usrIn = usrIn.decode('utf8')
                                        if usrIn == 'f':
                                                cmdOut = "Folding"
                                                sendDataToPlayer(x, cmdOut, port)
                                                del presentPlayers[i] 
                                                validInput = True
                                        elif usrIn == 'c':
                                                if presentPlayers[i] > highestBet:
                                                        cmdOut = "Calling"
                                                        sendDataToPlayer(x, cmdOut, port)
                                                        call(infoArray, presentPlayers,  highestBet, presentPlayers[i][1])
                                                        i += 1
                                                        countCall += 1
                                                else:
                                                        cmdOut = "Folding"
                                                        sendDataToPlayer(x, cmdOut, port)
                                                        del presentPlayers[i]
                                                validInput = True
                                        elif usrIn == 'r':
                                                if presentPlayers[i] > highestBet:
                                                        cmdOut = "9Raising. How much do you want to raise the bet by?"
                                                        sendDataToPlayer(x, cmdOut, port)
                                                        (pBetR, x[1]) = UDPSock.recvfrom(buf)
                                                        pBetR = pBetR.decode('utf8')
                                                        highestBet += pBetR
                                                        infoArray[3] += pBetR
                                                        presentPlayers[i][2] -= pBetR
                                                        i += 1
                                                        countCall = 1
                                                else:
                                                        cmdOut = "Folding"
                                                        sendDataToPlayer(x, cmdOut, port)
                                                        del presentPlayers[i] 
                                                validInput = True
                                        else:
                                                cmdOut = "Invalid Input"
                                                sendDataToPlayer(x, cmdOut, port)
                                                validInput = False
        
        reassign(infoArray, playersAvailable)
        return infoArray, playersAvailable

def shiftList(someList):
    newList = someList[1:] + someList[0]
    return newList

print("\nWelcome to Pyker!")
print("Created by Harrison, Jackie, and Jacky")

#Setup
port = int(input("What is the port number: "))
print("Choose a game.")
gameChosen = input("texas(t): ")
maxRounds = int(input("Number of rounds: "))
chipNumber = input("Number of chips: ")

#Open up files to get ip and name associated
playerList = []
IPFile = open("players.txt","r")
i = 0
playerCount = 0
for line in IPFile:
    if (i > 1):
        playerList.append([line[0:line.find(" ")],line[line.find(" ")+1:]]) #name, ip
        playerCount += 1
    i += 1

print("\nPlayers:")
for player in playerList:
    print(str(player[0]),str(player[1]))

#Begin Connection
host = ""
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

print("\nWaiting for players to join")
playersJoined = 0
while(playersJoined < playerCount):
    (playerName, addr) = UDPSock.recvfrom(buf)
    playerName = playerName.decode('utf8')
    for user in playerList:
        if playerName.lower() in user:
            playersJoined += 1
            print("Player",playerName,"has joined.",str(playerCount-playersJoined),"left.")
            user.append(chipNumber) #name, ip, chips, [card1, card2, ...]
            sendDataToPlayer(user,"wassap",port)

#Tell players game has begun
print("\nThe game has begun.\n")
for user in playerList:
    sendDataToPlayer(user,gameChosen,port)
    
if gameChosen == "t":
    print("Running Texas Hold'em")
    keepGoing = True
    roundNumber = 1
    infoArray = [playerList] #Add Deck
    infoArray.append(deck.makedeck())
    deck.shuffle(infoArray[1])
    river = []
    infoArray.append(river)
    infoArray.append(0)    # Pot
    while(roundNumber <= maxRounds and keepGoing == True):
        infoArray[1] = deck.makedeck()
        deck.shuffle(infoArray[1])
        infoArray[2] = []
        for user in infoArray[0]: # Ante up
            user[2] -= 1
        for user in infoArray[0]:
            user[3] = []
            for x in range(3):
                user[3].append(deck.draw(infoArray[1]))
        for user in infoArray[0]:
            sendString = "Hand: "
            for card in user[3]:
                sendString += str(card) 
            sendDataToPlayer(user,sendString,port)
            user.append(0)    # Bets
        replies = 0
        '''
        while (replies < playerCount): # Check if users have replied to bet
            (message, addr) = UDPSock.recvfrom(buf)
            message = message.decode('utf8')
            if (message[:3] != "msg"):
                replies += 1
        '''
        infoArray = texas.initRiver(infoArray)
        for user in infoArray[0]:
            sendString = "River: " + "Hand: "
            for card in user[3]:
                sendString += str(card) 
            sendDataToPlayer(user,sendString,port)
        replies = 0
        currentPlayerArray = [infoArray,infoArray[0]]
        currentPlayerArray = bet(infoArray, currentPlayerArray[1],port)
        infoArray = texas.plusRiver(infoArray)
        currentPlayerArray = bet(infoArray, currentPlayerArray[1],port)
        infoArray = texas.plusRiver(infoArray)
        currentPlayerArray = bet(infoArray, currentPlayerArray[1],port)
        #players choose hands start
        for user in currentPlayerArray[0]:
            cardString = ""
            for card in range(len(user[3])):
                cardString += str(card) + user[3][card]
            cardString += " | "
            for card in range(len(infoArray[2])):
                cardString += str(card+2) + infoArray[2][card]
            sendDataToPlayer(user,cardString,port)
            totalCards = [user[3][0],user[3][1],infoArray[2][0],infoArray[2][1],infoArray[2][2],infoArray[2][3],infoArray[2][4]]
            cardHandArray = []
            while(len(cardHandArray) < 5):
                sendDataToPlayer(user,"Type a number 0-6",port)
                (usrIn,addr) = UDPSock.recvfrom(buf)
                usrIn = usrIn.decode('utf8')
                chosenCard = int(usrIn)
                if totalCards[chosenCard] not in cardHandArray:
                    cardHandArray.append(totalCards[chosenCard])
            user[3] = cardHandArray
        #players choose hands end
        topPoints = 0
        winnerList = []
        for user in currentPlayerArray[1]:
            if (hands.evaluate(user[3]) > topPoints):
                topPoints = hands.evaluate(user[3])
        for user in currentPlayerArray[1]:
            if (hands.evaluate(user[3] == topPoints)):
                user[2] += infoArray[3] / 2 #modify*
                winnerList.append(user[0])
        winnerString = "The pot taker is "
        for name in winnerList:
            winnerString += name + " "
        for user in infoArray[0]:
            sendDataToPlayer(user,winnerString,port)
        infoArray[0] = shiftList(infoArray[0])                
        for user in infoArray[0]:
            if (user[2] <= 1):
                keepGoing = False
        roundNumber += 1
    topPoints = 0
    winner = ""
    for user in infoArray[0]:
        if (user[2] > topPoints):
            topPoints = hands.evaluate(user[3])
    for user in infoArray[0]:
        if (user[2] == topPoints):
            winner = user[0]
    winner = "The winner is " + winner
    for user in infoArray[0]:
        sendDataToPlayer(user,winner,port)

if gameChosen == "b":
    print("Running Blackjack")
    keepGoing = True
    infoArray = [playerList] #Add Deck
    infoArray.append(deck.makedeck())
    deck.shuffle(infoArray[1])
    # River still necessary for infoArray to work
    river = []
    infoArray.append(river)
    infoArray.append(0)
    while(roundNumber <= maxRounds and keepGoing == True):
        infoArray[1] = deck.makedeck()
        deck.shuffle(infoArray[1])
        infoArray[2] = []
        for user in infoArray[0]: # Ante up
            user[2] -= 1
	blackjack.initialDeal(infoArray)
        for user in infoArray[0]:
            sendString = "Hand: "
            for card in user[3]:
                sendString += str(card) + " "
            sendDataToPlayer(user,sendString,port)
	    sendString = user[0] + "'s Card: " + user[3][0]
	    for x in infoArray[0]:
		if x[1] != user[1]:
			sendDataToPlayer(x, sendString, port)
            user.append(0)    # Creates bets
      
	currentPlayerArray = [infoArray, infoArray[0]]
	currentPlayerArray = bet(infoArray, currentPlayerArray[1], port)
	for user in currentPlayerArray[1]:
		user.append(0)	# Point total
		points = 0
		for card in user[3]:
			if card(rank) == 1:
				cmdOut = "You have an ace. Is this a 1 or 11? (1/11)"
				sendDataToPlayer(user, cmdOut, port)
				(usrIn, user[1]) = UDPSock.recvfrom(buf)
				usrIn = usrIn.decode('utf8')
				if usrIn == '1':
					points += 1
				elif usrIn == '11':
					points += 11
				else:
					cmdOut = "Invalid input."
					sendDataToPlayer(user, cmdOut, port)
			elif card(rank) >= 11 and card(rank) <= 13:
				points += 10
				cmdOut = "Points: " + points
				sendDataToPlayer(user, cmdOut, port)
			else:
				points += card(rank)
				cmdOut = "Points: " + points
				sendDataToPlayer(user, cmdOut, port)
		if points >= 9 and points <= 11:
			cmdOut = "You can double down. Would you like to? (y/n)"
			sendDataToPlayer(user, cmdOut, port)
			(usrIn, user[1]) = UDPSock.recvfrom(buf)
			usrIn = usrIn.decode('utf8')
			if usrIn == 'y':
				user[2] -= user[4]
				infoArray[3] += user[4]
				blackjack.hitPlayer(infoArray, user[1])
				cmdOut = "New card: " + user[3][cardNum]
				sendDataToPlayer(user, cmdOut, port)
				cmdOut = "All cards: "
				for card in user[3]:
					cmdOut += card + " "
				sendDataToPlayer(user, cmdOut, port)
				wouldHit == False
				user[5] = points
			elif usrIn == 'n':
				cmdOut = "You choose not to double down."
				sendDataToPlayer(user, cmdOut, port)
			else:
				cmdOut = "Invalid input."
				sendDataToPlayer(user, cmdOut, port)	
		wouldHit = True
		cardNum = 0
		while wouldHit == True:
			cmdOut = "Would you like to hit? (y/n)"
			sendDataToPlayer(user, cmdOut, port)
			(usrIn, user[1]) = UDPSock.recvfrom(buf)
			usrIn = usrIn.decode('utf8')
			if usrIn == 'y':
				cmdOut = "You asked for a card."
				sendDataToPlayer(user, cmdOut, port)
				blackjack.hitPlayer(infoArray, user[1])
				cmdOut = "New card: " + user[3][cardNum]
				sendDataToPlayer(user, cmdOut, port)
				cmdOut = "All cards: "
				for card in user[3]:
					cmdOut += card + " "
				sendDataToPlayer(user, cmdOut, port)
				wouldHit == True
			elif usrIn == 'n':
				cmdOut = "You denied a card."
				sendDataToPlayer(user, cmdOut, port)
				wouldHit == False
 
        # Calculate hands
	for user in infoArray[0]:
		if user[5] = 0:
			for card in user[3]:
				if card(rank) == 1:
					cmdOut = "You have an ace. Is this a 1 or 11? (1/11)"
					sendDataToPlayer(user, cmdOut, port)
					(usrIn, user[1]) = UDPSock.recvfrom(buf)
					usrIn = usrIn.decode('utf8')
					if usrIn == '1':
						points += 1
					elif usrIn == '11':
						points += 11
					else:
						cmdOut = "Invalid input."
						sendDataToPlayer(user, cmdOut, port)
				elif card(rank) >= 11 and card(rank) <= 13:
					points += 10
					cmdOut = "Points: " + points
					sendDataToPlayer(user, cmdOut, port)
				else:
					points += card(rank)
					cmdOut = "Points: " + points
					sendDataToPlayer(user, cmdOut, port)
			user[5] = points
					  
        winnerList = []
	highestPoints = 0
	i = 0
        for user in infoArray[0]:
		if user[5] > highestPoints:
			highestPoints = user[5]
			winnerList[i] = user[1]
		elif user[5] = highestPoints:
			winnerList.append(user[1])
			i += 1
	
	winnerString = "The pot taker is "
        for name in winnerList:
            winnerString += name + " "
        for user in infoArray[0]:
            sendDataToPlayer(user,winnerString,port)
        infoArray[0] = shiftList(infoArray[0])                
        for user in infoArray[0]:
            if (user[2] <= 1):
                keepGoing = False
        roundNumber += 1
    topPoints = 0
else:
    print("Wrong game :( ")

UDPSock.close()
