n = int(input("Nhap N: "))
snt1 = 1
for i in range(2,n//2+1):
    if n%i==0:
        snt1 = 0
        m = n+1
        snt2 = 1
        while 1:
            for j in range(2,m//2+1):
                if m%j==0:
                    snt2 = 0
                    break
            if snt2==1:
                print(m)
                break
            m += 1
            snt2 = 1
        break
        
if snt1==1:
    print(n)