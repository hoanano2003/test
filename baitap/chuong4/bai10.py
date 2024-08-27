def convert():
    a=int(input("Nhap so gio: "))
    b=int(input("Nhap so phut: "))
    c=int(input("Nhap so giay: "))
    x = a/24+b/1440+c/86400
    print(x)
convert()