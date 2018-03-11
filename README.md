# Pyker
Poker in Python for CUhackit 2018. Currently running Texas Hold`em.

## Getting Started
The below instructions will help you get up and running with Pyker. Currently only works on a Linux terminal.

### Prerequisites
You will need Python 3.6.
Check if you have Python.
```
python -V
```
If not, run one of the following or what is necessary for your distribution.

Ubuntu
```
sudo apt-get install python3.6
```

Arch Linux
```
sudo pacman -S python
```

## Installing and Running
Make sure Python is installed. Then, clone the repository.
```
git clone https://github.com/HarrisonHall/pyker.git
```
The user who wants to run the server in which all other computers connect to should run
```
python server.py
```
Everybody who is playing (which can include the server computer) should run
```
python main.py
```
Everybody follows the on screen instructions.

## Outline
### main.py
Program which all player run and interact with in order to play the game.
### server.py
Program which all player`s main.py programs interact with in order to send and recieve data to allow for the game to be played.
### deck.py
Creates a standard deck of 52 cards, draws a card, and shuffles the deck.
### hands.py
Evaluates the player`s hand for the standard poker hands.
### texas.py
Creates the community cards and deals cards from the deck to the flop, turn, and river. Also deals an initial 2 cards to all players.
