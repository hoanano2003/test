from telnetlib import DO


year = int(input("Nhap vao nam can kiem tra: "))
if(year%400==0 or (year%4==0 and year%100!=0)):
    print("Nam nhuan")
else:
    print("Nam khong nhuan")