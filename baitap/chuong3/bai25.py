for i in range(2,10000):
    snt1 = 1
    for j in range(2,i//2+1):
        if i%j==0:
            snt1 = 0
            break
    if snt1==1:
        snt2 = 1
        for j in range(2,(i+2)//2+1):
            if (i+2)%j==0:
                snt2 = 0
                break
        if snt2==1:
            print(i,i+2)