fi = open("input.txt","r")
n = fi.readline()
n.rstrip()
n = int(n)
a = fi.read()
a = list(a.split())
for i in range(n):
    a[i] = eval(a[i])
print(n)
print(a)
fi.close()