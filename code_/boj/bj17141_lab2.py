from collections import deque
from itertools import combinations

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
cnt = 0
for i in range(N):
	for j in range(N):
		if arr[i][j] == 2:
			virus.append((i,j))
		elif arr[i][j] == 1:
			cnt += 1
empty = N*N - cnt
day = N*N + 1
for cb in combinations(virus, M):
	cb_cnt = M
	visit = [[0]*N for _ in range(N)]
	que = deque(cb)
	for v in cb:
		visit[v[0]][v[1]] = 1
	while que:
		q = que.popleft()
		if visit[q[0]][q[1]] >= day:
			break
		for d in range(4):
			ni = q[0] + di[d]
			nj = q[1] + dj[d]
			if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visit[ni][nj] == 0:
				que.append((ni,nj))
				visit[ni][nj] = visit[q[0]][q[1]] + 1
				cb_cnt += 1
	if cb_cnt == empty:
		tmp_day = visit[q[0]][q[1]]
		if tmp_day < day:
			day = tmp_day
if day > N*N:
	print(-1)
else:
	print(day-1)