from collections import deque
T = int(input())

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for tc in range(1, T+1):
	N, M = map(int,input().split())
	grid = [input() for _ in range(N)]
	visit = [[0] * M for _ in range(N)]
	sample_cnt = {'A': 0, 'B': 0}
	largest = 0
	que = deque([])
	for i in range(N):
		for j in range(M):
			if grid[i][j] != '_' and visit[i][j] == 0:
				tmp_large = 1
				sample = grid[i][j]
				sample_cnt[sample] += 1
				que.append((i,j))
				visit[i][j] = 1
				while que:
					v = que.popleft()
					for d in range(4):
						ni = v[0] + di[d]
						nj = v[1] + dj[d]
						if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0 and grid[ni][nj] == sample:
							visit[ni][nj] = 1
							que.append((ni,nj))
							tmp_large += 1
				if tmp_large > largest:
					largest = tmp_large
	ans1 = sample_cnt['A']
	ans2 = sample_cnt['B']
	print(f'#{tc} {ans1} {ans2} {largest}')

