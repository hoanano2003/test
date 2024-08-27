class Triple:
    def __init__(self,ten,a=0,b=0,c=0,s=0):
        self.ten =  ten
        self.a = a
        self.b = b
        self.c = c
        self.s = s
    def update(self):
        self.s = self.a + self.b + self.c
    def change(self,a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
        self.s = a + b + c
    def triange(self):
        return self.a+self.b > self.c and self.b+self.c > self.a and self.a+self.c > self.b