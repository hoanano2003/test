n = int(input("Nhap N: "))
dem = 0
for i in range(1,n//2+1):
    if n%i==0:
        dem += 1
print(dem)