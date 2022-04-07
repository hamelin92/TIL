import sys
def square(i,j):
	global max_cnt
	if i+1 < N and j+1 < M:
		result = paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1]
		if result > max_cnt:
			max_cnt = result
	return
def line(i,j):
	global max_cnt
	if j+3 < M:
		result = sum(paper[i][j:j+4])
		if result > max_cnt:
			max_cnt = result
	if i+3 < N:
		result = 0
		for k in range(4):
			result += paper[i+k][j]
		if result > max_cnt:
			max_cnt = result
	return
def L_form(i,j):
	global max_cnt
	tmp = [0]
	if j + 2 < M:
		base = sum(paper[i][j:j + 3])
		for d in range(3):
			if 0 <= i - 1:
				tmp.append(base + paper[i - 1][j+d])
			if i+1 < N:
				tmp.append(base + paper[i + 1][j+d])
	if i + 2 < N:
		base = 0
		for k in range(3):
			base += paper[i+k][j]
			for d in range(3):
				if 0 <= j - 1:
					tmp.append(base + paper[i+d][j - 1])
				if j + 1 < M:
					tmp.append(base + paper[i+d][j + 1])
	result = max(tmp)
	if result > max_cnt:
		max_cnt = result
	return
def z_form(i,j):
	global max_cnt
	tmp = [0]
	if j + 2 < M:
		base = paper[i][j] + paper[i][j+1]
		if 0 <= i - 1:
			tmp.append(base + paper[i - 1][j+1] + paper[i-1][j+2])
		if i + 1 < N:
			tmp.append(base + paper[i + 1][j+1] + paper[i+1][j+2])
	if i + 2 < N:
		base = paper[i][j]+paper[i+1][j]
		if 0 <= j - 1:
			tmp.append(base + paper[i+1][j - 1] + paper[i+2][j-1])
		if j + 1 < M:
			tmp.append(base + paper[i+1][j + 1]+paper[i+2][j+1])
	result = max(tmp)
	if result > max_cnt:
		max_cnt = result
	return

N, M = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_cnt = paper[0][0] + paper[0][1] + paper[0][2] + paper[0][3]

for i in range(N):
	for j in range(M):
		square(i,j)
		line(i,j)
		L_form(i,j)
		z_form(i,j)
print(max_cnt)

'''
6 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
1 2 1 2 1
'''