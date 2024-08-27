class Shape:
    def __init__(self,color):
        self.color = color
    def __str__(self):
        return "hinh co mau {}".format(self.color)
class Circle(Shape):
    def __init__(self, color,r):
        super().__init__(color)
        self.r = r
    def __str__(self):
        return "hinh tron mau {}, ban kinh {}".format(self.color,self.r)
    def get_area(self):
        return 3.14*self.r**2
class Rectangle(Shape):
    def __init__(self, color,l,w):
        super().__init__(color)
        self.l = l
        self.w = w
    def __str__(self):
        return "hinh chu nhat mau {}, chieu dai {}, chieu rong {}".format(self.color,self.l,self.w)
    def get_area(self):
        return self.l*self.w
class Square(Rectangle):
    def __init__(self, color, c):
        Shape.__init__(color)
        self.c = c
    def __str__(self):
        return "hinh vuong mau {}, canh {}".format(self.color,self.c)