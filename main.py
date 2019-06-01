# main.py
# Used by clients

import socket

END_KEY = "GAME END"

server_ip = input("What is the server IP address? >>> ")
port = int(input("What is the server Port? >>> "))
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.connect((host, port))

buf = ""
while buf != END_KEY:
    buf = serversocket.recv(100)
    serversocket.sendall(input(">>> "))
