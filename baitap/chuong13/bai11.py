dic = {"Bui Viet Ha":8,"Nguyen Thanh Binh":9.5}
ten = input()
diem = int(input())
n = len(dic)
dic.update({ten:diem})
if len(dic) == n:
    print("Da cap nhap")
else:
    print("Da tao moi")