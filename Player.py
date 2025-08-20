class Account:
    'Player Account'
    def __init__(self, name='nobody'):
        self.typesOfplayers = []
        self.password = ''
        self.bank = 0

    def setName(self,name):
        self.name = name


class Player:
    'our base player class'
    def __init__(self, name):
        self.name = name


class BlackJackPlayer(Player):
    'our blackjack player'

    def __init__(self, name, moneyAmount=100):
        self.name = name
        self.moneyAmount = moneyAmount
        self.currentHand = []
        self.handValue = 0
        self.currentBet = 0

    def getCurrentHand(self):
        return self.currentHand
    
    def winningHand(self):
        self.moneyAmount += self.currentBet*1.5