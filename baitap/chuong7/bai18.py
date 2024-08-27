def dayConMax(A):
    B = [0]
    k = 1
    maxLength = 0
    for i in range(len(A)-2,-1,-1):
        if A[i] < A[i+1]:
            k += 1
        if A[i] > A[i+1]:
            k = 1
        B += [k]
    B.reverse()
    for i in B:
        if i > maxLength:
            maxLength = i
    for i in range(len(A)):
        if B[i] == maxLength:
            for j in range(B[i]):
                print(A[i+j],end=" ")
            break
A = [3,1,2,4,-1,8,7,10,11,7,8,9,0,16,40,50,-100,1]
dayConMax(A)