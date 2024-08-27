def uocSoThucSu(n):
    dem = 0;
    for i in range(1,n//2+1):
        if n%i==0:
            dem += 1
    return dem
def kiemTraSnt(n):
    for i in range(2,n//+1):
        if n%i==0:
            return 0
    return 1
def demSoUocLe(n):
    dem = 0
    for i in range(1,n+1):
        if n%i==0 and i%2==1:
            dem += 1
    return dem
def demSoUocNguyenTo(n):
    dem = 0
    for i in range(2,n//2+1):
        if n%i==0:
            snt = 1
            for j in range(2,i//2+1):
                if i%j==0:
                    snt = 0
                    break
            if snt == 1:
                dem += 1
    if kiemTraSnt(n):
        return dem+1
    else:
        return dem
def tongUocSoThucSu(n):
    tong = 0
    for i in range(1,n//2+1):
        if n%i==0:
            tong += i
    return tong
print(demSoUocNguyenTo(20))