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
UDPSock.sendto(userName.encode('utf-8'), addr)

started = False
while(started == False):
    (startString,addr) = UDPSock.recvfrom(buf)
    if startString == "start":
        started = True
        print("It started, this works!")

UDPSock.close()
sys.exit()
