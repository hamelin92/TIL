T = int(input())
for tc in range(1, T+1):
	N, M, C = map(int, input().split())
	honey = [list(map(int, input().split())) for _ in range(N)]
	on_line = True if 2*M <= N else False
	results = []
	tmp_dmax = 0
	if on_line:
		for i in range(N):
			for j in range(N - 2*M):
				tmpd = 0
				for m in range(2*M):
					tmpd += (min(C, honey[i][j+m]))**2
				if tmpd > tmp_dmax:
					tmp_dmax = tmpd
	results.append(tmp_dmax)
	tmp_max1 = honey[0][0]
	tmp_idx1 = [0, 0]
	for i in range(N):
		for j in range(N-M):
			tmp = 0
			for m in range(M):
				tmp += (min(C, honey[i][j + m])) ** 2
			if tmp > tmp_max1:
				tmp_max1 = tmp
				tmp_idx1 = [i, j]
	for m in range(M):
		honey[tmp_idx1[0]][tmp_idx1[1]+m] = -1

	tmp_max2 = honey[0][0]
	tmp_idx2 = [0, 0]
	for i in range(N):
		for j in range(N - M):
			tmp = 0
			for m in range(M):
				tmp += (min(C, honey[i][j + m])) ** 2
			if tmp > tmp_max2:
				tmp_max2 = tmp
				tmp_idx2 = [i, j]
	results.append(tmp_max1+tmp_max2)
	print(f'#{tc} {max(results)}')
