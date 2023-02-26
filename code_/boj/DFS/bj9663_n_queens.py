def queens(n, i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not col[j] and not diag[N+i-j] and not xdiag[i+j]:
            col[j] = True
            diag[N+i-j] = True
            xdiag[i+j] = True
            queens(n, i+1)
            col[j] = False
            diag[N+i-j] = False
            xdiag[i+j] = False


ans = 0
N= int(input())
col = [False]*N
diag = [False]*(2*N)
xdiag = [False]*(2*N)
queens(N, 0)
print(ans)
