from Card import *
from Deck import *

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcord=0,ycord=0):
        'this is the Point constructor'
        self.x = xcord
        self.y = ycord
        self.name = 'MyPointxy'

    def __add__(self, anotherPoint):
        '''Returns a new point as a result of the addition
        original points are unchanged'''
        vals = anotherPoint.get()

        return Point(self.x+vals[0], self.y+vals[1])

    def __sub__(self, anotherPoint):
        vals = anotherPoint.get()
        self.x -= vals[0]
        self.y -= vals[1]

        return Point(self.x, self.y)

    def __mul__(self, anotherPoint):
        vals = anotherPoint.get()
        self.x *= vals[0]
        self.y *= vals[1]
        return Point(self.x, self.y)

    def __truediv__(self,anotherPoint):
        vals = anotherPoint.get()
        self.x /= vals[0]
        self.y /= vals[1]
        return Point(self.x, self.y)

    def __floordiv__(self,anotherPoint):
        vals = anotherPoint.get()
        self.x //= vals[0]
        self.y //= vals[1]
        return Point(self.x, self.y)

    def __eq__(self, anotherPoint):
        return self.x == anotherPoint.x and self.y == anotherPoint.y
    
    def __ne__(self, anotherPoint):
        return self.x != anotherPoint.x or self.y != anotherPoint.y
    
    def __gt__(self, anotherPoint):
        return self.x > anotherPoint.x or self.y > anotherPoint.y
    
    def __ge__(self, anotherPoint):
        return self.x >= anotherPoint.x or self.y >= anotherPoint.y
    
    def __lt__(self, anotherPoint):
        return self.x < anotherPoint.x or self.y < anotherPoint.y
    
    def __le__(self, anotherPoint):
        return self.x <= anotherPoint.x or self.y <= anotherPoint.y
    
    def __repr__(self):
        return 'Point: x-cord: {}, ycord: {}'.format(self.x,self.y)
    
    def __str__(self):
        return 'Point({},{})'.format(self.x, self.y)
    
    def setx(self, xcord):
        'sets the x axis'

        self.x = xcord

    def sety(self,ycord):
        'sets the y axis'
        self.y = ycord

    def get(self):
        return (self.x,self.y)

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

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

