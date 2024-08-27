def f(m,n):
    sntMax = 0
    min = m if m<=n else n
    for i in range(2,min+1):
        snt = 1
        for j in range(2,i):
            if i%j==0:
                snt = 0
                break
        if snt == 1:
            if m%i==0 and n%i==0:
                sntMax = i
    return sntMax
print(f(44,22))