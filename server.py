#server.py
import os
import sys
from socket import *
import deck
import hands
import texas

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

def bet (infoArray, port):
        playerList = copy.copy(infoArray[0])
        presentPlayers = copy.deepcopy(infoArray[0])
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
                                        if usrIn == 'c':
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
                                        if usrIn == 'r':
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
        
        reassign(infoArray, presentPlayers)
        return [infoArray, presentPlayers]

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
    keepPlaying = True
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
        currentPlayerArray = bet(currentPlayerArray[1],port)
        infoArray = texas.plusRiver(infoArray)
        currentPlayerArray = bet(currentPlayerArray[1],port)
        infoArray = texas.plusRiver(infoArray)
        currentPlayerArray = bet(currentPlayerArray[1],port)
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
            winnerString += "name" + " "
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

else:
    print("Wrong game :( ")

UDPSock.close()
