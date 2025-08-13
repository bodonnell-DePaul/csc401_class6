from Card import *
from Deck import *


class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='grunts'):
        self.species = species
        self.language = language


    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))






if __name__ == "__main__":
    p = Point()
    p.setx(10)
    p.sety(25)
    p.move(25,-10)

    p1 = Point(100,200)
    p1.move(-250, -500)

    p+=p1

    snoopy = Animal()
    snoopy.setSpecies('dog') 
    snoopy.setLanguage('bark')
    snoopy.speak()

    garfield = Animal()
    garfield.setSpecies('cat')
    garfield.setLanguage('meow and I talk')
    garfield.speak()

    c = Card('3', '\u2660')

    d = Deck()

    for card in d.deck:
        print(card)

    d.shuffle()

    for card in d.deck:
        print(card)

    

    lst = [p, 'i made a class', 12]
    
    print(lst)

