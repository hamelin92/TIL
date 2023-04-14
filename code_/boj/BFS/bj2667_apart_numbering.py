import sys
from collections import deque

N = int(sys.stdin.readline())
aparts = [list(map(int, list(sys.stdin.readline().strip("\n")))) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
que = deque()
apart_cnt = []
for i in range(N):
    for j in range(N):
        if aparts[i][j] and not visit[i][j]:
            cnt = 0
            que.append((i, j))
            visit[i][j] = 1
            while que:
                q = que.popleft()
                cnt += 1
                for k in range(4):
                    ni = q[0] + di[k]
                    nj = q[1] + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and aparts[ni][nj]:
                        que.append((ni, nj))
                        visit[ni][nj] = visit[q[0]][q[1]]
            apart_cnt.append(cnt)
apart_cnt.sort()
print(len(apart_cnt))
print(*apart_cnt, sep="\n")
