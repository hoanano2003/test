ss = int(input("Nhap tong so giay: "))
a = ss//3600
b = (ss-a*3600)//60
c = ss-a*3600-b*60
print(a,"gio",b,"phut",c,"giay")