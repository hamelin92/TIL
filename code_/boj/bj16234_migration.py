from collections import deque
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
day = 0
check = [[0]*N for _ in range(N)]
while True:
	flag = 0
	unions = [[0]*N for _ in range(N)]
	k_avg = [0]
	k = 1
	for i in range(N):
		for j in range(N):
			cnt = 0
			total = 0
			if unions[i][j] == 0:
				check[i][j] = 1
				unions[i][j] = k
				que = deque([(i,j)])
				cnt += 1
				total += A[i][j]
				while que:
					q = que.popleft()
					for d in range(4):
						ni = q[0] + di[d]
						nj = q[1] + dj[d]
						if 0 <= ni < N and 0 <= nj < N and unions[ni][nj] == 0 and check[ni][nj] == 0 and L <= abs(A[ni][nj] - A[q[0]][q[1]]) <= R:
							unions[ni][nj] = unions[q[0]][q[1]]
							que.append((ni,nj))
							cnt += 1
							total += A[ni][nj]
							flag = 1
							check[ni][nj] = 1
				k_avg.append(total//cnt)
				k += 1
	for i in range(N):
		for j in range(N):
			if k_avg[unions[i][j]] != A[i][j]:
				A[i][j] = k_avg[unions[i][j]]
				check[i][j] = 0
	if flag == 0:
		break
	else:
		day += 1
print(day)