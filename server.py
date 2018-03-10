#server.py
import os
from socket import *

print("\nWelcome to Pyker!")
print("Created by Harrison, Jackie, and Jacky")

#Setup
port = int(input("What is the port number: "))
print("Choose a game.")
gameChosen = input("texas(t): ")
maxRounds = input("Number of rounds: ")
chipNumber = input("Number of chips: ")

#Open up files to get ip and name associated
playerList = []
IPFile = open("ip.txt","r")
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
    playerName = playerName.decode('utf-8')
    for user in playerList:
        if playerName in user:
            playersJoined += 1
            print("Player",playerName,"has joined.",str(playerCount-playersJoined),"left.")
            user.append(chipNumber) #name, ip, chips, [card1, card2, ...]

print("\nThe game has begun.\n")

if gameChosen == "t":
    #Game logic goes here
    roundNumber = 1
    while(roundNumber <= maxRounds):
        roundNumber += 1
else:
    print("Wrong game :( ")
    UDPSock.close()
    sys.exit()


UDPSock.close()
sys.exit()
