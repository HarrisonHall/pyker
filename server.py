#server.py
import os
import sys
from socket import *

def sendDataToPlayer(player,data,port):
    try:
        ip = player[1]
        addr = (ip, port+1)
        newSock = socket(AF_INET, SOCK_DGRAM)
        newSock.sendto(data.encode('utf8'), addr)
    except:
        print("Error: Did not send correctly.")
    newSock.close()

def betsEqual(betArray):
    initVal = betArray[0]
    for bet in betArray:
        if bet != initVal:
            return False
    return True

def betsHighest(betsArray):
    initVal = betArray[0]
    for bet in betArray:
        if bet > initVal:
            initVal = bet
    return initVal
    
def bet(infoArray,port):
    messages = ""
    replies = 0
    bets = []
    for user in range(len(infoArray)):
        bets.append(user+1000)
    while(betsEqual() == False): #Need to only let lower bets make it
        (message, addr) = UDPSock.recvfrom(buf)
        message = message.decode('utf8')
        if (message[:3] != "msg"):
            for user in range(len(infoArray[0])):
                if (infoArray[0][user][1] == addr):
                    if (infoArray[0][user][2] >= int(message)):
                        bets[user] = int(message)
                        infoArray[0][user][2] -= int(message)
                    else:
                        bets[user] = infoArray[0][user][2]
                        infoArray[0][user][2] = 0
        elif (message[:3] == "msg"):
            messages += message[3:] + "\n"
        elif (message == "chips"):
            for user in infoArray[0]:
                if user[1] == addr:
                    sendDataToPlayer(user,str(user[2]),port)
        for user in infoArray[0]:
            sendDataToPlayer(user,messages,port)

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
    for user in infoArray[0]:
        if (user[2] <= 1):
            #gameover code
            keepGoing = False
    #make deck
    #shuffle deck
    while(roundNumber <= maxRounds and keepGoing == True):
        for user in infoArray[0]: # Ante up
            user[2] -= 1
        #deal to players*
        for user in infoArray[0]:
            sendString = "Hand: "
            for card in user[3]:
                sendString += str(card) 
            sendDataToPlayer(user,sendString,port)
        replies = 0
        while (replies < playerCount): # Check if users have replied to bet
            (message, addr) = UDPSock.recvfrom(buf)
            message = message.decode('utf8')
            if (message[:3] != "msg"):
                replies += 1
        #set the river
        for user in infoArray[0]:
            sendString = "River: " + "Hand: "
            for card in user[3]:
                sendString += str(card) 
            sendDataToPlayer(user,sendString,port)
        replies = 0
        while (replies < playerCount): # Check if users have replied to bet
            (message, addr) = UDPSock.recvfrom(buf)
            message = message.decode('utf8')
            if (message[:3] != "msg"):
                replies += 1
        #add one to river
        while (replies < playerCount): # Check if users have replied to bet
            (message, addr) = UDPSock.recvfrom(buf)
            message = message.decode('utf8')
            if (message[:3] != "msg"):
                replies += 1
        #add one to river
        while (replies < playerCount): # Check if users have replied to bet
            (message, addr) = UDPSock.recvfrom(buf)
            message = message.decode('utf8')
            if (message[:3] != "msg"):
                replies += 1
        

                
        for user in infoArray[0]:
            if (user[2] <= 1):
                #gameover code
            keepGoing = False
        roundNumber += 1

else:
    print("Wrong game :( ")
pp    
UDPSock.close()
