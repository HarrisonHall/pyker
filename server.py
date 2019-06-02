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
        self.last_command = "h"
        
    def busted(self):
        tot = 0
        for card in hand:
            tot += card.val()
        return True if (tot > 21) else return False
    
    def is_over(self):
        return (self.busted() or self.last_command == "q")
    
    def score(self):
        tot = 0
        for card in hand:
            tot += card.val()
        return tot    
        

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
deck = deck.Deck()
while [player.is_over() for player in players] != [True for player in players]:
    for player in players:
        if player.last_command == "h":
            player.hand.append(deck.draw())
            player.last_command = ""
            while player.last_command not in ["h","q"]:
                player.connection.sendall(str(player.hand)+" [h]it or [q]uit?")
                player.last_command = player.connection.recv(10)
                
## End game                
for player in players:
    player.sendall("Player Scores: "+str([str(player.ip_address)+str(player.score()) for player in players]) + "GAME END")
    player.connection.close()
    
