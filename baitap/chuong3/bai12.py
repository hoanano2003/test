import math
n = int(input("Nhap vao so tu nhien n: "))
kiemTra = 1
for i in range(2,int(math.sqrt(n))):
    if(n%i==0):
        kiemTra = 0
        break
if(kiemTra==1):
    print(n, "la so nguyen to")
else:
    print(n, "khong la so nguyen to")