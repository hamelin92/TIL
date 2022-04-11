from collections import deque, defaultdict

def trans(string):
	if string == '_':
		return 1
	elif string == '#':
		return 0
	elif string == 'S':
		return 3
	else:
		return 2
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for tc in range(1, T+1):
	X, Y = map(int, input().split())
	loca = [list(map(trans, input())) for _ in range(Y)]
	nodes = defaultdict(int)
	start = []
	K = 0
	for x in range(X):
		for y in range(Y):
			if loca[y][x] == 3:
				start.append((y,x))
			elif loca[y][x] == 2:
				K += 1
	while len(start) < K+1:
		visit = [[0]*X for _ in range(Y)]
		for s in start:
			visit[s[0]][s[1]] = 1
		que = deque(start)
		while que:
			q = que.popleft()
			if loca[q[0]][q[1]] == 2 and visit[q[0]][q[1]] != 1:
				nodes[q] = visit[q[0]][q[1]]-1
				start.append(q)
				break
			for d in range(4):
				ny = q[0] + dy[d]
				nx = q[1] + dx[d]
				if 0 <= nx < X and 0 <= ny < Y and visit[ny][nx] == 0 and 0 < loca[ny][nx] < 3:
					que.append((ny,nx))
					visit[ny][nx] = visit[q[0]][q[1]] + 1
	print(sum(nodes.values()))