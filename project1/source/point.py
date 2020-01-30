import math

class Point():
    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.X = x
        self.Y = y

    def __str__(self):
        return "%s %s\n"%(self.X, self.Y)

    def distanceTo(self,p):
        return math.sqrt( ((int(self.X)-int(p.X))**2)+((int(self.Y)-int(p.Y))**2) )
