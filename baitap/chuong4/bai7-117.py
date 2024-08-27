def chuvi(c1,c2,c3):
    return c1+c2+c3
def dientich(c1,c2,c3):
    p = chuvi(c1,c2,c3)/2
    return (p*(p-c1)*(p-c2)*(p-c3))**0.5
xa,ya=eval(input("Nhap toa do diem a(x,y): "))
xb,yb=eval(input("Nhap toa do diem b(x,y): "))
xc,yc=eval(input("Nhap toa do diem c(x,y): "))
c1 = ((xb-xa)**2
+(yb-ya)**2)**0.5
c2 = ((xc-xa)**2+(yc-ya)**2)**0.5
c3 = ((xc-xb)**2+(yc-yb)**2)**0.5
print(chuvi(c1,c2,c3))
print(dientich(c1,c2,c3))