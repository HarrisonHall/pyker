# server.py

import socket
import sys
from modules import deck
from modules import hands

number_of_players = int(input("How many players? >>> ")) 
players = []

class Player:
    def __init__(self,ip_address,connection):
        self.ip_address = ip_address
        self.hand = []
        self.connection = connection
        self.last_command = ""

## Connect
try:
    print("Your IP is",socket.gethostbyname(socket.gethostname()))
    port = int(input("Port Number >>> "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',port))
    sock.listen(number_of_players)
except:
    print("Failure at connection setup")
    sys.exit()
    
while len(players) < number_of_players:
    connection, client_address = sock.accept()
    players.append(Player(client_address,connection))

## Play game (blackjack)
### TODO


