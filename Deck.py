from Card import *
from random import shuffle

class Deck:
    'a deck of cards'

    def __init__(self):
        self.deck = []
        suits = ['\u2660', '\u2661', '\u2662', '\u2663']
        ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))

    def __repr__(self):
        retVal = ''
        for card in self.deck:
            retVal += str(card)
        return retVal

    def shuffle(self):
        'shuffles the deck'
        shuffle(self.deck)

    def dealCard(self):
        'deals a card'
        return self.deck.pop(0)