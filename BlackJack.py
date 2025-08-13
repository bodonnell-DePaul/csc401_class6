from Deck import *

class BlackJack:
    'a basic BlackJack game'

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.playerName = input('Enter your name')
        self.houseDealer = 'Dealer'
        self.players = {self.playerName: [], self.houseDealer: []}

    def dealCards(self):
        cnt = 0
        while cnt < 2 :
            for p in self.players:
                #temp = self.players[p]
                self.players[p].append(self.deck.dealCard())
            cnt += 1

    def calculateHand(self, playerHand):
        retVal = 0
        for card in playerHand:
            try:
                retVal += int(card.rank)
            except:
                if card.rank == 'A':
                    retVal += 1
                else:
                    retVal += 10

        return retVal

    def evaluate(self):
        playerHand = 0
        dealerHand = 0
        for p in self.players:
            if p.lower().find('dealer') > -1:
                playerHand = self.calculateHand(self.players[p])
            else:
                dealerHand = self.calculateHand(self.players[p])

        if playerHand == 21:
            print('{} wins with a score of {}'.format(self.playerName, playerHand))
        elif playerHand > dealerHand and playerHand <= 21:
            print('{} wins with a score of {}'.format(self.playerName, playerHand))
            print('Dealer has a score of {}'.format(dealerHand))
        elif playerHand > 21:
            print('Dealer has a score of {}'.format(dealerHand))
        elif dealerHand > playerHand and dealerHand <= 21:
            print('Dealer has a score of {}'.format(dealerHand))
            print('{} lost with a score of {}'.format(self.playerName, playerHand))

    



if __name__ == "__main__":
    game = BlackJack()
    game.dealCards()
    game.evaluate()
#order of events
# initiate BlackJack
# Shuffle Deck
# Deal Cards to all players
# Evaluate both hands