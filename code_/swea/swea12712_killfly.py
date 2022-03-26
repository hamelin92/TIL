T = int(input())
for tc in range(1, T+1):
	N, M = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]
	di = [1, 0 , -1, 0]
	dj = [0, 1, 0 , -1]
	si = [1, 1, -1, -1]
	sj = [1, -1, 1, -1]
	max_value = 0
	for i in range(N):
		for j in range(N):
			cross = diag = arr[i][j]
			for k in range(4):
				for m in range(1,M):
					ni, nj = i+m*di[k], j+m*dj[k]
					nsi, nsj = i+m*si[k], j+m*sj[k]
					if 0 <= ni < N and 0 <= nj < N:
						cross += arr[ni][nj]
					if 0 <= nsi < N and 0 <= nsj < N:
						diag += arr[nsi][nsj]
			if cross > max_value:
				max_value = cross
			if diag > max_value:
				max_value = diag
	print(f'#{tc} {max_value}')
