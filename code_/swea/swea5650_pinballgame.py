from collections import defaultdict


def block(direction,k):
	if k == 5:
		return (direction+2)%4
	else:
		if k == 1:
			mapping = [1, 3, 0, 2]
		elif k == 2:
			mapping = [2, 3, 1, 0]
		elif k == 3:
			mapping = [2, 0, 3, 1]
		else:
			mapping = [3, 2, 0, 1]
		return mapping[direction]


def score(y,x,direction):
	global N
	result = 0
	i = y
	j = x
	d = direction
	while board[i][j] != -1:
		ni = i + di[d]
		nj = j + dj[d]
		if 0 <= ni < N and 0 <= nj < N:
			if board[ni][nj] == 0:
				i = ni
				j = nj
			elif board[ni][nj] >= 6:
				if (ni,nj) == wormhole[board[ni][nj]][0]:
					i, j = wormhole[board[ni][nj]][1][0], wormhole[board[ni][nj]][1][1]
				else:
					i, j = wormhole[board[ni][nj]][0][0], wormhole[board[ni][nj]][0][1]
			else:
				result += 1
				i, j = ni, nj
				d = block(d, board[ni][nj])
		else:
			result += 1
			d = (d+2)%4
		print(i, j, y, x)
		if i == y and j == x:
			return result
	return result
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	board = [list(map(int, input().split())) for _ in range(N)]
	wormhole = defaultdict(list)
	blank = []
	for i in range(N):
		for j in range(N):
			if board[i][j] == 0:
				blank.append((i,j))
			elif board[i][j] >= 6:
				wormhole[board[i][j]].append((i,j))
	max_val = 0
	for b in blank:
		for d in range(4):
			tmp = score(b[0], b[1], d)
			if tmp > max_val:
				max_val = tmp
	print(f'#{tc} {max_val}')
