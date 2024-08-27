import random as r
A = set()
while(len(A)<10):
    A.add(r.randint(2,1000))
print(A)
B = set()
for x in A:
    for i in range(2,x+1):
        if x%i==0:
            snt = 1
            for j in range(2,i//2+1):
                if i%j==0:
                    snt = 0
            if snt == 1:
                B.add(i)
print(B)