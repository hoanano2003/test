n = int(input("Nhap N: "))
tong = 0
for i in range(1,n+1):
    tong += i**2
print(tong)
print((n*(n+1)*(2*n+1))/6)
x = tong == (n*(n+1)*(2*n+1))/6
print(x)