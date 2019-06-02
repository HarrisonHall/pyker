# main.py
# Used by clients

import socket

END_KEY = "GAME END"

server_ip = input("What is the server IP address? >>> ")
port = int(input("What is the server Port? >>> "))
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.connect((host, port))

buf = ""
buf = serversocket.recv(100)
print(buf)
while END_KEY not in buf:
    serversocket.sendall(input(">>> "))
    buf = serversocket.recv(100)
    print(buf.replace("GAME END",""))
