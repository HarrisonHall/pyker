# Bullet UML for development process

## Outline
### main.py
Program which all player run and interact with in order to play the game.
### server.py
Program which all player's main.py programs interact with in order to send and recieve data to allow for the game to be played.
### deck.py
Creates a standard deck of 52 cards, draws a card, and shuffles the deck.
### hands.py
Evaluates the player's hand for the standard poker hands.
### texas.py
Creates the community cards and deals cards from the deck to the flop, turn, and river. Also deals an initial 2 cards to all players.

## Functions

### main.py
* Client side file to run
* Also must be ran if server wants to play

### server.py
* Run by server
* Manages game
* Inputs (requests from user)
  * game
  * port
  * number of rounds
  * number of chips
* Functions only called by self
  

### deck.py
* Card objects
* Player
  * Object
    * name
    * money
    * hand
* Functions
  * Player
    *
  * Deck
    * Shuffle
    * Reset

### texas.py
* game
* functions
  * initialDeal(infoArray) - clears player hand and deals 2 cards to each
  * initRiver(infoArray) - clears river and draws 3 cards to it
  * plusRiver(infoArray) - adds one card to river
  * replaceHand(infoArray, playerChoice) - takes player's choice of 5 cards from hand and river and replaces their hand with it

### blackjack.py
* game
* functions
  * initialDeal(infoArray) - deals 2 cards to each player; server must print first card of each player to everybody
  * hitPlayer(infoArray, currIp) - deals one card to the specified player; if player wants to double down, then execute the function, double their bet, and do not allow a second execution
 
### players.txt
* contains list of players
* ex. "john 127.0.0.1"
* players must match this name
* name must be lowercase
* no unnecessary spaces
