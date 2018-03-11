# Pyker
Poker in Python for CUhackit 2018. Currently running Texas Hold'em.

## About
  Pyker (Python + Poker, omg!) was created by Harrison Hall, Jackie Doan, and Jacky Wong during the Clemson University Hackit 2018 competition. Pyker allows players to play poker (Texas Hold'em and Blackjack) with each from different Unix terminals over the same internet connection. Over the course of 23 hours, we coded this project from scratch, with help from mentors and, of couse, lots of documentation.
  The three of us have lately been in a bit of a poker binge, but are often at the disadantage of finding a place to play on campus on a saturday night. With our custom engine we can play whatever poker~esque games we can think of (and code). THe only requirement is for the players to know each others ip addresses.
  During development we had a few stretch goals:
* Add a messaging feature
* An AI to play with
* More games asside from Texas Hold'em
* A help menu
* In-game hand statistics
* A gui version

During development we did have time to add one more game, Blackjack. We also were able to impliment a primitive messaging system. 

## Getting Started
The below instructions will help you get up and running with Pyker. Pyker currently only works on a Linux terminal.

### Prerequisites
You will need Python 3.6.
Check if you have Python.
```bash
python -V
```
If not, run one of the following or what is necessary for your distribution.

Ubuntu
```bash
sudo apt-get install python3.6
```

Arch Linux
```bash
sudo pacman -S python
```

## Installing and Running
Make sure Python is installed. Then, clone the repository.
```bash
git clone https://github.com/HarrisonHall/pyker.git
```
The user who wants to run the server in which all other computers connect to should run
```bash
python server.py
```
Everybody who is playing (which can include the server computer) should run
```bash
python main.py
```
Everybody follows the on screen instructions. Make sure to set up the players.txt file. 
