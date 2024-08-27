def Multiple(A,B):
    C = []
    for i in range(len(A)):
        D = []
        for j in range(len(B[i])):
            temp = 0
            for x in range(len(A[i])):
                temp += (A[i][x]*B[x][j])
            D += [temp]
        C += [D]
    return C
A = [[1,2,3],[4,5,6]]
B = [[1,2],[3,4],[5,6]]
C = Multiple(A,B)
print(C)