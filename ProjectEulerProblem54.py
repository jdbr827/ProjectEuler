"""
Project Euler Problem 54 (Poker Hands)
"""
from collections import defaultdict

VALUE = 0
SUIT = 1
NUM_GAMES = 1000

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8
ROYAL_FLUSH = 9

JACK = 11
QUEEN = 12
KING = 13
ACE = 14


def run():
	p1wins = 0
	f = open("ProjectEulerProblem54Input", "r")
	for i in range(NUM_GAMES):
		game = f.readline()
		cards = game.split()
		hand1 = cards[:5]
		hand2 = cards[5:]
		if compare_hands(hand1, hand2):
			p1wins += 1
	print p1wins


def isFlush(hand):
	"""
	determines if the given hand is a flush
	"""
	suit = hand[0][SUIT]
	for card in hand[1:]:
		if card[SUIT] != suit:
			return False
	return True

def isStraight(values):
	"""
	returns True if the cards form a straight, false otherwise
	"""
	for i in range(1, 5):
		if values[i] != 1 + values[i-1]:
			return False
	return True


def card_values(hand):
	values = []
	for card in hand:
		if card[VALUE] == "T": 
			values.append(10)
		elif card[VALUE] == "J":
			values.append(JACK)
		elif card[VALUE] == "Q":
			values.append(QUEEN)
		elif card[VALUE] == "K":
			values.append(KING)
		elif card[VALUE] == "A":
			values.append(ACE)
		else:
			values.append(int(card[VALUE]))
	values.sort()
	return values


def compare_scores(score1, score2):
	"""
	Addresses the tiebreaker (both cards have )
	"""
	# Solve_tiebreaker (we could do this later but its easier to do now.)
	scores = zip(score1, score2)
	scores.reverse() 
	for (s1, s2) in scores:
		if s1 > s2:
			return True
		if s2 > s1: 
			return False
			
	pass


def compare_hands(hand1, hand2):
	"""
	compares the hands hand1 and hand2 as poker hands. 
	Returns True if hand1 wins, False if hand2 wins.
	"""
	score1 = score(hand1)
	score2 = score(hand2)
	p1wins = compare_scores(score1, score2)
	#print score1, score2, p1wins
	return p1wins

def make_freq_table(values):
	freq_table = defaultdict(lambda: 0)
	for val in values:
		freq_table[val] += 1
	return freq_table

def inverse_freq_table(freqs):
	inv_freq_table = {i : [] for i in range(1, 5)}
	for val in freqs:
		inv_freq_table[freqs[val]].append(val)
	return inv_freq_table



def score(hand):
	values = card_values(hand)

	if isFlush(hand):
		# all cards have different values

		if isStraight(values):
			# we have a straight flush, do we have a royal flush?
			if values[4] == ACE:
				return values + [0, ROYAL_FLUSH]
			else:
				return values + [0, STRAIGHT_FLUSH]
		else:
			return values + [0, FLUSH]
	else:
		if isStraight(values):
			return values + [0, STRAIGHT]

		else:
			# we are down to "frequency" hands
			inv_freqs = inverse_freq_table(make_freq_table(values))

			if inv_freqs[4]:
				return values + [inv_freqs[4][0], FOUR_OF_A_KIND]
			elif inv_freqs[3]:
				if inv_freqs[2]:
					return values + [inv_freqs[3][0], FULL_HOUSE]
				else:
					return values + [inv_freqs[3][0], THREE_OF_A_KIND]
			elif len(inv_freqs[2]) == 2:
				return values + [max(inv_freqs[2]), TWO_PAIR]
			elif len(inv_freqs[2]) == 1:
				return values + [inv_freqs[2][0], ONE_PAIR]
			else:
				return values + [0, HIGH_CARD]
				




	


run()