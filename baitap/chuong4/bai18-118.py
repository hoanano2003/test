def generatorPrimes(n):
    a = []
    for i in range(2,n+1):
        snt = 1
        for j in range(2,i//2+1):
            if i%j==0:
                snt = 0
        if snt == 1:
            a += [i]
    return tuple(a)
n = int(input("Nhap so tu nhien n: "))
print(generatorPrimes(n))