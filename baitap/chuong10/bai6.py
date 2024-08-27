fi = open("fin.dat","r")
n = fi.readline()
n = int(n.rstrip())
a = fi.readlines()
for i in range(n):
    a[i] = list(a[i].split())
    for j in range(len(a[i])):
        a[i][j] = eval(a[i][j])
fi.close()
fo = open("fout.dat","w")
s = 0
for i in a:
    s += sum(i)
fo.write(str(s)+"\n")
for i in a:
    s = sum(i)
    fo.write(str(s)+"\n")
fo.close()