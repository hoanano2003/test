fo = open("output.txt","w")
n = 5
a = [19,-2,9.8,7,-10]
fo.write(str(n)+"\n")
for i in a:
    print(str(i),file=fo,end=" ")
fo.close()