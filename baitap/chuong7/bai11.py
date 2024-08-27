def ChangeColumn(A,i,j):
    for x in range(len(A)):
        A[x][i-1],A[x][j-1] = A[x][j-1],A[x][i-1]
    for i in A:
        print(i)
A = [[1,2,3],[4,5,6],[7,8,9]]
ChangeColumn(A,3,2)