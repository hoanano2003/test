for i in range(2,10000):
    tongUoc = 1
    for j in range(2,i//2+1):
        if i%j==0:
            tongUoc += j
    if i==tongUoc:
        print(i)