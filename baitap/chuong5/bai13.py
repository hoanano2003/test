from math import pi
class circle:
    def __init__(self,r,x,y):
        self.r = r
        self.x = x
        self.y = y
    def chuvi(self):
        return 2*pi*self.r
    def dienTich(self):
        return pi*self.r**2