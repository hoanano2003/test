def f(m,n):
    min = m if m>n else n
    count = 0
    for i in range(1,min+1):
        if m%i==0 and n%i==0:
            count += 1
    return count