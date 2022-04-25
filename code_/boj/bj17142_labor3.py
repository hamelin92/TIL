from itertools import combinations
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = []
cnt = N*N
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append([i,j])
    cnt -= sum(arr[i])
cnt += len(virus)
min_sec = cnt+1
for cb in combinations(virus, M):
    sec = cnt+1
    tmp = 0
    visited = [[0]*N for _ in range(N)]
    for c in cb:
        visited[c[0]][c[1]] = 1
    que = deque(cb)
    while que:
        flag = 0
        q = que.popleft()
        if visited[q[0]][q[1]] > min_sec + 1:
            break
        if tmp >= cnt:
            sec = visited[q[0]][q[1]] - 1
            break
        for d in range(4):
            ni = q[0] + di[d]
            nj = q[1] + dj[d]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                que.append([ni,nj])
                visited[ni][nj] = visited[q[0]][q[1]] + 1
                if arr[ni][nj] == 0:
                    tmp += 1
                if tmp >= cnt:
                    sec = visited[ni][nj] -1
                    flag = 1
                    break
        if flag == 1:
            break
    else:
        if tmp == cnt:
            sec = visited[q[0]][q[1]] -1
    if min_sec > sec:
        min_sec = sec
if min_sec == cnt+1:
    print(-1)
else:
    print(min_sec)