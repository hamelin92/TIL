import sys
from collections import deque
from pprint import pprint
N, M = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
t = 0
que = deque()
outer = deque()
outer.append((0,0))
cheese[0][0] = -1
while outer:
    q = outer.popleft()
    for k in range(4):
        ni = q[0] + di[k]
        nj = q[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M and cheese[ni][nj] == 0:
            cheese[ni][nj] = -1
            outer.append((ni, nj))
for i in range(1, N-1):
    for j in range(1, M-1):
        if cheese[i][j] > 0:
            que.append((i, j))
while que:
    inner = []
    while que:
        q = que.popleft()
        cnt = 0
        for k in range(4):
            if cheese[q[0]+di[k]][q[1]+dj[k]] == -1:
                cnt += 1
        if cnt >= 2:
            cheese[q[0]][q[1]] = 0
            outer.append(q)
        else:
            inner.append(q)
    while outer:
        q = outer.popleft()
        if cheese[q[0]][q[1]] == 0:
            cheese[q[0]][q[1]] = -1
        for k in range(4):
            ni = q[0] + di[k]
            nj = q[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and cheese[ni][nj] == 0:
                cheese[ni][nj] = -1
                outer.append((ni, nj))
    que = deque(inner)
    t += 1
print(t)