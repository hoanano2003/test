# class DiemHocPhan:
#     def __init__(self,maHP="",tenHP="",soTC=0,diem=0):
#         self.maHP = maHP
#         self.tenHP = tenHP
#         self.soTC = soTC
#         self.diem = diem
#     def display(self):
#         print("{0} | {1} | {2} | {3}\n".format(self.maHP,self.tenHP,self.soTC,self.diem))
#     def getAll(self):
#         return "{0},{1},{2},{3}\n".format(self.maHP,self.tenHP,self.soTC,self.diem)
#     def __lt__(self,ob2):
#         return self.diem < ob2.diem
# f = open("DSDiem.csv","r",encoding="UTF-8")
# f.readline()
# dem = 0
# ds = []
# for line in f:
#     temp = line.split(",")
#     tontai = 0
#     for i in range(dem):
#         if ds[i].maHP == temp[0]:
#             tontai = 1
#     if tontai == 0:
#         ds.append(DiemHocPhan(temp[0],temp[1],int(temp[2]),int(temp[3])))
#         dem += 1
# print(dem)
# f.close()
# for i in range(dem-1):
#     for j in range(i+1,dem):
#         if ds[j] < ds[i]:
#             ds[j],ds[i] = ds[i],ds[j]
#     ds[i].display()
# ds[dem-1].display()
# diemTB = 0
# tongTC = 0
# for i in ds:
#     if i.diem >= 4:
#         diemTB += i.diem*i.soTC
#         tongTC += i.soTC
# diemTB /= tongTC
# print("{:.2f}".format(diemTB))
# f = open("HocPhanTOAN.csv","w")
# for i in ds:
#     if i.maHP.find("TOA") == 0:
#         print(i.getAll(),file=f,end="\n")
# f.close()