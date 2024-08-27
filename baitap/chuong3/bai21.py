dem = 0
for i in range(2,10000):
    snt = 1
    for j in range(2,i//2+1):
        if i%j==0:
            snt = 0
            break
    if snt==1:
        dem += 1
print(dem)