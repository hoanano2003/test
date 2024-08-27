def tongN(n):
    tong = 0
    for i in range(1,n+1):
        tong += i
    print(tong)
def nguyenToCungNhau(m,n):
    tong1 = tong2 = 0
    for i in range(1,m):
        if m%i==0:
            tong1 += i
    for i in range(1,n):
        if n%i==0:
            tong2 += i
    if tong1==1 and tong2==1:
        print("hai so nay nguyen to cung nhau")
    else:
        print("hai so nay khong nguyen to cung nhau")
def chuyenDoiThoiGian(s):
    h = s//3600
    m = (s - h*3600)//60
    s = s - h*3600 - m*60
    print(h,"Gio",m,"Phut",s,"Giay")
def abs(a,b):
    if a-b>=0:
        print(a-b)
    else:
        print(b-a)
# tongN(6)
# nguyenToCungNhau(11,5)
# chuyenDoiThoiGian(3678)
abs(-3,4)