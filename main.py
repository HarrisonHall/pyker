#main.py
import os
import sys
from socket import *

buf = 1024

host = input("Enter server ip: ")
port = int(input("Enter port number: "))
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
userName = input("Enter your name: ")
UDPSock.sendto(userName.encode('utf8'), addr)

started = False
newAddr = ("",port+1)
newSock = socket(AF_INET,SOCK_DGRAM)
newSock.bind(newAddr)

#Wait for the game to begin
while(started == False):
    (startString,newAddr) = newSock.recvfrom(buf)
    startString = str(startString.decode('utf8'))
    if startString == "t":
        started = True
        print("It started, this works!")
    else:
        print(startString)
        
#Manage betting process loop
#Card picking loop
recieveString = "im crying im so sad this better frickin work"
while(recieveString[:8] != "The Winn"):
    (recieveString,newAddr) = newSock.recvfrom(buf) #new
    recieveString = str(recieveString.decode('utf8'))
    if (recieveString[0] == "9" or recieveString[0] == " "):
        recieveString = recieveString[1:]
        userInput = input(recieveString + " ")
        UDPSock.sendto(userInput.encode('utf8'), addr) #new
        print("sent")
    else:
        print(recieveString)

    

(gameEndString,addr) = newSock.recvfrom(buf)
gameEndString = str(startString.decode('utf8'))
print(gameEndString)
print("Thanks for playing!")
