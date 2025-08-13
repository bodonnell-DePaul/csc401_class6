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

    def setName(self,theName):
        self.name = theName

    def get(self):
        return (self.x,self.y)

    def move(self,dx,dy):
        self.x += dx
        self.y += dy
