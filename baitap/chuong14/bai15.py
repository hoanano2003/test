import random as r
A = set()
while(len(A)<100):
    A.add(r.randint(1,1000))
B = set()
temp = list(A)
while(len(B)<20):
    B.add(r.choice(temp))
C = set()
temp = list(B)
while(len(C)<10):
    C.add(r.choice(temp))