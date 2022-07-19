# Rules of Blackjack:
# 
# Hit (take a card)
# Stand (end turn and stop without taking a card)
# Double (double wager, take a single card, and finish)
# Split (if the two cards have the same value, separate them to make two hands)
# Surrender (give up a half-bet and retire from the game)   
# 
# The dealer's hand is resolved by drawing until 17 or higher
# 
# A blackjack beats any hand that is not a blackjack (even one with a value of 21)
# Blackjacks are paid out at 3 to 2 odds

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def info(self):
        return f"{self.rank} of {self.suit}"
    def value(self):
        return rank_to_value[self.rank]

class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
    def display_cards(self):
        return [card.info() for card in self.cards]
    def is_ace(self):
        for card in self.cards:
            if card.rank == "Ace":
                return True
        return False
    def value_of_cards(self):
        total = sum([card.value() for card in self.cards])
        if self.is_ace():
            if total+10 > 21:
                return total
            return f"{total} or {total+10}"    
        return total

suits = ["♠", "♥", "♦", "♣"]
ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
rank_to_value = {"Ace":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7,
                "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}
deck = [Card(rank, suit) for rank in ranks for suit in suits]

def deal():
    global player0, dealer
    for x in range(2):
        player0.cards.append(random.choice(deck))
    dealer.cards.append(random.choice(deck))
    print("Cards have been dealt:")
def info():
    print(f"Player0's cards: {player0.display_cards()}")
    print(f"Player0's card value = {player0.value_of_cards()}")
    print(f"Dealer's cards: {dealer.display_cards()}")
    print(f"Dealer's card value = {dealer.value_of_cards()}")

print("\033[4m\tWelcome to Blackjack\t\033[0m")
# players = int(input("Number of players: "))
# decks = int(input("Number of decks: "))
dealer = Player("Dealer")
player0 = Player("Player0")
deal()
info()
