class Card:
    'represents a playing card'

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return '{} of {}\'s'.format(self.rank,self.suit)
    
    def __str__(self):
        return 'Card({},{})'.format(self.rank, self.suit)

    def getRank(self):
        'returns the rank'
        return self.rank

    def getSuit(self):
        'returns the suit'
        return self.suit