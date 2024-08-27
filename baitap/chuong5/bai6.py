import bai5
class tamgiac(bai5.Triple):
    def dienTich(self):
        self.update()
        p = self.s/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
    def RNgoaiTiep(self):
        return self.a*self.b*self.c/(4*self.dienTich())
    def RNoiTiep(self):
        return self.dienTich()/(self.s/2)
h1 = tamgiac("abc",3,4,5)
print(h1.dienTich())
print(h1.RNgoaiTiep())
print(h1.RNoiTiep())