c = 1

def Comprobar(Queens, n, k):
    for i in range(k):
        if Queens[i] == Queens[k] or abs(Queens[i]- Queens[k]) == abs(i-k):
            return False
    return True

def NQueens(Queens, n, k):
    global c
    if k == n:
        print('Solución',c,':',Queens)
        c += 1
        return

    for i in range(n):
        Queens[k] = i
        if Comprobar(Queens,n,k):
            NQueens(Queens,n,k+1)


N = 12
Queens = N*[-1]
NQueens(Queens, N, 0)