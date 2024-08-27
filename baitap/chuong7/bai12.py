def Sum(A,B):
    C = []
    for i in range(len(A)):
        D = []
        for j in range(len(A[i])):
            D += [A[i][j]+B[i][j]]
        C += [D]
    return C
A = [[1,2,3],[3,4,5]]
B = [[2,3,4],[5,6,7]]
C = Sum(A,B)
print(C)