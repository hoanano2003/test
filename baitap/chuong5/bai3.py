class QuadrilSquare:
    def __init__(self,w=0,h=0):
        self.w = w
        self.h = h
    def chuVi(self):
        return (self.w+self.h)*2
    def dienTich(self):
        return self.w*self.h
h1 = QuadrilSquare(4,5)
print(h1.chuVi())
print(h1.dienTich())