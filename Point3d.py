from Point import *

class NoZAxisError(Exception):
    pass

class Point3d(Point):

    def __init__(self, xcord=0,ycord=0,zcord=0):
        Point.__init__(self,xcord=xcord, ycord=ycord)
        self.z = zcord

    def __add__(self, x_cord, y_cord, z_cord):
        Point.__add__(self,x_cord,y_cord)
        self.z += z_cord

    def __eq__(self,anotherPoint):
        retVal = Point.__eq__(anotherPoint=anotherPoint)
        try:
            if retVal is True:
                return self.z == anotherPoint.z
            else:
                return False
        except NoZAxisError as nz:
            print('You don\'t have a z axis')
            print(nz)
    

    def __str__(self):
        val = Point.__str__(self)
        val = val.replace(')', ',{})'.format(self.z))
        return val

    def __repr__(self):
        val = Point.__repr__(self) 
        val += ', zcord: {}'.format(self.z)
        return val

    def setz(self,zcord):
        self.z = zcord

    #in ppt as a 'Replacer'
    #focuses only on new logic
    def get(self):
        return (self.x, self.y, self.z)
    
    #in ppt as a 'Extender'
    #uses preexisting logic and building upon it
    def move(self,move_x,move_y,move_z):
        Point.move(self,move_x,move_y)
        self.z += move_z
    

