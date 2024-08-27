fi = open("Inp.dat","r")
a = fi.readline()
a = a.split()
n = len(a)
for i in range(n):
    a[i] = int(a[i])
fi.close()
b = []
for i in range(1,n-1):
    if a[i-1]<a[i]>a[i+1] or a[i-1]>a[i]<a[i+1]:
        b.append(a[i])
fo = open("Out.dat","w")
fo.write(str(len(b))+"\n")
for i in b:
    print(i,file=fo,end=" ")
fo.close()