day, month, year = eval(input("Nhap vao ngay thang nam: "))
a = (31,29,31,30,31,30,31,31,30,31,30,31)
b = (31,28,31,30,31,30,31,31,30,31,30,31)
if(month>12):
    print("Du lieu khong hop ly")
else:
    if(year%400==0 or (year%4==0 and year%100!=0)):
        if(day<=a[month-1]):
            print("Du lieu hop ly")
        else:
            print("Du lieu khong hop ly")
    else:
        if(day<=b[month-1]):
            print("Du lieu hop ly")
        else:
            print("Du lieu khong hop ly")     