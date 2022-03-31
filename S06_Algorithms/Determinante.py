def MC(A,i,j):
    B = []
    for x in range(len(A)):
        if x == i:
            continue
        C = []
        for y in range(len(A)):
            if y == j:
                continue
            C.append(A[x][y])
        B.append(C)
    return B

def det(A, i = 0):
    if len(A) == 1:
        return A[0][0]
    ans = 0
    for j in range(len(A)):
        ans += (-1)**(i+j)*A[i][j]*det(MC(A,i,j))
    return ans

A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 10]]

print(det(A))