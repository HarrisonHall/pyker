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
    if startString == "start":
        started = True
        print("It started, this works!")
    else:
        print(startString)
        print("Ooops. Try restarting server and main.")
        UDPSock.close()
        sys.exit()

#Game has begun
#Game proceeds as following:
# 1) Wait for update
# 2) Send Command
#    a) If command is invalid, try again (Test client side)
#    b) If command is message, allow another command
#    Total List of commands: fold, bet 'amount, quit, message

#recieve beginning hand
(hand,addr) = newSock.recvfrom(buf)
hand = str(startString.decode('utf8'))
print("Bet: Hand:",startString)

returnInfo = ""
while(returnInfo != "game over"):
    sendInfo = "msg"
    while (sendInfo[0:3] == "msg"):
        sendInfo = input("Command: ")
        UDPSock.sendto(sendInfo.encode('utf8'), addr)
    (hand,addr) = newSock.recvfrom(buf)
    hand = str(startString.decode('utf8'))
    print("Bet: Hand:",startString)
    
UDPSock.close()
