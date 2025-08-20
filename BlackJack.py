from Deck import *
from Player import *

class BlackJack:
    'a basic BlackJack game'

    def __init__(self, player='', numberOfPlayers=2):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = {}
        self.casinoPlayer = ''
        
        self.players['Dealer'] = BlackJackPlayer('Dealer')
        if type(player) != BlackJackPlayer:
            startingPoint = 0
        else:
            startingPoint = 1
            self.players[player.name] = player
            self.casinoPlayer = player.name
        

        for i in range(startingPoint,numberOfPlayers):
            playerName = input('Enter your name: ')
            try:
                playerWagerAmount = int(input("Enter your bank amount: "))
            except:
                print('You must enter a number.  Default of 100 has been awarded')
            self.players[playerName] = BlackJackPlayer(playerName, playerWagerAmount)

            try:
                wager = int(input("How much do you want to bet? "))
                self.players[playerName].currentBet = wager
                self.players[playerName].moneyAmount -= wager
            except:
                print('You must enter a number.  Default of 10 has been placed.')
                self.players[playerName].currentBet = 10
                self.players[playerName].moneyAmount -= 10
        
            
        
        self.play()

    def dealCards(self, player):
        cnt = 0
        while cnt < 2 :
            self.players[player].currentHand.append(self.deck.dealCard())
            cnt += 1
        self.players[player].handValue = self.calculateHand(self.players[player].currentHand)

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
        gameOver = 0
        playerHand = 0
        dealerHand = self.players['Dealer'].handValue
        for p in self.players:
            self.players[p].handValue = self.calculateHand(self.players[p].getCurrentHand())
            if p.lower() != 'dealer':
                playerHand = self.players[p].handValue
        
            if playerHand == 21:
                self.players[p].winningHand()
                print('{} wins with a score of {}. You have won {}!'.format(self.playerName, playerHand, self.players[p].currentBet*1.5))
                
                gameOver+=1
            elif playerHand > dealerHand and playerHand <= 21:
                self.players[p].winningHand()
                print('{} wins with a score of {}.  You have won {}!'.format(p, playerHand, self.players[p].currentBet*1.5))
                print('Dealer has a score of {}'.format(dealerHand))
                
                gameOver+=1
            elif playerHand > 21:
                print('Dealer has a score of {}'.format(dealerHand))
                return gameOver+1
            elif dealerHand > playerHand and dealerHand <= 21:
                print('Dealer has a score of {}'.format(dealerHand))
                print('{} lost with a score of {}'.format(p, playerHand))
                gameOver+=1
            elif dealerHand > 21:
                print('Dealer has a score of {}'.format(dealerHand))
                print('Winner Winner Chicken Dinner!')
                gameOver+=1
        
        return gameOver

    
    def playerChoice(self, choice, player):
        if choice == 0:
            self.players[player].getCurrentHand().append(self.deck.dealCard())
            self.players[player].handValue = self.calculateHand(self.players[player].getCurrentHand())

    def play(self):
        
        inGame = 0
        playAgain = 'y'
        while playAgain.lower().find('y') > -1:
            for player in self.players:
                if len(self.players[player].currentHand) == 0:
                    self.dealCards(player)
                    print("{}'s hand is: {}".format(player, self.players[player].currentHand))
            choice = 0
            shouldContinue = 0
            currentValue = 0
            while shouldContinue < len(self.players.keys()):
                try:
                    for player in self.players:

                        while choice == 0:
                            if self.players['Dealer'].handValue < 17 and player.lower() == 'dealer':
                                print('Dealers hand is {}.  They must Hit'.format(self.players['Dealer'].getCurrentHand()))
                                choice = 0
                            else:
                                choice = int(input('{}\'s turn.  Enter 0 for Hit and 1 for Stay: '.format(player)))

                            self.playerChoice(choice, player)
                            print("{}'s hand is: {}".format(player, self.players[player].currentHand))
                            if self.players[player].handValue > 21:
                                print('{}\'s hand is over 21.  You lose!'.format(player))
                                shouldContinue += 1
                                break
                            if choice == 1:
                                shouldContinue += 1
                                choice = 0
                                break
                        if self.players['Dealer'].handValue > 21:
                            shouldContinue += 3
                            break
                except:
                    print('You must enter 0 or 1')


            inGame = self.evaluate(player)
            if inGame >= 1:
                
                playAgain = input('Do you want to play again? (Yes/No) ')
        return self.players[self.casinoPlayer].moneyAmount 

                
           
                


        

        



if __name__ == "__main__":
    game = BlackJack()
#order of events
# initiate BlackJack
# Shuffle Deck
# Deal Cards to all players
# Evaluate both hands