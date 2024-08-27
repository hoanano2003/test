n = int(input("Nhap N: "))
soUocNguyenTo = 0
for i in range(2,n+1):
    if n%i==0:
        snt = 1
        for j in range(2,i//2+1):
            if i%j==0:
                snt = 0
                break
        if snt==1:
            soUocNguyenTo += 1
print(soUocNguyenTo)
tongUocThucSu = 0
for i in range(1,n//2+1):
    if n%i==0:
        tongUocThucSu += i
print(tongUocThucSu)
tongBinhPhuong = 1
for i in range(2,n+1):
    tongBinhPhuong += i**2
print(tongBinhPhuong)