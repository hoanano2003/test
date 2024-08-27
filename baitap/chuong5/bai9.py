class tamGiac:
    def __init__(self,a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
    def chuVi(self):
        return self.a+self.b+self.c
    def dienTich(self):
        p = self.chuVi()/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
class tamGiacCan(tamGiac):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def chuVi(self):
        return self.a + self.b*2
    def dienTich(self):
        p = self.chuVi()/2
        return (p*(p-self.a)*((p-self.b)*2))**0.5
class tamGiacDeu(tamGiacCan):
    def __init__(self, a=0):
        self.a = a
    def chuVi(self):
        return self.a*3
    def dienTich(self):
        p = self.chuVi()/2
        return (p*((p-self.a)*3))**0.5
        