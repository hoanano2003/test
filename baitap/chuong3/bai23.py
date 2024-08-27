n = int(input("Nhap N: "))
tongUoc = 1
for i in range(2,n//2+1):
    if n%i==0:
        tongUoc += i
if n==tongUoc:
    print(n,"la so hoan hao")
else:
    print(n,"khong la so hoan hao")