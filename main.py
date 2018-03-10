#main.py
import os
import sys
from socket import *

host = input("Enter server ip: ")
port = int(input("Enter port number: "))
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
data = input("Enter your name: ")
UDPSock.sendto(data.encode('utf-8'), addr)

started = False
while(started == False):
    break    


UDPSock.close()
sys.exit()
