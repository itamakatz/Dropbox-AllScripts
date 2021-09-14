import msvcrt
import random
from enum import Enum

rank_str = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"];

suit_str = ["Clubs", \
			"Diamonds", \
			"Hearts", \
			"Spades"];

class Suit(Enum):
	Clubs, Diamonds, Hearts, Spades = range(4);

class Rank(Enum):
	R_2, R_3, R_4, R_5, R_6, R_7, R_8, R_9, R_10, Jack, Queen, King, Ace = range(13);

class Card:

	def __init__(self, suit, rank):
		self.suit = suit;
		self.rank = rank;

	def get_rank(self):
		return self.rank.value;

	def __str__(self):
		return "\t%s, %s" % (suit_str[self.suit.value], rank_str[self.rank.value])

class Deck_of_cards:

	def __init__(self):
		self.deck_of_cards = [];
		for s in Suit:
			for r in Rank:
				self.deck_of_cards.append(Card(s, r));
		random.shuffle(self.deck_of_cards);

	def display_deck_of_cards(self):
		for card in self.deck_of_cards:
			print(card);

	def pop(self):
		return self.deck_of_cards.pop(0);

class Hand:

	def __init__(self, name, Deck_of_cards, num_of_cards):
		self.name = name;
		self.cards = [Deck_of_cards.pop() for x in range(0,num_of_cards)];
		self.cards.sort(key = lambda x: x.get_rank());

	def display_hand(self):
		print("%s cards: \n" % self.name);
		for card in self.cards:
			print(card);
		print();


def wait_input_to_exit():
	msvcrt.getch();

print("=== Starting Program ===\n");

new_deck = Deck_of_cards();

player_1 = Hand("Player 1", new_deck, 2);
player_2 = Hand("Player 2", new_deck, 2);
dealer = Hand("Dealer", new_deck, 2);
community_cards = Hand("Community Cards", new_deck, 5);

player_1.display_hand();
player_2.display_hand();
dealer.display_hand();
community_cards.display_hand();

print("\nPlease press any key to exit");
wait_input_to_exit();


