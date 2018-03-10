#main.py
import os
from socket import *
host = "198.21.252.154" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
        data = input("Enter message to send or type 'exit': ")
        UDPSock.sendto(data.encode('utf-8'), addr)
        if data == "exit":
            break
UDPSock.close()
os._exit(0)
