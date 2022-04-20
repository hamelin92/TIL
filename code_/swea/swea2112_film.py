from itertools import combinations

def test(rows_idx):
	global D, W, K
	for w in range(W):
		cnt = 0
		chk = cells[0][w]
		i = 0
		while i < D:
			if cnt >= K:
				break
			if rows_idx[i] == 0:
				other = cells[i][w]
			elif rows_idx[i] == 1:
				other = 0
			else:
				other = 1
			if chk == other:
				i += 1
				cnt += 1
			else:
				chk = other
				i += 1
				cnt = 1
		if cnt < K:
			return False
	return True

def final():
	global D,W,K
	if test([0]*D):
		return 0
	for num in range(1,D):
		for cb in combinations(range(D),num):
			for n in range(num):
				for m in combinations(cb,n):
					rowid = [0] * D
					for k in range(D):
						if k in m:
							rowid[k] = 2
						elif k in cb:
							rowid[k] = 1
					result = test(rowid)
					if result == True:
						return num

T = int(input())
for tc in range(1, T+1):
	D, W, K = map(int, input().split())
	cells = [list(map(int, input().split())) for _ in range(D)]
	ans = final()
	if ans < 2:
		print(f'#{tc} 0')
	else:
		print(f'#{tc} {ans}')
