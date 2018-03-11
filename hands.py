import deck
import collection

RoyalF = 900
StraightF = 800
FourKind = 700
FullHouse = 600
Flush = 500
Straight = 400
ThreeKind = 300
TwoPair = 200
Pair = 100

#takes all functions below to
#calculate point total of hand
def evaluate(input):
	points = 0
	highpoint = 0

	points+=royalF(input)
	if royalF(input) == 0:
		if royal(input) != 0:
			points += royal(input)

	points+=straightF(input):
	if straightF(input) == 0:
		if straight(input) != 0:
			points += straight(input)

	if multi(input) > 100:
		points += multi(input)
	if multi(input) == 4:
		points += FourKind
	if multi(input) == 3:
		points += ThreeKind
	if multi(input) == 2:
		points += Pair

	if flush(hand) != 0:
		points += flush(hand)

	for card in input:
		highpoint = highcard(card, highpoint)

	points += highpoint

	return points


#converts the suit to a
#numeric value from 0-3
#then multiplies by 13 for
#point value of suit
def conversion(suit)
	suitNum = 0
	points = 0
	if suit == 'C':
		suitNum = 0
	elif suit == 'D':
		suitNum = 1
	elif suit == 'H':
		suitNum = 2
	elif suit == 'S':
		suitNum = 3
	points = suitNum * 13
	return points

#checks card to see if high card
#returns point value of card
def highCard(input, highCard):
	if input.rank > 1:
		currCard = input.rank
			+ conversion(input.rank)
	else
		currCard = input.rank
			+ 13 + conversion
	if currCard > highCard:
		highCard = currCard
	return highcard

#checks hand for Pair, 2 pair,
#3 of a kind, Full house, and
#4 of a kind
def multi(hand):
	points = 0
	count = collection.count()
	for card in hand:
		count[card.rank] += 1
	c_s = sort(count.values(), reverse = true)
	if 3 in c_s and 2 in c_s:
		return FullHouse
	for last, current in zip(c_s,c_s[1:]):
		if last == 2 and current == 2:
			return TwoPair
	return c_s[0]

#checks hand for flush
def flush(hand):
	h_s = sort(hand)
	suit = h_s[0].suit
	for card in h_s[1:]:
		if suit != card.suit:
			return False
	return Flush

#checks for straight
def striaght(hand):
	h_s = sort(hand)
	rank = h_s[0].rank
	for card in h_s[1:]:
		if rank != card.rank - 1:
			return False
		rank = card.rank
	return Straight

#checks for straight flush
def straightF(hand):
	if flush(hand) == 0:
		return False
	if straight(hand) == 0:
		return False
	return StraightF

#checks for 10-A straight
def royal(hand):
	h_s = sort(hand, reverse = True)
	if h_s[0] != 13:
		return False
	if h_s[1] != 12:
		return False
	if h_s[2] != 11:
		return False
	if h_s[3] != 10:
		return False
	if h_s[4] != 1:
		return False
	return Straight

#checks for royal flush
def royalF(hand):
	if flush(hand) == 0:
		return False
	if royal(hand) == 0:
		return False
	return RoyalF
