n = int(input("Nhap N: "))
veTrai = 0
vePhai = 0
for i in range (1,n+1):
    veTrai += i**3
    vePhai += i
vePhai = vePhai**2
print(veTrai==vePhai)