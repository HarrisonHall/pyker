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
    (startString,addr) = newSock.recvfrom(buf)
    startString = str(startString.decode('utf8'))
    if startString == "t":
        started = True
        print("It started, this works!")
    else:
        print(startString)
        print("Ooops. Try restarting server and main.")
        UDPSock.close()
        sys.exit()
        
#Manage betting process loop
#Card picking loop
(gameEndString,addr) = newSock.recvfrom(buf)
gameEndString = str(startString.decode('utf8'))
print(gameEndString)
print("Thanks for playing!")
