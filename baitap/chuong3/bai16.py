n = int(input("Nhap N: "))
tong2n = 0
for i in range(2*n+1):
    tong2n += i
print("Tong cac so tu 1 den",2*n,"la: ",tong2n)
tongle = 0
for i in range(1,n,2):
    tongle += i
print("Tong cac so le tu 1 den",n,"la: ",tongle)
tongchan = 0
for i in range(2,n,2):
    tongchan += i
print("Tong cac so chan tu 1 den",n,"la: ",tongchan)