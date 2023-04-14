def bishop(n, arr, i, cnt):
    global maximal
    if i == len(arr):
        if cnt > maximal:
            maximal = cnt
        return
    for k in range(i, len(arr)):
        r = arr[k][0]
        c = arr[k][1]
        if not diag[N+r-c] and not xdiag[r+c]:
            diag[N+r-c] = True
            xdiag[r+c] = True
            bishop(n, arr, k+1, cnt+1)
            diag[N+r-c] = False
            xdiag[r+c] = False


ans = 0
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
odd = []
even = []
for i in range(N):
    for j in range(N):
        if board[i][j]:
            if (i+j)%2:
                odd.append((i, j))
            else:
                even.append((i, j))
diag = [False]*(2*N)
xdiag = [False]*(2*N)
maximal = 0
bishop(N, odd, 0, 0)
ans += maximal
maximal = 0
bishop(N, even, 0, 0)
ans += maximal
print(ans)
