from collections import deque
def bfs(r,c,size):
	ans = (N, N)
	que = deque([(r,c)])
	result = []
	visit = [[0]*N for _ in range(N)]
	visit[r][c] = 1
	times = N*N
	while que:
		t = que.popleft()
		if 0 < sea[t[0]][t[1]] < size and visit[t[0]][t[1]]-1 <= times:
			result.append(t)
			times = visit[t[0]][t[1]]-1
		if visit[t[0]][t[1]] < times:
			for d in range(4):
				nr = t[0] + dr[d]
				nc = t[1] + dc[d]
				if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and sea[nr][nc] <= size:
					que.append((nr,nc))
					visit[nr][nc] = visit[t[0]][t[1]] + 1
	else:
		if not result:
			return [ans, 0]
	for t in result:
		if t[0] < ans[0]:
			ans = t
		elif t[0] == ans[0] and t[1] < ans[1]:
			ans = t
	return [ans, times]

def cnt(sr,sc):
	total = 0
	size = 2
	eat = 0

	nr = sr
	nc = sc
	for n in range(target[-1]):
		move = bfs(nr,nc,size)
		total += move[1]
		nr = move[0][0]
		nc = move[0][1]
		if nr == N:
			return total
		else:
			sea[nr][nc] = 0
			eat += 1

		if eat == size:
			size += 1
			eat = 0
	return total

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
target = [0]*7
eaten = 0
for r in range(N):
	for c in range(N):
		if sea[r][c] == 9:
			start = (r,c)
			sea[r][c] = 0
		elif sea[r][c] > 0:
			target[sea[r][c]] += 1
for k in range(1,7):
	target[k] += target[k-1]
answer = cnt(start[0], start[1])
print(answer)