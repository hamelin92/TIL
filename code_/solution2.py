from collections import deque

T = int(input())
for tc in range(1,T+1):
	N, M = map(int, input().split())
	ice = [list(input()) for _ in range(N)]
	que = deque()
	answer = -1
	di = [1, -1, 0 ,0]
	dj = [0, 0, 1, -1]
	visit = [[0]*M for _ in range(N)]
	for i in range(N):
		for j in range(M):
			if ice[i][j] == '3':
				start = (i,j)
			elif ice[i][j] == '2':
				end = (i,j)

	que.append(start)
	visit[start[0]][start[1]] = 1
	ice[start[0]][start[1]] = '0'

	while que:
		q = que.popleft()
		if ice[q[0]][q[1]] == '2':
			answer = visit[q[0]][q[1]] -1
			break
		for d in range(4):
			ni = q[0] + di[d]
			nj = q[1] + dj[d]
			if 0 <= ni < N and 0 <= nj < M and ice[ni][nj] != '1':
				for k in range(1,max(N,M)):
					nni = q[0] + k*di[d]
					nnj = q[1] + k*dj[d]
					if 0 <= nni < N and 0 <= nnj < M and ice[nni][nnj] == '2':
						ni, nj = nni, nnj
						break
					elif 0 <= nni < N and 0 <= nnj < M and ice[nni][nnj] != '1':
						ni, nj = nni, nnj
					else:
						break
				if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0:
					que.append((ni,nj))
					visit[ni][nj] = visit[q[0]][q[1]] + 1
	print(f'#{tc} {answer}')
