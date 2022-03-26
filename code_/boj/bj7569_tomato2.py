from pprint import pprint
import sys
from collections import deque
M, N, H = map(int, input().split()) # 2 <= M,N <= 100, 1 <= H <= 100
tomatos = [[list(map(int,  sys.stdin.readline().split())) for i in range(N)] for _ in range(H)]
di = [1, 0, -1, 0, 0, 0]
dj = [0, 1, 0, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]
cnt = 0
que = deque()
for i in range(M):
	for j in range(N):
		for k in range(H):
			if tomatos[k][j][i] == 1:
				que.append([k,j,i])
day = 0

while len(que) > 0:
	x = que.popleft()
	for d in range(6):
		ni, nj, nk = x[2] + di[d], x[1] + dj[d], x[0] + dk[d]
		if 0 <= ni < M and 0 <= nj < N and 0 <= nk < H and tomatos[nk][nj][ni] == 0:
			que.append([nk,nj,ni])
			tomatos[nk][nj][ni] = tomatos[x[0]][x[1]][x[2]] + 1
			if tomatos[x[0]][x[1]][x[2]] > day:
				day = tomatos[x[0]][x[1]][x[2]]
stopper = 0
for h in range(H):
	for n in range(N):
		if tomatos[h][n].count(0) > 0:
			stopper = 1
			print(-1)
			break
	if stopper == 1:
		break
else:
	print(day)


'''
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1

4 3 2
0 -1 -1 -1
0 0 0 -1
-1 -1 -1 -1
0 0 0 0
-1 -1 -1 0
1 0 0 0
'''