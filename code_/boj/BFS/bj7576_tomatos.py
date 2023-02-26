import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
storage = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
days = [[0]*M for _ in range(N)]
tomatos = []
cnt = 0
for i in range(N):
    for j in range(M):
        if storage[i][j] == 1:
            tomatos.append((i,j))
        elif storage[i][j] == 0:
            cnt += 1
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
que = deque(tomatos)
while que:
    q = que.popleft()
    for k in range(4):
        ni = q[0] + di[k]
        nj = q[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M and storage[ni][nj] == 0:
            days[ni][nj] = days[q[0]][q[1]] + 1
            storage[ni][nj] = 1
            que.append((ni, nj))
            cnt -= 1
if not cnt:
    print(days[q[0]][q[1]])
else:
    print(-1)
