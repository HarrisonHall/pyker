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
while(started == False):
    (startString,addr) = newSock.recvfrom(buf)
    startString = str(startString.decode('utf8'))
    if startString == "start":
        started = True
        print("It started, this works!")
    else:
        print(startString)
        print("Something is not right...")

UDPSock.close()
sys.exit()
