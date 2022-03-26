from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def kill_check(i, j, M):
	for m in range(1, M):
		ni = i+m
		nj = j+m
		di = i-m
		dj = j-m
		if ni < M and nj < M and board_new[ni][nj] > 1:
			return False
		elif di > 0 and dj > 0 and board_new[di][dj] > 1:
			return False
		elif di > 0 and nj < M and board_new[di][nj] > 1:
			return False
		elif ni > 0 and dj > 0 and board_new[ni][dj] > 1:
			return False
	return True



while True:
	board_new = deepcopy(board)
	cnt = 0
	for i in range(N):
		for j in range(N):
			if board_new[i][j] != 0 and kill_check(i, j, N):
				board_new[i][j] = 2
				cnt += 1
