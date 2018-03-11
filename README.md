# Pyker
Poker in Python for CUhackit 2018. Currently running Texas Hold'em and Blackjack.

## About
Pyker (Python + Poker, omg!) was created by Harrison Hall, Jackie Doan, and Jacky Wong during the 23-hour CUhackit (Clemson University Hackit) 2018 competition. Pyker allows players to play poker (Texas Hold'em and Blackjack) with each from different Unix terminals over the same internet connection. Over the course of 23 hours, we coded this project from scratch, with help from mentors and, of couse, lots of documentation.
  
The three of us have lately been in a bit of a poker binge, but are often at the disadantage of finding a place to play on campus on a saturday night. With our custom engine we can play whatever poker~esque games we can think of (and code). The only requirement is for the players to know each others IP addresses.

### Goals
Our initial goals were to simply be able to play poker with each other from our rooms via the command line. This, we accomplished. 

During development we had a few stretch goals:
* Add a messaging feature
* An AI to play with
* More games aside from Texas Hold'em
* A help menu
* In-game hand statistics
* A GUI version

During development we did have time to add one more game, Blackjack. We also were able to impliment a primitive messaging system. 

### What would we have done differently? 
A ton! And that's great, because it shows that we learned something. None of us were familiar with networking beforehand, and only one of us were familiar with python. We should have spent more than twenty minutes planning, and instead took an hour to create a thorough UML document, as it would have saved time and hardship later on. We should have probably used TCP instaed of the UDP protocol, but since we began the night not knowing the difference, we forgive ourselves. 

### Future Plans
We may impliment some of the stretch goals we did not have time to accomplish. Specifically, adding more games and in-game statistics. 

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

Fedora
```bash
sudo dnf install python3
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
