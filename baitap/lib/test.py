import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("ThoiTietHue_2016_2021.csv")
nhietDo = df["Nhiet do"]
ngay = df["Ngay"]
thang_nam = []
for i in ngay:
    thang_nam += [i.split("/",1)]
yvalues = []
temp = 0
dem = 0
for i in range(len(df)-1):
    if thang_nam[i][2] == thang_nam[i+1][2]:
        temp += nhietDo[i]
        dem += 1
    else:
        yvalues += ([temp]/dem)
        dem = 0
if thang_nam[len(df)-1][2] == thang_nam[len(df)-2][2]:
        temp += nhietDo[i]
        dem += 1
else:
    yvalues += ([temp]/dem)