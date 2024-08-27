a = [0,2,4,6,8,10,12,13]
b = [1,3,5,7,9,11]
c = []
n = min(len(a),len(b))
for i in range(n):
    c.append(a[i])
    c.append(b[i])
if n < len(a):
    c.extend(a[n:])
else:
    c.extend(b[n:])
print(c)