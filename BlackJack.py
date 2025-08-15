from Deck import *

class BlackJack:
    'a basic BlackJack game'

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.playerName = input('Enter your name: ')
        self.houseDealer = 'Dealer'
        self.players = {self.playerName: [], self.houseDealer: []}
        self.play()

    def dealCards(self, player):
        cnt = 0
        while cnt < 2 :
            self.players[player].append(self.deck.dealCard())
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

    def evaluate(self, player):
        playerHand = 0
        dealerHand = 0
        gameOver = 0
        if player.lower().find('dealer') > -1:
            playerHand = self.calculateHand(self.players[player])
        else:
            dealerHand = self.calculateHand(self.players[player])

        if playerHand == 21:
            print('{} wins with a score of {}'.format(self.playerName, playerHand))
            return gameOver+1
        elif playerHand > dealerHand and playerHand <= 21:
            print('{} wins with a score of {}'.format(self.playerName, playerHand))
            print('Dealer has a score of {}'.format(dealerHand))
            return gameOver+1
        elif playerHand > 21:
            print('Dealer has a score of {}'.format(dealerHand))
            return gameOver+1
        elif dealerHand > playerHand and dealerHand <= 21:
            print('Dealer has a score of {}'.format(dealerHand))
            print('{} lost with a score of {}'.format(self.playerName, playerHand))
            return gameOver+1
        
        return gameOver

    
    def playerChoice(self, choice, player):
        if choice > 0:
            self.players[player].append(self.deck.dealCard())

    def play(self):

        
        
        inGame = 0
        playAgain = 'y'
        while playAgain.lower().find('y') > -1:
            for player in self.players:
                if len(self.players[player]) == 0:
                    self.dealCards(player)
                print("{}'s hand is: {}".format(player, self.players[player]))
                choice = 0
                while True:
                    try:
                        choice = int(input('Enter 0 for Hit and 1 for Stay'))
                        break
                    except:
                        print('You must enter 0 or 1')

                self.playerChoice(choice, player)
                inGame = self.evaluate(player)
                if inGame > 1:
                    playAgain = input('Do you want to play again? (Yes/No) ')
                    break
                print('Do you want to Hit or Stay?')
                


        

        



if __name__ == "__main__":
    game = BlackJack()
#order of events
# initiate BlackJack
# Shuffle Deck
# Deal Cards to all players
# Evaluate both hands