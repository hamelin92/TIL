import sys
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N = int(sys.stdin.readline())
region = [list(sys.stdin.readline()) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
normal = 0
xnormal = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            normal += 1
            start_color = region[i][j]
            start = (i,j)
            que = deque([start])
            visit[i][j] = 1
            if region[i][j] == "G":
                region[i][j] = "R"
            while que:
                q = que.popleft()
                for k in range(4):
                    ni = q[0] + di[k]
                    nj = q[1] + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and region[ni][nj] == start_color:
                        que.append((ni, nj))
                        visit[ni][nj] = 1
                        if region[ni][nj] == "G":
                            region[ni][nj] = "R"
visit = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            xnormal += 1
            start_color = region[i][j]
            start = (i,j)
            que = deque([start])
            visit[i][j] = 1
            while que:
                q = que.popleft()
                for k in range(4):
                    ni = q[0] + di[k]
                    nj = q[1] + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and region[ni][nj] == start_color:
                        que.append((ni, nj))
                        visit[ni][nj] = 1
print(normal, xnormal)
