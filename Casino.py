from Player import *
from BlackJack import *

class Casino:
    'Our Shell'

    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.signedInAccount = ''
        self.signedIn = False
        self.signOnMenu = '''
        Welcome to {}\'s Casino!
        Select from the following options:
        \t1. Register an account
        \t2. Sign in
        '''.format(self.name)

        self.menu()

    def menu(self):

        while True:
            if self.signedIn is True:
                while True:
                    self.playMenu = '''
                    Hi {}!.  Thanks for coming.  
                    Here is your current account status
                    Name: {}
                    Balance: {}
                    Game Accounts: {}
                    Please select from the following options
                    \t1. Play BlackJack
                    \t2. Play Poker
                    \t3. Play Craps
                    \t4. Play Roulette 
                    \t5. Press 'q' to Quit
                    '''.format(self.signedInAccount.name, self.signedInAccount.name, 
                               self.signedInAccount.bank, self.signedInAccount.typesOfplayers)
                    print(self.playMenu)

                    gameSelection = input('Enter your selection: ')
                    if gameSelection == '1':
                        blackjackPlayer = ''
                        for player in self.signedInAccount.typesOfplayers:
                            if type(player) is 'BlackJackPlayer':
                                blackjackPlayer = player
                        if len(blackjackPlayer) == 0:
                            blackjackPlayer = BlackJackPlayer(self.signedInAccount.name)
                            
                        wager = int(input('How much do you want to wager? '))
                        blackjackPlayer.moneyAmount = wager
                        self.signedInAccount.bank -= wager
                        self.signedInAccount.bank += BlackJack(blackjackPlayer)
                    elif gameSelection == '2':
                        pass
                    elif gameSelection == '3':
                        pass
                    elif gameSelection == '4':
                        pass
                    elif gameSelection == '5':
                        pass
                    else:
                        print('Please select an appropriate option!')
            else:
                print(self.signOnMenu)
                val = input('Enter you choice: ')
                if val == '1':
                    self.registerAccount()
                if val == '2':
                    self.signIn()

    def registerAccount(self):
        print('To create an acount we need your name, password and amount you would like to gamble with.')
        account = Account()
        account.setName(input('Enter your name:'))
        temp = input('Enter your password: ')
        encrypt = ''
        for c in temp:
            encrypt+= str(ord(c))+ ' '

        account.password = encrypt

        account.bank = int(input('Enter the amount of money you want to lose.'))

        print('Great, thanks!  We look forward to taking your money!  Please sign in')
        self.accounts.append(account)




    def signIn(self):
        print('Enter your name and password!')
        name = input('Your name is: ')            
        password = input('Your password is: ')

        for a in self.accounts:
            decrypt = ''
            for c in password:
                decrypt += str(ord(c))+ ' ' 
            if decrypt == a.password and name == a.name:
                self.signedIn = True
                print('Hooray you have logged in!')  
                self.signedInAccount = a






if __name__ == "__main__":
    casino = Casino('Hooray for Money!')