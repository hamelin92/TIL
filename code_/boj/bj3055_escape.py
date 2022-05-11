from collections import deque

R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)] # .: 빈 곳, *: 물, X: 돌, D: 비버굴, S: 고슴도치 위치
water = []
start = []
den = (0,0)
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
answer = -1
for i in range(R):
	for j in range(C):
		if forest[i][j] == '*':
			water.append((i,j))
		elif forest[i][j] =='S':
			start.append((i,j))
			forest[i][j] = '.'
		elif forest[i][j] == 'D':
			den = (i,j)

visited = [[-1]*C for _ in range(R)]
for s in start:
	visited[s[0]][s[1]] = 0

water_que = deque(water)
que = deque(start)

while que:
	w_len = len(water_que)
	for _ in range(w_len):
		w = water_que.popleft()
		for d in range(4):
			nwi = w[0] + di[d]
			nwj = w[1] + dj[d]
			if 0 <= nwi < R and 0 <= nwj < C and forest[nwi][nwj] == '.':
				forest[nwi][nwj] = '*'
				water_que.append((nwi, nwj))
	q_len = len(que)
	for _ in range(q_len):
		q = que.popleft()
		if q == den:
			answer = visited[q[0]][q[1]]
			break
		for d in range(4):
			ni = q[0] + di[d]
			nj = q[1] + dj[d]
			if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == -1 and forest[ni][nj] != '*' and forest[ni][nj] != 'X':
				visited[ni][nj] = visited[q[0]][q[1]] + 1
				que.append((ni, nj))
	if answer > 0:
		break
if answer > 0:
	print(answer)
else:
	print('KAKTUS')





