# cau1
# def tuCuoiCung(str):
#     x = str.rfind(" ")
#     return str[x+1:]
# ds = []
# while(True):
#     temp = input("Nhap vao ho ten: ")
#     if temp =="":
#         break
#     ds.append(temp)
# dem = 0
# for i in ds:
#     if tuCuoiCung(i)=="Anh":
#         dem += 1
# print("So sinh vien co ten Anh la: ",dem)
# # cau 2
# dic = {"mahp":"","tenhp":"","sotc":0}
# n = int(input("Nhap so luong hoc phan: "))
# ds = []
# for i in range(n):
#     mahp = input("Ma hoc phan: ")
#     tenhp = input("Ten hoc phan: ")
#     sotc = int(input("So tin chi: "))
#     dic.update({"mahp":mahp,"tenhp":tenhp,"sotc":sotc})
#     ds.append(dic.copy())
# for i in ds:
#     if i["mahp"].find("TIN") == 0:
#         print("{0} | {1} | {2}".format(i["mahp"],i["tenhp"],i["sotc"]))
# s =  input("Nhap chuoi s: ")
# for i in ds:
#     if s.upper() in i["tenhp"].upper():
#         print(i["tenhp"])
# cau 3
class HoaDon:
    def __init__(self,maKH="",hoTen="",diaChi="",chiSoCu=0,chiSoMoi=0):
        self.maKH = maKH
        self.hoTen = hoTen
        self.diaChi = diaChi
        self.chiSoCu = chiSoCu
        self.chiSoMoi = chiSoMoi
    def getMaKH(self):
        return self.maKH
    def getLuongDienTT(self):
        return self.chiSoMoi - self.chiSoCu
    def hienThi(self):
        print("{0} | {1} | {2} | {3}".format(self.maKH,self.hoTen,self.diaChi,self.getLuongDienTT()))
    def __gt__(self,ob2):
        return self.getLuongDienTT() > ob2.getLuongDienTT()
# cau 4
n = int(input("Nhap so luong khach hang: "))
ds = []
for i in range(n):
    while True:
        print("Khach hang thu {0}:".format(i+1))
        maKH = input("Ma khach hang: ")
        tonTai = 0
        for j in range(i):
            if ds[j].maKH == maKH:
                print("Ma khach hang da ton tai, nhap lai: ")
                tonTai = 1
                break
        if tonTai == 0:
            hoTen = input("Ho ten: ")
            diaChi = input("Dia chi: ")
            chiSoCu = int(input("Chi so cu: "))
            chiSoMoi = int(input("Chi so moi: "))
            ds.append(HoaDon(maKH,hoTen,diaChi,chiSoCu,chiSoMoi))
            break
for i in range(n-1):
    for j in range(i+1,n):
        if ds[i] > ds[j]:
            ds[i],ds[j] = ds[j],ds[i]
tonTai = 0
ma  = input("Nhap ma: ")
for i in ds:
    if i.maKH == ma:
        i.hienThi()
        tonTai = 1
        break
if tonTai == 0:
    print("Khong ton tai khach hang nay")
f = open("output.data","w")
for i in ds:
    if i.getLuongDienTT()>100:
        print("{0}; {1}; {2}".format(i.maKH,i.hoTen,i.diaChi),file=f)