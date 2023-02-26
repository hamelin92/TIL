import sys

N = int(sys.stdin.readline())
board = [[0]* 1001 for _ in range(1001)]
for k in range(1, N+1):
    p, q, w, h = map(int, sys.stdin.readline().split())
    for i in range(p, p+w):
        board[i][q:q+h] = [k]*h
for k in range(1, N+1):
    ans = 0
    for i in range(1001):
        ans += board[i].count(k)
    print(ans)
