import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
miro = [sys.stdin.readline().strip("\n") for _ in range(N)]
visit = [[0]*M for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
que = deque([(0, 0)])
visit[0][0] = 1
while que:
    q = que.popleft()
    if q[0] == N-1 and q[1] == M-1:
        break
    for k in range(4):
        ni = q[0] + di[k]
        nj = q[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj] and miro[ni][nj] == "1":
            que.append((ni, nj))
            visit[ni][nj] = visit[q[0]][q[1]] + 1
print(visit[N-1][M-1])