from collections import deque

N, M = map(int, input().split()) # 3 <= <= 8
L = [list(map(int, input().split())) for _ in range(N)]	# 0 : 빈칸(>= 3), 1 : 벽 , 2: 바이러스(2<= * <= 10)
infect = set()
virus = []
walls = set()
new_walls = set()
for i in range(N):
	for j in range(M):
		if L[i][j] == 2:
			virus.append([i, j])
			infect.add((i,j))
		elif L[i][j] == 1:
			walls.add((i, j))

def safezone(arr):
	new_infect = set(infect)
	n = len(arr)
	m = len(arr[0])
	chk = deque(virus)
	di = [-1, 0, 1, 0]
	dj = [0, 1, 0, -1]
	while len(chk) > 0:
		a = chk.popleft()
		for k in range(4):
			ni = a[0] + di[k]
			nj = a[1] + dj[k]
			if 0 <= ni < n and 0 <= nj < m and (ni,nj) not in new_infect and (ni,nj) not in walls and (ni,nj) not in new_walls:
				chk.append([ni,nj])
				new_infect.add((ni, nj))
	return len(new_infect)
res = N * M
for i in range(N*M - 3):
	for j in range(i+1, N*M -2):
		for k in range(j+1, N*M -1):
			if L[divmod(i, M)[0]][divmod(i,M)[1]] == 0 and L[divmod(j, M)[0]][divmod(j,M)[1]] == 0 and L[divmod(k, M)[0]][divmod(k,M)[1]] == 0:
				new_walls = {(divmod(i, M)[0],divmod(i, M)[1]), (divmod(j, M)[0],divmod(j, M)[1]), (divmod(k, M)[0],divmod(k, M)[1])}

				if safezone(L) < res:
					res = safezone(L)
print(N*M - res -len(walls) -3)